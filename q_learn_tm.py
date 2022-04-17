import random
import numpy as np
import matplotlib.pyplot as plt

#gridQ is 4*16
#imitates the journey through initial state t
def episode(gridR, gridQ, epsilon, gamma, alpha, reinforcement_averages,
            episode_number, num_iterations):
    #initialize S
    s = 12
    #to get the average reinforcement value, i.e the average reward
    total_episode_rewards = 0
    total_episode_steps = 0
    #loop for each step
    while (s != 15 and s != 0):
      num_iterations += 1
      total_episode_steps += 1
      
      alpha = float(1/num_iterations)
      epsilon = float(1/num_iterations)
      #choose A using epsilon-greedy
      A = epsilon_greedy(gridQ, s, epsilon)
      #store s'
      s1 = calc_s(s, A)
      #observe reward
      r = gridR[s1]

      #to get our average
      total_episode_rewards += r

      #equation
      gridQ[s][A] = gridQ[s][A] + alpha * (r + (gamma * max_value_next_action(s1, gridQ)) - gridQ[s][A])
      
      #set s as s'
      s = s1
    reinforcement_averages[episode_number] += float(total_episode_rewards/total_episode_steps)

    return num_iterations


#policy determination method
#returns the action, number between 0 and 4
def epsilon_greedy(gridQ, i, epsilon):
    n = np.random.random()
    action = -1
    if n < epsilon:
        action = random.choice([0, 1, 2, 3])
        return action
    else:
        #we need the index
        max = 0
        current = 0
        for j in range(4):
            if (gridQ[i][j] > max):
                max = gridQ[i][j]
                current = j
        return current

#max value of next action given a state
def max_value_next_action(index, grid):
    value_max_action = max(grid[index][0], grid[index][1], grid[index][2],
                           grid[index][2])
    return value_max_action

# calculate new state from actiom
def calc_s(s, A):
    if A == 0:
        new_s = s + 1
    elif A == 1:
        new_s = s - 1
    elif A == 2:
        new_s = s + 4
    elif A == 3:
        new_s = s - 4

    if (new_s < 0 or new_s > 15):
        return s
    else:
        return new_s


def q_learning():
    #initialize parameters (I think we already did so)
    num_iterations = 0
    #Loop for each episode
    for i in range(num_episodes):
        num_iterations += episode(gridR, gridQ, epsilon, gamma, alpha, reinforcement_averages, i, num_iterations)

#simulation
gridR = [1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1]
num_episodes= 50
reinforcement_averages = [0.0] * num_episodes
epsilon = 0.25
alpha = 0.1
gamma = 0.9
gridQ = np.zeros((16, 4), dtype=np.float16)

for i in range(10):
    q_learning()

new_re_average = [x / 10 for x in reinforcement_averages]

#now to plot the line graph:
x = np.array(list(range(1, num_episodes + 1)))
y = np.array(new_re_average)

# plotting
plt.title("Line graph")
plt.xlabel("Episode")
plt.ylabel("Average Reinforcement Value")
plt.plot(x, y, color="green")
plt.show()
