# 고정점 찾기

def search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        elif array[mid] < mid:
            start = mid + 1
        else:
            end = mid - 1
    return None

n = int(input())
array = list(map(int, input().split()))
result = search(array, 0, n-1)

if result != None:
    print(result)
else:
    print(-1)
