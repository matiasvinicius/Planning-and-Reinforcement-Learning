from ale_py import ALEInterface
import atari_py
import matplotlib.pyplot as plt
import gym

if __name__ == "__main__":
    env = gym.make("Freeway-v0")
    env.reset()
    env.render()