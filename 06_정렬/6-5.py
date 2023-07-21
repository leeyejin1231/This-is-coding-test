# 퀵 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left = [i for i in tail if i < pivot]
    right = [i for i in tail if i > pivot]

    return quick_sort(left)+[pivot]+quick_sort(right)

print(quick_sort(array))