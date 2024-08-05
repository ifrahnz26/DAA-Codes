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
#WITHOUT FINDING PATH 
def tsp(current_city, current_cost, n):
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
            min_cost = min(min_cost, tsp(v, new_cost, n))
            visited[v] = False
    
    return min_cost


#WITH FINDING PATH
# def tsp(current_city, current_cost, path):
#     if all(visited):
#         for (u, v, cost) in edges:
#             if u == current_city and v == 0:
#                 path.append(0)
#                 return current_cost + cost, path
#         return float('inf'), []  # No valid path

#     min_cost = float('inf')
#     best_path = []

#     for (u, v, cost) in edges:
#         if u == current_city and not visited[v]:
#             visited[v] = True
#             new_cost = current_cost + cost
#             new_path = path + [v]
#             cost_with_path, candidate_path = tsp(v, new_cost, new_path)
#             if cost_with_path < min_cost:
#                 min_cost = cost_with_path
#                 best_path = candidate_path
#             visited[v] = False
    
#     return min_cost, best_path

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
#initial_path = [0]
    
min_cost = tsp(0, 0, n)
#min_cost, best_path = tsp(0, 0, initial_path)
print("The minimum cost of the tour is:", min_cost)
#print("The path of the tour is:", ' -> '.join(map(str, best_path)))



