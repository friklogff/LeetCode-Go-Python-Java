# [83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

## 题目

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

```
Input: 1->1->2
Output: 1->2
```

Example 2:

```
Input: 1->1->2->3->3
Output: 1->2->3
```

## 题目大意

删除链表中重复的结点，以保障每个结点只出现一次。


## 解题思路

当然可以，接下来我将为您分别介绍每个版本的解题思路。

1. Go

- **解题思路**:
  1. 首先检查链表是否为空或只有一个节点，如果是，则直接返回原链表，因为没有重复值需要删除。
  2. 递归地对当前节点的下一个节点调用`deleteDuplicates`函数，这样可以确保从当前节点开始的所有后续节点都不包含重复值。
  3. 在递归返回后，比较当前节点与其下一个节点的值。如果它们的值相同，则将当前节点的`next`指针设置为下一个节点的`next`指针，从而跳过下一个节点。
  4. 返回处理后的链表头节点。

2. Python

- **解题思路**:
  1. 首先检查链表是否为空，如果是，则直接返回。
  2. 用`entry`变量引用当前节点的下一个节点。
  3. 如果`entry`不为None，那么比较当前节点和`entry`的值。
  4. 如果它们的值相同，则将当前节点的`next`指向`entry`的`next`，从而跳过`entry`节点。
  5. 递归地对当前节点调用`deleteDuplicates`函数，这样可以确保从当前节点开始的所有节点都不包含重复值。
  6. 如果当前节点和`entry`的值不同，则递归地对`entry`调用`deleteDuplicates`函数。

3. Java

- **解题思路**:
  1. 首先检查链表是否为空或只有一个节点，如果是，则直接返回原链表。
  2. 递归地对当前节点的下一个节点调用`deleteDuplicates`函数。
  3. 在递归返回后，比较当前节点与其下一个节点的值。如果它们的值相同，则将当前节点的`next`指针设置为下一个节点的`next`指针。
  4. 返回处理后的链表头节点。

4. Cpp

- **解题思路**:
  1. 首先检查链表是否为空或只有一个节点，如果是，则直接返回原链表。
  2. 递归地对当前节点的下一个节点调用`deleteDuplicates`函数。
  3. 在递归返回后，比较当前节点与其下一个节点的值。如果它们的值相同，则将当前节点的`next`指针设置为下一个节点的`next`指针。
  4. 返回处理后的链表头节点。

对于这四种语言版本，解题思路基本是相同的，主要的区别在于语言语法和具体实现细节。
## 代码

## Go

```Go
/**
 * 链表节点的定义
 * type ListNode struct {
 *     Val int           // 节点的值
 *     Next *ListNode    // 指向下一个节点的指针
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
    // 如果链表为空或者只有一个节点，直接返回原链表
    if head == nil || head.Next == nil {
        return head
    }
    
    // 递归调用，删除链表中从第二个节点开始的重复元素
    head.Next = deleteDuplicates(head.Next)
    
    // 如果当前节点的值与下一个节点的值相同，删除当前节点
    if head.Val == head.Next.Val {
        head = head.Next
    }
    
    return head
}

```

## Python

```Python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 如果链表为空，直接返回
        if not head:
            return head

        # entry是当前节点的下一个节点
        entry = head.next

        # 如果有下一个节点
        if entry:
            # 如果当前节点的值与下一个节点的值相同
            if head.val == entry.val:
                # 跳过下一个节点，将当前节点的next指向下一个节点的下一个节点
                head.next = entry.next
                # 递归调用，继续处理当前节点，因为它可能还有重复元素
                self.deleteDuplicates(head)
            else:
                # 如果当前节点的值与下一个节点的值不同，递归调用处理下一个节点
                self.deleteDuplicates(entry)
        
        # 返回处理后的链表头节点
        return head

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
    public ListNode deleteDuplicates(ListNode head) {
        // 如果链表为空或者只有一个节点，直接返回原链表
        if (head == null || head.next == null) {
            return head;
        }
        
        // 递归调用，删除链表中从第二个节点开始的重复元素
        head.next = deleteDuplicates(head.next);
        
        // 如果当前节点的值与下一个节点的值相同，删除当前节点
        if (head.val == head.next.val) {
            head = head.next;
        }
        
        return head;
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
    ListNode* deleteDuplicates(ListNode* head) {
        // 如果链表为空或者只有一个节点，直接返回原链表
        if (head == nullptr || head->next == nullptr) {
            return head;
        }
        
        // 递归调用，删除链表中从第二个节点开始的重复元素
        head->next = deleteDuplicates(head->next);
        
        // 如果当前节点的值与下一个节点的值相同，删除当前节点
        if (head->val == head->next->val) {
            head = head->next;
        }
        
        return head;
    }
};

```

好的，接下来我会分别为Go、Python、Java和Cpp版本的代码解释所需掌握的基础知识。

**1. Go**

- **基础知识**:
  - Go语言的基本语法，包括数据类型、变量、条件语句和循环。
  - Go语言中的指针概念。在这个题目中，链表节点是通过指针进行连接的。
  - Go语言的结构体。ListNode是一个结构体，用于表示链表节点。
  - Go语言的递归函数。deleteDuplicates函数是递归的。

**2. Python**

- **基础知识**:
  - Python的基本语法，包括数据类型、变量、条件语句和循环。
  - Python中的类和对象。在这个题目中，ListNode是一个类，用于表示链表节点。
  - Python中的self关键字。它用于引用对象的当前实例。
  - Python的递归函数。deleteDuplicates方法是递归的。

**3. Java**

- **基础知识**:
  - Java的基本语法，包括数据类型、变量、条件语句和循环。
  - Java中的类和对象。ListNode和Solution都是类。
  - Java中的访问修饰符，如public。
  - Java中的构造方法。ListNode类中有多个构造方法。
  - Java的递归函数。deleteDuplicates方法是递归的。

**4. Cpp**

- **基础知识**:
  - C++的基本语法，包括数据类型、变量、条件语句和循环。
  - C++中的指针和引用。在这个题目中，链表节点是通过指针进行连接的。
  - C++中的类和对象。ListNode和Solution都是类。
  - C++中的构造函数和析构函数。ListNode类中有多个构造函数。
  - C++的递归函数。deleteDuplicates方法是递归的。

对于每种语言，如果想深入理解和掌握这个题目和代码，你还需要对数据结构中的链表有所了解，包括链表的基本操作（如插入、删除节点）和常见的链表问题。