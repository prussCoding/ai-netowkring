# Real-world QoS optimization with AI in a network simulation
import networkx as nx
import random

# Create a network topology
G = nx.Graph()
G.add_edge('Router A', 'Switch 1', weight=10)
G.add_edge('Switch 1', 'Server 1', weight=5)
G.add_edge('Switch 1', 'Server 2', weight=3)

# Simulate network traffic
traffic_load = {'Server 1': random.randint(1, 10), 'Server 2': random.randint(1, 10)}

# AI-driven QoS optimization algorithm
def optimize_qos(network, traffic):
    for node, load in traffic.items():
        if load > 5:
            print(f"Optimizing QoS for {node}...")
            # Implement QoS optimization logic here
        else:
            print(f"Traffic load for {node} is within acceptable limits.")

# Simulate real-world QoS optimization with AI
optimize_qos(G, traffic_load)
