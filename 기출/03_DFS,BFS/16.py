# 연구소
# 백준 골드4
# https://www.acmicpc.net/problem/14502
import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

for y in range(n):
    for x in range(m):

def BFS():