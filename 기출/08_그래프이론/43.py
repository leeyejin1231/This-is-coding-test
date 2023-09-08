# 어두운 길
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
graph = []
parent = [i for i in range(n+1)]
result = 0
total = 0

for _ in range(m):
    x, y, z = map(int, input().split())
    total += z
    graph.append((z, x, y))

graph.sort()

for i in graph:
    cost, a, b = i
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(total - result)
