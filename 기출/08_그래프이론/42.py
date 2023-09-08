# 탑승구
g = int(input())
gate = [0] * (g+1)
p = int(input())

graph = [[] for _ in range(p+1)]
indegree = []

for i in range(1, p+1):
    a = int(input())
    indegree.append((a, i))
    for j in range(1, a+1):
        graph[i].append(j)

indegree.sort()

for i in indegree:
    _, now = i
    for j in graph[now]:
        if gate[j] == 0:
            gate[j] = 1
            break

print(gate.count(1))