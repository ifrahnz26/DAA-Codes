'''def match(w_pref,m_pref,n):
    free_men = list(range(n))
    proposals = [0]*n
    w_partner = [-1]*n
    while free_men:
        m = free_men[0]
        w = m_pref[m][proposals[m]]
        proposals[m]+=1
        if w_partner[w] == -1:
            w_partner[w] = m
            free_men.pop(0)
        else:
            m_current = w_partner[w]
            if w_pref[w].index(m)<m_pref[w].index(m_current):
                free_men.append(m_current)
                free_men.pop(0)
                w_partner[w] = m
    return [(w_partner[w],w) for w in range(n)]

n = 3
def get_pref(identifiers, entitites, is_man):
    preference = []
    for i in identifiers:
        pref = input(f"Enter preference of {'man' if is_man else 'woman'} {i}: ").split()
        preference.append([entitites.index(p) for p in pref])
    return preference

w_pref = get_pref(['V','W','X'], ['A','B','C'], False)
m_pref = get_pref(['A','B','C'], ['V','W','X'], True)

print(match(m_pref,w_pref,n))'''

'''def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(f"{start} ", end=" ")
    for neighbours in graph[start]:
        if neighbours not in visited:
            dfs(graph,neighbours,visited)
    
n = 5
e = 6
graph = {}
for _ in range(e):
    u,v = map(int,input().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

start = 0
dfs(graph,start)'''

'''def bfs(graph, start):
    discovered = {node:False for node in graph}
    discovered[start] = True
    L = [[]]
    i = 0
    T=[]
    L[0].append(start)
    while L[i]:
        L.append([])
        for u in L[i]:
            for v in graph[u]:
                if not discovered[v]:
                    discovered[v] = True
                    T.append((u,v))
                    L[i+1].append(v)
        i+=1
    reachable = [node for layer in L for node in layer if layer]
    return reachable, T

n = 5
e = 6
graph = {}
for _ in range(e):
    u,v = map(str,input().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

start = 'A'
r, t = bfs(graph,start)
print(r)
print(t)'''

'''def mergesort(arr,low,high):
    if high-low+1>1:
        mid=(low+high)//2
        mergesort(arr,low,mid)
        mergesort(arr,mid+1,high)
        merge(arr,low,mid,high)
def merge(arr,low,mid,high):
    b=[]
    i=low
    j = mid+1
    while i<=mid and j<=high:
        if arr[i]<=arr[j]:
            b.append(arr[i])
            i+=1
        else:
            b.append(arr[j])
            j+=1
    while i<=mid:
        b.append(arr[i])
        i+=1
    while j<=high:
        b.append(arr[j])
        j+=1
    for k in range(low,high+1):
        arr[k] = b[k-low]
    
arr=list(map(int,input().split()))
mergesort(arr,0,len(arr)-1)
print(arr)'''

'''def SC(L):
    if len(L)<=1:
        return 0, L
    mid = len(L)//2
    left = L[:mid]
    right = L[mid:]
    ra,la = SC(left)
    rb,lb = SC(right)
    r,ln = MC(left,right)
    return r+ra+rb, ln
def MC(A,B):
    merged =[]
    i = inv=j=0
    while i <len(A) and j<len(B):
        if A[i] <=B[j]:
            merged.append(A[i])
            i+=1
        else:
            merged.append(B[j])
            j+=1
            inv+=(len(A)-i)
    merged.extend(A[i:])
    merged.extend(B[j:])
    return inv, merged

users = []
for i in range(3):
    print(f"Enter song ranking for user {i+1}: ")
    user = list(map(int, input().split()))
    users.append(user)

invB = SC(users[1])
invC = SC(users[2])

print(f"User 2 has {invB[0]} inversions.")
print(f"User 3 has {invC[0]} inversions.")

if invC[0] < invB[0]:
    print("User 3 has similar taste to user 1")
elif invB[0] < invC[0]:
    print("User 2 has similar taste to user 1")
else:
    print("All users have similar taste.")'''

'''def partition(A,l,r):
    pivot = A[l]
    i = l
    j = r
    while True:
        while A[i]<pivot:
            i+=1
        while A[j]> pivot:
            j-=1
        if i>=j:
            return j
        A[i],A[j] = A[j],A[i]
        i+=1
        j-=1
def quicksort(A,l,r):
    if l<r:
        s = partition(A,l,r)
        quicksort(A,l,s)
        quicksort(A,s+1,r)

arr = list(map(int,input().split()))
quicksort(arr,0,len(arr)-1)
print(arr)'''

'''def dijkstra(n,graph,start):
    dist = [float('inf')]*(n+1)
    dist[start] = 0
    visited = [False]*(n+1)
    prev = [None]*(n+1)

    for _ in range(n):
        min_dist = float('inf')
        min_node = -1
        for v in range(1,n+1):
            if not visited[v] and dist[v]<min_dist:
                min_dist = dist[v]
                min_node = v
        if min_node == -1:
            break
        u = min_node
        visited[u] = True
        for v,w in graph[u]:
            if not visited[v]:
                new_dist = dist[u]+w
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    prev[v] = u
    return dist,prev
def get_path(prev,target):
    path = []
    while target is not None:
        path.append(target)
        target = prev[target]
    path.reverse()
    return path

n = 5
e = 6
graph = {}
for _ in range(e):
    u,v,w= map(int,input().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v,w))
    graph[v].append((u,w))

start = 1
dist,prev = dijkstra(n,graph,start)
print("Shortest distances from source:")
for i in range(1, n + 1):
    print(f"Vertex {i}: {dist[i]}")

print("Shortest paths from source:")
for i in range(1, n + 1):
    if dist[i] == float('inf'):
        print(f"Vertex {i}: No path")
    else:
        path = get_path(prev, i)
        print(f"Vertex {i}: {' -> '.join(map(str, path))}")'''

'''def prim(G,n):
    selected = [False]*n
    selected[0] = True
    numE = 0
    cost = 0
    while numE<n-1:
        a=0
        b=0
        min = float('inf')
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and G[i][j]:
                        if min> G[i][j]:
                            min = G[i][j]
                            a,b = i,j
        print(str(a+1)+"-"+str(b+1)+" : "+str(G[a][b]))
        selected[b] = True
        numE+=1
        cost+=G[a][b]
    return cost
n = 5
G = [[float('inf') if i!=j else 0 for j in range(n)] for i in range(n)]
e = 7
for _ in range(e):
    u,v,w = map(int,input().split())
    G[u-1][v-1] = w
    G[v-1][u-1] = w
min = prim(G,n)
print(min)'''


'''def find(parent,u):
    if parent[u] == u:
        return u
    parent[u] = find(parent, parent[u])
    return parent[u]
def union(parent,u,v):
    root_u = find(parent,u)
    root_v = find(parent,v)
    if root_u!=root_v:
        parent[root_v] = root_u

def kruskal(n,edges):
    edges.sort(key = lambda x:x[2])
    parent = list(range(n+1))
    mst = []
    min = 0

    for u,v,w in edges:
        if find(parent,u) != find(parent,v):
            union(parent,u,v)
            mst.append((u,v,w))
            min+=w
    return mst,min

n = 5
e = 7
edges = []
for _ in range(e):
    u,v,w = map(int,input().split())
    edges.append((u,v,w))
mst,min = kruskal(n,edges)
print("The edges in the Minimum Spanning Tree are:")
for u, v, weight in mst:
    print(f"{u} - {v}: {weight}")
print(f"The total weight of the Minimum Spanning Tree is: {min}")'''

'''def get_input():
    n = 6
    intervals =[]
    for _ in range(n):
        start,finish,w = map(int,input().split())
        intervals.append((start,finish,w))
    return intervals
def predecessor(intervals):
    p = [0]*len(intervals)
    for j in range(len(intervals)):
        for i in range(j-1,-1,-1):
            if intervals[i][1] <=intervals[j][0]:
                p[j] = i+1
                break
    return p

def OPT(j):
    if j==0:
        return 0
    elif M[j] is not None:
        return M[j]
    else:
        M[j]  = max(OPT(j-1), intervals[j-1][2]+OPT(p[j-1]))
        return M[j]
    
def find_solution(j):
    if j>0:
        if intervals[j-1][2]+M[p[j-1]]>=M[j-1]:
            print(f"Interval {j}: {intervals[j - 1]}")
            find_solution(p[j - 1])
        else:
            find_solution(j-1)
    

intervals = get_input()
intervals.sort(key=lambda x:x[1])
p = predecessor(intervals)
M = [0]+[None]*len(intervals)
weight = OPT(len(intervals))
print(weight) 
find_solution(len(intervals))   

'''

'''def get_input():
    n = 3
    items =[]
    for _ in range(n):
        w = int(input())
        items.append(w)
    W = int(input())
    return items,W
def subset(items,W):
    n = len(items)
    M = [[0]*(W+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for w in range(1, W+1):
            if items[i-1]>w:
                M[i][w] = M[i-1][w]
            else:
                M[i][w] = max(M[i-1][w], items[i-1]+M[i-1][w-items[i-1]])
    return M
def find_items(M,items,W):
    i = len(items)
    k = W
    result=[]
    while i>0 and k>0:
        if M[i][k] != M[i-1][k]:
            result.append((i,items[i-1]))
            k-=items[i-1]
        i-=1
    return result
items, W = get_input()
M = subset(items, W)
max_weight = M[len(items)][W]
print(f"Maximum weight: {max_weight}")
#check if it satisfies the bound
if max_weight == W:
   print("The subset satisfies the bound.")
else:
   print("The subset does not satisfy the bound.")
optimal_items = find_items(M, items, W)
optimal_items.reverse()
print("Items in the optimal solution (weights):")
print(optimal_items)'''

'''def get_input():
    n = 4
    items =[]
    for _ in range(n):
        w,v= map(int,input().split())
        items.append((w,v))
    W = int(input())
    return items,W
def subset(items,W):
    n = len(items)
    M = [[0]*(W+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for w in range(1, W+1):
            if items[i-1][0]>w:
                M[i][w] = M[i-1][w]
            else:
                M[i][w] = max(M[i-1][w], items[i-1][1]+M[i-1][w-items[i-1][0]])
    return M
def find_items(M,items,W):
    i = len(items)
    k = W
    result=[]
    while i>0 and k>0:
        if M[i][k] != M[i-1][k]:
            result.append((i,items[i-1][1]))
            k-=items[i-1][0]
        i-=1
    return result
items, W = get_input()
M = subset(items, W)
max_weight = M[len(items)][W]
print(f"Maximum weight: {max_weight}")
#check if it satisfies the bound
if max_weight == W:
   print("The subset satisfies the bound.")
else:
   print("The subset does not satisfy the bound.")
optimal_items = find_items(M, items, W)
optimal_items.reverse()
print("Items in the optimal solution (weights):")
print(optimal_items)'''

'''def bellman(vertices,edges,start):
    dist = {vertex:float('inf') for vertex in vertices}
    parent ={vertex:None for vertex in vertices}
    dist[start] = 0
    parent[start] = start

    for _ in range(len(vertices)-1):
        for u,v,w in edges:
            if dist[u]+w < dist[v]:
                dist[v] = dist[u]+w
                parent[v] = u
    
    for u,v,w in edges:
        if dist[u]+w < dist[v]:
            print("contains negative edges")
            return None, None
    return dist, parent

def path(parent,vertex):
    if parent[vertex] == vertex:
        print(vertex, end = ' ')
    else:
        path(parent, parent[vertex])
        print(vertex, end= ' ')

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
distance, parent = bellman(vertices, edges, start_vertex)
 
# Print results
if distance is not None:
   print("Vertex distances from start vertex:")
   for vertex in vertices:
       print(f"Vertex {vertex}: Distance = {distance[vertex]}\n")
       path(parent, vertex)
       print()
      '''

'''def placeQueens(board,N,row,solutions):
    if row == N:
        solutions.append(board[:])
        return True
    res = False
    for col in range(N):
        if isSafe(board,row,col):
            board[row] = col
            res = placeQueens(board,N,row+1,solutions) or res
            board[row] = -1
    return res
def isSafe(board,row,col):
    for i in range(row):
        if board[i] == col or abs(board[i]-col) == row -i:
            return False
    return True

N = 5
board = [-1]*N
solutions = []
placeQueens(board,N,0,solutions)
for idx,solution in enumerate(solutions,start=1):
    sol = [pos+1 for pos in solution]
    print(f"Solution {idx}: {sol}")'''

'''def placeQueens(board, row,N,solutions):
    if row == N:
        solutions.append(board[:])
        return True
    res = False
    for col in range(N):
        if isSafe(board,row,col):
            board[row] = col
            res = placeQueens(board, row+1,N, solutions) or res
            board[row] = -1
    return res
def isSafe(board,row,col):
    for i in range(row):
        if board[i]==col or abs(board[i]-col)==row-i:
            return False
    return True
N = 5
solutions=[]
board = [-1]*N
placeQueens(board,0,N,solutions)
for idx, solution in enumerate(solutions, start=1):
    sol = [pos+1 for pos in solution]
    print(f"Solution {idx}: {sol}")

'''
'''def tsp(current_city, current_cost, path, start):
    if all(visited):
        for u,v,c in edges:
            if u == current_city and v == start:
                path.append(start)
                return current_cost + c, path
        return float('inf'),[]
    min = float('inf')
    best = []
    for u,v,c in edges:
        if u == current_city and not visited[v]:
            visited[v] = True
            new_cost = current_cost + c
            new_path = path+[v]
            cost_new,path_new = tsp(v,new_cost,new_path, start)
            if cost_new < min:
                min = cost_new
                best = path_new
            visited[v] =False
    return min,best


n = 5
e = 8
edges = []
for _ in range(e):
    u,v,c = map(int,input().split())
    edges.append((u,v,c))
    edges.append((v,u,c))
start = 0
visited = [False]*n
visited[start] = True
initial = [start]
min,best = tsp(start,0,initial,start)
print(min)
print(best)
'''
