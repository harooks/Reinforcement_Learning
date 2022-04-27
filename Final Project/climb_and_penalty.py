import enum
import random

from agent import Agent


NUM_OF_EPISODE = 1000
NUM_OF_SIMULATION = 10
environment_grid_climb = [[11,-30,0],[-30,0,5],[0,0,5]]

k = 0 #placeholder value to be changed
environment_grid_penalty = [[10, 0, k], [0, 2, 0], [k, 0, 10]]


def climb_and_penalty(grid, alpha, gamma, ex):

    max_reward = 0
    for row in range(3):
        for col in range(3):
            if grid[row][col] > max_reward:
                max_reward = grid[row][col]


    action_arr = ['a','b','c']
    reward = 0

    q_a1 = [0, 0, 0]
    q_b1 = [0, 0, 0]
    q_a2 = [0, 0, 0]
    q_b2 = [0, 0, 0]

    # make agents and 2 q tables for each agent
    agent1 = Agent(q_a1, q_b1, action_arr, ex, reward, alpha, gamma)
    agent2 = Agent(q_a2, q_b2, action_arr, ex, reward, alpha, gamma)

    count = 0
    for episode in range(NUM_OF_EPISODE):
        reward = 0

        # choose action
        action1 = agent1.choose_action() # does this take in q_a and q_b??
        action2 = agent2.choose_action()

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

        # reinforcement_val += reward
        # reinforcement_val_arr[episode] += reinforcement_val

        # Update Q value
        ## QUESTION: since there is only one policy, is next state current state?
        # Q[cur_row][cur_col][action] = val + (alpha * (reward + (gamma * max(Q[next_row][next_col])) - val))
        next_q_a1 = q_a1
        next_q_b1 = q_b1

        next_q_a2 = q_a2
        next_q_b2 = q_b2

        agent1.update_Qtable(
            action1[0], action1[1], action1[2], reward, alpha, gamma, q_a1, q_b1, next_q_a1, next_q_b1)
        agent2.update_Qtable(
            action2[0], action2[1], action2[2], reward, alpha, gamma, q_a2, q_b2, next_q_a2, next_q_b2)

        # Count max reward numbers
        #print("max reward is:", max_reward, "reward is: ", reward)
        if reward == max_reward:
            count += 1

    # return proportion
    print((count / NUM_OF_EPISODE) * 100)
    return (count / NUM_OF_EPISODE) * 100


# def climb_and_penalty(grid, alpha, gamma, ex):
climb_and_penalty(environment_grid_penalty, 0.1, 0, 0.5)



# set reward based on action ,reward
# return
#  make new agent
# action_a = agent.chooseAction()
