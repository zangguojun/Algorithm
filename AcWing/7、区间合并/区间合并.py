"""
给定 n 个区间 [li,ri]，要求合并所有有交集的区间。
注意如果在端点处相交，也算有交集。
输出合并完成后的区间个数。
---------------------
第一行包含整数n。
接下来n行，每行包含两个整数 l 和 r。
---------------------
共一行，包含一个整数，表示合并区间完成后的区间个数。
---------------------
5
1 2
2 4
5 6
7 8
7 9
---------------------
3
"""
n = int(input())
ll = []
res = []
while n:
    n -= 1
    ll.append(list(map(int,input().split())))
ll.sort()

start = end = float('-inf')
for l, r in ll:
    if end < l:
        if start != float('-inf'): res.append([start, end])
        start = l
        end = r
    else:
        end = max(end, r)
if start != float('-inf'): res.append([start, end])
print(res)







