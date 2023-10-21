# [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

## 题目

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
```

Explanation: 342 + 465 = 807.

## 题目大意

2 个逆序的链表，要求从低位开始相加，得出结果也逆序输出，返回值是逆序结果链表的头结点。

## 解题思路

需要注意的是各种进位问题。

极端情况，例如

```
Input: (9 -> 9 -> 9 -> 9 -> 9) + (1 -> )
Output: 0 -> 0 -> 0 -> 0 -> 0 -> 1
```

为了处理方法统一，可以先建立一个虚拟头结点，这个虚拟头结点的 Next 指向真正的 head，这样 head 不需要单独处理，直接 while
循环即可。另外判断循环终止的条件不用是 p.Next ！= nil，这样最后一位还需要额外计算，循环终止条件应该是 p != nil。


对于Go版本的解题思路：

1. 创建一个空节点作为返回链表的头节点。 
2. 使用变量n1、n2表示链表l1和l2的当前节点值，carry表示当前位的进位，current指向返回链表的当前节点。 
3. 当l1、l2任意一个链表未遍历完或有进位时，继续循环。 
4. 如果l1链表已遍历完，将n1设为0；否则取l1当前节点值。 
5. 对l2链表进行同样处理。 
6. 求当前位相加结果，新建节点，节点值是当前位求和对10取余的结果。 
7. current指针前移，计算下一位的进位。 
8. 返回头节点的下一个节点，作为链表结果。


对于Python版本的解题思路：

1. 创建一个空节点作为返回链表的头节点。 
2. current指向返回链表的当前节点，carry表示当前位的进位。
3. 遍历l1和l2链表，同时存在节点或有进位时，继续循环。 
4. 获取当前节点的值，如果节点不存在则取0。 
5. 计算当前位的和以及进位，并创建新节点。 
6. current指针前移，更新l1和l2的指针。 
7. 返回头节点的下一个节点，作为链表结果。


对于Java版本的解题思路：

1. 创建一个空节点作为返回链表的头节点。 
2. current指向返回链表的当前节点，carry表示当前位的进位。 
3. 遍历l1和l2链表，同时存在节点或有进位时，继续循环。 
4. 获取当前节点的值，如果节点不存在则取0。 
5. 计算当前位的和以及进位，并创建新节点。 
6. current指针前移，更新l1和l2的指针。 
7. 返回头节点的下一个节点，作为链表结果。



对于C++版本的解题思路：

1. 创建一个空节点作为返回链表的头节点。 
2. current指向返回链表的当前节点，carry表示当前位的进位。 
3. 遍历l1和l2链表，同时存在节点或有进位时，继续循环。 
4. 获取当前节点的值，如果节点不存在则取0。 
5. 计算当前位的和以及进位，并创建新节点。 
6. current指针前移，更新l1和l2的指针。 
7. 返回头节点的下一个节点，作为链表结果。

## Go

```Go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {

    // 创建一个空节点作为返回链表的头节点
    head := &ListNode{Val: 0} 
    
    // 定义变量 n1、n2 表示链表 l1 和 l2 的当前节点值
    // carry 表示当前位的进位
    // current 指向返回链表的当前节点
    n1, n2, carry, current := 0, 0, 0, head

    // 当 l1、l2 任意一个链表未遍历完 或 有进位时,继续循环
    for l1 != nil || l2 != nil || carry != 0 {
        
        // 如果 l1 链表已遍历完,将 n1 设为 0
        if l1 == nil {
           n1 = 0
        } else {
           // 否则取 l1 当前节点值
           n1 = l1.Val
           // l1 指针前移
           l1 = l1.Next
        }
        
        // 对 l2 链表进行同样处理   
        if l2 == nil {
           n2 = 0
        } else {
           n2 = l2.Val
           l2 = l2.Next
        }
        
        // 求当前位相加结果
        // 新建节点,节点值是当前位求和对 10 取余的结果
        current.Next = &ListNode{Val: (n1 + n2 + carry) % 10}
        // current 指针前移
        current = current.Next
        // 计算下一位的进位
        carry = (n1 + n2 + carry) / 10
    }

    // 返回头节点的下一个节点,作为链表结果
    return head.Next
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()  # 创建一个空节点作为返回链表的头节点
        current = head  # current指向返回链表的当前节点
        carry = 0  # carry表示当前位的进位

        while l1 or l2 or carry:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            sum = n1 + n2 + carry
            carry = sum // 10  # 计算下一位的进位
            current.next = ListNode(sum % 10)  # 新节点，节点值是当前位求和对10取余的结果
            current = current.next  # current指针前移
            if l1:
                l1 = l1.next  # l1指针前移
            if l2:
                l2 = l2.next  # l2指针前移

        return head.next  # 返回头节点的下一个节点，作为链表结果
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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(); // 创建一个空节点作为返回链表的头节点
        ListNode current = head; // current指向返回链表的当前节点
        int carry = 0; // carry表示当前位的进位

        while (l1 != null || l2 != null || carry != 0) {
            int n1 = (l1 != null) ? l1.val : 0;
            int n2 = (l2 != null) ? l2.val : 0;
            int sum = n1 + n2 + carry;
            carry = sum / 10; // 计算下一位的进位

            current.next = new ListNode(sum % 10); // 新建节点，节点值是当前位求和对10取余的结果
            current = current.next; // current指针前移

            if (l1 != null) l1 = l1.next; // l1指针前移
            if (l2 != null) l2 = l2.next; // l2指针前移
        }

        return head.next; // 返回头节点的下一个节点，作为链表结果
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
#include <iostream>
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head = new ListNode(); // 创建一个空节点作为返回链表的头节点
        ListNode* current = head; // current指向返回链表的当前节点
        int carry = 0; // carry表示当前位的进位

        while (l1 != nullptr || l2 != nullptr || carry != 0) {
            int n1 = (l1 != nullptr) ? l1->val : 0;
            int n2 = (l2 != nullptr) ? l2->val : 0;
            int sum = n1 + n2 + carry;

            carry = sum / 10; // 计算下一位的进位
            current->next = new ListNode(sum % 10); // 新建节点，节点值是当前位求和对10取余的结果
            current = current->next; // current指针前移

            if (l1 != nullptr) l1 = l1->next; // l1指针前移
            if (l2 != nullptr) l2 = l2->next; // l2指针前移
        }

        return head->next; // 返回头节点的下一个节点，作为链表结果
    }
};
```
四个版本解法所需的基础知识:

对于Go版本，你需要掌握以下基础知识：

- 了解链表的概念和基本操作，例如遍历链表和创建新节点。 
- 熟悉Go语言的基本语法和数据类型，包括变量声明、条件语句、循环语句等。 
- 理解函数的定义和调用，以及函数参数和返回值的使用。 
- 熟悉指针的概念和用法，因为链表节点通常使用指针来连接。 

对于Python版本，你需要掌握以下基础知识：

- 理解链表的概念和基本操作，包括遍历链表和创建新节点。 
- 熟悉Python的基本语法和数据类型，例如变量、条件语句、循环语句等。 
- 熟悉类的定义和使用，因为链表节点可以使用类来表示。 
- 理解函数的定义和调用，以及函数参数和返回值的使用。

对于Java版本，你需要掌握以下基础知识：

- 理解链表的概念和基本操作，例如遍历链表和创建新节点。 
- 熟悉Java的基本语法和数据类型，包括变量声明、条件语句、循环语句等。 
- 熟悉类的定义和使用，因为链表节点可以使用类来表示。 
- 理解函数的定义和调用，以及函数参数和返回值的使用。

对于C++版本，你需要掌握以下基础知识：

- 理解链表的概念和基本操作，包括遍历链表和创建新节点。 
- 熟悉C++的基本语法和数据类型，例如变量声明、条件语句、循环语句等。 
- 熟悉类的定义和使用，因为链表节点可以使用类来表示。 
- 理解指针的概念和用法，因为链表节点通常使用指针来连接。
