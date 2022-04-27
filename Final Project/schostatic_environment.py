from agent import Agent
import random

#
k = 0 #placeholder value to be changed
partial_for_b_b = -1
enviroment_partially_schostatic = [[11,-30,0],[-30,[14,0],5],[0,0,5]] 
enviroment_fully_schostatic = [[[10,12],[5,-65],[8,-8]],[[5,-65],[14,0],[12,0]],[[8,-8],[12,0],[10,0]]] 

def partial_schostatic_climb(grid, alpha, gamma,ex):

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
        index = random.choice([0,1])
        reward = grid[1][1][index]

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

def fully_schostatic_climb(grid, alpha, gamma,ex):

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
        index = random.choice([0,1])
        reward = grid[0][0][index]
    if(action1[1]==0 and action2[1]==1):
        index = random.choice([0,1])
        reward = grid[0][1][index]
    if(action1[1]==0 and action2[1]==2):
        index = random.choice([0,1])
        reward = grid[0][2][index]

    if(action1[1]==1 and action2[1]==0):
        index = random.choice([0,1])
        reward = grid[1][0][index]

    if(action1[1]==1 and action2[1]==1):
        index = random.choice([0,1])
        reward = grid[1][1][index]

    if(action1[1]==1 and action2[1]==2):
        index = random.choice([0,1])
        reward = grid[1][2][index]

    if(action1[1]==2 and action2[1]==0):
        index = random.choice([0,1])
        reward = grid[2][0][index]

    if(action1[1]==2 and action2[1]==1):
        index = random.choice([0,1])
        reward = grid[2][1][index]

    if(action1[1]==2 and action2[1]==2):
        index = random.choice([0,1])
        reward = grid[2][2][index]

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

# def climb_and_penalty(grid, alpha, gamma, ex):
partial_schostatic_climb(enviroment_partially_schostatic, 0.1, 0, 0.5)
fully_schostatic_climb(enviroment_fully_schostatic, 0.1, 0, 0.5)

# set reward based on action ,reward
# return
#  make new agent
# action_a = agent.chooseAction()
