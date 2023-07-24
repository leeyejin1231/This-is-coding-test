# 정렬된 배열에서 특정 수의 개수 구하기

# 시간초과^_^
# cnt = array.count(x)
# if cnt > 0:
#     print(cnt)
# else:
#     print(-1)

def start_num(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid + 1
        else:
            if mid == 0 or array[mid-1] != target:
                return mid
            end = mid - 1
    return None

def end_num(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] > target:
            end = mid - 1
        else:
            if array[mid+1] != target:
                return mid
            start = mid + 1
    return None

n, x = map(int, input().split())
array = list(map(int, input().split()))

start_index = start_num(array, x, 0, n-1)
end_index = end_num(array, x, 0, n-1)

if start_index == None:
    print(-1)
else:
    print(end_index - start_index + 1)