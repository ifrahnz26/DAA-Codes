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
def tsp(current_city, current_cost, n, start_city):
    if all(visited):
        for (u, v, cost) in edges:
            if u == current_city and v == start_city:
                return current_cost + cost
        return float('inf')  # If there's no edge back to the start city, return infinity

    min_cost = float('inf')

    for (u, v, cost) in edges:
        if u == current_city and not visited[v]:
            visited[v] = True
            new_cost = current_cost + cost
            min_cost = min(min_cost, tsp(v, new_cost, n, start_city))
            visited[v] = False
    
    return min_cost


def tsp_with_path(current_city, current_cost, path, start_city):
    if all(visited):
        for (u, v, cost) in edges:
            if u == current_city and v == start_city:
                path.append(start_city)
                return current_cost + cost, path
        return float('inf'), []  # No valid path

    min_cost = float('inf')
    best_path = []

    for (u, v, cost) in edges:
        if u == current_city and not visited[v]:
            visited[v] = True
            new_cost = current_cost + cost
            new_path = path + [v]
            cost_with_path, candidate_path = tsp_with_path(v, new_cost, new_path, start_city)
            if cost_with_path < min_cost:
                min_cost = cost_with_path
                best_path = candidate_path
            visited[v] = False
    
    return min_cost, best_path

n = int(input("Enter the number of cities: "))
m = int(input("Enter the number of edges: "))

edges = []
print("Enter the edges in the format (city1 city2 cost):")
for _ in range(m):
    u, v, cost = map(int, input().split())
    edges.append((u, v, cost))
    edges.append((v, u, cost))  # Assuming the graph is undirected

start_city = int(input("Enter the starting city: "))
visited = [False] * n
visited[start_city] = True  # starting from the selected city

# Run without path tracking
min_cost = tsp(start_city, 0, n, start_city)
print("The minimum cost of the tour without path tracking is:", min_cost)

# Run with path tracking
initial_path = [start_city]
min_cost_with_path, best_path = tsp_with_path(start_city, 0, initial_path, start_city)
print("The minimum cost of the tour with path tracking is:", min_cost_with_path)
print("The path of the tour is:", ' -> '.join(map(str, best_path)))
