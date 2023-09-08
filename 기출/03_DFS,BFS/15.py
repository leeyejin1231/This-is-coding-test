# 특정 거리의 도시 찾기
# 백준 실버2
# https://www.acmicpc.net/problem/18352
# 가중치 없는 노드는 BFS로

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

q = []
heapq.heappush(q, (0, x))
distance[x] = 0

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + 1
        if cost < distance[i]:
            distance[i] = cost
            heapq.heappush(q, (cost, i))

if k not in distance:
    print(-1)
else:
    for idx, dist in enumerate(distance):
        if dist == k:
            print(idx)