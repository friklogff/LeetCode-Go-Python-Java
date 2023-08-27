# [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

## 题目

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of
the first two lists.

Example :

```
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

```

## 题目大意
合并 2 个有序链表


## 解题思路
Go 解决方案解题思路：

1. 如果链表 `l1` 为空，直接返回链表 `l2`，无需合并。
2. 如果链表 `l2` 为空，直接返回链表 `l1`，无需合并。
3. 如果链表 `l1` 的当前节点值小于链表 `l2` 的当前节点值，说明链表 `l1` 的当前节点可以放在合并链表中，并继续合并剩余部分。
4. 否则，链表 `l2` 的当前节点可以放在合并链表中，并继续合并剩余部分。
5. 返回合并后的链表头节点。

Python 解决方案解题思路：

1. 创建一个虚拟头节点 `dummy`，它不属于合并链表的一部分，仅用于简化代码。
2. 创建一个指针 `current`，初始时指向虚拟头节点，表示合并链表的当前节点。
3. 通过比较链表 `list1` 和 `list2` 的当前节点值，将较小的节点链接到合并链表，并更新相应的链表指针。
4. 重复步骤 3 直到其中一个链表为空。
5. 将剩余部分的链表直接链接到合并链表的末尾。
6. 返回虚拟头节点的下一个节点，即合并后的链表头节点。

Java 解决方案解题思路：

1. 如果链表 `list1` 为空，直接返回链表 `list2`，无需合并。
2. 如果链表 `list2` 为空，直接返回链表 `list1`，无需合并。
3. 如果链表 `list1` 的当前节点值小于等于链表 `list2` 的当前节点值，说明链表 `list1` 的当前节点可以放在合并链表中，并继续合并剩余部分。
4. 否则，链表 `list2` 的当前节点可以放在合并链表中，并继续合并剩余部分。
5. 返回合并后的链表头节点。

C++ 解决方案解题思路：

1. 如果链表 `l1` 为空，直接返回链表 `l2`，无需合并。
2. 如果链表 `l2` 为空，直接返回链表 `l1`，无需合并。
3. 如果链表 `l1` 的当前节点值小于等于链表 `l2` 的当前节点值，说明链表 `l1` 的当前节点可以放在合并链表中，并继续合并剩余部分。
4. 否则，链表 `l2` 的当前节点可以放在合并链表中，并继续合并剩余部分。
5. 返回合并后的链表头节点。

## 代码

## Go

```Go
/**
 * Definition for singly-linked list.
 * 单链表的定义，每个节点有一个整数值和指向下一个节点的指针。
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

// mergeTwoLists 函数用于合并两个有序链表，返回合并后的链表头节点。
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
    // 若链表 l1 为空，直接返回链表 l2，无需合并。
    if l1 == nil {
        return l2
    }
    // 若链表 l2 为空，直接返回链表 l1，无需合并。
    if l2 == nil {
        return l1
    }
    // 若链表 l1 的节点值小于链表 l2 的节点值，
    // 则将链表 l1 的当前节点与合并后的链表继续合并，
    // 并返回合并后的链表头节点为 l1。
    if l1.Val < l2.Val {
        l1.Next = mergeTwoLists(l1.Next, l2)
        return l1
    }
    // 若链表 l2 的节点值小于等于链表 l1 的节点值，
    // 则将链表 l2 的当前节点与合并后的链表继续合并，
    // 并返回合并后的链表头节点为 l2。
    l2.Next = mergeTwoLists(l1, l2.Next)
    return l2
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 创建一个虚拟头节点，简化操作
        dummy = ListNode(0)
        current = dummy  # 指向当前节点的指针

        # 依次比较两个链表的节点，将较小的节点链接到合并链表
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # 将剩余部分链接到合并链表
        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next  # 返回合并后的链表头节点

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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // 若其中一个链表为空，直接返回另一个链表
        if (list1 == null) {
            return list2;
        }
        if (list2 == null) {
            return list1;
        }
        
        // 若链表 list1 的节点值小于等于链表 list2 的节点值，
        // 则将链表 list1 的当前节点与合并后的链表继续合并，
        // 并返回合并后的链表头节点为 list1。
        if (list1.val <= list2.val) {
            list1.next = mergeTwoLists(list1.next, list2); // 递归合并剩余部分
            return list1;
        }
        
        // 若链表 list2 的节点值小于链表 list1 的节点值，
        // 则将链表 list2 的当前节点与合并后的链表继续合并，
        // 并返回合并后的链表头节点为 list2。
        list2.next = mergeTwoLists(list1, list2.next); // 递归合并剩余部分
        return list2;
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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        // 若其中一个链表为空，直接返回另一个链表
        if (l1 == NULL) {
            return l2;
        }
        if (l2 == NULL) {
            return l1;
        }
        
        // 若链表 l1 的节点值小于等于链表 l2 的节点值，
        // 则将链表 l1 的当前节点与合并后的链表继续合并，
        // 并返回合并后的链表头节点为 l1。
        if (l1->val <= l2->val) {
            l1->next = mergeTwoLists(l1->next, l2); // 递归合并剩余部分
            return l1;
        }
        
        // 若链表 l2 的节点值小于链表 l1 的节点值，
        // 则将链表 l2 的当前节点与合并后的链表继续合并，
        // 并返回合并后的链表头节点为 l2。
        l2->next = mergeTwoLists(l1, l2->next); // 递归合并剩余部分
        return l2;
    }
};

```
Go 解决方案所需基础知识：

- **Go 语言基础**: 了解 Go 语言的基本语法、变量声明、函数定义等。
- **递归**: 理解递归的概念和用法，能够编写递归函数。
- **链表**: 知道链表的基本概念，理解链表节点的结构以及如何通过指针操作链表。

Python 解决方案所需基础知识：

- **Python 基础**: 熟悉 Python 语言的基本语法，包括变量、函数、类的定义等。
- **递归**: 理解递归的原理和应用，能够使用递归解决问题。
- **链表**: 了解链表的基本概念，知道如何定义链表节点并进行操作。

Java 解决方案所需基础知识：

- **Java 基础**: 熟悉 Java 语言的基本语法，包括变量、函数、类的定义等。
- **递归**: 理解递归的概念和原理，能够编写递归函数。
- **链表**: 理解链表的概念，知道如何定义链表节点并进行操作。

C++ 解决方案所需基础知识：

- **C++ 基础**: 了解 C++ 语言的基本语法，包括变量、函数、类的定义等。
- **递归**: 理解递归的原理和用法，能够编写递归函数。
- **链表**: 知道链表的基本概念，了解如何定义链表节点并进行操作。

