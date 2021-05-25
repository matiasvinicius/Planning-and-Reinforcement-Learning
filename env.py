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

def move_player(env, pos_A, new_pos_A):
    env[pos_A] = '-'
    if env[new_pos_A] == 'O':
        env[0,2] = 'A'
    else: env[new_pos_A] = 'A'
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
    
def is_valid_state(state, n_states):
    if state < 0 or state >= n_states: return False
    return True

def transition_matrix(states, actions):
    n_states = len(states)
    n_actions = len(actions)
    transition = np.zeros((n_states, n_actions, n_states))  
    
    for state in states:
        for action in range(n_actions):
            s_linha = state + actions[action]
            if (s_linha < 0 or 
            s_linha >= n_states or 
            state == (n_states)-1):
                s_linha = state
            transition[state, action, s_linha] = 1
    return transition

def play(env):
    # The game limit is 02:16 min, or 136 seconds
    # Here, every second will be one epoch
    time_limit = 10
    actions = np.array([1, 0, -1])
    rewards = {'O':-1, '-':0, 'A':0, 'F':1}
    states = np.arange(len(env))
    transition = transition_matrix(states, actions)
    
    gamma = 0.9
    delta = 0 # diferença entre política anterior e atual
    n_states = len(states)

    #initialize v arbitratily e.g. V(s) = 0 for all s in S
    V = {s: 0 for s in states}

    for s in reversed(states):
        cur_a = -1
        cur_max = -1
        for a in actions:
            if is_valid_state(s+a, n_states):
                for s_linha in states:
                    print("s:", s, 
                    "| a:", a, 
                    "| s':", s_linha, 
                    "| Pr(s'|s, a) =", transition[s,a,s_linha],
                    "| r(s'):", rewards[env[s_linha, 2]],
                    "| V(s'):", V[s_linha],
                    "| V(s) = ", (rewards[env[s_linha, 2]] + gamma*transition[s,a,s_linha]*V[s_linha]))
            
    #return V

    #for epoch in range(time_limit):
    #    env = move_vehicles(env)
    #    print(env)    


if __name__ == "__main__":
    env = create_env(10,6)
    print(play(env))
    print(env)