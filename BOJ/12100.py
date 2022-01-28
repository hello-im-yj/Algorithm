import sys

N = int(input())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]


print(map(max,board))