n, k = list(map(int,input().split()))
alist = list(map(int,input().split()))
def kSort(q, l, r, k):
    if l >= r: return q[l]
    i = l - 1
    j = r + 1
    x = q[i + j >> 1]
    while i < j:
        while True:
            i += 1
            if not q[i] < x: break
        while True:
            j -= 1
            if not q[j] > x: break
        if i < j: q[i], q[j] = q[j], q[i]
    length = j - l + 1
    if k <= length:
        return kSort(q, l, j, k)
    else:
        return kSort(q, j + 1, r, k - length)

print(kSort(alist, 0, n - 1, k))
