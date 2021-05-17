"""
给定两个升序排序的有序数组A和B，以及一个目标值x。数组下标从0开始。
请你求出满足A[i] + B[j] = x的数对(i, j)。数据保证有唯一解。
-----------
第一行包含三个整数n，m，x，分别表示A的长度，B的长度以及目标值x。

第二行包含n个整数，表示数组A。

第三行包含m个整数，表示数组B。
-----------
共一行，包含两个整数 i 和 j。
-----------
4 5 6
1 2 4 7
3 4 6 8 9
-----------
1 1
"""
n, m, x = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
setList = [0] * 100000
def findMax(p, n, q, m, x):
    l = 0
    r = m - 1
    while l < n and r >= 0:
        if p[l] + q[r] > x:
            r -= 1
        elif p[l] + q[r] < x:
            l += 1
        else:
            return l, r
          
i,j = findMax(A, n, B, m, x)
print(i,j)
