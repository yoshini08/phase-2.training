#Graphs with Matrix
"""nodes=int(input())
edges=int(input())

mat=[]

for i in range(nodes+1):
    res=[0]*(nodes+1)
    mat.append(res)

for i in range(edges):
    u,v=map(int,input().split())
    mat[u][v]=1
    mat[v][u]=1

print(mat)"""
#Graphs with Lists and DFS

def initiateDFSTraversal(node, visited, adj, result):
    result.append(node)
    visited[node] = True 
 
    for neighbour in adj[node]:
        if visited[neighbour] == False:
            initiateDFSTraversal(neighbour, visited, adj, result)
 
 
def printDFSTraversal(adj, n):
    result = []
    visited = [False] * n 
    for node in range(n):
        if visited[node] == False:
            initiateDFSTraversal(node, visited, adj, result)
 
    print("DFS Traversal is: ", result)
 
 
 
n, m = map(int, input().split())
adj = [] 
for i in range(n):
    adj.append([])
 
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
 

printDFSTraversal(adj, n)