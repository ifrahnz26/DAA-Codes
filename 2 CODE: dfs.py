'''Design and implement recursive DFS algorithm to determine the traversal 
of a graph from any arbitrary source node. Find the running time of the algorithm.

GRAPH:
0 1
0 2
0 3
1 4
1 5
2 5

'''

# Graph with nodes from 0 to n-1

def dfs(graph, start, visited=None):
    # Create a visited list
    if visited is None:
        visited = set() 
    visited.add(start)
    print(f"{start}", end = " ")
    
    # Traverse through the adjacency list depth wise
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


n = int(input("Enter the number of vertices: "))
e = int(input("Enter the number of edges: "))
edges = []

# either this way or ask the user for neighbours of each node and append in the graph directly

print("Enter each edge in the format 'u v':")
for _ in range(e):
    u, v= map(int, input().strip().split())
    edges.append((u, v))
    
graph = [[] for _ in range(n)]  # Graph with nodes from 0 to n-1
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

# Read the starting node for DFS
start_node = int(input("Enter the starting node for DFS: "))

# Perform DFS
print("DFS traversal starting from node", start_node)
dfs(graph, start_node)
print()


