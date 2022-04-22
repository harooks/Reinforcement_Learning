import enum
import random

class Agent:

  def __init__(self, q_a, q_b, action_arr, ex):
    self.q_a = q_a
    self.q_b = q_b
    self.action_arr = action_arr
    self.ex = ex

  def choose_action(self):

    # Greedy
    if random.random() > self.ex:
        a_or_b = random.randint(0,1)

        if a_or_b == 0:
          val = max(self.q_a)
          action = self.q_a.index(val_a)
        else:
          val_a = max(self.q_b)
          action = self.q_b.index(val_a)

     # Random
    else:
        # index of action choice chosen randomly
        action = random.randrange(0, len(self.action_arr))
        a_or_b = random.randint(0, 1)

        if a_or_b == 0:
          val = self.q_a[action]  # the q value of the action chosen
        else:
          val = self.q_b[action]
