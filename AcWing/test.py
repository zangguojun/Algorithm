n = int(input())
alist = list(map(int,input().split()))
def quickSort (q, l, r):
    if l >= r: return
    i = l - 1
    j = r + 1
    x = q[r]
    while i < j:
        while True:
            i += 1
            if not q[i] < x:
                break
        while True:
            j -= 1
            if not q[j] > x:
                break
        if i < j: q[i], q[j] = q[j], q[i]
    quickSort(q, l, i - 1)
    quickSort(q, i, r)

quickSort(alist, 0, n - 1)
for i in alist:
    print(i, end=' ')