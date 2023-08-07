# 정수 삼각형
# 백준 1932 실버1

import sys
input = sys.stdin.readline

n = int(input())
dp = []
for i in range(n):
    zero = [0] * (n-1-i)
    temp = list(map(int, input().split()))
    temp.extend(zero)
    dp.append(temp)

for i in range(1, n):
    for j in range(n):
        if j == 0:
            left = 0
        else:
            left = dp[i-1][j-1]
        if j == n-1:
            right = 0
        else:
            right = dp[i-1][j]
        dp[i][j] = dp[i][j] + max(left, right)

print(max(dp[n-1]))