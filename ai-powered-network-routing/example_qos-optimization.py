# Quality of Service (QoS) optimization example
import random

def route_network_traffic(traffic_type):
    if traffic_type == 'voice':
        print("Routing voice traffic with high priority.")
    elif traffic_type == 'video':
        print("Routing video traffic with medium priority.")
    else:
        print("Routing other traffic with low priority.")

# Simulate different types of network traffic
traffic_types = ['voice', 'video', 'data']
for _ in range(5):
    selected_traffic = random.choice(traffic_types)
    route_network_traffic(selected_traffic)
