# 퇴사
# 백준 14501 실버3

import sys
input = sys.stdin.readline

n = int(input())
t = []
p = []
dp = [0] * n
for i in range(1, n+1):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)


