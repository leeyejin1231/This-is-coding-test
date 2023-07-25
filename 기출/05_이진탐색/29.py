# 공유기 설치
#백준 골드4

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
array = []

for i in range(n):
    array.append(map(int, input()))

array.sort()
