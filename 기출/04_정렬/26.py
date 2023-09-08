# 카드 정렬하기
# 백준 1715 골드4
import sys
import heapq
input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
    cards = int(input())
    heapq.heappush(q, cards)

result = 0

while len(q) != 1:
    one = heapq.heappop(q)
    two = heapq.heappop(q)
    sum_cards = one + two
    result += sum_cards
    heapq.heappush(q, sum_cards)
    
print(result)