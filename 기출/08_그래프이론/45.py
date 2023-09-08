# 최종 순위
import sys
input = sys.stdin.readline

test_case = int(input())

n = int(input())
graph = [[] for _ in range(n+1)]
team = list(map(int, input().split()))
for i in range(1, n):
    graph[i-1] = [i]

m = int(input())
changes = []
for _ in range(m):
    a, b = map(int, input().split())
    changes.append((a, b))

result = []
for change in changes:
    a, b = change
    
