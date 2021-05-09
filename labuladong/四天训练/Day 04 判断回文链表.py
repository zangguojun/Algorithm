class Node:
    def __init__(self,item=None):
        self.item = item
        self.next = None

class SingleNode:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def length(self):
        count = 0
        cur = self._head
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def traverse(self):
        cur = self._head
        while cur is not None:
            yield cur.item
            cur = cur.next

    def appendleft(self,item):
        node = Node(item)
        node.next = self._head
        self._head = node
        
    def append(self,item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node    

    def insert(self,index,item):
        if index <= 0:
            self.appendleft(item)
        elif index >= self.length():
            self.append(item)
        else:            
            node = Node(item)
            cur = self._head
            for i in range(index-1):
                cur = cur.next
            node.next = cur.next
            cur.next = node
    def remove(self,item):
        cur = self._head
        pre = None
        while cur is not None:
            if cur.item == item:
                if pre is None:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                return True
            else:
                pre = cur
                cur = cur.next
        return False
    
    def find(self,item):
        return item in self.traverse()
#1
from collections import deque
li = deque()
def traverse(head):
    if head is None:
        return
    traverse(head.next)
    li.append(head.item)
    
def isPalindrome(head):
    traverse(head)
    cur = head
    while cur is not None:
        if cur.item != li.popleft():
            return False
        cur = cur.next
    return True and len(li) == 0
#2
def traverse2(right,left):
    if right is None:
        return True
    res = traverse2(right.next,left.next)
    return res and (right.item == left.item)
    
def isPalindrome2(head):
    left = head
    return traverse2(head,left)


ln = SingleNode()
for i in list('上海自来水来自海上'):
    ln.append(i)

isP = isPalindrome(ln._head)
print(isP)

isP2 = isPalindrome2(ln._head)
print(isP2)

for i in ln.traverse():
    print(i,end=' ')












