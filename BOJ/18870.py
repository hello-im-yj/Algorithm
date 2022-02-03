import sys 
    
N = int(sys.stdin.readline())
matrix = list(map(int, sys.stdin.readline().split()))
s_matrix = sorted(list(set(matrix)))
d = {s_matrix[idx]:idx for idx in range(len(s_matrix))}

c = []
for e in matrix :
    c.append(d[e])
    
print(*c)