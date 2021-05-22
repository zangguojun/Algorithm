"""
实现一个队列，队列初始为空，支持四种操作：
(1) “push x” – 向队尾插入一个数x
(2) “pop” – 从队头弹出一个数
(3) “empty” – 判断队列是否为空
(4) “query” – 查询队头元素
------------
第一行包含整数M，表示操作次数。
接下来M行，每行包含一个操作命令，
操作命令为”push x”，”pop”，”empty”，”query”中的一种
------------
对于每个”empty”和”query”操作都要输出一个查询结果，每个结果占一行。
其中，”empty”操作的查询结果为“YES”或“NO”，
”query”操作的查询结果为一个整数，表示队头元素的值
------------
10
push 6
empty
query
pop
empty
push 3
push 4
pop
query
push 6
------------
NO
6
YES
4
"""
N = 100010
q = [0]*N
head = tail = 0
def push(x):
    global tail
    q[tail] = x
    tail += 1
def pop():
    global head
    val = q[head]
    head += 1
    return val
def empty():
    global head, tail
    return "YES" if head == tail else "NO"
def query():
    global head
    return q[head]
m = int(input())
while m:
    m -= 1
    li = input().split()
    op = li[0]
    if op == 'push':
        push(int(li[1]))
    elif op == 'pop':
        pop()
    elif op == 'empty':
        print(empty())
    else:
        print(query())
