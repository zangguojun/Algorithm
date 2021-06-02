## Trie字符串统计

### 数组实现Trie

```
N = 100010
idx = 0
str = ['0'] * N
cnt = [0] * N
son = [[0] * 26 for i in range(N)]

def insert(str):
    global idx, cnt, son
    p = 0
    for ch in str:
        u = ord(ch) - ord('a')
        if son[p][u] == 0:
            idx += 1
            son[p][u] = idx
        p = son[p][u]
    cnt[p] += 1

def query(str):
    global cnt, son
    p = 0
    for ch in str:
        u = ord(ch) - ord('a')
        if son[p][u] == 0: return 0
        p = son[p][u]
    return cnt[p]

n = int(input())
while n:
    n -= 1
    opt, s = input().split()
    if (opt == 'I'):
        insert(s)
    else: print(query(s))
```

### 字典实现Trie
```
root = {}

def insert(str):
    p = root
    for ch in str:
        p = p.setdefault(ch, {})
    p['count'] = p.get('count', 0) + 1

def query(str):
    p = root
    for ch in str:
        if p.get(ch) == None: return 0
        p = p[ch]
    return p.get('count', 0)

n = int(input())
while n:
    n -= 1
    opt, s = input().split()
    if (opt == 'I'):
        insert(s)
    else: print(query(s))
```

### 类实现Trie
```
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
```