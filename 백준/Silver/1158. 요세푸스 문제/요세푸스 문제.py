from collections import deque
import sys

N, K = map(int, sys.stdin.readline().strip().split())

# 덱 생성
q = deque(range(1, N + 1))
y = []

while q:
    q.rotate(-(K-1))
    y.append(q.popleft())

output = ', '.join(map(str, y))
print(f'<{output}>')