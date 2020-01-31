import gym
import numpy as np

# Variables
num_episodes = 2
reward_on_crash = -10
render_freq = 40

def run():
    for e in range(num_episodes):
        t = 0
        crashed = False
        state = env.reset()

        while not crashed:
            next_state, reward, crashed, _ = env.step(env.action_space.sample())
            reward = calculate_reward(reward, crashed)

            if crashed:
                print("episode: {}/{}, score: {}, e: {:.2}".format(e, num_episodes-1, t, 0.0))

            if t % render_freq == 0:
                env.render()

            t += 1

        pass

def calculate_reward(reward, crashed):
    return reward if not crashed else reward_on_crash

if __name__ == "__main__":

    # Create environment
    env = gym.make('CarRacing-v0')
    env.reset()
    run()
    env.close()
    # state_shape = np.array(env.observation_space.shape)