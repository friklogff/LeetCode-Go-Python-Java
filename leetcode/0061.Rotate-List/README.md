# [61. Rotate List](https://leetcode.com/problems/rotate-list/description/)

## 题目

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:  

```
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL 
```

Example 2:  

```
Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL 
```

## 题目大意

旋转链表 K 次。


## 解题思路

这道题需要注意的点是，K 可能很大，K = 2000000000 ，如果是循环肯定会超时。应该找出 O(n) 的复杂度的算法才行。由于是循环旋转，最终状态其实是确定的，利用链表的长度取余可以得到链表的最终旋转结果。

这道题也不能用递归，递归解法会超时。
解决这个问题的思路：

Go 版本解题思路：

1. 首先，检查是否需要旋转。如果链表为空，只包含一个节点，或者旋转次数 k 为 0，则直接返回原始链表。

2. 计算链表的长度。使用一个循环遍历链表，计算链表中的节点数量。

3. 检查是否需要旋转。如果 k 对链表长度取模等于 0，表示不需要旋转，直接返回原始链表。

4. 找到新头节点的位置。这是通过链表长度和 k 的关系来确定的，即链表长度减去 k 对链表长度取模的结果。

5. 创建一个新的头节点，并将其指向新头节点的下一个节点。然后断开循环链表，将新链表的尾部指向空。

6. 返回新链表的头节点。

Python 版本解题思路：

1. 同样地，首先检查是否需要旋转。如果链表为空，只包含一个节点，或者旋转次数 k 为 0，则直接返回原始链表。

2. 计算链表的长度。使用一个循环遍历链表，计算链表中的节点数量。

3. 检查是否需要旋转。如果 k 对链表长度取模等于 0，表示不需要旋转，直接返回原始链表。

4. 找到新头节点的位置。这是通过链表长度和 k 的关系来确定的，即链表长度减去 k 对链表长度取模的结果。

5. 更新链表的头尾连接关系，形成新的旋转链表。

6. 返回新链表的头节点。

Java 版本解题思路：

1. 同样地，首先检查是否需要旋转。如果链表为空，只包含一个节点，或者旋转次数 k 为 0，则直接返回原始链表。

2. 计算链表的长度。使用一个循环遍历链表，计算链表中的节点数量。

3. 检查是否需要旋转。如果 k 对链表长度取模等于 0，表示不需要旋转，直接返回原始链表。

4. 找到新头节点的位置。这是通过链表长度和 k 的关系来确定的，即链表长度减去 k 对链表长度取模的结果。

5. 更新链表的头尾连接关系，形成新的旋转链表。

6. 返回新链表的头节点。

C++ 版本解题思路：

1. 同样地，首先检查是否需要旋转。如果链表为空，只包含一个节点，或者旋转次数 k 为 0，则直接返回原始链表。

2. 计算链表的长度。使用一个循环遍历链表，计算链表中的节点数量。

3. 检查是否需要旋转。如果 k 对链表长度取模等于 0，表示不需要旋转，直接返回原始链表。

4. 找到新头节点的位置。这是通过链表长度和 k 的关系来确定的，即链表长度减去 k 对链表长度取模的结果。

5. 更新链表的头尾连接关系，形成新的旋转链表。

6. 返回新链表的头节点。

无论使用哪种编程语言，解决这个问题的思路都是相似的，都是基于链表的长度和旋转次数 k 来确定新头节点的位置，然后重新连接链表节点以得到旋转后的链表。
## 代码

## Go

```Go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
// ListNode 结构体定义了链表节点，包括一个整数值 Val 和指向下一个节点的指针 Next。

func rotateRight(head *ListNode, k int) *ListNode {
	// 如果链表为空，或者只包含一个节点，或者旋转次数 k 为 0，则直接返回原始链表。
	if head == nil || head.Next == nil || k == 0 {
		return head
	}
	// 创建一个新的头节点 newHead，将其指向原始链表的头节点。
	newHead := &ListNode{Val: 0, Next: head}
	// 计算链表的长度 len。
	len := 0
	cur := newHead
	for cur.Next != nil {
		len++
		cur = cur.Next
	}
	// 如果 k 对链表长度取模等于 0，表示不需要旋转，直接返回原始链表。
	if (k % len) == 0 {
		return head
	}
	// 将链表首尾相连，形成一个循环链表。
	cur.Next = head
	cur = newHead
	// 计算新头节点的位置，即链表长度减去 k 对链表长度取模的结果。
	for i := len - k%len; i > 0; i-- {
		cur = cur.Next
	}
	// 创建一个新的结果链表 res，将其指向新头节点的下一个节点，然后断开循环链表。
	res := &ListNode{Val: 0, Next: cur.Next}
	cur.Next = nil
	// 返回结果链表的头节点。
	return res.Next
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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 如果链表为空，或者只包含一个节点，或者旋转次数 k 为 0，则直接返回原始链表。
        if not head or not head.next or k == 0:
            return head
        
        # 计算链表的长度 len。
        cur = head
        length = 1
        while cur.next:
            cur = cur.next
            length += 1
        
        # 如果 k 对链表长度取模等于 0，表示不需要旋转，直接返回原始链表。
        if k % length == 0:
            return head
        
        # 找到新头节点的位置，即链表长度减去 k 对链表长度取模的结果。
        cur = head
        for _ in range(length - k % length - 1):
            cur = cur.next
        
        # 更新链表的头尾连接关系，并返回新的头节点。
        new_head = cur.next
        cur.next = None
        cur = new_head
        while cur.next:
            cur = cur.next
        cur.next = head
        
        return new_head

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
    public ListNode rotateRight(ListNode head, int k) {
        // 如果链表为空，或者只包含一个节点，或者旋转次数 k 为 0，则直接返回原始链表。
        if (head == null || head.next == null || k == 0) {
            return head;
        }
        
        // 计算链表的长度 len。
        ListNode cur = head;
        int length = 1;
        while (cur.next != null) {
            cur = cur.next;
            length++;
        }
        
        // 如果 k 对链表长度取模等于 0，表示不需要旋转，直接返回原始链表。
        if (k % length == 0) {
            return head;
        }
        
        // 找到新头节点的位置，即链表长度减去 k 对链表长度取模的结果。
        cur = head;
        for (int i = 0; i < length - k % length - 1; i++) {
            cur = cur.next;
        }
        
        // 更新链表的头尾连接关系，并返回新的头节点。
        ListNode newHead = cur.next;
        cur.next = null;
        cur = newHead;
        while (cur.next != null) {
            cur = cur.next;
        }
        cur.next = head;
        
        return newHead;
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
    ListNode* rotateRight(ListNode* head, int k) {
        // 如果链表为空，或者只包含一个节点，或者旋转次数 k 为 0，则直接返回原始链表。
        if (!head || !head->next || k == 0) {
            return head;
        }
        
        // 计算链表的长度 len。
        ListNode* cur = head;
        int length = 1;
        while (cur->next) {
            cur = cur->next;
            length++;
        }
        
        // 如果 k 对链表长度取模等于 0，表示不需要旋转，直接返回原始链表。
        if (k % length == 0) {
            return head;
        }
        
        // 找到新头节点的位置，即链表长度减去 k 对链表长度取模的结果。
        cur = head;
        for (int i = 0; i < length - k % length - 1; i++) {
            cur = cur->next;
        }
        
        // 更新链表的头尾连接关系，并返回新的头节点。
        ListNode* newHead = cur->next;
        cur->next = nullptr;
        cur = newHead;
        while (cur->next) {
            cur = cur->next;
        }
        cur->next = head;
        
        return newHead;
    }
};

```

每个版本的基础知识要点：

Go 版本：

1. **链表**：你需要了解链表数据结构，这是问题的核心数据结构。在 Go 中，通常使用 `struct` 来定义链表节点，包含一个整数值 `Val` 和指向下一个节点的指针 `Next`。

2. **条件语句和循环**：你需要了解 Go 中的条件语句（`if`语句）和循环（`for`语句），因为代码中有一些条件检查和循环遍历链表。

3. **指针**：了解如何在 Go 中使用指针是非常重要的，因为链表的节点是通过指针连接的。你需要知道如何创建和使用指针，以及如何访问指针指向的值。

Python 版本：

1. **链表**：与 Go 版本一样，你需要了解链表数据结构。在 Python 中，通常使用类来定义链表节点，每个节点有一个整数值和一个指向下一个节点的引用。

2. **条件语句和循环**：你需要了解 Python 中的条件语句（`if`语句）和循环（`for`语句），因为代码中有一些条件检查和循环遍历链表。

3. **类和对象**：在 Python 中，链表节点通常是类的实例。了解如何定义类、创建对象和访问对象属性是必要的。

Java 版本：

1. **链表**：与 Go 和 Python 版本一样，你需要了解链表数据结构。在 Java 中，链表节点通常是一个自定义类，包含整数值和下一个节点的引用。

2. **条件语句和循环**：了解 Java 中的条件语句（`if`语句）和循环（`for`循环）是必要的，因为代码中有条件检查和循环遍历链表。

3. **类和对象**：在 Java 中，链表节点是类的实例。你需要了解如何定义类、创建对象和访问对象的属性和方法。

C++ 版本：

1. **链表**：你需要了解链表数据结构，这是问题的核心数据结构。在 C++ 中，链表节点通常是一个自定义的结构体，包含整数值和下一个节点的指针。

2. **条件语句和循环**：了解 C++ 中的条件语句（`if`语句）和循环（`for`循环）是必要的，因为代码中有条件检查和循环遍历链表。

3. **结构体和指针**：了解如何在 C++ 中定义结构体和使用指针非常重要，因为链表节点是结构体，通过指针连接。

在理解这些基础知识的基础上，你将能够理解和修改提供的代码以解决 "Rotate List" 这道题目。链表操作是这个问题的核心，所以对链表的理解至关重要。如果你对链表操作不熟悉，建议先学习链表的基本操作，然后再尝试解决这个问题。