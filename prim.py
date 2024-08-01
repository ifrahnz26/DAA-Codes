
def prim(n,G):
    selected = [False]*n
    numE=0
    cost = 0
    selected[0] = True
    while numE<n-1:
        a=0
        b=0
        min = INF
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if(not selected[j]) and G[i][j]:
                        if min>G[i][j]:
                            min = G[i][j]
                            a,b = i,j
        print(str(a)+"-"+str(b)+" : "+str(G[a][b]))
        selected[b] = True
        cost+=G[a][b]
        numE+=1
    return cost
INF = float('inf')
n = int(input("Enter number of nodes: "))
G = [[INF if i!=j else 0 for j in range(n) ] for i in range(n)]
e = int(input("Enter the number of edges: "))
print("Enter edges in u v w format: ")
for i in range(e):
    u,v,w = map(int,input().split())
    G[u][v] = w
    G[v][u] = w
min = prim(n,G)
print("Minimum Cost: ", min)
                    