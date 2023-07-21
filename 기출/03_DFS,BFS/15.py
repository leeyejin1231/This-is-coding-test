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



# 시간 초과
# road_map = []
# result = []
# shortest = [1000000] * (n)
# shortest[x-1] = 0

# for i in range(m):
#     road_map.append(list(map(int, input().split())))

# def dfs(road_map, head, cnt):
#     for value in road_map:
#         if value[0] == head:
#             if shortest[value[1]-1] > cnt:
#                 shortest[value[1]-1] = cnt
#             dfs(road_map, value[1], cnt+1)
#     return
            
# dfs(road_map, x, 1)

# for i, dist in enumerate(shortest, 1):
#     if dist == k:
#         result.append(i)

# if len(result) > 0:
#     for i in sorted(result):
#         print(i)
# else:
#     print(-1)