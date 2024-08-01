def dfs(capacity, flow, node, sink, path):
    # Base case: if we reached the sink, return True
    if node == sink:
        return True
    
    # Explore all adjacent nodes
    for neighbor in capacity[node]:
        residual_capacity = capacity[node][neighbor] - flow[node].get(neighbor, 0)
        if neighbor not in path and residual_capacity > 0:
            path[neighbor] = node
            if dfs(capacity, flow, neighbor, sink, path):
                return True
    return False

def ford_fulkerson(capacity, source, sink):
    # Initialize flow and maximum flow
    flow = {u: {} for u in capacity}
    max_flow = 0
    
    while True:
        path = {}
        if not dfs(capacity, flow, source, sink, path):
            break
        
        # Find the minimum residual capacity along the path
        path_flow = float('Inf')
        s = sink
        while s != source:
            u = path[s]
            path_flow = min(path_flow, capacity[u][s] - flow[u].get(s, 0))
            s = u
        
        # Update the flow for the path
        v = sink
        while v != source:
            u = path[v]
            flow[u][v] = flow[u].get(v, 0) + path_flow
            flow[v][u] = flow[v].get(u, 0) - path_flow
            v = u
        
        max_flow += path_flow
    
    return max_flow

# Example graph
graph_ford_fulkerson = {
    's': {'a': 10, 'b': 5},
    'a': {'b': 15, 't': 10},
    'b': {'t': 10},
    't': {}
}

print("Ford-Fulkerson Max Flow:", ford_fulkerson(graph_ford_fulkerson, 's', 't'))
