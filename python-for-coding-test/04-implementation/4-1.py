'''
입력 예시 1
5
R R R U D D

출력 예시 1 
3 4
'''
N = int(input())
map_list = input().split()

x,y = 1,1
dxdy = {'L':(0,-1),'R':(0,1),'U':(-1,0),'D':(1,0)}

for dir in map_list :
    nx = x + dxdy[dir][0] 
    ny = y + dxdy[dir][1]
    
    if nx>0 and nx<=N and ny>0 and nx<=N:
        x = nx
        y = ny

print(x,y)