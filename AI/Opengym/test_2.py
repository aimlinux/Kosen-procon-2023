#https://qiita.com/masataka46/items/7729a74d8dc15de7b5a8
#Quick Startを試す


import chainer
import chainer.functions as F
import chainer.links as L
import chainerrl
import gym
import numpy as np

env = gym.make('CartPole-v1')
env._max_episode_steps = None  # 可視化を無効にする
print('observation space:', env.observation_space)
print('action space:', env.action_space)

obs = env.reset()
env.render()
print('initial observation:', obs)

action = env.action_space.sample()
obs, r, done, info = env.step(action)
print('next observation:', obs)
print('reward:', r)
print('done:', done)
print('info:', info)


#python train.py
#observationは4つの要素の配列
#actionのspaceがDiscrete(2)となってるので、行動は２種類
#報酬はスカラー。

#env.resetで環境を初期化して初期状態のobservationを得る。
#env.stepは行動を与えて次の状態のobservation、報酬、などなどを返す。
#強化学習の1Stepね。