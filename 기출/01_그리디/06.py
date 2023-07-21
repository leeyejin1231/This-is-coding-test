#무지의 먹방 라이브
#프로그래머스

def solution(food_times, k):
    array = []
    n = len(food_times)
    pre = 0
    time = 0
    
    if sum(food_times) <= k:
        return -1
    
    for idx, value in enumerate(food_times, 1):
        array.append((idx, value))
    
    array.sort(key=lambda x:x[1], reverse=True)
    
    while True:
        idx, value = array.pop()
        time = value - pre
        if k - time*n > 0:
            k -= time*n
            n -= 1
            pre = value
        else:
            array.append((idx, value))
            break
    
    array.sort()
    
    return array[k%n][0]
        
        
        
    
        
    