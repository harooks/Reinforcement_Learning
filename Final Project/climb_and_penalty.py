import enum
import random

from agent import Agent


NUM_OF_EPISODE = 200
NUM_OF_SIMULATION = 10
environment_grid = [[11,-30,0],[-30,0,5],[0,0,5]]

k = 0 #placeholder value to be changed
enviroment_grid_penaly = [[10,0,k],[0,2,0],[k,0,10]]


def climb_and_penalty(grid, alpha, gamma, ex):


    action_arr = ['a','b','c']
    reinforcement_val = 0
    reinforcement_val_arr = [0 for _ in range(NUM_OF_EPISODE)]
    reward = 0

    q_a1 = [0, 0, 0]
    q_b1 = [0, 0, 0]
    q_a2 = [0, 0, 0]
    q_b2 = [0, 0, 0]

    # make agents and 2 q tables for each agent
    agent1 = Agent(q_a1, q_b1, action_arr, ex, reward, alpha, gamma)
    agent2 = Agent(q_a1, q_b1, action_arr, ex, reward, alpha, gamma)


    for episode in range(NUM_OF_EPISODE):

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
        agent1.update_Qtable(action1[0], action1[1], action1[2], reward, alpha, gamma, q_a1, q_b1)
        agent2.update_Qtable(action2[0], action2[1], action2[2], reward, alpha, gamma, q_a2, q_b2)


# def climb_and_penalty(grid, alpha, gamma, ex):
climb_and_penalty(environment_grid, 0.1, 0, 0.5)



# set reward based on action ,reward
# return
#  make new agent
# action_a = agent.chooseAction()
