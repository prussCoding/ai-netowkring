import heapq
import logging

# Set logging basic configuration
logging.basicConfig(format='%(levelname)s:  %(message)s - (Line no: %(lineno)d)', level=logging.DEBUG)
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
        logging.info(f'Instantiating Distance Dictionay: {distances}')
        visited = {}
        logging.info(f'Instantiating Visted Dictionay: {visited}')
        distances[start_node] = 0
        logging.info(f'Setting Start Node to Distances: {distances}')

        # Priority queue to track nodes to visit
        priority_queue = [(0, start_node)]
        logging.info(f'Setting Priority Queue: {priority_queue}')

        while priority_queue:
            logging.info(f'Current Proirity Queue: {priority_queue}')
            current_distance, current_node = heapq.heappop(priority_queue)
            logging.info(msg=f'Called Heapq func(Pop) return values: ({current_distance}, {current_node}) -> Priority Queue: {priority_queue}')

            if current_node in visited:
                logging.info(f'Current node ({current_node}) was found in Visted Dictionary')
                continue

            visited[current_node] = True
            logging.info(f'Add Current Node ({current_node}) to Visited Dictionary: {visited}')

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight
                logging.info(f'Neighbor ({neighbor}) Distance Calculation: {current_distance} + {weight} = {distance}')
                if distance < distances[neighbor]:
                    distances[neighbor] = distance  
                    logging.info(f'Add Neigbhor ({neighbor}) to Distance Dictionary: {distances}') 
                    heapq.heappush(priority_queue, (distance, neighbor))
                    logging.info(f'Called Heapq func(Push) with params: ({distance}, {neighbor}) -> Priority Queue: {priority_queue}')
                    
                    
        logging.info(f'Returning Distance: {distances[end_node]}')   
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
start_node = "B"
end_node = "D"
shortest_distance = network.dijkstra(start_node=start_node, end_node=end_node)

logging.info(f"Shortest Distance from {start_node} to {end_node}: {shortest_distance}")
