'''A truck driver is given a set of locations to be covered 
with their distances by a company. The company strictly orders that 
truck should be started from a particular location. Design and 
implement Dijkstra’s algorithm that gives a greedy solution 
to the truck driver’s problem and display the shortest path 
for a given source location to all other locations. 
State the design strategy used and comment on 
the time complexity of the same.

Graph:
EDGE   WEIGHT
1-2     10
2-3     50
3-4     20
4-5     60
1-5     100
3-5     10
'''

#This code takes in nodes from 1 to n

def dijkstra(n, graph, start):
    dist = [float('inf')] * (n + 1)  # Initialize distances for nodes 1 to n
    dist[start] = 0
    visited = [False] * (n + 1)
    prev = [None] * (n + 1)
    
    for _ in range(n):
        # Find the minimum distance vertex not yet processed
        min_dist = float('inf')
        min_node = -1
        for v in range(1, n + 1):
            if not visited[v] and dist[v] < min_dist:
                min_dist = dist[v]
                min_node = v
        
        if min_node == -1:
            break
        
        u = min_node
        visited[u] = True
        
        # Update distances and predecessors for adjacent vertices
        for v, w in graph[u]:
            if not visited[v]:
                new_dist = dist[u] + w
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    prev[v] = u
    
    return dist, prev

def get_path(prev, target):
    path = []
    while target is not None:
        path.append(target)
        target = prev[target]
    path.reverse()
    return path

n = int(input("Enter the number of vertices: "))
e = int(input("Enter the number of edges: "))
edges = []
print("Enter each edge in the format 'u v weight':")
for _ in range(e):
    u, v, w = map(int, input().strip().split())
    edges.append((u, v, w))
    
graph = [[] for _ in range(n + 1)]  # Graph with nodes from 1 to n

for u, v, w in edges:
    graph[u].append((v, w))
    graph[v].append((u, w))

start = int(input("Enter the source vertex: "))
dist, prev = dijkstra(n, graph, start)

print("Shortest distances from source:")
for i in range(1, n + 1):
    print(f"Vertex {i}: {dist[i]}")

print("Shortest paths from source:")
for i in range(1, n + 1):
    if dist[i] == float('inf'):
        print(f"Vertex {i}: No path")
    else:
        path = get_path(prev, i)
        print(f"Vertex {i}: {' -> '.join(map(str, path))}")
