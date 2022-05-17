import enum
import random
import numpy as np
import matplotlib.pyplot as plt
from agent_softmax import Agent_softmax
import math

from agent import Agent
from random_agent import AgentR


NUM_OF_EPISODE = 1000
NUM_OF_SIMULATION = 500

def climb_and_penalty(grid, alpha, gamma, ex):
    reward_arr = []
    percentage_arr = []

    max_reward = 0
    for row in range(3):
        for col in range(3):
            if grid[row][col] > max_reward:
                max_reward = grid[row][col]

    action_arr = ['a','b','c']
    reinforcement_val_arr = [0 for _ in range(NUM_OF_EPISODE)]

    for simulation in range(NUM_OF_SIMULATION):

        reward = 0
        reinforcement_val = 0
        q_a1 = [0, 0, 0]
        q_b1 = [0, 0, 0]
        q_a2 = [0, 0, 0]
        q_b2 = [0, 0, 0]

        # make agents and 2 q tables for each agent
        agent1 = Agent_softmax(q_a1, q_b1, action_arr, reward, alpha, gamma)
        agent2 = Agent_softmax(q_a2, q_b2, action_arr, reward, alpha, gamma)

        count = 0
        T = 1
        temp = 0
        # print("simulation", simulation, "ex:", ex)
        for episode in range(NUM_OF_EPISODE):

            reward = 0
            temp = 500 * math.exp(-0.006 * episode) + 1
            
            # choose action
            action1 = agent1.choose_action_softmax(temp) # does this take in q_a and q_b??
            action2 = agent2.choose_action_softmax(temp)


            #index 1 is where action is
            if(action1[1]==0 and action2[1]==0):
                reward = grid[0][0]

            if(action1[1]==0 and action2[1]==1):
                reward = grid[0][1]

            if(action1[1]==0 and action2[1]==2):
                reward = grid[0][2]

            if(action1[1]==1 and action2[1]==0):
                reward = grid[1][0]

            if(action1[1]==1 and action2[1]==1):
                reward = grid[1][1]

            if(action1[1]==1 and action2[1]==2):
                reward = grid[1][2]

            if(action1[1]==2 and action2[1]==0):
                reward = grid[2][0]

            if(action1[1]==2 and action2[1]==1):
                reward = grid[2][1]

            if(action1[1]==2 and action2[1]==2):
                reward = grid[2][2]

            next_q_a1 = q_a1
            next_q_b1 = q_b1

            next_q_a2 = q_a2
            next_q_b2 = q_b2

            # (self, a_or_b, action, val, reward, alpha, gamma, q_a, q_b, next_q_a, next_q_b)
            agent1.update_Qtable(
                action1[0], action1[1], action1[2], reward, alpha, gamma, q_a1, q_b1, next_q_a1, next_q_b1)
            agent2.update_Qtable(
                action2[0], action2[1], action2[2], reward, alpha, gamma, q_a2, q_b2, next_q_a2, next_q_b2)

            ## add reward in array
            reward_arr.append(reward)
            reinforcement_val_arr[episode] += reward

            # Count max reward numbers
            #print("max reward is:", max_reward, "reward is: ", reward)
            if reward == max_reward:
                count += 1
            T += 1
        percentage = (count / NUM_OF_EPISODE) * 100
        percentage_arr.append(percentage)

    mean_per = np.mean(percentage_arr)

    for episode in range(NUM_OF_EPISODE):
        reinforcement_val_arr[episode] /= NUM_OF_SIMULATION

    x = np.arange(NUM_OF_EPISODE)
    y = np.array(reinforcement_val_arr)
    plt.plot(x, y, color="green")
    plt.show()

    print(mean_per)
    return mean_per

environment_grid_climb = [[11, -30, 0], [-30, 7, 6], [0, 0, 5]]

k = -100  # placeholder value to be changed
environment_grid_penalty = [[10, 0, k], [0, 2, 0], [k, 0, 10]]
# def climb_and_penalty(grid, alpha, gamma, ex):
climb_and_penalty(environment_grid_climb, 0.1, 0, 1)
# Climb: 17.5002
# Penalty k=0: 86.126
# Penalty k=100: 61.0236
