import sys
input = sys.stdin.readline

def check(mid):
    global n, m, M

    if M > mid:
        return False

    temp = mid
    cnt = 0

    for i in range(n):
        if temp - data[i] < 0:
            cnt += 1
            temp = mid
        
        temp -= data[i]
    
    if mid != temp:
        cnt += 1

    if cnt <= m:
        return True
    else:
        return False


n, m = map(int, input().split())
data = list(map(int, input().split()))
low = 0
high = sum(data)
M = max(data)

while low <= high:
    mid = (low + high) // 2

    if check(mid):
        high = mid - 1
        answer = mid
    else:
        low = mid + 1

print(answer)