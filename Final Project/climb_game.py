import enum
import random
import numpy as np

from agent import Agent
from random_agent import AgentR

NUM_OF_EPISODE = 1000
NUM_OF_SIMULATION = 500

new_environment = [[11, -30, 0, 5], [-30, 7, 6, 0], [0, 0, 5, -30]]
new_environment_grid_penalty = [[10, 0, 0, -10], [0, 2, 0, -10], [0, 0, 10, -10]]


def climb_and_penalty(grid, alpha, gamma, ex):
    reward_arr = []
    percentage_arr = []

    max_reward = 0
    for row in range(3):
        for col in range(4):
            if grid[row][col] > max_reward:
                max_reward = grid[row][col]

    action_arr_1 = ['a', 'b', 'c']
    action_arr_2 = ['a', 'b', 'c', 'd']

    for simulation in range(NUM_OF_SIMULATION):
        q_a1 = [0, 0, 0]
        q_b1 = [0, 0, 0]
        q_a2 = [0, 0, 0, 0]
        q_b2 = [0, 0, 0, 0]

        reward = 0
        # make agents and 2 q tables for each agent
        agent1 = Agent(q_a1, q_b1, action_arr_1, reward, alpha, gamma)
        agent2 = AgentR(q_a2, q_b2, action_arr_2, reward, alpha, gamma)

        count = 0
        T = 1
        for episode in range(NUM_OF_EPISODE):
            if episode == 0:
                ex = 1
            else:
                ex = 1 / T

            reward = 0

            # choose action
            action1 = agent1.choose_action(ex)
            action2 = agent2.choose_action(ex)

            #index 1 is where action is
            if(action1[1] == 0 and action2[1] == 0):
                reward = grid[0][0]

            if(action1[1] == 0 and action2[1] == 1):
                reward = grid[0][1]

            if(action1[1] == 0 and action2[1] == 2):
                reward = grid[0][2]

            if(action1[1] == 0 and action2[1] == 3):
                reward = grid[0][3]

            if(action1[1] == 1 and action2[1] == 0):
                reward = grid[1][0]

            if(action1[1] == 1 and action2[1] == 1):
                reward = grid[1][1]

            if(action1[1] == 1 and action2[1] == 2):
                reward = grid[1][2]

            if(action1[1] == 1 and action2[1] == 3):
                reward = grid[1][3]

            if(action1[1] == 2 and action2[1] == 0):
                reward = grid[2][0]

            if(action1[1] == 2 and action2[1] == 1):
                reward = grid[2][1]

            if(action1[1] == 2 and action2[1] == 2):
                reward = grid[2][2]

            if(action1[1] == 2 and action2[1] == 3):
                reward = grid[2][3]

            # reinforcement_val += reward
            # reinforcement_val_arr[episode] += reinforcement_val

            # Update Q value
            ## QUESTION: since there is only one policy, is next state current state?
            # Q[cur_row][cur_col][action] = val + (alpha * (reward + (gamma * max(Q[next_row][next_col])) - val))
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

            # Count max reward numbers
            #print("max reward is:", max_reward, "reward is: ", reward)
            if reward == max_reward:
                count += 1
            T += 1
        percentage = (count / NUM_OF_EPISODE) * 100
        percentage_arr.append(percentage)

    mean_per = np.mean(percentage_arr)
    # print(percentage_arr)
    # return proportion
    # print("q_a1:", q_a1, "q_b1:", q_a2, "max:", max_reward)

    # x = np.arange(NUM_OF_EPISODE)
    # y = np.array(reward_arr)
    # plt.plot(x, y, color="green")
    # plt.show()

    print(mean_per)
    return mean_per


# def climb_and_penalty(grid, alpha, gamma, ex):
climb_and_penalty(new_environment, 0.1, 0, 1)
