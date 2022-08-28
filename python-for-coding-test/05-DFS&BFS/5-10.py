# input 
'''
입력 예시 1
4 5
00110
00011
11111
00000

출력 예시 1
3
'''
N,M = map(int,input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

# Algorithm
'''
1) (0,0) 부터 시작해서 0이면 좌표를 stack에 넣음
2) 상하좌우를 탐색해서 0이 있는 곳을 찾아서 이동 -> 1)과 마찬가지로 좌표를 stack에 넣음
3) 더 갈 곳이 없으면 cnt +1 
'''

visit = [[False]*M for _ in range(N)]
cnt = 0 

def dfs(x,y) :
    if x<0 or x>=N or y<0 or y>=M : 
        return 0
    if (not visit[x][y]) and (graph[x][y] == 0):
        visit[x][y] = True
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return 1
    return 0
        
for i in range(N):
    for j in range(M) :
        cnt += dfs(i,j)

print(cnt)