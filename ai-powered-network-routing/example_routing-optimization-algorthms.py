# Q-learning for dynamic routing optimization
import numpy as np

# Define the network topology as a graph
network_graph = np.array([[0, 1, 1],
                           [1, 0, 1],
                           [1, 1, 0]])

# Define the Q-table for routing decisions
q_table = np.zeros_like(network_graph, dtype=np.float32)

# Q-learning parameters
learning_rate = 0.1
discount_factor = 0.9
num_episodes = 1000

# Q-learning training loop
for episode in range(num_episodes):
    state = np.random.randint(0, 3)  # Start at a random node
    while True:
        available_actions = np.where(network_graph[state] == 1)[0]
        action = np.random.choice(available_actions)
        next_state = action
        reward = -1  # Negative reward for each step
        q_table[state, action] = (1 - learning_rate) * q_table[state, action] + \
                                 learning_rate * (reward + discount_factor * np.max(q_table[next_state]))
        state = next_state
        if state == 2:  # Destination node
            break

print("Optimal routing Q-table:")
print(q_table)
