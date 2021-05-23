from collections import deque
n, k = map(int,input().split())
alist = list(map(int,input().split()))
small = deque([])
big = deque([])
for i in range(n):
    if small and small[0] < i - k + 1: 
        small.popleft()
    while small and alist[small[-1]] >= alist[i]: 
        small.pop()
    small.append(i)
    if i >= k - 1: print(alist[small[0]], end = ' ')
print()
for i in range(n):
    if big and big[0] < i - k + 1: big.popleft()
    while big and alist[big[-1]] <= alist[i]: big.pop()
    big.append(i)
    if i >= k - 1: print(alist[big[0]], end = ' ')
