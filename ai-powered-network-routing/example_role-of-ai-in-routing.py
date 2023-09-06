# Simulated network traffic and routing optimization
import random

def simulate_network_traffic():
    servers = ['Server A', 'Server B', 'Server C']
    for _ in range(10):
        source, destination = random.sample(servers, 2)
        print(f"Sending data from {source} to {destination}")

simulate_network_traffic()
