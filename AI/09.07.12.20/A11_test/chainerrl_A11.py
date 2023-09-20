import chainer
import chainer.functions as F
import chainer.links as L
import chainerrl
import numpy as np
import logging
import sys
import os

"""
以下のような2層の全結合ニューラルネットワークを実装
  入力：状態
  出力：最適な行動
"""