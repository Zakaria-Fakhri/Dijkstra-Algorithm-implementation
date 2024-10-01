import heapq

def dijkstra(s, adj_list, length):
    # Initialization
    distance = {}
    for v in adj_list:
        distance[v] = float('inf')  # All other nodes have initial
    distance[s] = 0  # Start node s has distance 0

    predecessor = {}# Empty array for each node to store predecessors
    for v in adj_list:
        predecessor[v] = []
  

    # Priority queue "Min-Heap"
    queue = []
    heapq.heappush(queue, (0, s))  # Add start node s with distance 0 to the queue

    # While the queue is not empty
    while queue:
        w_dist, w = heapq.heappop(queue)  # Take the node w with the smallest distance from the queue

        # For each successor u of w in the adjacency list
        for u in adj_list[w]:
            distance_new = distance[w] + length[w][u]  # Calculate new distance via w

            # If the new path is shorter, update the distance and predecessors
            if distance[u] > distance_new:
                distance[u] = distance_new  # Set the new shortest distance to u
                predecessor[u] = [w]  # Overwrite predecessor of u with w
                heapq.heappush(queue, (distance_new, u))  # Add u with the new distance to the queue

            # If the new path has the same distance, add the predecessor
            elif distance[u] == distance_new:
                predecessor[u].append(w)  # Add w to the predecessors of u

    return distance, predecessor

