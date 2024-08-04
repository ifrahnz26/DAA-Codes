'''Design and implement an algorithm for Traveling Salesman Problem using backtracking technique

GRAPH:
0 1 2
1 2 4
2 3 3
3 4 10
0 4 5
0 3 12
2 4 3
1 3 8

'''

def tsp(current_city, visited, current_cost, edges, n):
    if all(visited):
        for (u, v, cost) in edges:
            if u == current_city and v == 0:
                return current_cost + cost
        return float('inf')  # If there's no edge back to the start city, return infinity

    min_cost = float('inf')

    for (u, v, cost) in edges:
        if u == current_city and not visited[v]:
            visited[v] = True
            new_cost = current_cost + cost
            min_cost = min(min_cost, tsp(v, visited, new_cost, edges, n))
            visited[v] = False
    
    return min_cost

n = int(input("Enter the number of cities: "))
m = int(input("Enter the number of edges: "))
    
edges = []
print("Enter the edges in the format (city1 city2 cost):")
for _ in range(m):
    u, v, cost = map(int, input().split())
    edges.append((u, v, cost))
    edges.append((v, u, cost))  # Assuming the graph is undirected

visited = [False] * n
visited[0] = True  # starting from the first city
    
min_cost = tsp(0, visited, 0, edges, n)
print("The minimum cost of the tour is:", min_cost)



