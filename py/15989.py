import sys
input = sys.stdin.readline

dp = [1 for _ in range(10001)]
for i in range(2, 10001):
    dp[i] += dp[i-2]
for i in range(3, 10001):
    dp[i] += dp[i-3]

tk = int(input())
for _ in range(tk):
    n = int(input())
    print(dp[n])
