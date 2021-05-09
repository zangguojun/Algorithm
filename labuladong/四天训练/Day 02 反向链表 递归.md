## [反转链表的一部分](http://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247484467&idx=1&sn=beb3ae89993b812eeaa6bbdeda63c494&chksm=9bd7fa3baca0732dc3f9ae9202ecaf5c925b4048514eeca6ac81bc340930a82fc62bb67681fa&scene=21#wechat_redirect)   迭代方式

### 〇、链表实现

```python
class Node:
    def __init__(self,item):
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
        
ln = SingleNode()
ln.appendleft(2)
ln.appendleft(1)
ln.append(3)
ln.append(4)
for i in ln.traverse():
    print(i)
```

#### 一、递归反转整个链表

- 
    ```python
    class Node(object):
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next

        @staticmethod
        def reverse(head):
            if head.next == None:
                return head
            last = reverse(head.next)
            head.next.next = head
            head.next = None
            return last

    ln = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))
    root = Node.reverse(ln)
    while root:
            print(root.value)
            root =root.next
    ```

- ```python
  @staticmethod
  def reverse(head):
      if head.next == None:
          return head
      last = SingleNode.reverse(head.next)
      head.next.next = head
      head.next = None
      return last
  
  print('整体反转后：')
  ln._head = SingleNode.reverse(ln._head)
  
  for i in ln.traverse():
      print(i)
  ```

#### 二、反转链表前 N 个节点

```python
rear = Node()
def reverseN(head,count):
    global rear
    if count == 1:
        rear = head.next
        
        return head
    last = reverseN(head.next,count-1)
    head.next.next = head
    head.next = rear
    return last

print('反转前n个后：')
ln._head = reverseN(ln._head,3)

for i in ln.traverse():
    print(i)
```



#### 三、反转链表的一部分

```python
def reverseBetween(head,m,n):
    if m == 1:
        return reverseN(head,n)

    head.next = reverseBetween(head.next,m-1,n-1)
    return head

print('反转[m,n]后：（例：[2,4]）')

ln._head = reverseBetween(ln._head,2,4)

for i in ln.traverse():
    print(i)

```





















