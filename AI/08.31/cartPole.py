import chainer
import chainer.functions as F
import chainer.links as L
import chainerrl
import gym
import numpy as np
 
"""
以下のような2層の全結合ニューラルネットワークを実装
入力：状態
出力：最適な行動
"""
# エージェントの判断器となるニューラルネットワークを定義
class QFunction(chainer.Chain):
    def __init__(self, obs_size, n_actions, n_hidden_channels=50):
        super().__init__()
        with self.init_scope():
            self.l0 = L.Linear(obs_size, n_hidden_channels)
            self.l1 = L.Linear(n_hidden_channels, n_hidden_channels)
            self.l2 = L.Linear(n_hidden_channels, n_actions)
 
    def __call__(self, x, test=False):
        h = F.tanh(self.l0(x))
        h = F.tanh(self.l1(h))
        return chainerrl.action_value.DiscreteActionValue(self.l2(h))
 
# エージェントを定義
def get_agent(env, obs_size, n_actions):
    # 上記のニューラルネットワークを利用
    q_func = QFunction(obs_size, n_actions)
    optimizer = chainer.optimizers.Adam(eps=1e-2)
    optimizer.setup(q_func)
 
    # DoubleDQNに必要なパラメータを定義
    gamma = 0.95
    explorer = chainerrl.explorers.ConstantEpsilonGreedy(
        epsilon=0.3, random_action_func=env.env.action_space.sample)
    replay_buffer = chainerrl.replay_buffer.ReplayBuffer(capacity=10 ** 6)
    phi = lambda x: x.astype(np.float32, copy=False)
 
    # ChainerRLに用意されたDoubleDQNアルゴリズムを利用
    agent = chainerrl.agents.DoubleDQN(
        q_func, optimizer, replay_buffer, gamma, explorer,
        replay_start_size=500, update_interval=1,
        target_update_interval=100, phi=phi)
 
    return agent
 
# 学習を定義
def train(n_episodes=200, max_episode_len=200):
    # OpenAI Gymに用意された環境を利用
    env = gym.make('CartPole-v0')
    obs_size = env.observation_space.shape[0]
    n_actions = env.action_space.n
 
    agent = get_agent(env, obs_size, n_actions)
 
    # n_episodesの数だけ試行を繰り返す
    for i in range(1, n_episodes + 1):
        # シミュレーターを初期位置に戻す
        obs = env.reset()
        reward = 0
        done = False
        R = 0
        t = 0
 
        # １試行の中で行動を繰り返す
        while not done and t < max_episode_len:
            env.render()
            action = agent.act_and_train(obs, reward)
            obs, reward, done, _ = env.step(action)
            R += reward
            t += 1
        if i % 10 == 0:
            print('episode:', i,
                  'R:', R,
                  'statistics:', agent.get_statistics())
        agent.stop_episode_and_train(obs, reward, done)
 
    # 学習したモデルを保存する
    # agent.save('任意の保存先に書き換えてください')
 
if __name__ == '__main__':
    train()