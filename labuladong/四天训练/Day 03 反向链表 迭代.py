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

    @staticmethod
    def reverse(head):
        pre = None
        cur = head
        nxt = head
        while cur is not None:
            nxt = cur.next
            cur.next = pre

            pre = cur
            cur = nxt
        return pre

    @staticmethod
    def reverse2another(head,another):
        pre = None
        cur = head
        nxt = head
        while cur.item != another.item:
        #while cur != another:
            if cur == head:
                rear = cur
            nxt = cur.next
            cur.next = pre

            pre = cur
            cur = nxt
        rear.next = nxt
        return pre

    @staticmethod
    def reverseN(head,n):
        pre = None
        cur = head
        nxt = head
        for i in range(n):
            if cur == head:
                rear = cur
            nxt = cur.next
            cur.next = pre

            pre = cur
            cur = nxt
        rear.next = nxt
        return pre

    @staticmethod
    def reverseBetween(head,m,n):
        pre = None
        cur = head
        nxt = head
        for i in range(m-1):
            nxt = cur.next
            pre = cur
            cur = nxt
        for i in range(n):
            print(pre.item,cur.item,nxt.item)
            if i == 0:
                before = pre
                rear = cur
            nxt = cur.next
            cur.next = pre

            pre = cur
            cur = nxt
        rear.next = nxt
        before.next = pre
        return head

    
    
    @staticmethod
    def reverseKGroup(head,k):
        a = b = head
        for i in range(k):
            if b is None:
                return head
            b = b.next
        if b is None:
            last = SingleNode.reverse(a)
        else:
            last = SingleNode.reverse2another(a,b)
        a.next = SingleNode.reverseKGroup(b,k)
        return last
    


ln = SingleNode()
ln.appendleft(2)
ln.appendleft(1)
ln.append(3)
ln.append(4)
ln.insert(-1,0)
ln.insert(100,5)
ln.insert(3,2.333)
ln.remove(2.333)
print(ln.find(2))
print(ln.is_empty())
print(ln.length())

for i in ln.traverse():
    print(i)

print('整体反转后：')
ln._head = SingleNode.reverse(ln._head)

for i in ln.traverse():
    print(i)
    
print('反转到另一节点后：（例：Node(3)）')
ln._head = SingleNode.reverse2another(ln._head,Node(3))

for i in ln.traverse():
    print(i)

print('反转前n个后：（例：3）')
ln._head = SingleNode.reverseN(ln._head,3)

for i in ln.traverse():
    print(i)


print('反转[m,n]后：（例：[2,4]）')

ln._head = SingleNode.reverseBetween(ln._head,2,4)

for i in ln.traverse():
    print(i)

print('k个每组反转后：（例：2）')

ln._head = SingleNode.reverseKGroup(ln._head,2)

for i in ln.traverse():
    print(i)








