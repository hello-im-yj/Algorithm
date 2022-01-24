import sys

N, M = map(int, sys.stdin.readline().split())
dict = {}
for i in range(N) :
    site, passwd = sys.stdin.readline().split()
    dict[site] = passwd

for j in range(M) :
    link = sys.stdin.readline().rstrip('\n')
    print(dict[link])