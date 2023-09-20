import matplotlib.pyplot as plt
import numpy as np
import torch, copy, random, gym
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from collections import deque



class ReplayBuffer:
    def __init__(self, buffer_size, batch_size):
        self.buffer = deque(maxlen=buffer_size)
        self.batch_size = batch_size

    def add(self, state, action, reward, next_state, done):
        data = (state, action, reward, next_state, done)
        self.buffer.append(data)

    def __len__(self):
        return len(self.buffer)

    def get_batch(self):
        data = random.sample(self.buffer, self.batch_size)
        state = torch.tensor([x[0] for x in data], dtype=torch.float32)
        action = np.array([x[1] for x in data])
        reward = np.array([x[2] for x in data], dtype=np.float32)
        next_state = torch.tensor([x[3] for x in data], dtype=torch.float32)
        done = np.array([x[4] for x in data], dtype=np.float32).astype(np.int32)

        return state, action, reward, next_state, done

# ニューラルネットワークの設定
# 単純なlinear層を用いる
class QNet(nn.Module):
    def __init__(self, action_size):
        super().__init__()
        # stateの情報が台車の位置、台車の速度、棒の角度、棒の先端の速度の４つなので入力は4
        # cartpoleではaction_sizeは右か左かの2つ
        self.l1 = nn.Linear(4, 128)
        self.l2 = nn.Linear(128, 128)
        self.l3 = nn.Linear(128, action_size)

    def forward(self, x):
        x = F.relu(self.l1(x))
        x = F.relu(self.l2(x))
        x = self.l3(x)
        return x


class DQNAgent:
    def __init__(self):
        # ハイパーパラメータの設定
        self.gamma = 0.98
        self.lr = 0.0005
        self.epsilon = 0.1
        self.buffer_size = 10000
        self.batch_size = 32
        self.action_size = 2
        # 経験再生の設定
        self.replay_buffer = ReplayBuffer(self.buffer_size, self.batch_size)
        # モデル等の設定
        # Target Networkを実装し、学習の安定化を図る
        self.qnet = QNet(self.action_size)
        self.qnet_target = QNet(self.action_size)
        self.optimizer = optim.Adam(self.qnet.parameters(), self.lr)

    def get_action(self, state):
        # ε-greedy法によるactionの取得
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.action_size)
        else:
            qs = self.qnet(torch.tensor(state))
            return qs.data.argmax().numpy()

    def update(self, state, action, reward, next_state, done):
        # replay bufferに経験をためる
        self.replay_buffer.add(state, action, reward, next_state, done)
        if len(self.replay_buffer) < self.batch_size:
            return

        # モデルの学習
        # replay bufferにためたデータからミニバッチを作成して学習に用いる
        state, action, reward, next_state, done = self.replay_buffer.get_batch()
        # Target Networkの出力値を得る
        next_qs = self.qnet_target(next_state)
        next_q = next_qs.max(axis=1).values
        # main Networkの出力値を得る
        self.qnet.train()
        qs = self.qnet(state)
        q = qs[np.arange(self.batch_size), action]

        self.optimizer.zero_grad()
        # モデルの更新
        target = torch.tensor(reward, dtype=torch.float32) + torch.mul(torch.mul(next_q, self.gamma), torch.tensor(1.0 - done))
        loss = nn.MSELoss()(q.to(torch.float32), target.to(torch.float32))

        loss.backward()
        self.optimizer.step()

    # Target NetworkとMain Networkを同期させる
    def sync_qnet(self):
        self.qnet_target = copy.deepcopy(self.qnet)

# 設定いろいろ
episodes = 100
sync_interval = 20
env = gym.make('CartPole-v1')
agent = DQNAgent()
reward_history = []
# コードを動かす
for episode in range(episodes):
    # env.reset()をするとstateとしてnext_state, reward, done, infoの４つと謎の値１つの合計5つと謎の値を含むtupleが返ってくる
    state = env.reset()
    done = False
    total_reward = 0

    while not done:
        # replay bufferでミニバッチを作成する際に型やsizeでエラーが出る
        # env.reset()で得たstateはtupleであることが問題
        # tupleの時は0番目の要素が必要な情報
        if isinstance(state, tuple):
            state = state[0]
        # actionを取得する
        action = agent.get_action(state)
        # env.step(action)をするとstateとしてnext_state, reward, done, infoの４つと謎の値１つの合計5つが返ってくる
        next_state, reward, done, info, _ = env.step(action)
        # モデルの学習を行う
        agent.update(state, action, reward, next_state, done)
        state = next_state
        total_reward += reward

    if episode % sync_interval == 0:
        agent.sync_qnet()

    reward_history.append(total_reward)
    if episode % 1 == 0:
        print("episode :{}, total reward : {}".format(episode, total_reward))


# 結果をPlotする
plt.xlabel('Episode')
plt.ylabel('Total Reward')
plt.plot(range(len(reward_history)), reward_history)
plt.show()


# 学習結果を確かめる
agent.epsilon = 0  # greedy policy
state = env.reset()
done = False
total_reward = 0

while not done:
    action = agent.get_action(state)
    next_state, reward, done, info, _ = env.step(action)
    state = next_state
    total_reward += reward
    env.render()
print('Total Reward:', total_reward)