n, q = list(map(int,input().split()))
alist = list(map(int,input().split()))
# q[mid] >= x
def searchLeft(q, l, r, k):
    while l < r:
        mid = l + r >> 1
        if q[mid] >= k: r = mid
        else: l = mid + 1
    return l
def searchRight(q, l, r, k):
    while l < r:
        mid = l + r + 1 >> 1
        if q[mid] <= k: l = mid
        else: r = mid - 1
    return l


while q:
    q -= 1
    k = int(input())
    l = searchLeft(alist, 0, n - 1, k)
    if alist[l] != k:
        print('-1 -1')
    else:
        r = searchRight(alist, 0, n - 1, k)
        print(l, r)
