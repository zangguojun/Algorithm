m = int(input())
N = 100010
e = [0]*N
ne = [0]*N
head = -1
idx = 0

def insert_to_head(x):
    global head, idx
    e[idx] = x
    ne[idx] = head
    head = idx
    idx += 1
def insert_to_k(k, x):
    global idx
    e[idx] = x
    ne[idx] = ne[k]
    ne[k] = idx
    idx += 1
def remove(k):
    if k == -1:
        global head
        head = ne[head]
    ne[k] = ne[ne[k]]

while m:
    m -= 1
    li = input().split()
    op = li[0]
    if op == "H":
        insert_to_head(int(li[1]))
    elif op == "D":
        remove(int(li[1]) - 1)
    else:
        insert_to_k(int(li[1]) - 1, int(li[2]))
i = head
while i != -1:
    print(e[i],end = ' ')
    i = ne[i]
