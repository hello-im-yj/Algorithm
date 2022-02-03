# X= int(input())

# dp = [0 for _ in range(X+1)]

# for i in range(2, X+1):
#     dp[i] = dp[i-1] + 1  

#     if i%2 == 0 and dp[i] > dp[i//2] + 1 :
#         dp[i] = dp[i//2]+1
        
#     if i%3 == 0 and dp[i] > dp[i//3] + 1 :
#         dp[i] = dp[i//3] + 1
        
# print(dp[X])


X = int(input())
cache = {1: 0, 2: 1}

def dp(n):
    if n in cache:
        return cache[n]

    cnt = 1 + min(dp(n//3) + n%3, dp(n//2) + n%2)
    cache[n] = cnt
    return cnt
    
print(dp(X))