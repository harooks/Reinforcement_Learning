import enum
import random

class Agent:

  def __init__(self, q_a, q_b, action_arr, ex, reward, alpha, gamma):
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
          action = self.q_a.index(val)
        else:
          val = max(self.q_b)
          action = self.q_b.index(val)

    # Random
    else:
        # index of action choice chosen randomly
        action = random.randrange(0, len(self.action_arr))
        a_or_b = random.randint(0, 1)

        if a_or_b == 0: #A
          val = self.q_a[action]  # the q value of the action chosen
        else: #B
          val = self.q_b[action]

    # Q[cur_row][cur_col][action] = val + \
       # (alpha * (reward + (gamma * max(Q[next_row][next_col])) - val))

    return [a_or_b, action, val]

    # Get reward from enviroment

  def update_Qtable(self, a_or_b, action, val, reward, alpha, gamma, q_a, q_b, next_q_a, next_q_b):

    if a_or_b == 0: #A
      q_a[action] = val + (alpha * (reward + (gamma * max(next_q_b) - val)))
    else:
      q_b[action] = val + (alpha * (reward + (gamma * max(next_q_a) - val)))
