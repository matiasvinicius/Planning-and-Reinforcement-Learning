import numpy as np
from random import randint

def create_env(n_rows, n_cols):
    env = np.zeros((n_rows, n_cols))
    env = add_vehicles(env)
    env = add_g_states(env)
    return env

def add_vehicles(env):
    n_rows = env.shape[0]
    n_cols = env.shape[1]

    for row in range(1, n_rows-1):
        column_with_vehicle = randint(0, n_cols-1)
        env[row, column_with_vehicle] = -1
    return env    

def add_g_states(env):
    env[-1] = 1
    return env

def move_vehicles(env):
    n_rows, n_cols = env.shape
    for row in range(1, n_rows-1):
        pos_vechicle = np.where(env[row,] == -1)[0]
        if pos_vechicle > 0: 
            env[row, pos_vechicle-1] = -1
        else:
            env[row, -1] = -1
        env[row, pos_vechicle] = 0
    return env
    
def play(env):
    # The game limit is 02:16 min, or 136 seconds
    # Here, every second will be one epoch
    time_limit = 136

    for epoch in range(time_limit):
        env = move_vehicles(env)
        
if __name__ == "__main__":
    env = create_env(10,6)
    play(env)
