# 여행 계획
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
matrix = []

parent = [0] * (n+1)

for _ in range(n):
    matrix.append(list(map(int, input().split())))

for a in range(n):
    for b in range(n):
        if matrix[a][b] == 1:
            union_parent(parent, a, b)

route = list(map(int, input().split()))

for i in range(1, m):
    if parent[route[i]] != parent[route[i-1]]:
        print("NO")

print("YES")
