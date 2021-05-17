"""
输入一个n行m列的整数矩阵，再输入q个询问，每个询问包含四个整数x1, y1, x2, y2，

表示一个子矩阵的左上角坐标和右下角坐标。对于每个询问输出子矩阵中所有数的和。
---------
第一行包含三个整数n，m，q。

接下来n行，每行包含m个整数，表示整数矩阵。

接下来q行，每行包含四个整数x1, y1, x2, y2，表示一组询问。
---------
共q行，每行输出一个询问的结果。
--------
3  4  3
1  7  2  4
3  6  2  8
2  1  2  3
1  1  2  2
2  1  3  4
1  3  3  4
--------
17
27
21

"""
n, m, q = map(int,input().split())
ll = [[] for i in range(n + 1)]
ll[0] = [0 for i in range(m)]
for i in range(1, n + 1):
    ll[i] = list(map(int,('0 ' + input()).split()))
s = [[0 for i in range(m + 1)] for i in range(n + 1)]
for i in range(1,n + 1):
    for j in range(1,m + 1):
        s[i][j] = ll[i][j] + s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1]   
while q:
    q -= 1
    x1, y1, x2, y2 = map(int,input().split())
    print(s[x2][y2] - s[x1 - 1][y2] - s[x2][y1 - 1] + s[x1 - 1][y1 - 1])






