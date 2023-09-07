# 특정 거리의 도시 찾기
# 백준 실버2
# https://www.acmicpc.net/problem/18352
# 가중치 없는 노드는 BFS로

from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
 