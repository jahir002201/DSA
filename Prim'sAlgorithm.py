import heapq

def prim(graph):
    # Initialize the MST, the priority queue, and the visited set
    mst = []
    visited = set()
    edges = []
    
    # Start from an arbitrary node, here we start from 'A'
    start_node = next(iter(graph))
    visited.add(start_node)
    for weight, neighbor in graph[start_node]:
        heapq.heappush(edges, (weight, start_node, neighbor))
    
    # While there are edges to process
    while edges:
        weight, u, v = heapq.heappop(edges)
        
        # If the vertex is already visited, skip
        if v in visited:
            continue
        
        # Add the edge to the MST and mark the vertex as visited
        visited.add(v)
        mst.append((u, v, weight))
        
        # Add all edges from the newly added vertex to the priority queue
        for next_weight, neighbor in graph[v]:
            if neighbor not in visited:
                heapq.heappush(edges, (next_weight, v, neighbor))
    
    return mst

# Example graph
graph_prim = {
    'A': [(1, 'B'), (4, 'C')],
    'B': [(1, 'A'), (2, 'C'), (5, 'D')],
    'C': [(4, 'A'), (2, 'B'), (1, 'D')],
    'D': [(5, 'B'), (1, 'C')]
}

print("Prim's Minimum Spanning Tree:", prim(graph_prim))
