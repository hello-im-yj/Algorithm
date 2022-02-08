import heapq
import sys

N = int(input())
stu = [list(map(int,sys.stdin.readline().split())) for _ in range(N**2)]
stdict = {}
for i in range(N**2) : 
    stdict[stu[i][0]] = stu[i][1:]
result = [[0]*(N+1) for _ in range(N+1)]   
dx, dy = [-1,1,0,0], [0,0,-1,1]

def rule(idx) :
    stdnum = stu[idx][0]
    likenum = stu[idx][1:]
    cand = [[(1,1,0,0)]*(N+1) for _ in range(N+1)] 
    
    for r in range(1,N+1) :
        for c in range(1,N+1) :
            like,empty = 0,0
            for i in range(4) : 
                if result[r][c] == 0 :
                    if 0 < r+dx[i]< N+1 and 0 < c+dy[i]< N+1 :
                        if result[r+dx[i]][c+dy[i]] == 0 :
                            empty +=1 
                        elif result[r+dx[i]][c+dy[i]] in likenum :
                            like +=1
                    cand[r][c] = (-1*like, -1*empty, r, c) 
    candheap = []
    for r in range(1,N+1) :
        for c in range(1,N+1) : 
            candheap.append(cand[r][c])                                
    heapq.heapify(candheap)
    print(candheap)
    final_r , final_c = candheap[0][2] , candheap[0][3]
    result[final_r][final_c] = stdnum

def get_sat() :
    total_sat =0
    for r in range(1,N+1) :
        for c in range(1,N+1) :
            sat = 0
            for i in range(4) : 
                if 0 < r+dx[i]< N+1 and 0 < c+dy[i]< N+1 and result[r+dx[i]][c+dy[i]] in stdict[result[r][c]] :
                    sat += 1
            total_sat += 0 if sat==0 else 10**(sat-1)
    return total_sat

for i in range(N**2) :
    rule(i)
    print(stu[i][0],result)
print(result)
print(get_sat() )