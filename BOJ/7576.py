from collections import deque
import sys

M,N=  map(int, sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
# day = 0
q = deque()

for i in range(N) :
    for j in range(M) :
        if board[i][j] == 1 :
            q.append((i,j))

# <!-- 변경된 부분 : 토마토가 안익음~>익음으로 변경된 후에 한번씩만 큐에 넣고 탐색하여 시간초과 해결 --> 
dx, dy = [-1,1,0,0], [0,0,-1,1]
while q :
    x, y = q.popleft()
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0 : 
                board[nx][ny] = board[x][y] + 1
                q.append((nx,ny))

def isFull() :
    for i in range(N) :
        for j in range(M) :
            if board[i][j] == 0 :
                return False
    return True

if not isFull() : 
        print(-1)
else : print(max(map(max, board)) - 1)  
# 1에서 시작했으므로 -1 해준 값을 정답(=모두 익는데 걸린 일수)으로 출력