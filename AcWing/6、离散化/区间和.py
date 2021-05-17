"""
假定有一个无限长的数轴，数轴上每个坐标上的数都是0。
我们首先进行 n 次操作，每次操作将某一位置x上的数加c。
然后，进行 m 次询问，每个询问包含两个整数l和r，
你需要求出在区间[l, r]之间的所有数的和。
-------------------
第一行包含两个整数n和m。
接下来 n 行，每行包含两个整数x和c。
再接下里 m 行，每行包含两个整数l和r。
-------------------
共m行，每行输出一个询问中所求的区间内数字和。
-------------------
3 3
1 2
3 6
7 5
1 3
4 6
7 8
-------------------
8
0
5
"""
n, m = map(int,input().split())
nli = []
origin = []
mli = []
while n:
    n -= 1
    arr = list(map(int,input().split()))
    origin.append(arr[0])
    nli.append(arr)

while m:
    m -= 1
    arr = list(map(int,input().split()))
    origin.append(arr[0])
    origin.append(arr[1])
    mli.append(arr)
origin = sorted(list(set(origin)))
origin_len = len(origin)
origin.insert(0,0)

a = [0] * (origin_len + 1)
s = [0] * (origin_len + 1)
for i, val in nli:
    x = origin.index(i)
    a[x] += val

for i in range(1, origin_len + 1):
    s[i] = s[i - 1] + a[i]

for l, r in mli:
    l = origin.index(l)
    r = origin.index(r)
    print(s[r] - s[l - 1])













