# 금광

def gold(n, m, array):
    maximum = 0

    for i in range(n):
        dp = [0] * m
        dp[0] = array[i][0]
        idx = i
        for j in range(1, m):
            if dp[j] <= dp[j-1] + array[idx][j]:
                dp[j] = dp[j-1] + array[idx][j]
                after_idx = idx
            if 0 < (idx-1) and dp[j] <= dp[j-1] + array[idx-1][j]:
                dp[j] = dp[j-1] + array[idx-1][j]
                after_idx = idx - 1
            if n > (idx+1) and dp[j] <= dp[j-1] + array[idx+1][j]:
                dp[j] = dp[j-1] + array[idx+1][j]
                after_idx = idx + 1
            idx = after_idx
        if maximum < max(dp):
            maximum = max(dp)

    return maximum

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    pre_array = list(map(int, input().split()))
    array = []
    idx = 0
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(pre_array[idx])
            idx += 1
        array.append(temp)

    print(gold(n, m, array))