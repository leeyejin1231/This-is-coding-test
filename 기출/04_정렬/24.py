# 안테나
# 백준 18310 실버 3
import sys
input = sys.stdin.readline

n = int(input())
position = list(map(int, input().split()))
position.sort()
print(position[(len(position)-1)//2])