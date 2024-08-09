def has_cycle(graph):
    def dfs(node, visited, recursion_stack):
        # Mark the current node as visited and add it to the recursion stack
        visited.add(node)
        recursion_stack.add(node)
        
        # Recur for all vertices adjacent to this vertex
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor, visited, recursion_stack):
                    return True
            elif neighbor in recursion_stack:
                return True
        
        # Remove the vertex from recursion stack
        recursion_stack.remove(node)
        return False

    # Set to track visited nodes
    visited = set()
    # Set to track nodes currently in the recursion stack
    recursion_stack = set()
    
    # Call the recursive helper function for all vertices
    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, visited, recursion_stack):
                return True
                
    return False

# Example graph with a cycle
graph_with_cycle = {
    1: [2],
    2: [3],
    3: [4],
    4: [1]  
}

print("Graph has cycle:", has_cycle(graph_with_cycle))
