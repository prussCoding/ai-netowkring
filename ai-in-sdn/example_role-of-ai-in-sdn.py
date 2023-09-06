# Simulated SDN network resource allocation with AI
import random

# Simulated network devices and resource demand
devices = ['Device A', 'Device B', 'Device C']
resource_demand = [random.randint(1, 10) for _ in range(len(devices))]

# AI-based resource allocation algorithm
def allocate_resources(devices, resource_demand):
    total_resources = 20  # Total available resources in the network
    resource_allocation = {}

    for device, demand in zip(devices, resource_demand):
        allocation = min(demand, total_resources)
        resource_allocation[device] = allocation
        total_resources -= allocation

    return resource_allocation

# Simulate resource allocation with AI
allocation_result = allocate_resources(devices, resource_demand)
print("Resource Allocation Result:")
for device, allocation in allocation_result.items():
    print(f"{device}: {allocation} resources")
