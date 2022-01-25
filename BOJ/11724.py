import sys
from collections import deque

def dfs(graph, visited, start) :
    deq.append(start)
    visited[start] = 1
    while deq :
        x = deq.popleft()
        for i in range(1,N+1) :
            if graph[x][i] and not visited[i] : 
                visited[i] = 1
                deq.append(i)
    return

# setting
deq = deque()
N , M = map(int, input().split())
graph = [[0]*(N+1) for i in range(N+1)]
for i in range(M) :
    x,y = map(int,sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1
visited = [0 for i in range(N+1)]

linked = 0
for i in range(1,N+1) :
    if not visited[i] :
        dfs(graph, visited, i)
        linked += 1
print(linked)