n = int(input())
numbers = list(map(int,input().split()))
dp = [0 for _ in range(n)]
dp[0] = numbers[0]
maxx = dp[0]
# dp[n] = n + dp[n-1]
for i in range(1,n):
    if dp[i-1] < 0:
        dp[i] = max(dp[i-1], numbers[i])
    elif dp[i-1] + numbers[i] > 0 :
        dp[i] = numbers[i] + dp[i-1]

    if maxx < dp[i]:
        maxx = dp[i]

print(maxx)