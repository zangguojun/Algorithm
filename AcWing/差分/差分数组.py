n, m = map(int, input().split())
alist = list(map(int,('0 '+ input()).split()))
b = [0 for i in range(n + 2)]
def insert(l, r, c):
    b[l] += c
    b[r + 1] -= c
for i in range(1, n + 1):
    insert(i, i, alist[i])
while m:
    m -= 1
    l, r, c = map(int, input().split())
    insert(l, r, c)

for i in range(1, n + 1):
    b[i] += b[i - 1]
    print(b[i], end=' ')
