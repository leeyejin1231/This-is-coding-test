# 탑승구
g = int(input())
p = int(input())

graph = [[] for _ in range(p+1)]
indegree = [0] * (p+1)

for i in range(1, p+1):
    a = int(input())
    for j in range(1, a+1):
        graph[i]
        indegree[i] += 1