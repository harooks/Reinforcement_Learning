import enum
import random
import numpy as np
import matplotlib.pyplot as plt

NUM_OF_EXPERIENCE = 200
NUM_OF_SIMULATION = 10
BOARD_ROWS = 4
BOARD_COLS = 4

# row col action
def qLearning(alpha, gamma, ex):
    # alpha = learning rate
    # how much you value reward
    # for simulation in range(10):
    # do 300 times, 10 times
    reinforcement_val_arr = [0 for _ in range(NUM_OF_EXPERIENCE)]
    for simulation in range(10):

        ## Episode
        T = 1
        Q = [[[0 for _ in range(4)] for _ in range(BOARD_COLS)]
             for _ in range(BOARD_ROWS)]
        for episode in range(NUM_OF_EXPERIENCE):

            # Starting point
            cur_row = 3
            cur_col = 0
            reinforcement_val = 0

            if alpha == 1:
                alpha = 1 / T

            if ex == 1:
                ex = 1 / T

            while not(cur_row == 0 and cur_col == 0) and not(cur_row == 3 and cur_col == 3):

                #Choose action depending on random val
                if random.random() > ex:
                # don't explore = greedy
                    val = max(Q[cur_row][cur_col])
                    action = Q[cur_row][cur_col].index(val)
                else:
                    action = random.randrange(0, 4)
                    val = Q[cur_row][cur_col][action]

                next_row = cur_row
                next_col = cur_col

                # take action
                # up
                if action == 0 and cur_row != 0:
                    next_row -= 1

                # down
                elif action == 1 and cur_row != 3:
                    next_row += 1

                # left
                elif action == 2 and cur_col != 0:
                    next_col -= 1

                # right
                elif action == 3 and cur_col != 3:
                    next_col += 1

                # Calculate reward
                if (next_row == 0 and next_col == 0) or (next_row == 3 and next_col == 3):
                    reward = 1
                else:
                    reward = -1

                # Add reinforcement_val
                reinforcement_val += reward

                # QQ
                Q[cur_row][cur_col][action] = val + (alpha * (reward + (gamma * max(Q[next_row][next_col])) - val))

                # S <- S'
                cur_row = next_row
                cur_col = next_col
                T += 1

            reinforcement_val_arr[episode] += reinforcement_val

    for episode in range(NUM_OF_EXPERIENCE):
        reinforcement_val_arr[episode] /= 10

    x = np.arange(NUM_OF_EXPERIENCE)
    y = np.array(reinforcement_val_arr)
    plt.plot(x, y, color="green")
    plt.show()

# qLearning(alpha, gamma, ex):


# qLearning(0.1, 0.9, 0.25)
qLearning(1, 0.9, 1)
# qLearning(0.1, 0.9, 1)
# qLearning(1, 0.9, 0.1)
# qLearning(1, 1, 1)
