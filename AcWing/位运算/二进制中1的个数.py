"""
输入一个 32 位整数
------------------
输出该数二进制表示中 1 的个数。
负数在计算机中用其绝对值的补码来表示。
-------------------
9
-------------------
2
"""
n = int(input())
def getNum(n):
    n = n & ((1 << 32) - 1)
    res = 0
    while n:
        res += n & 1
        n = n >> 1
    return res
res = getNum(n)
print(res)
