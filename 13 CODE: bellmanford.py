'''Design and implement Bellman ford algorithm 
to find the shortest path from a given source to all other nodes. 
State the design strategy used and comment on the 
time complexity of the same.

GRAPH:
0 1 -4
0 5 -3
2 1 8
4 2 -3
4 5 2
2 5 3
3 0 6
3 5 4
1 3 -1
1 4 -2
'''
def bellman_ford(vertices, edges, start_vertex):
   #Initialize distance and parent
   distance = {vertex: float('inf') for vertex in vertices}
   parent = {vertex: None for vertex in vertices}
   distance[start_vertex] = 0
   parent[start_vertex] = start_vertex
 
   # Relax all edges V - 1 times
   for _ in range(len(vertices) - 1):
       for u, v, weight in edges:
           if distance[u] + weight < distance[v]:
               distance[v] = distance[u] + weight
               parent[v] = u
 
   # Check for negative-weight cycles
   for u, v, weight in edges:
       if distance[u] + weight < distance[v]:
           print("Graph contains a negative-weight cycle")
           return None, None
 
   return distance, parent
 
#Find the path from source to all vertex
def print_path(parent, vertex):
   if parent[vertex] == vertex:
       print(vertex, end=' ')
   else:
       print_path(parent, parent[vertex])
       print(vertex, end=' ')
 
# Get user input
n = int(input("Enter the number of vertices: "))
vertices = [i for i in range(n)]
 
m = int(input("Enter the number of edges: "))
edges = []
print("Enter the edges (u, v, weight):")
for _ in range(m):
   u, v, weight = map(int, input().split())
   edges.append((u, v, weight))
 
start_vertex = int(input("Enter the start vertex: "))
 
# Run Bellman-Ford algorithm
distance, parent = bellman_ford(vertices, edges, start_vertex)
 
# Print results
if distance is not None:
   print("Vertex distances from start vertex:")
   for vertex in vertices:
       print(f"Vertex {vertex}: Distance = {distance[vertex]}")
       print("Path: ", end='')
       print_path(parent, vertex)
       print()
