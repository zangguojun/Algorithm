"""
实现一个栈，栈初始为空，支持四种操作：
(1) “push x” – 向栈顶插入一个数x
(2) “pop” – 从栈顶弹出一个数
(3) “empty” – 判断栈是否为空
(4) “query” – 查询栈顶元素
-------------

> 

现在要对栈进行M个操作，其中的每个操作3和操作4都要输出相应的结果
-------------
第一行包含整数M，表示操作次数
接下来M行，每行包含一个操作命令，
操作命令为”push x”，”pop”，”empty”，”query”中的一种
-------------
对于每个”empty”和”query”操作都要输出一个查询结果，每个结果占一行
其中，”empty”操作的查询结果为“YES”或“NO”，
”query”操作的查询结果为一个整数，表示栈顶元素的值
-------------
10
push 5
query
push 6
pop
query
pop
empty
push 4
query
empty
-------------
5
5
YES
4
NO
"""
N = 100010
s = [0]*N
tt = 0
def push(x):
    global tt
    tt += 1
    s[tt] = x
def pop():
    global tt
    val = s[tt]
    tt -= 1
    return val
def empty():
    global tt
    return "NO" if tt > 0 else "YES"
def query():
    global tt
    return s[tt]

m = int(input())
while m:
    m -= 1
    li = input().split()
    op = li[0]
    if op == 'push':
        push(int(li[1]))
    elif op == 'pop':
        pop()
    elif op == 'query':
        print(query())
    elif op == 'empty':
        print(empty())
