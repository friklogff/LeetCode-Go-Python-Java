# [86. Partition List](https://leetcode.com/problems/partition-list/)

## 题目

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

```
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
```


## 题目大意

给定一个数 x，比 x 大或等于的数字都要排列在比 x 小的数字后面，并且相对位置不能发生变化。由于相对位置不能发生变化，所以不能用类似冒泡排序的思想。

## 解题思路

这道题最简单的做法是构造双向链表，不过时间复杂度是 O(n^2)。

(以下描述定义，大于等于 x 的都属于比 x 大)

更优的方法是新构造 2 个链表，一个链表专门存储比 x 小的结点，另一个专门存储比 x 大的结点。在原链表头部开始扫描一边，依次把这两类点归类到 2 个新建链表中，有点入栈的意思。由于是从头开始扫描的原链表，所以原链表中的原有顺序会依旧被保存下来。最后 2 个新链表里面会存储好各自的结果，把这两个链表，比 x 小的链表拼接到 比 x 大的链表的前面，就能得到最后的答案了。
每个版本的解题思路如下：

Go

- 创建两个哑节点，一个dummy1用于存储小于x的值，一个dummy2用于存储大于等于x的值。
- 定义指针p1和p2分别指向dummy1和dummy2的头结点。
- 遍历原链表，将节点插入到对应的哑节点之后。
- 将dummy2和dummy1拼接起来，返回dummy2的next即可。

Python

- 创建两个哑节点，一个dummy1用于存储小于x的值，一个dummy2用于存储大于等于x的值。
- 定义指针p1和p2分别指向dummy1和dummy2的头结点。
- 遍历原链表，将节点插入到对应的哑节点之后。
- 将dummy2和dummy1拼接起来，返回dummy2的next即可。

Java

- 创建两个哑节点，一个dummy1用于存储小于x的值，一个dummy2用于存储大于等于x的值。
- 定义指针p1和p2分别指向dummy1和dummy2的头结点。
- 遍历原链表，将节点插入到对应的哑节点之后。
- 将dummy2和dummy1拼接起来，返回dummy2的next即可。

C++

- 创建两个哑节点，一个dummy1用于存储小于x的值，一个dummy2用于存储大于等于x的值。
- 定义指针p1和p2分别指向dummy1和dummy2的头结点。
- 遍历原链表，将节点插入到对应的哑节点之后。
- 将dummy2和dummy1拼接起来，返回dummy2的next即可。
## 代码

## Go

```Go
// 定义 ListNode 结构体表示单向链表节点
type ListNode struct {
    Val int // 当前节点存储的值
    Next *ListNode // 指向下一个节点的指针
}

// 声明 partition 函数接收一个 head 指针和一个整数 x，并返回一个新的链表头指针
func partition(head *ListNode, x int) *ListNode {
    // 用 dummy1 和 dummy2 分别表示小于和大于等于 x 的两个链表的哑节点
    dummy1, dummy2 := &ListNode{-1, nil}, &ListNode{-101, nil}
    // p1 和 p2 分别表示两个链表的当前节点，初始化为对应哑节点
    p1, p2 := dummy1, dummy2
    // p 表示当前遍历到的原链表节点，从头开始
    p := head
    
    // 遍历整个原链表，将其拆分成两个新链表
    for p != nil {
        if p.Val >= x { // 如果当前节点值大于等于 x，放入第一个新链表中
            p1.Next = p
            p1 = p1.Next
        } else { // 否则放入第二个新链表中
            p2.Next = p
            p2 = p2.Next
        }
        tmp := p.Next // 记录下一个节点的位置
        p.Next = nil // 将当前节点从原链表中分离出来
        p = tmp // 更新当前节点为下一个节点
    }
    
    // 连接两个新链表，并返回第二个新链表的头指针(dummy2.Next)
    p2.Next = dummy1.Next
    return dummy2.Next
}

```

## Python

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1, dummy2 = ListNode(-1), ListNode(-101)
        p1, p2 = dummy1, dummy2
        p = head
        while p:
            if p.val >= x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            tmp = p.next
            p.next = None
            p = tmp
        p2.next = dummy1.next
        return dummy2.next
```

## Java

```Java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode dummy1 = new ListNode(-1);
        ListNode dummy2 = new ListNode(-101);
        ListNode p1 = dummy1;
        ListNode p2 = dummy2;
        ListNode p = head;

        while (p != null) {
            if (p.val >= x) {
                p1.next = p;
                p1 = p1.next;
            } else {
                p2.next = p;
                p2 = p2.next;
            }

            ListNode tmp = p.next;
            p.next = null;
            p = tmp;
        }

        p2.next = dummy1.next;
        return dummy2.next;
    }
}

```

## Cpp

```Cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode* dummy1 = new ListNode(-1);
        ListNode* dummy2 = new ListNode(-101);
        ListNode* p1 = dummy1;
        ListNode* p2 = dummy2;
        ListNode* p = head;

        while (p != nullptr) {
            if (p->val >= x) {
                p1->next = p;
                p1 = p1->next;
            } else {
                p2->next = p;
                p2 = p2->next;
            }

            ListNode* tmp = p->next;
            p->next = nullptr;
            p = tmp;
        }

        p2->next = dummy1->next;
        return dummy2->next;
    }
};

```
Go

- Go语言中struct结构体的定义和使用
- 链表的基本操作，如遍历、插入、删除等

Python

- Python语言中class类的定义和使用
- 链表的基本操作，如遍历、插入、删除等

Java

- Java语言中class类的定义和使用
- 链表的基本操作，如遍历、插入、删除等

C++

- C++语言中struct结构体的定义和使用
- 链表的基本操作，如遍历、插入、删除等

每个版本的解题思路详见上面的代码部分。