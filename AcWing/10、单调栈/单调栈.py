"""
给定一个长度为N的整数数列，输出每个数左边第一个比它小的数，如果不存在则输出-1。
-------------
第一行包含整数N，表示数列长度。
第二行包含N个整数，表示整数数列。
-------------
共一行，包含N个整数，其中第i个数表示第i个数的左边第一个比它小的数，
如果不存在则输出-1。
-------------
5
3 4 2 7 5
-------------
-1 3 -1 2 2
"""

## 1
n = int(input())
stack = [0]*n
tt = 0
alist = list(map(int,input().split()))
for i in alist:
    while tt and stack[tt] >= i: tt -= 1
    if tt:
        print(stack[tt], end = ' ')
    else:
        print(-1, end = ' ')
    tt += 1
    stack[tt] = i
## 2
n = int(input())
stack = []
alist = list(map(int,input().split()))
for i in alist:
    while stack and stack[-1] >= i: stack.pop()
    if stack:
        print(stack[-1], end = ' ')
    else:
        print(-1, end = ' ')
    stack.append(i)
