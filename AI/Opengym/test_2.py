import gym

#CarPoleの読み取りセット
env = gym.make("CartPole-v1")

# ゲームを試行する回数
num_episodes = 5

for episode in range(num_episodes):
    state = env.reset()  # 環境をリセットして初期状態を取得
    total_reward = 0
    
    while True:
        env.render()  # ゲーム画面を描画
        action = env.action_space.sample()  # ランダムなアクションを選択
        next_state, reward, done, info = env.step(action)  # アクションを実行
        
        total_reward += reward
        
        if done:
            print(f"Episode {episode + 1}: Total Reward = {total_reward}")
            break

env.close()  # 環境を閉じる