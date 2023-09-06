# Simulate a network failure scenario
import random
import time

def simulate_network_failure():
    print("Simulating network operation...")
    time.sleep(random.uniform(5, 10))
    if random.random() < 0.2:
        print("Network failure detected!")
    else:
        print("Network operation successful.")

simulate_network_failure()
