def bellman_ford(graph, start):
    # Initialize distances from start to all nodes as infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Relax all edges |V| - 1 times (where |V| is the number of vertices)
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node]:
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
    
    # Check for negative weight cycles
    for node in graph:
        for neighbor, weight in graph[node]:
            if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                raise ValueError("Graph contains a negative weight cycle")
    
    return distances

# Example graph
graph_bellman_ford = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

print("Bellman-Ford Shortest Paths:", bellman_ford(graph_bellman_ford, 'A'))
