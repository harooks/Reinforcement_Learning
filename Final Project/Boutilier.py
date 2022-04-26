from calendar import c
from curses import curs_set
import enum
import random

from agent import Agent

NUM_OF_EPISODE = 200
NUM_OF_SIMULATION = 10


def boutilier(alpha, gamma, ex, k):

  action_arr = ['a', 'b']

  # each state and action is a key and the q-Val is the value

  # Q = {'S1a': 0, 'S1b': 0, 'S2a': 0, 'S2b': 0, 'S3a': 0, 'S3b': 0, 'S4a': 0, 'S4b': 0, 'S5a': 0, 'S5b': 0, 'S6a': 0, 'S6b': 0}
  Q1a = [[0, 0] for _ in range(6)]
  Q1b = [[0, 0] for _ in range(6)]
  Q2a = [[0, 0] for _ in range(6)]
  Q2b = [[0, 0] for _ in range(6)]

  # initialize current state to 0 (S1)
  cur_state = 0

  reward = 0

  agent1 = Agent(Q1a[cur_state], Q1b[cur_state], action_arr, ex, reward, alpha, gamma)
  agent2 = Agent(Q2a[cur_state], Q2b[cur_state], action_arr, ex, reward, alpha, gamma)

  cur_state = 0 #S1
  # [S1, S2, S3, S4, S5, S6]

  while not(cur_state == 3) and not(cur_state == 4) and not(cur_state == 5):

    # take action
    action1 = agent1.choose_action()
    action2 = agent2.choose_action()

    print("agent 1 chose: ", action1[1])
    print("agent 2 chose: ", action2[1])
    # create next_state
    next_state = cur_state

    # S1
    if cur_state == 0:
      # S1 -> S2 (agent1 picks a)
      if action1[1] == 0:
        next_state = 1
      # S1 -> S3 agent1 picks b
      else:
        next_state = 2

    # S2
    elif cur_state == 1:
      # S2 -> S4 (agent 1 and agent 2 both pick same action)
      if action1[1] == action2[1]:
        next_state = 3
      # S2 -> S5 (agent 1 and agent 2 pick different action)
      else:
        next_state = 4

    # S3
    elif cur_state == 2:
      # S3 -> S6
      next_state = 5

    # Calculate reward
    if next_state == 3:
      reward = 11
    elif next_state == 4:
      reward = k
    elif next_state == 5:
      reward = 7
    # else reward = 0??

    # Q value Calculation
    # (self, a_or_b, action, val, reward, alpha, gamma, q_a, q_b, prev_q_a, prev_q_b):
    agent1.update_Qtable(action1[0], action1[1], action1[2], reward, alpha, gamma, Q1a[cur_state], Q1b[cur_state], Q1a[next_state], Q1b[next_state])

    agent2.update_Qtable(action1[0], action2[1], action2[2], reward, alpha,
                         gamma, Q2a[cur_state], Q2b[cur_state], Q2a[next_state], Q2b[next_state])

    # S <- S'
    cur_state = next_state
    print(cur_state)

boutilier(0.1, 0, 0.5, 10)
