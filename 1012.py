import sys
sys.setrecursionlimit(10**6)

def cluster(veg, x, y, visited) :
    if veg[y][x] and not visited[y][x]:
        visited[y][x] = 1
        if x+1 < len(veg[0]) : cluster(veg, x+1, y, visited)
        if y+1 < len(veg) : cluster(veg, x, y+1, visited)
        if x-1 >= 0 : cluster(veg, x-1 , y, visited)
        if y-1 >= 0 : cluster(veg, x, y-1, visited)
        return 1
    return 0
    
T = int(input())
for t in range(T) :
    M, N, K  = map(int, input().split())
    veg = [[0 for i in range(M)] for j in range(N)]
    visited = [[0 for i in range(M)] for j in range(N)]
    coordinates = []
    for k in range(K) :
        x,y = map(int, sys.stdin.readline().split())
        veg[y][x] = 1
        coordinates.append((x,y))
    ans = 0
    for cx,cy in coordinates :
        ans += cluster(veg, cx, cy, visited)
    print("ans : ",ans)