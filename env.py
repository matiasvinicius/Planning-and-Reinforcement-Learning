import numpy as np
from random import randint

def create_env(n_rows, n_cols):
    env = np.full((n_rows, n_cols), '-')
    env = add_margin(env)
    env = add_vehicles(env)
    env = add_player(env)
    return env

def add_vehicles(env):
    n_rows = env.shape[0]
    n_cols = env.shape[1]

    for row in range(1, n_rows-1):
        column_with_vehicle = randint(0, n_cols-1)
        env[row, column_with_vehicle] = 'O'
    return env    

def add_player(env):
    env[0,2] = 'A'
    return env

def add_margin(env):
    env[0] = 'I'
    env[-1] = 'F'
    return env

def move_vehicles(env):
    n_rows, n_cols = env.shape
    for row in range(1, n_rows-1):
        pos_vechicle = np.where(env[row,] == 'O')[0]
        if pos_vechicle > 0: 
            env[row, pos_vechicle-1] = 'O'
        else:
            env[row, -1] = 'O'
        env[row, pos_vechicle] = '-'
    return env
    
def transition_matrix(states, actions):
    n_states = len(states)
    n_actions = len(actions)
    transition = np.zeros((n_states, n_actions, n_states))  
    
    for state in states:
        for action in range(n_actions):
            s_linha = state + actions[action]
            if s_linha < 0 or s_linha >= n_states:
                s_linha = state
            transition[state, action, s_linha] = 1
    return transition

def play(env):
    # The game limit is 02:16 min, or 136 seconds
    # Here, every second will be one epoch
    time_limit = 136
    actions = np.array([1, 0, -1])
    rewards = {'O':-1, '-':0, 'F':1}
    states = np.arange(len(env))
    transition = transition_matrix(states, actions)

    print(transition[0,2,0])

    #for epoch in range(time_limit):
    #    env = move_vehicles(env)

        
if __name__ == "__main__":
    env = create_env(10,6)
    play(env)

    
