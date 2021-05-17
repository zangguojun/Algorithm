N = 100010
e = [0]*N
ne = [0]*N
l = [0]*N
r = [0]*N
r[0] = 1
l[1] = 0
idx = 2
def insert_to_k(k, x):
    global idx
    e[idx] = x
    r[idx] = r[k]
    l[idx] = k
    l[r[k]] = idx
    r[k] = idx
    idx += 1
def remove(k):
    r[l[k]] = r[k]
    l[r[k]] = l[k]
m = int(input())
while m:
    m -= 1
    li = input().split()
    op = li[0]
    if op == "L":
        insert_to_k(0, int(li[1]))
    elif op == "R":
        insert_to_k(l[1], int(li[1]))
    elif op == "D":
        remove(int(li[1]) + 1)
    elif op == "IL":
        insert_to_k(l[int(li[1]) + 1], int(li[2]))
    else:
        insert_to_k(int(li[1]) + 1, int(li[2]))

i = r[0]
while i != 1:
    print(e[i], end = " ")
    i = r[i]
