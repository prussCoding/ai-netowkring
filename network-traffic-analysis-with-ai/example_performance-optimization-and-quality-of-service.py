# Simple network load balancer example
import random

# List of server IPs
servers = ['192.168.1.101', '192.168.1.102', '192.168.1.103']

# Simulate incoming network traffic requests
def simulate_network_traffic():
    for _ in range(20):
        incoming_request = random.choice(servers)
        print(f"Request to server: {incoming_request}")

# Load balancing algorithm
def load_balance():
    return random.choice(servers)

# Simulate network traffic distribution
for _ in range(20):
    selected_server = load_balance()
    print(f"Load balancing to server: {selected_server}")
