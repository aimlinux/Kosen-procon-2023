import gym
import math
import random
import numpy as np
import matplotlib
#%matplotlib inline
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')   # Suppress Matplotlib warnings
from collections import namedtuple
from itertools import count
from PIL import Image

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torchvision.transforms as T


env = gym.make('CartPole-v0').unwrapped

# set up matplotlib
is_ipython = 'inline' in matplotlib.get_backend()
if is_ipython:
    from IPython import display

# plt.ion()
plt.ioff() # インタラクティブモードを無効にする

# if gpu is to be used
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")