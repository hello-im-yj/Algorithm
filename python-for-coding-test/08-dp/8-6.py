N = int(input())
food = list(map(int,input().split()))

'''
4
1 3 1 5
'''

dp = [0]*N
dp[0] = food[0]
dp[1] = max(food[0],food[1])
for i in range(2,N) : 
    dp[i] = max(dp[i-2]+food[i],dp[i-1])

print(dp[N-1])