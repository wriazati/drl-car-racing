import gym
env = gym.make('CarRacing-v0')
env.reset()



for i in range(2):

    time = 0
    done = False
    env.reset()
    env.render()

    while not done:
        next_state, reward, done, _ = env.step(env.action_space.sample())
        next_state, reward, done, _ = env.step(env.action_space.sample())
        next_state, reward, done, _ = env.step(env.action_space.sample())
        if time % 50 == 0:
            env.render()
        time += 1




env.close()
