import enum
import random
import numpy as np
import math

class Agent_softmax:

  def __init__(self, q_a, q_b, action_arr, reward, alpha, gamma):
    self.q_a = q_a
    self.q_b = q_b
    self.action_arr = action_arr

  def softmax(self, qtable, temp):
    total = sum([math.exp(val/temp) for val in qtable])
    probs = [math.exp(val/temp) / total for val in qtable]

    threshold = random.random()
    cul_prob = 0.0

    for i in range(len(probs)):
      cul_prob += probs[i]
      if (cul_prob > threshold):
        return i

    return np.argmax(probs)


  def choose_action_softmax(self, temp):
    # action = softmax(qtable, 100)
    # return action
    a_or_b = random.randint(0, 1)

    if a_or_b == 0:
      action = self.softmax(self.q_a, temp)
      val = self.q_a[action]
    else:
      action = self.softmax(self.q_b, temp)
      val = self.q_b[action]

    return [a_or_b, action, val]


  def update_Qtable(self, a_or_b, action, val, reward, alpha, gamma, q_a, q_b, next_q_a, next_q_b):

    if a_or_b == 0:  # A
      q_a[action] = val + (alpha * (reward + (gamma * max(next_q_b) - val)))
    else:
      q_b[action] = val + (alpha * (reward + (gamma * max(next_q_a) - val)))
