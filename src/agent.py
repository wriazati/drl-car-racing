from collections import deque


class Agent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(2000)

        # Hyperparameters
        self.gamma
        self.epsilon
