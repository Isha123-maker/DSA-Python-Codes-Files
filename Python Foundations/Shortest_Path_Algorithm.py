# Define a weighted graph using an adjacency list.
# Each key is a node, and its value is a list of (neighbor, distance) tuples.
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

# Function to compute the shortest path from a start node to all others.
# This is a variant of Dijkstra's algorithm.
def shortest_path(graph, start, target = ''):
    # Keep track of unvisited nodes
    unvisited = list(graph)

    # Distance dictionary: start = 0, everything else = infinity
    distances = {node: 0 if node == start else float('inf') for node in graph}

    # Paths dictionary: keeps track of the actual path taken to each node
    paths = {node: [] for node in graph}
    paths[start].append(start)  # Path to start is just itself
    
    # Loop until all nodes are visited
    while unvisited:
        # Pick the unvisited node with the smallest distance so far
        current = min(unvisited, key=distances.get)

        # Check each neighbor of the current node
        for node, distance in graph[current]:
            # If going through current gives a shorter path to this neighbor
            if distance + distances[current] < distances[node]:
                # Update the distance
                distances[node] = distance + distances[current]

                # Update the path:
                # If node already has a path and ends with itself, overwrite with current’s path
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    # Otherwise, extend the existing path with current’s path
                    paths[node].extend(paths[current])
                # Add this neighbor to the path
                paths[node].append(node)

        # Mark the current node as visited
        unvisited.remove(current)
    
    # Decide which nodes to print results for
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        # Print both distance and path from start to this node
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    # Return results so they can be used later if needed
    return distances, paths
    
# Example: find shortest paths starting from 'F'
shortest_path(my_graph, 'F')
