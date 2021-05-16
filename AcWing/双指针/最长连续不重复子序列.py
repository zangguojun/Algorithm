"""
给定一个长度为n的整数序列，
请找出最长的不包含重复数字的连续区间，输出它的长度。
-----------
第一行包含整数n。
-----------
第二行包含n个整数（均在0~100000范围内），表示整数序列。
-----------
共一行，包含一个整数，表示最长的不包含重复数字的连续子序列的长度。
-----------
5
1 2 2 3 5
-----------
3
"""
n = int(input())
alist = list(map(int,input().split()))
setList = [0] * 100000
def findMax(q, n, s):
    j = 0
    res = 0
    for i in range(n):
        s[q[i]] += 1
        while s[q[i]] > 1:
            s[q[j]] -= 1
            j += 1
        res = max(res, i - j + 1)
    return res
          
res = findMax(alist, n, setList)
print(res)
