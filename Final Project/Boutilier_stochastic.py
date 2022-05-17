import enum
import random
import numpy as np
import matplotlib.pyplot as plt

from agent import Agent
from random_agent import AgentR 

NUM_OF_EPISODE = 1000
NUM_OF_SIMULATION = 500


def boutilier(alpha, gamma, ex, k):
  percentage_arr = []
  action_arr = ['a', 'b']
  max_reward = max(7, k, 11)
  reinforcement_val_arr = [0 for _ in range(NUM_OF_EPISODE)]

  for simulation in range(NUM_OF_SIMULATION):
    # each state and action is a key and the q-Val is the value
    Q1a = [[0, 0] for _ in range(6)]
    Q1b = [[0, 0] for _ in range(6)]
    Q2a = [[0, 0] for _ in range(6)]
    Q2b = [[0, 0] for _ in range(6)]

    reward = 0
    cur_state = 0
    agent1 = Agent(Q1a[cur_state], Q1b[cur_state],
                   action_arr, reward, alpha, gamma)
    agent2 = Agent(Q2a[cur_state], Q2b[cur_state],
                   action_arr, reward, alpha, gamma)

    count = 0
    T = 1
    for episode in range(NUM_OF_EPISODE):
      if episode == 0:
        ex = 1
      else:
        ex = 1 / T
      reward = 0
      reinforcement_val = 0
      # initialize current state to 0 (S1)
      cur_state = 0  # S1
      # [S1, S2, S3, S4, S5, S6]
      while not(cur_state == 3) and not(cur_state == 4) and not(cur_state == 5):

        # take action
        action1 = agent1.choose_action(ex)
        action2 = agent2.choose_action(ex)

        # print("agent 1 chose: ", action1[1])
        # print("agent 2 chose: ", action2[1])
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
        agent1.update_Qtable(action1[0], action1[1], action1[2], reward, alpha,
                             gamma, Q1a[cur_state], Q1b[cur_state], Q1a[next_state], Q1b[next_state])

        agent2.update_Qtable(action1[0], action2[1], action2[2], reward, alpha,
                             gamma, Q2a[cur_state], Q2b[cur_state], Q2a[next_state], Q2b[next_state])

        # S <- S'
        cur_state = next_state

      # Put reward in array
      reinforcement_val += reward
      reinforcement_val_arr[episode] += reinforcement_val

      if reward == max_reward:
        count += 1
      T += 1

  for episode in range(NUM_OF_EPISODE):
      reinforcement_val_arr[episode] /= NUM_OF_SIMULATION

  # x = np.arange(NUM_OF_EPISODE)
  # y = np.array(reinforcement_val_arr)
  # plt.plot(x, y, color="green")
  # plt.show()
  percentage = (count / NUM_OF_EPISODE) * 100
  percentage_arr.append(percentage)

  mean_per = np.mean(percentage_arr)
  print(mean_per)
  return reinforcement_val_arr

def boutilier_d_R(alpha, gamma, ex, k):
  percentage_arr = []
  action_arr = ['a', 'b']
  max_reward = max(7, k, 11)
  reinforcement_val_arr = [0 for _ in range(NUM_OF_EPISODE)]

  for simulation in range(NUM_OF_SIMULATION):
    # each state and action is a key and the q-Val is the value
    Q1a = [[0, 0] for _ in range(6)]
    Q1b = [[0, 0] for _ in range(6)]
    Q2a = [[0, 0] for _ in range(6)]
    Q2b = [[0, 0] for _ in range(6)]

    reward = 0
    cur_state = 0
    agent1 = Agent(Q1a[cur_state], Q1b[cur_state],
                   action_arr, reward, alpha, gamma)
    agent2 = AgentR(Q2a[cur_state], Q2b[cur_state],
                   action_arr, reward, alpha, gamma)

    count = 0
    T = 1
    for episode in range(NUM_OF_EPISODE):
      if episode == 0:
        ex = 1
      else:
        ex = 1 / T
      reward = 0
      reinforcement_val = 0
      # initialize current state to 0 (S1)
      cur_state = 0  # S1
      # [S1, S2, S3, S4, S5, S6]
      while not(cur_state == 3) and not(cur_state == 4) and not(cur_state == 5):

        # take action
        action1 = agent1.choose_action(ex)
        action2 = agent2.choose_action(ex)

        # print("agent 1 chose: ", action1[1])
        # print("agent 2 chose: ", action2[1])
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
        agent1.update_Qtable(action1[0], action1[1], action1[2], reward, alpha,
                             gamma, Q1a[cur_state], Q1b[cur_state], Q1a[next_state], Q1b[next_state])

        agent2.update_Qtable(action1[0], action2[1], action2[2], reward, alpha,
                             gamma, Q2a[cur_state], Q2b[cur_state], Q2a[next_state], Q2b[next_state])

        # S <- S'
        cur_state = next_state

      # Put reward in array
      reinforcement_val += reward
      reinforcement_val_arr[episode] += reinforcement_val

      if reward == max_reward:
        count += 1
      T += 1

  for episode in range(NUM_OF_EPISODE):
      reinforcement_val_arr[episode] /= NUM_OF_SIMULATION

  # x = np.arange(NUM_OF_EPISODE)
  # y = np.array(reinforcement_val_arr)
  # plt.plot(x, y, color="green")
  # plt.show()
  percentage = (count / NUM_OF_EPISODE) * 100
  percentage_arr.append(percentage)

  mean_per = np.mean(percentage_arr)
  print(mean_per)
  return reinforcement_val_arr

def boutilier_r_r(alpha, gamma, ex, k):
  percentage_arr = []
  action_arr = ['a', 'b']
  max_reward = max(7, k, 11)
  reinforcement_val_arr = [0 for _ in range(NUM_OF_EPISODE)]

  for simulation in range(NUM_OF_SIMULATION):
    # each state and action is a key and the q-Val is the value
    Q1a = [[0, 0] for _ in range(6)]
    Q1b = [[0, 0] for _ in range(6)]
    Q2a = [[0, 0] for _ in range(6)]
    Q2b = [[0, 0] for _ in range(6)]

    reward = 0
    cur_state = 0
    agent1 = AgentR(Q1a[cur_state], Q1b[cur_state],
                   action_arr, reward, alpha, gamma)
    agent2 = AgentR(Q2a[cur_state], Q2b[cur_state],
                   action_arr, reward, alpha, gamma)

    count = 0
    T = 1
    for episode in range(NUM_OF_EPISODE):
      if episode == 0:
        ex = 1
      else:
        ex = 1 / T
      reward = 0
      reinforcement_val = 0
      # initialize current state to 0 (S1)
      cur_state = 0  # S1
      # [S1, S2, S3, S4, S5, S6]
      while not(cur_state == 3) and not(cur_state == 4) and not(cur_state == 5):

        # take action
        action1 = agent1.choose_action(ex)
        action2 = agent2.choose_action(ex)

        # print("agent 1 chose: ", action1[1])
        # print("agent 2 chose: ", action2[1])
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
        agent1.update_Qtable(action1[0], action1[1], action1[2], reward, alpha,
                             gamma, Q1a[cur_state], Q1b[cur_state], Q1a[next_state], Q1b[next_state])

        agent2.update_Qtable(action1[0], action2[1], action2[2], reward, alpha,
                             gamma, Q2a[cur_state], Q2b[cur_state], Q2a[next_state], Q2b[next_state])

        # S <- S'
        cur_state = next_state

      # Put reward in array
      reinforcement_val += reward
      reinforcement_val_arr[episode] += reinforcement_val

      if reward == max_reward:
        count += 1
      T += 1

  for episode in range(NUM_OF_EPISODE):
      reinforcement_val_arr[episode] /= NUM_OF_SIMULATION

  # x = np.arange(NUM_OF_EPISODE)
  # y = np.array(reinforcement_val_arr)
  # plt.plot(x, y, color="green")
  # plt.show()
  percentage = (count / NUM_OF_EPISODE) * 100
  percentage_arr.append(percentage)

  mean_per = np.mean(percentage_arr)
  print(mean_per)
  return reinforcement_val_arr
# boutilier(alpha, gamma, ex, k)
# boutilier(0.1, 0, 0.1, 0)
x = np.arange(NUM_OF_EPISODE)
plt.plot(x, boutilier(0.1, 0.9, 1, 0), label = "doubleQ and doubleQ")
plt.plot(x, boutilier_d_R(0.1, 0.9, 1, 0), label = "doubleQ and random")
plt.plot(x, boutilier_r_r(0.1, 0.9, 1, 0), label = "random and random")
plt.legend()
plt.show()
# boutilier(0.1, 0.9, 1, -100)
