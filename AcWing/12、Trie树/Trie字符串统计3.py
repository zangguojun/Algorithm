"""
维护一个字符串集合，支持两种操作：
------------------------------------
“I x”向集合中插入一个字符串x；
“Q x”询问一个字符串在集合中出现了多少次。
------------------------------------
共有N个操作，输入的字符串总长度不超过 105105，字符串仅包含小写英文字母。
------------------------------------
第一行包含整数N，表示操作数。
------------------------------------
接下来N行，每行包含一个操作指令，指令为”I x”或”Q x”中的一种。
------------------------------------
对于每个询问指令”Q x”，都要输出一个整数作为结果，表示x在集合中出现的次数。
------------------------------------
5
I abc
Q abc
Q ab
I ab
Q ab
------------------------------------
1
0
1
"""
class TreeNode:
    def __init__(self):
        self.val = 0
        self.next = [None]*26

root = TreeNode()

def insert(str):
    p = root
    for ch in str:
        u = ord(ch) - ord('a')
        if p.next[u] == None:
            p.next[u] = TreeNode()
        p = p.next[u]
    p.val += 1

def query(str):
    p = root
    for ch in str:
        u = ord(ch) - ord('a')
        if p.next[u] == None: return 0
        p = p.next[u]
    return p.val

n = int(input())
while n:
    n -= 1
    opt, s = input().split()
    if (opt == 'I'):
        insert(s)
    else: print(query(s))     
