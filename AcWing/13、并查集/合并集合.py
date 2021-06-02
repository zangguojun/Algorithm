n, m = map(int, input().split())
p = [i for i in range(n + 1)]

def find(x):
    if p[x] != x: p[x] = find(p[x])
    return p[x]

while m:
    m -= 1
    t, a, b = input().split()
    a, b = int(a), int(b)
    
    if t == 'M':
        p[find(a)] = find(b)
    else:
        if find(a) == find(b):
            print('Yes')
        else:
            print('No')
    
