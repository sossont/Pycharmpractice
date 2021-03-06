# 연속으로 놓여 있는 3잔을 마실 수 없는 것을 어떻게 따질것인가. 이게 가장 중요한듯?
# dp[n] = max(dp[n-2] + wine[n], dp[n-3] + wine[n-1] + wine[n]

n = int(input())
wine = []
for _ in range(n):
    inputnum = int(input())
    wine.append(inputnum)

dp = [0 for _ in range(n)]
dp[0] = wine[0]
if n == 1:
    print(dp[0])
elif n == 2:
    print(wine[0] + wine[1])
else:
    dp[1] = wine[0] + wine[1]
    dp[2] = max(wine[0]+wine[1],wine[0]+wine[2],wine[1]+wine[2])
    for i in range(3,n):
        dp[i] = max(dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])
        dp[i] = max(dp[i-1],dp[i])
    print(dp[n-1])