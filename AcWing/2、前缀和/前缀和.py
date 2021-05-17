"""
输入一个长度为n的整数序列。

接下来再输入m个询问，每个询问输入一对l, r。

对于每个询问，输出原序列中从第l个数到第r个数的和。
--------
第一行包含两个整数n和m。

第二行包含n个整数，表示整数数列。

接下来m行，每行包含两个整数l和r，表示一个询问的区间范围。
-------
5 3
2 1 3 6 4
1 2
1 3
2 4
----
3
6
10
"""
##n, m = map(int,input().split())
##alist = list(map(int,input().split()))
##def create(q, n):
##    res = [0 for i in range(n + 1)]
##    for i in range(1,n + 1):
##        res[i] = res[i - 1] + q[i - 1]
##    return res
##    
##res = create(alist, n)
##while m:
##    m -= 1
##    l, r = map(int,input().split())
##    print(res[r] - res[l - 1])

n, m = map(int,input().split())
alist = list(map(int,('0 ' + input()).split()))
def create(q, n):
    res = [0 for i in range(n + 1)]
    for i in range(1,n + 1):
        res[i] = res[i - 1] + q[i]
    return res
    
res = create(alist, n)
while m:
    m -= 1
    l, r = map(int,input().split())
    print(res[r] - res[l - 1])
