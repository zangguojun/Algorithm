n = int(input())
alist = list(map(int,input().split()))
def quickSort (q, l, r):
    if l >= r: return
    i = l - 1
    j = r + 1
    x = q[l + r >> 1]
    while i < j:
        i += 1
        while q[i] < x:
            i += 1
        j -= 1
        while q[j] > x:
            j -= 1
        if i < j: q[i], q[j] = q[j], q[i]
    quickSort(q, l, j)
    quickSort(q, j + 1, r)

quickSort(alist, 0, n - 1)
for i in alist:
    print(i, end=' ')
