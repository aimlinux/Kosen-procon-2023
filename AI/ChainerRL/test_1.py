import chainer
import chainer.functions as F
import chainer.links as L
import chainerrl
import gym
import numpy as np

print("observation space   : {}".format(env.observation_space))
print("action space        : {}".format(env.action_space))
obs = env.reset() #初期化
#env.render()#レンダリングした環境を見せてくれる
print("initial observation : {}".format(obs))

action = env.action_space.sample()
obs, r, done, info = env.step(action)

### どんな値が入っているのか確認！
print('next observation    : {}'.format(obs))
print('reward              : {}'.format(r))
print('done                : {}'.format(done))
print('info                : {}'.format(info))