from collections import deque
import sys

def nextday(changed, board, x, y) :
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    for i in range(4) :
        if 0 <= x + dx[i] < N and 0 <=y + dy[i]< M and board[x + dx[i]][y + dy[i]] == 0 :
            board[x + dx[i]][y + dy[i]] = 1
            changed = True
    return changed

M,N=  map(int, sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
day = 0
q = deque()

Full = False
while not Full : 
    Full = True
    for i in range(N) :
        for j in range(M) :
            if board[i][j] == 1 : q.append((i,j))
            elif board[i][j] == 0 : Full = False
    if Full : print(day)

    changed = False
    while q :
        x,y = q.popleft() 
        changed = nextday(changed, board,x,y) 
    day += 1
    
    if not changed and not Full : 
        print(-1)
        break  