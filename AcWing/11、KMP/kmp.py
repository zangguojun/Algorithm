"""
给定一个模式串S，以及一个模板串P，所有字符串中只包含大小写英文字母以及阿拉伯数字。
模板串P在模式串S中多次作为子串出现。
求出模板串P在模式串S中所有出现的位置的起始下标。
----------------
第一行输入整数N，表示字符串P的长度。
第二行输入字符串P。
第三行输入整数M，表示字符串S的长度。
第四行输入字符串S。
----------------
共一行，输出所有出现位置的起始下标（下标从0开始计数），整数之间用空格隔开。
----------------
3
aba
5
ababa
----------------
0 2
"""
n = int(input())
p = list('0 ' + input())

m = int(input())
s = list('0 ' + input())

ne = [-1] * (n + 1)

j = 0
for i in range(2, n + 1):
    while j and p[i] != p[j + 1]: j = ne[j]
    if p[i] == p[j + 1]: j += 1
    ne[i] = j
print(ne)

##j = 0
##for i in range(1, m + 1):
##    while j and s[i] != p[j + 1]: j = ne[j]
##    if s[i] == p[j + 1]: j += 1
##    if j == n:
##        print(i - j, end = ' ')
##        j = ne[j]
