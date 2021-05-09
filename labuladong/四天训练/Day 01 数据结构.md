### [学习算法和数据结构的思路指南](http://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247484852&idx=1&sn=85b50b8b0470bb4897e517955f4e5002&chksm=9bd7fbbcaca072aa75e2a241064a403fde1e579d57ab846cd8537a54253ceb2c8b93cc3bf38e&scene=21#wechat_redirect)

#### 一、数据结构的存储方式

##### 基础的数据类型（结构基础）

- 数组   顺序存储
  - 由于是紧凑连续存储,可以随机访问，通过索引**快速找到对应元素**，而且相对节约存储空间。但正因为连续存储，内存空间必须一次性分配够，所以说数组如果要扩容，需要重新分配一块更大的空间，再把数据全部复制过去，**扩容时间复杂度 O(N)**；而且你如果想在数组中间进行插入和删除，每次必须搬移后面的所有数据以保持连续，**增删时间复杂度 O(N)、改查时间复杂度 O(1)**
- 链表   链式存储
  - 因为元素不连续，而是靠指针指向下一个元素的位置，所以**不存在数组的扩容问题**；如果知道某一元素的前驱和后驱，操作指针即可删除该元素或者插入新元素，**增删时间复杂度 O(1)**。但是正因为存储空间不连续，你无法根据一个索引算出对应元素的地址，所以不能随机访问；而且由于每个元素必须存储指向前后元素位置的指针，会消耗相对更多的储存空间，**改查时间复杂度 O(n)**

##### 栈、队列、图、散列表、树、堆 

- 队列、栈：
  - 数组处理：扩容缩容问题
  - 链表处理：指针需要额外的空间存储

- 图：

  - 邻接矩阵：数组，稀疏矩阵浪费空间、迅速判断连通性、可以使用矩阵运算
  - 邻接表：链表，节省空间、很多操作效率不如邻接矩阵

- 散列表：

  - 通过散列函数把键映射到一个大数组里 
  - 解决散列冲突方法
    - 拉链法：链表，操作简单、但需要额外的空间存储指针
    - 线性探查法：数组，连续寻址、不需要指针的存储空间、但操作稍微复杂些

- 树：

  - 数组 --「堆」，因为「堆」是一个完全二叉树，用数组存储不需要节点指针，操作也比较简单
  - 链表 -- 常见「树」，因为不一定是完全二叉树，所以不适合用数组存储
    - 常见树：二叉搜索树、AVL 树、红黑树、区间树、B 树

  > Redis 提供列表、字符串、集合等等几种常用数据结构，但是对于每种数据结构，底层的存储方式都至少有两种，以便于根据存储数据的实际情况使用合适的存储方式

***



#### 二、数据结构的基本操作

> 对于任何数据结构，其基本操作无非**遍历 + 访问**，再具体一点就是：**增删查改**
>
> 各种数据结构的遍历 + 访问无非两种形式：**线性的和非线性**

* 线性 for迭代
  * 数组for遍历
  * 链表for遍历
* 非线性 递归
  * 链表递归遍历
  * 二叉树递归遍历
  * N叉树遍历（与二叉树类似，遍历子树）
  * 图遍历（多个N叉树，但是为了避免环，需要visited标记）

#### 三、算法刷题指南

> **先刷二叉树，先刷二叉树，先刷二叉树**！



#### 四、最后总结

> **先刷二叉树，先刷二叉树，先刷二叉树**！！！！！！！！！！！！！



#### 数组的内置函数

```python
# 数组
li = [1, 2, 3]
for i in li:
    print(i)

for i in len(li):
    print(li[i])

#append(self, object, /)
li.append(4)

#copy(self, /)
##相当于li2 = li[:]
li2 = li.copy()

#extend(self, iterable, /)
##前者合并可迭代对象
li2.extend(li)

#index(self, value, start=0, stop=9223372036854775807, /)
##通过元素值查找元素下标（元素值，开始坐标=0,结束坐标=无穷大）
li2.index(2,4,7)

#count(self, value, /)
li2.count(1)

#insert(self, index, object, /)
li2.insert(1,7)

#pop(self, index=-1, /)
li2.pop(-2)

#remove(self, value, /)
li2.remove(2)

#reverse(self, /)
li2.reverse()

#sort(self, /, *, key=None, reverse=False)
li2.sort(reverse=True)

#clear(self, /)
li2.clear()
```

#### 链表实现

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
ln.insert(-1,0)
ln.insert(100,5)
ln.insert(3,2.333)
ln.remove(2.333)
print(ln.find(2))
print(ln.is_empty())
print(ln.length())
print('===')
for i in ln.traverse():
    print(i)
```





#### 二叉树实现

```python
"""
二叉树
"""


class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class Tree:
    def __init__(self, root=None):
        self.root = root

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
        else:
            q = [self.root]
            while True:
                pop_node = q.pop(0)
                if pop_node.left is None:
                    pop_node.left = node
                    return
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)

    def get_parent(self, item):
        # 找到item的父节点
        if self.root.data == item:
            return None
        q = [self.root]
        while q:
            pop_node = q.pop(0)
            if pop_node.left and pop_node.left.data == item:
                return pop_node
            elif pop_node.right and pop_node.right.data == item:
                return pop_node
            else:
                if pop_node.left is not None:
                    q.append(pop_node.left)
                if pop_node.right is not None:
                    q.append(pop_node.right)
        return None

    def delete(self, item):
        '''
        从二叉树中删除一个元素
        先获取 待删除节点 item 的父节点
        如果父节点不为空，
            判断 item 的左右子树
            如果左子树为空，那么判断 item 是父节点的左孩子，还是右孩子，如果是左孩子，将父节点的左指针指向 item 的右子树，反之将父节点的右指针指向 item 的右子树
            如果右子树为空，那么判断 item 是父节点的左孩子，还是右孩子，如果是左孩子，将父节点的左指针指向 item 的左子树，反之将父节点的右指针指向 item 的左子树
            如果左右子树均不为空，寻找右子树中的最左叶子节点 x ，将 x 替代要删除的节点。
        删除成功，返回 True
        删除失败, 返回 False

        '''
        if self.root is None:  # 如果根为空，就什么也不做
            return False

        parent = self.get_parent(item)
        if parent:
            del_node = parent.left if parent.left.data == item else parent.right  # 待删除节点
            if del_node.left is None:
                if parent.left.data == item:
                    parent.left = del_node.right
                else:
                    parent.right = del_node.right
                del del_node
                return True
            elif del_node.right is None:
                if parent.left.data == item:
                    parent.left = del_node.left
                else:
                    parent.right = del_node.left
                del del_node
                return True
            else:  # 左右子树都不为空
                tmp_pre = del_node
                tmp_next = del_node.right
                if tmp_next.left is None:
                    # 替代
                    tmp_pre.right = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right

                else:
                    while tmp_next.left:  # 让tmp指向右子树的最后一个叶子
                        tmp_pre = tmp_next
                        tmp_next = tmp_next.left
                    # 替代
                    tmp_pre.left = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
                if parent.left.data == item:
                    parent.left = tmp_next
                else:
                    parent.right = tmp_next
                del del_node
                return True
        else:
            return False

    def preorder(self, root):
        if not root:
            return []
        result = [root.data]
        left_item = self.preorder(root.left)
        right_item = self.preorder(root.right)
        return result + left_item + right_item

    def inorder(self, root):
        if not root:
            return []
        result = [root.data]
        left_item = self.inorder(root.left)
        right_item = self.inorder(root.right)
        return left_item + result + right_item

    def postorder(self, root):
        if not root:
            return []
        result = [root.data]
        left_item = self.postorder(root.left)
        right_item = self.postorder(root.right)
        return left_item + right_item + result

    def traverse(self):
        if self.root is None:
            return None
        q = [self.root]
        res = [self.root.data]
        while q != []:
            pop_node = q.pop(0)
            if pop_node.left is not None:
                q.append(pop_node.left)
                res.append(pop_node.left.data)
            if pop_node.right is not None:
                q.append(pop_node.right)
                res.append(pop_node.right.data)
        return res

if __name__ == '__main__':
    t = Tree()
    for i in range(10):
        t.add(i)
print(t.preorder(t.root))
print(t.inorder(t.root))
print(t.postorder(t.root))
print(t.traverse())
```



