import sys

N, M = map(int, sys.stdin.readline().split())
map = [sys.stdin.readline().rstrip('\n') for _ in range(N)]
dist = [[0 for j in range(M)] for i in range(N)]
queue = [(0,0)]
dist[0][0] = 1      # 시작위치와 도착위치 포함

while queue : 
    x, y = queue.pop(0) #★
    if x == N-1 and y == M-1 :
        print(dist[x][y])
        break
    else :
        if x+1 < N and dist[x+1][y] == 0 and map[x+1][y] == '1' :
            dist[x+1][y] = dist[x][y] + 1
            queue.append((x+1, y))
        if 0 <= x-1  and dist[x-1][y] == 0 and map[x-1][y] == '1' :
            dist[x-1][y] = dist[x][y] + 1
            queue.append((x-1, y))
        if y+1 < M and dist[x][y+1] == 0 and map[x][y+1] == '1' :
            dist[x][y+1] = dist[x][y] + 1
            queue.append((x, y+1))
        if 0 <= y-1 and dist[x][y-1] == 0 and map[x][y-1] == '1' :
            dist[x][y-1] = dist[x][y] + 1
            queue.append((x, y-1))            