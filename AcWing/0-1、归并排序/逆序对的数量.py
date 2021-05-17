n = int(input())
alist = list(map(int,input().split()))
def mergeSort(q, l, r):
    if l == r: return 0
    mid = l + r >> 1
    count = mergeSort(q, l, mid) + mergeSort(q, mid + 1, r)
    i = l
    j = mid + 1
    res = []
    while i <= mid and j <= r:
        if q[i] <= q[j]:
            res.append(q[i])
            i += 1
        else:
            res.append(q[j])
            j += 1
            count += mid - i + 1
    while i <= mid:
        res.append(q[i])
        i += 1
    while j <= r:
        res.append(q[j])
        j += 1
    q[l:r+1] = res
    return count

print(mergeSort(alist, 0, n - 1))
