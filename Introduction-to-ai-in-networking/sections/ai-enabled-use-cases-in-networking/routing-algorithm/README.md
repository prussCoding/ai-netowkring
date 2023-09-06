Explanation:

1. We define a NetworkGraph class to represent a weighted graph where nodes are routers or network devices, and edges represent network connections with associated weights (representing distances or costs).
2. The add_edge method allows us to add connections and weights between nodes.
3. The dijkstra method implements Dijkstra's algorithm to find the shortest path from a given starting node to an ending node. This algorithm intelligently determines the routing path based on the weights of the connections.
4. We create a network graph, add connections with weights, and then use Dijkstra's algorithm to find the shortest path from node "A" to node "E."