import gym 

env = gym.make("MountainCar-v1")

for episode in range(10):
    observation = env.reset()  
    for _ in range(200):
        env.render()  
        action = env.action_space.sample() 
        observation, reward, done, info = env.step(action)  
        if done:
            #print(f"Episode {episode + 1}: Total Reward = {total_reward}")
            env.reset()

env.close()  