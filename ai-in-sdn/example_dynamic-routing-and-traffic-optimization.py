# Reinforcement learning for dynamic routing optimization in SDN
import numpy as np

# Define the network topology and state space
num_states = 5  # Number of network states
num_actions = 3  # Number of routing actions

# Initialize Q-table with zeros
q_table = np.zeros((num_states, num_actions))

# Define the rewards for different routing actions
rewards = np.array([[0, -1, -1],
                    [-1, 0, -1],
                    [-1, -1, 100],
                    [-1, -1, 0],
                    [-1, -1, -1]])

# Q-learning parameters
learning_rate = 0.1
discount_factor = 0.9
num_episodes = 1000

# Q-learning training loop
for episode in range(num_episodes):
    state = np.random.randint(0, num_states)  # Start at a random state
    while True:
        action = np.argmax(q_table[state, :])
        next_state = np.random.choice(num_states)
        reward = rewards[state, action]
        q_table[state, action] = (1 - learning_rate) * q_table[state, action] + \
                                 learning_rate * (reward + discount_factor * np.max(q_table[next_state, :]))
        state = next_state
        if state == 2:  # Destination state
            break

print("Optimal routing Q-table:")
print(q_table)
