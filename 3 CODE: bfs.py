'''Design and implement BFS algorithm to determine the traversal of a graph
from any arbitrary source node. Find the running time of the algorithm.

GRAPH:
0 1
0 3
0 4
1 2
3 5
4 5

'''

# Graph with nodes from 0 to n-1

def bfs(G,start):
    discovered = {node:False for node in G}
    discovered[start]= True
    L=[[]]
    L[0].append(start)
    i=0
    T=[]
    # Following the algorithm
    while L[i]:
        L.append([])
        for u in L[i]:
            for v in G[u]:
                if not discovered[v]:
                    discovered[v]=True
                    T.append((u,v))
                    L[i+1].append(v)
        i+=1
    reachable = [node for layer in L for node in layer if layer]
    return reachable,T

G = {}
e = int(input("Enter the number of edges: "))

# Create adjacency list
print("Enter edges in u v format: ")
for _ in range(e):
    u,v = input().split()
    if u not in G:
        G[u] = []
    if v not in G:
        G[v] = []
    G[u].append(v)
    G[v].append(u)
start = input("Enter source: ")
reachable,T = bfs(G,start)
print("Reachable nodes:",reachable)
print("Tree:",T)  # Print the tree

