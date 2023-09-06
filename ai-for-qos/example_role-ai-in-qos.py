# AI-driven QoS traffic prioritization
import random

# Simulated network traffic with different priorities
network_traffic = [
    {'source': 'Server A', 'destination': 'Client 1', 'priority': 'High'},
    {'source': 'Server B', 'destination': 'Client 2', 'priority': 'Low'},
    {'source': 'Server C', 'destination': 'Client 3', 'priority': 'Medium'},
]

# AI-based traffic prioritization algorithm
def prioritize_traffic(traffic):
    for packet in traffic:
        if packet['priority'] == 'High':
            print(f"Prioritizing {packet['source']} to {packet['destination']} (High Priority)")
        elif packet['priority'] == 'Medium':
            print(f"Prioritizing {packet['source']} to {packet['destination']} (Medium Priority)")
        else:
            print(f"Prioritizing {packet['source']} to {packet['destination']} (Low Priority)")

# Simulate traffic prioritization with AI
prioritize_traffic(network_traffic)
