N,M = map(int,input().split())
coin = [int(input()) for _ in range(N)]
'''
입력 1
2 15
2
3
출력 1 
5

입력 2
3 4 
3
5
7
출력 2
-1
'''
dp = [float('inf')]*(M+1)
for c in coin : 
    if c > M : coin.remove(c)
    else : dp[c] = 1 

for i in range(min(coin),M+1) : 
    for c in coin : 
        dp[i] = min(dp[i-c]+1,dp[i])

if dp[M] == float('inf') : print(-1)
else : print(dp[M])
