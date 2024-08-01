'''A phone company wants to lay lines for communication in a city. 
Different amounts are charged for connecting between each pair of cities. 
Design and implement Kruskal’s greedy solution such that 
it forms a spanning tree with minimum cost and 
find the time complexity of the same.

GRAPH:
Edge  Weight
1-2     10
2-3     1
3-4     2
4-5     3
2-4     6
3-5     7
1-5     5
'''

# This code takes nodes from 1 to N

def find(parent, u):
    if parent[u] == u:
        return u
    parent[u] = find(parent, parent[u])  # Path compression
    return parent[u]

def union(parent, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)
    if root_u != root_v:
        parent[root_v] = root_u

def kruskal(n, edges):
    # Sort edges based on their weight
    edges.sort(key=lambda x: x[2])
    
    # Initialize parent array for union-find (disjoint set)
    parent = list(range(n + 1))  # Adjusted for nodes 1 to n
    mst = []         # List to store edges in the MST
    mst_weight = 0   # Total weight of the MST
    
    for u, v, weight in edges:
        # Check if adding the current edge forms a cycle
        if find(parent, u) != find(parent, v):
            union(parent, u, v)  # Union the sets of u and v
            mst.append((u, v, weight))  # Add edge to MST
            mst_weight += weight  # Add weight to total MST weight
    
    return mst, mst_weight

# User input
n = int(input("Enter the number of vertices: "))
m = int(input("Enter the number of edges: "))
edges = []
print("Enter each edge in the format 'u v weight':")
for _ in range(m):
    u, v, weight = map(int, input().strip().split())
    edges.append((u, v, weight)) 

# Find MST using Kruskal's algorithm
mst, mst_weight = kruskal(n, edges)

# Output MST edges and total weight
print("The edges in the Minimum Spanning Tree are:")
for u, v, weight in mst:
    print(f"{u} - {v}: {weight}")
print(f"The total weight of the Minimum Spanning Tree is: {mst_weight}")
