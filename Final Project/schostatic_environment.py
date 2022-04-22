from agent import Agent
import random

#
k = 0 #placeholder value to be changed
enviroment_partially_schostatic = [[11,-30,0],[-30,random.choice([14,0]),5],[0,0,5]]
enviroment_grid_penaly = [[10,0,k],[0,2,0],[k,0,10]]

def climb(grid, alpha, gamma,ex):

    action_arr = ['a','b','c']
    reward = 0

    # make agents and 2 q tables for each agent
    
    q_a1 = [0, 0, 0]
    q_b1 = [0, 0, 0]
    q_a2 = [0, 0, 0]
    q_b2 = [0, 0, 0]
    agent1 = Agent(q_a1, q_b1, action_arr,ex,reward,alpha,gamma)
    agent2 = Agent(q_a1, q_b1, action_arr,ex,reward,alpha,gamma)
    # choose action
    action1 = Agent.choose_action()
    action2 = Agent.choose_action()

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

    agent1.update_Qtable(action1[0],action1[1],action1[2],reward, alpha,gamma, q_a1,q_b1)
    agent2.update_Qtable(action2[0],action2[1],action2[2],reward, alpha,gamma, q_a2,q_b2)


climb(enviroment_grid, 0.1,0.5,1)

# set reward based on action ,reward
# return
#  make new agent
# action_a = agent.chooseAction()
