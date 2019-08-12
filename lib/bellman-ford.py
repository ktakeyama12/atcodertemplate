# Time complexity O(VE)
# Supports negatives
# Slower than Dijkstra O(VlogV), but easier to implement

def bellman_ford(graph, source):
    # Step 1. Prepare distance and predecessor for each node
    distance, predecessor = dict(), dict()
    for node in graph:
        distance[node], predecessor[node] = float('inf'), None
    distance[source] = 0

    # Step 2. Resolve the edges
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor in graph[node]:
                # If the distance between the node and the neighbor is lower than the current, store it
                if distance[neighbor] > distance[node] + graph[node][neighbor]:
                    distance[neighbor], predecessor[neighbor] = distance[node] + graph[node][neighbor], node

    # Step 3. Check for negative weight cycles
    for node in graph:
        for neighbor in graph[node]:
            assert distance[neighbor] <= distance[node] + graph[node][neighbor], "Negative weight cycle."

    return distance, predecessor

if __name__ == '__main__':
    graph = {
        'a': {'b': -1, 'c':  4},
        'b': {'c':  3, 'd':  2, 'e':  2},
        'c': {},
        'd': {'b':  1, 'c':  5},
        'e': {'d': -3}
    }

    distance, predecessor = bellman_ford(graph, source='a')

    print(distance)