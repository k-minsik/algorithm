import sys, heapq
# from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
gem = []
bag = []

for _ in range(n):
    m, v = map(int, input().split())
    gem.append([m, v])

for _ in range(k):
    bag.append(int(input()))

# gem = deque(sorted(gem))
gem.sort()
bag.sort()

answer = 0
temp = []
for b in bag:
    while gem and b >= gem[0][0]:
        heapq.heappush(temp, -gem[0][1])
        # gem.popleft()
        heapq.heappop(gem)
    
    if temp:
        answer -= heapq.heappop(temp)

print(answer)