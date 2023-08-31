# [25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/description/)

## 题目

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a
multiple of k then left-out nodes in the end should remain as it is.

Example:

```c
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
```

Note:

- Only constant extra memory is allowed.
- You may not alter the values in the list's nodes, only nodes itself may be changed.

## 题目大意

按照每 K 个元素翻转的方式翻转链表。如果不满足 K 个元素的就不翻转。

## 解题思路

这一题是 problem 24 的加强版，problem 24 是两两相邻的元素，翻转链表。而 problem 25 要求的是 k 个相邻的元素，翻转链表，problem
相当于是 k = 2 的特殊情况。

Go 版本解题思路：

1. 创建一个 `reverseKGroup` 函数，该函数接收一个头节点和一个整数 k，用于翻转每 k 个节点。

2. 在 `reverseKGroup` 函数中，使用一个循环来判断是否剩余 k 个节点。

3. 在循环中，调用 `reverse` 函数来翻转当前的 k 个节点。

4. 将当前节点组的头节点连接到下一个节点组的头节点，然后递归处理下一个节点组。

5. 最终返回整个链表翻转后的头节点。

6. `reverse` 函数用于翻转从 `first` 到 `last` 之间的节点，它使用指针操作来实现翻转。

Python 版本解题思路：

1. 创建一个 `reverseKGroup` 方法，该方法接收一个头节点和一个整数 k，用于翻转每 k 个节点。

2. 在 `reverseKGroup` 方法中，使用递归来处理每个节点组。

3. 在递归中，调用 `reverse` 方法来翻转当前的 k 个节点。

4. 将当前节点组的头节点连接到下一个节点组的头节点，然后递归处理下一个节点组。

5. 最终返回整个链表翻转后的头节点。

6. `reverse` 方法用于翻转从 `first` 到 `last` 之间的节点，它使用指针操作来实现翻转。

Java 版本解题思路：

1. 创建一个 `reverseKGroup` 方法，该方法接收一个头节点和一个整数 k，用于翻转每 k 个节点。

2. 在 `reverseKGroup` 方法中，使用递归来处理每个节点组。

3. 在递归中，调用 `reverse` 方法来翻转当前的 k 个节点。

4. 将当前节点组的头节点连接到下一个节点组的头节点，然后递归处理下一个节点组。

5. 最终返回整个链表翻转后的头节点。

6. `reverse` 方法用于翻转从 `first` 到 `last` 之间的节点，它使用指针操作来实现翻转。

C++ 版本解题思路：

1. 创建一个 `reverseKGroup` 方法，该方法接收一个头节点和一个整数 k，用于翻转每 k 个节点。

2. 在 `reverseKGroup` 方法中，使用循环来处理每个节点组。

3. 在循环中，调用 `reverse` 方法来翻转当前的 k 个节点。

4. 将当前节点组的头节点连接到下一个节点组的头节点，然后继续循环处理下一个节点组。

5. 最终返回整个链表翻转后的头节点。

6. `reverse` 方法用于翻转从 `target` 节点开始的 k 个节点，它使用指针操作来实现翻转。

## 代码

## Go

```Go
/**
 * 单链表节点的定义。
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

// reverseKGroup 函数接收一个头节点和一个整数 k，将链表中每 k 个节点进行翻转操作。
func reverseKGroup(head *ListNode, k int) *ListNode {
    node := head // 保存头节点的引用，用于后面返回
    for i := 0; i < k; i++ {
        if node == nil {
            return head // 如果剩余节点不足 k 个，不进行翻转，直接返回头节点
        }
        node = node.Next // 移动节点指针到下一个节点
    }
    newHead := reverse(head, node) // 调用 reverse 函数翻转当前的 k 个节点
    head.Next = reverseKGroup(node, k) // 递归处理剩余节点，并将返回的头节点连接到当前节点组的末尾
    return newHead // 返回翻转后的头节点
}

// reverse 函数用于将从 first 到 last 之间的节点进行翻转，返回翻转后的头节点。
func reverse(first *ListNode, last *ListNode) *ListNode {
    prev := last // prev 指向翻转后的链表末尾，初始为 last
    for first != last {
        tmp := first.Next   // 保存下一个节点的引用
        first.Next = prev   // 将当前节点的 Next 指向 prev，实现翻转
        prev = first        // 更新 prev 为当前节点，以便下一轮循环使用
        first = tmp         // 更新 first 为下一个节点，以便下一轮循环使用
    }
    return prev // 返回翻转后的头节点
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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = head  # 保存头节点的引用，用于后面返回
        for i in range(k):
            if not node:
                return head  # 如果剩余节点不足 k 个，不进行翻转，直接返回头节点
            node = node.next  # 移动节点指针到下一个节点

        new_head = self.reverse(head, node)  # 调用 reverse 函数翻转当前的 k 个节点
        head.next = self.reverseKGroup(node, k)  # 递归处理剩余节点，并将返回的头节点连接到当前节点组的末尾
        return new_head  # 返回翻转后的头节点

    # reverse 函数用于将从 first 到 last 之间的节点进行翻转，返回翻转后的头节点。
    def reverse(self, first: Optional[ListNode], last: Optional[ListNode]) -> Optional[ListNode]:
        prev = last  # prev 指向翻转后的链表末尾，初始为 last
        while first != last:
            tmp = first.next  # 保存下一个节点的引用
            first.next = prev  # 将当前节点的 next 指向 prev，实现翻转
            prev = first  # 更新 prev 为当前节点，以便下一轮循环使用
            first = tmp  # 更新 first 为下一个节点，以便下一轮循环使用
        return prev  # 返回翻转后的头节点

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
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode node = head; // 保存头节点的引用，用于后面返回
        for (int i = 0; i < k; i++) {
            if (node == null) {
                return head; // 如果剩余节点不足 k 个，不进行翻转，直接返回头节点
            }
            node = node.next; // 移动节点指针到下一个节点
        }
        ListNode newHead = reverse(head, node); // 调用 reverse 函数翻转当前的 k 个节点
        head.next = reverseKGroup(node, k); // 递归处理剩余节点，并将返回的头节点连接到当前节点组的末尾
        return newHead; // 返回翻转后的头节点
    }

    // reverse 函数用于将从 first 到 last 之间的节点进行翻转，返回翻转后的头节点。
    private ListNode reverse(ListNode first, ListNode last) {
        ListNode prev = last; // prev 指向翻转后的链表末尾，初始为 last
        while (first != last) {
            ListNode tmp = first.next; // 保存下一个节点的引用
            first.next = prev; // 将当前节点的 next 指向 prev，实现翻转
            prev = first; // 更新 prev 为当前节点，以便下一轮循环使用
            first = tmp; // 更新 first 为下一个节点，以便下一轮循环使用
        }
        return prev; // 返回翻转后的头节点
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
    // 主函数，翻转每 k 个节点的组
    ListNode* reverseKGroup(ListNode* head, int k) {
        auto cur = head; // 当前组的头节点
        ListNode* prev_tail = nullptr; // 上一组的尾节点
        ListNode *cur_head = nullptr; // 当前组的头节点
        ListNode *cur_tail = nullptr; // 当前组的尾节点
        ListNode *next_cur = nullptr; // 下一个组的头节点

        ListNode *ans = nullptr; // 最终翻转后的链表的头节点

        // 循环处理每个组
        do {
            // 调用 reverse 函数翻转当前的 k 个节点
            next_cur = reverse(cur, cur_head, cur_tail, k);

            if(!ans) {
                ans = cur_head; // 如果 ans 为空，将当前组的头节点作为答案的头节点
            }

            if(prev_tail) {
                prev_tail->next = cur_head; // 将上一组的尾节点与当前组的头节点相连
            }

            prev_tail = cur_tail; // 更新 prev_tail 为当前组的尾节点
            cur = next_cur; // 将 cur 更新为下一个组的头节点
        } while(next_cur);

        cur_tail->next = next_cur; // 将最后一个组的尾节点与下一个组的头节点相连

        return ans; // 返回整个翻转后的链表头节点
    }

    // 辅助函数，翻转从 target 节点开始的 k 个节点
    ListNode* reverse(ListNode *target, ListNode *(&ret_head), ListNode *(&ret_tail), int k) {
        if(!target->next) {
            ret_head = target;
            ret_tail = target;
            return nullptr; // 如果 target 节点后面没有节点了，返回空，表明不需要翻转
        }

        int cnt = 1;
        ListNode *tmp = target;
        for(; tmp->next != nullptr; tmp=tmp->next) {
            if(cnt >= k ) {
                break;
            }
            cnt++;
        }
        if(cnt < k) {
            ret_head = target;
            ret_tail = tmp;
            return nullptr; // 如果剩余节点数量不足 k，返回空，表明不需要翻转
        }

        ret_tail = target; // 更新当前组的尾节点为 target

        auto cur = target;
        auto next = target->next;
        cnt = 1;
        while(next && cnt < k) {
            auto next_next = next->next;

            next->next = cur;

            cur = next;
            next = next_next;
            cnt++;
        }

        ret_head = cur; // 更新当前组的头节点为 cur
        ret_tail->next = nullptr; // 将当前组的尾节点的 next 指向空，表示该组翻转后的尾节点

        return next; // 返回下一个组的头节点
    }
};

```
Go 版本代码：

结构体与指针： Go 使用结构体表示链表节点，这是一种自定义的数据结构。代码中的 ListNode 结构体有一个整数字段 Val 和一个指向下一个节点的指针字段 Next。head 是指向链表头节点的指针。

递归： reverseKGroup 函数使用递归来处理每一组节点的翻转。递归是一种重要的编程技巧，它可以在解决问题时将问题拆分成更小的相同子问题。

Python 版本代码：

类与方法： Python 使用类来定义链表节点，代码中的 ListNode 类包含整数字段 val 和指向下一个节点的引用字段 next。Solution 类定义了处理问题的方法。

递归： 与 Go 版本相同，Python 版本也使用递归来处理每一组节点的翻转。

Java 版本代码：

类与方法： Java 也使用类来定义链表节点，代码中的 ListNode 类有一个整数字段 val 和一个指向下一个节点的引用字段 next。Solution 类定义了处理问题的方法。

递归： 与 Go 和 Python 版本类似，Java 版本也使用递归来处理每一组节点的翻转。

C++ 版本代码：

类与指针： C++ 使用 struct 结构体来定义链表节点，代码中的 ListNode 结构体有一个整数字段 val 和一个指向下一个节点的指针字段 next。Solution 类定义了处理问题的方法。

递归： 与其他版本一样，C++ 版本也使用递归来处理每一组节点的翻转。

指针操作： C++ 版本中涉及指针的操作，如节点的指针赋值、遍历等。理解指针的基本概念和操作对于理解这些代码是很重要的。