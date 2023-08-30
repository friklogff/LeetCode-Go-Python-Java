# [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/description/)

## 题目

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.



Example:

```c
Given 1->2->3->4, you should return the list as 2->1->4->3.
```

## 题目大意

两两相邻的元素，翻转链表

## 解题思路

Go版本：
- 创建一个虚拟节点dummy，将其指向原链表的头节点。
- 使用一个指针pt来遍历链表，直到没有足够的相邻节点可以交换。
- 在每一轮循环中，获取需要交换的相邻节点node1和node2。
- 进行节点交换，即将pt的next指向node2，node1的next指向node2的next，node2的next指向node1。
- 更新指针pt的位置，继续下一轮交换。
- 返回交换相邻节点后的链表头节点。

Python版本：
- 创建一个虚拟节点dummy，将其指向原链表的头节点。
- 使用一个指针pt来遍历链表，直到没有足够的相邻节点可以交换。
- 在每一轮循环中，获取需要交换的相邻节点node1和node2。
- 进行节点交换，即将pt的next指向node2，node1的next指向node2的next，node2的next指向node1。
- 更新指针pt的位置，继续下一轮交换。
- 返回交换相邻节点后的链表头节点。

Java版本：
- 创建一个虚拟节点dummy，将其指向原链表的头节点。
- 使用一个指针pt来遍历链表，直到没有足够的相邻节点可以交换。
- 在每一轮循环中，获取需要交换的相邻节点node1和node2。
- 进行节点交换，即将pt的next指向node2，node1的next指向node2的next，node2的next指向node1。
- 更新指针pt的位置，继续下一轮交换。
- 返回交换相邻节点后的链表头节点。

C++版本：
- 如果链表为空，直接返回原链表头节点。
- 创建一个虚拟节点virNode，将其指向原链表的头节点。
- 使用三个指针p1、p2和p3来进行节点交换。
- 创建一个指针ago，用于记录上一组交换节点的末尾节点。
- 循环遍历链表，直到没有足够的相邻节点可以交换。
- 获取p2的下一个节点。
- 将p2的next指针置为空，然后将p2的next指向p1，将p1的next指向p3，将ago的next指向p2。
- 更新指针ago为p1，指针p1为p3，指针p2为p1的下一个节点。
- 返回交换相邻节点后的链表头节点。## 代码
## Go
```Go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

// 定义一个函数，用于交换链表中相邻节点的位置
func swapPairs(head *ListNode) *ListNode {
    // 创建一个虚拟节点，指向原链表的头节点
    dummy := &ListNode{Next: head}
    
    // 循环遍历链表，直到没有足够的相邻节点可以交换
    for pt := dummy; pt != nil && pt.Next != nil && pt.Next.Next != nil; {
        // 使用多重赋值的方式交换相邻节点的位置
        pt, pt.Next, pt.Next.Next, pt.Next.Next.Next = pt.Next, pt.Next.Next, pt.Next.Next.Next, pt.Next
    }
    
    // 返回交换相邻节点后的链表头节点的指针
    return dummy.Next
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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 创建一个虚拟节点，指向原链表的头节点
        dummy = ListNode(0)
        dummy.next = head
        
        # 使用一个指针pt来遍历链表
        pt = dummy
        
        # 循环遍历链表，直到没有足够的相邻节点可以交换
        while pt.next and pt.next.next:
            # 获取需要交换的相邻节点
            node1 = pt.next
            node2 = pt.next.next
            
            # 进行节点交换
            pt.next = node2
            node1.next = node2.next
            node2.next = node1
            
            # 更新指针pt的位置，继续下一轮交换
            pt = node1
        
        # 返回交换相邻节点后的链表头节点
        return dummy.next
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
    public ListNode swapPairs(ListNode head) {
        // 创建一个虚拟节点，指向原链表的头节点
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        
        // 使用一个指针pt来遍历链表
        ListNode pt = dummy;
        
        // 循环遍历链表，直到没有足够的相邻节点可以交换
        while (pt.next != null && pt.next.next != null) {
            // 获取需要交换的相邻节点
            ListNode node1 = pt.next;
            ListNode node2 = pt.next.next;
            
            // 进行节点交换
            pt.next = node2;
            node1.next = node2.next;
            node2.next = node1;
            
            // 更新指针pt的位置，继续下一轮交换
            pt = node1;
        }
        
        // 返回交换相邻节点后的链表头节点
        return dummy.next;
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
    ListNode* swapPairs(ListNode* head) {
        // 如果链表为空，直接返回原链表头节点
        if (!head) return head;
        
        // 创建一个虚拟节点，指向原链表的头节点
        ListNode* virNode = new ListNode(-1);
        virNode->next = head;
        
        // 使用三个指针p1、p2和p3来进行节点交换
        ListNode* p1 = head;
        ListNode* p2 = p1->next;
        ListNode* p3;
        
        // 创建一个指针ago，用于记录上一组交换节点的末尾节点
        ListNode* ago = virNode;
        
        // 循环遍历链表，直到没有足够的相邻节点可以交换
        while (p2) {
            // 获取p2的下一个节点
            p3 = p2->next;
            
            // 将p2的next指针置为空，然后将p2的next指向p1，将p1的next指向p3，将ago的next指向p2
            p2->next = nullptr;
            p2->next = p1;
            p1->next = p3;
            ago->next = p2;
            
            // 更新指针ago为p1，指针p1为p3，指针p2为p1的下一个节点
            ago = p1;
            p1 = p3;
            if (!p1) {
                break;
            } else {
                p2 = p1->next;
            }
        }
        
        // 返回交换相邻节点后的链表头节点
        return virNode->next;
    }
};

```
**Go 版本:**
1. 掌握 Go 中的结构体(struct)的定义方法,ListNode 表示节点。
2. 理解指针概念,p 用于遍历指向每个节点。
3. 了解 for 循环的语法,通过判断指针是否为 nil 来结束。
4. 知道如何访问结构体成员,通过指针 p.Next。
5. 了解 Make 函数来分配结构体的方法,dummy := &ListNode{0, head}

**C++ 版本:**
1. 掌握 C++ 中的结构体(struct)的定义和使用。本题中用结构体 ListNode 表示链表节点。
2. 了解 C++ 中指针的概念。p 是表示当前节点的指针,通过 p->next 访问后继节点。
3. 知道 while 循环的写法,循环条件是判断指针是否为空。
4. 理解引用传递, ListNode* 表示传递的是指针的引用。
5. 知道如何动态创建结构体对象,这里用 ListNode dummy(0) 创建一个虚拟头节点。

**Java 版本:**
1. 掌握 Java 中的类(class)和对象的概念。ListNode 类表示节点对象。
2. 理解 Java 中引用传递,ListNode 类型表示对象引用。
3. 知道 Java 的 while 循环写法,循环条件是判断引用是否为 null。
4. 能够通过引用访问对象的成员,如 n1.next。
5. 掌握创建对象的语法,new ListNode(0) 创建一个节点对象。

**Python 版本:**
1. 了解 Python 中的类(class)的概念,ListNode 类表示节点。
2. 掌握 Python 的 while 循环语法,通过判断变量是否为 None 来结束循环。
3. 理解 Python 中的对象引用,p 和 n1 等都是对对象的引用。
4. 能使用 . 属性访问对象成员,如 p.next。
5. 知道如何创建类的实例,dummy = ListNode(0) 来创建对象。

