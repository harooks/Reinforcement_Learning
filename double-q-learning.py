## Climb and penalty game
# agent A , randomly select state from a,b or c
# arrayA[a,b,c] (array of different state)
# agent B
# arrayB[a,b,c] (array of different state)

import enum
import random

climbing_matrix = [[11,-30,0],[-30,7,6],[0,0,5]]
agentA = [0,0,0]
agentB = [0, 0, 0]


#a and b picking one is one time step and one episode

def climb_and_penalty(matrix, ex):
    q_a = [0, 0, 0]  # a, b, c
    q_b = [0, 0, 0]  # a, b, c

    state_a = 0 # index within array
    state_b = 0

    # greedy choice
    if random.random() > ex:
        val_a = max(q_a)
        action_a = q_a.index(val_a)

        val_b = max(q_b)
        action_b = q_b.index(val_b)
    else: #random
        action_a = random.randrange(0, 3) # index of action choice chosen randomly
        val_a = q_a[action_a] # the q value of the action chosen

        action_b = random.randrange(0, 3)
        val_b = q_a[action_b]  # the q value of the action chosen
