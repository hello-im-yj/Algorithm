import sys
import heapq

h = []
N = int(input())
for i in range(N) :
    num = int(sys.stdin.readline())
    if num == 0 :
        if len(h) == 0 : print(0)
        else : 
            _, num = heapq.heappop(h)
            print(num)
    else : 
        if num < 0 : 
            heapq.heappush(h,(abs(num),num))
        elif num > 0 :
            heapq.heappush(h,(abs(num),num))