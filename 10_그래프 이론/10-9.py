# 커리큘럼
from collections import deque

n = int(input())
edges = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for i in range(1, n+1):
    temp = list(map(int, input().split()))
    edges[i].append(temp[0])
    indegree[i] = len(temp[1:-1])
    for j in temp[1:-1]:
        edges[j].append(i)

def topology():
    result = [[] for _ in range(n+1)]
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append((i, 1))

    while q:
        now, index = q.popleft()
        result[index].append(now)
        index += 1
        for i in edges[now][1:]:
            indegree[i] -= 1
            if indegree[i] == 0:
            q.append((i, index))
    return result

result = topology()
print(result)
