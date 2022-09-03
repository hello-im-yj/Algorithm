X = int(input())
dp = [0]*(X+1)

for i in range(2,X+1) :
    tmp = dp[i-1]
    if i % 5 == 0 :
        tmp = min(dp[i//5],tmp) 
    if i % 3 == 0 :
        tmp = min(dp[i//3],tmp)
    if i % 2 == 0 : 
        tmp = min(dp[i//2],tmp)
    dp[i] = tmp + 1

print(dp[X])    