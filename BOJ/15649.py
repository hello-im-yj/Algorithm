import itertools

N , M = map(int, input().split())
res = list(itertools.permutations(range(1,N+1), M)) 
for p in res :
    print(*p)