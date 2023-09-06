import heapq

class NetworkGraph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []
        
        self.graph[node1].append((node2, weight))
        self.graph[node2].append((node1, weight))

    def dijkstra(self, start_node, end_node):
        # Initialize distance and visited dictionaries
        distances = {node: float('inf') for node in self.graph}
        visited = {}
        distances[start_node] = 0

        # Priority queue to track nodes to visit
        priority_queue = [(0, start_node)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            visited[current_node] = True

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances[end_node]

# Create a network graph
network = NetworkGraph()

# Add edges with weights (representing network connections)
network.add_edge("A", "B", 2)
network.add_edge("A", "C", 4)
network.add_edge("B", "C", 1)
network.add_edge("B", "D", 7)
network.add_edge("C", "D", 3)
network.add_edge("D", "E", 1)

# Find the shortest path from node A to E using Dijkstra's algorithm
shortest_distance = network.dijkstra("A", "E")

print(f"Shortest Distance from A to E: {shortest_distance}")
