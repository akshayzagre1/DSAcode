import heapq

class Graph:
    def __init__(self):
        self.graph = {}    # adjacency list

    def add_edge(self, u, v, time):
        # if location not already in graph, add
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        # undirected graph
        self.graph[u].append((v, time))
        self.graph[v].append((u, time))

    def dijkstra(self, start):
        # distance dictionary with infinity
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0

        # priority queue
        priority_queue = [(0, start)]   # (distance, node)

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # if current distance is greater, skip
            if current_distance > distances[current_node]:
                continue

            # explore neighbours
            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight

                # relaxation
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


# ------- Main Program -------
g = Graph()

g.add_edge('Shop', 'A', 10)
g.add_edge('Shop', 'B', 15)
g.add_edge('A', 'C', 12)
g.add_edge('B', 'D', 10)
g.add_edge('C', 'D', 2)
g.add_edge('C', 'E', 1)
g.add_edge('D', 'E', 5)

source = 'Shop'
shortest_times = g.dijkstra(source)

print("Minimum Delivery Time from Shop:")
for location, time in shortest_times.items():
    print(f"{location}: {time} minutes")
