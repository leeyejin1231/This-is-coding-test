# 실패율
# 프로그래머스 42889

def solution(N, stages):
    prob = {}
    answer = []
        
    for i in range(1, N+1):
        if i not in stages:
            prob[i] = 0
        else:
            cnt = 0
            for j in stages:
                if j >= i:
                    cnt += 1
            else: 
                prob[i] = stages.count(i) / cnt
                
    prob = sorted(prob.items(), key = lambda item: item[1], reverse = True)  
    
    for i in prob:
        answer.append(i[0])
        
    return answer