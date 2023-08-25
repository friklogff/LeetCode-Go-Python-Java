# [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

## 题目

Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.

**Follow up:** Could you do this in one pass?

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)

```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

```

**Example 2:**

```
Input: head = [1], n = 1
Output: []

```

**Example 3:**

```
Input: head = [1,2], n = 1
Output: [1]

```

**Constraints:**

- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`


## 题目大意

删除链表中倒数第 n 个结点。

## 解题思路

Go 版本解题思路
1. 首先，创建一个虚拟节点 `dummy`，将其下一个节点指向链表的头节点 `head`，这是为了处理删除头节点的情况。
2. 初始化两个指针 `first` 和 `second`，分别指向链表的头部和虚拟节点。
3. 让指针 `first` 先移动 n 步，这样 `first` 指针将会比 `second` 指针领先 n 个节点。
4. 接下来，同时移动 `first` 和 `second` 指针，直到 `first` 到达链表末尾。
5. 此时，`second` 指针停在倒数第 n+1 个节点，然后将其 `next` 指针指向下下个节点，即跳过倒数第 n 个节点，实现了删除操作。
6. 最后，返回虚拟节点的下一个节点，即处理后的链表头部。

Python 版本解题思路
1. 创建一个虚拟节点 `dummy`，将其 `next` 指向链表的头节点 `head`，以便处理删除头节点的情况。
2. 初始化两个指针 `first` 和 `second`，分别指向链表的头部和虚拟节点。
3. 让指针 `first` 先移动 n 步，这样 `first` 指针将会领先 `second` 指针 n 个节点。
4. 接下来，使用一个 `while` 循环，同时移动 `first` 和 `second` 指针，直到 `first` 到达链表末尾。
5. 此时，`second` 指针停在倒数第 n+1 个节点，然后将其 `next` 指针指向下下个节点，即跳过倒数第 n 个节点，实现了删除操作。
6. 最后，返回虚拟节点的下一个节点，即处理后的链表头部。

Java 版本解题思路
1. 创建一个虚拟节点 `dummy`，将其 `next` 指向链表的头节点 `head`，以便处理删除头节点的情况。
2. 初始化两个指针 `first` 和 `second`，分别指向链表的头部和虚拟节点。
3. 让指针 `first` 先移动 n 步，这样 `first` 指针将会领先 `second` 指针 n 个节点。
4. 接下来，使用一个 `while` 循环，同时移动 `first` 和 `second` 指针，直到 `first` 到达链表末尾。
5. 此时，`second` 指针停在倒数第 n+1 个节点，然后将其 `next` 指针指向下下个节点，即跳过倒数第 n 个节点，实现了删除操作。
6. 最后，返回虚拟节点的下一个节点，即处理后的链表头部。

C++ 版本解题思路
1. 创建一个虚拟节点 `dummy`，将其 `next` 指向链表的头节点 `head`，以便处理删除头节点的情况。
2. 初始化两个指针 `first` 和 `second`，分别指向链表的头部和虚拟节点。
3. 让指针 `first` 先移动 n 步，这样 `first` 指针将会领先 `second` 指针 n 个节点。
4. 接下来，使用一个 `while` 循环，同时移动 `first` 和 `second` 指针，直到 `first` 到达链表末尾。
5. 此时，`second` 指针停在倒数第 n+1 个节点，然后将其 `next` 指针指向下下个节点，即跳过倒数第 n 个节点，实现了删除操作。
6. 最后，返回虚拟节点的下一个节点，即处理后的链表头部。

以上就是每个版本的解题思路，它们都使用了双指针技巧，通过一次遍历就能找到并删除倒数第 n 个节点。

## 代码
## Go
```Go
/**
 * 单链表的定义
 * type ListNode struct {
 *     Val int             // 当前节点的值
 *     Next *ListNode      // 指向下一个节点的指针
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    dummy := &ListNode{Next: head}  // 创建一个虚拟节点，它的下一个节点是链表的头节点
    first, second := head, dummy    // 定义两个指针，分别称为 first 和 second，初始指向链表的头部和虚拟节点

    for i := 0 ; i < n ; i++ {      // 将 first 指针向前移动 n 步
        first = first.Next 
    }

    for ; first != nil ; first, second = first.Next, second.Next {}  // 同时移动 first 和 second 指针，直到 first 到达链表末尾

    second.Next = second.Next.Next   // 删除倒数第 n 个节点，即将 second 的下一个节点指针直接跳过第 n 个节点，指向第 n+1 个节点

    return dummy.Next  // 返回虚拟节点的下一个节点，即处理后的链表头部
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()  # 创建一个虚拟节点
        dummy.next = head  # 虚拟节点的下一个节点是链表的头节点
        first, second = head, dummy  # 定义两个指针，first 和 second，分别指向头节点和虚拟节点

        for i in range(n):
            first = first.next  # 将 first 指针向前移动 n 步

        while first:
            first = first.next
            second = second.next  # 同时移动 first 和 second 指针，直到 first 到达链表末尾

        second.next = second.next.next  # 删除倒数第 n 个节点

        return dummy.next  # 返回虚拟节点的下一个节点，即处理后的链表头部

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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode();  // 创建一个虚拟节点
        dummy.next = head;  // 虚拟节点的下一个节点是链表的头节点
        ListNode first = head, second = dummy;  // 定义两个指针，first 和 second，分别指向头节点和虚拟节点

        for (int i = 0; i < n; i++) {
            first = first.next;  // 将 first 指针向前移动 n 步
        }

        while (first != null) {
            first = first.next;
            second = second.next;  // 同时移动 first 和 second 指针，直到 first 到达链表末尾
        }

        second.next = second.next.next;  // 删除倒数第 n 个节点

        return dummy.next;  // 返回虚拟节点的下一个节点，即处理后的链表头部
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode();  // 创建一个虚拟节点
        dummy->next = head;  // 虚拟节点的下一个节点是链表的头节点
        ListNode* first = head, *second = dummy;  // 定义两个指针，first 和 second，分别指向头节点和虚拟节点

        for (int i = 0; i < n; i++) {
            first = first->next;  // 将 first 指针向前移动 n 步
        }

        while (first != nullptr) {
            first = first->next;
            second = second->next;  // 同时移动 first 和 second 指针，直到 first 到达链表末尾
        }

        second->next = second->next->next;  // 删除倒数第 n 个节点

        return dummy->next;  // 返回虚拟节点的下一个节点，即处理后的链表头部
    }
};

```

Go 版本的代码使用了 Go 语言来实现链表节点的删除操作。以下是相关的基础知识：

1. **定义结构体：** Go 使用结构体来定义自定义类型。在代码中，`ListNode` 是一个结构体，用于表示链表节点。结构体的成员包括 `Val`（节点的值）和 `Next`（指向下一个节点的指针）。

2. **指针操作：** Go 支持指针，可以通过指针来修改变量的值。在代码中，`dummy` 是一个指向虚拟节点的指针，`first` 和 `second` 是指向链表节点的指针，通过指针操作来进行链表的遍历和删除操作。

3. **循环：** Go 使用 `for` 关键字来进行循环操作。在代码中，通过 `for` 循环来将 `first` 指针移动 n 步，并且在第二个 `for` 循环中，同时移动 `first` 和 `second` 指针直到 `first` 到达链表末尾。


Python 版本的代码使用了 Python 语言来实现链表节点的删除操作。以下是相关的基础知识：

1. **类和对象：** Python 是面向对象的语言，通过类来定义对象的结构和行为。在代码中，`ListNode` 是一个类，用于表示链表节点。它有成员变量 `val`（节点的值）和 `next`（指向下一个节点的引用）。

2. **循环：** Python 使用 `for` 循环进行迭代。在代码中，通过 `for` 循环来将 `first` 指针移动 n 步，并在第二个 `while` 循环中，同时移动 `first` 和 `second` 指针直到 `first` 到达链表末尾。

Java 版本的代码使用了 Java 语言来实现链表节点的删除操作。以下是相关的基础知识：

1. **类和对象：** Java 也是面向对象的语言，使用类来定义对象的属性和方法。在代码中，`ListNode` 是一个类，用于表示链表节点。它有成员变量 `val`（节点的值）和 `next`（指向下一个节点的引用）。

2. **循环：** Java 使用 `for` 和 `while` 循环进行迭代。在代码中，通过 `for` 循环来将 `first` 指针移动 n 步，并在第二个 `while` 循环中，同时移动 `first` 和 `second` 指针直到 `first` 到达链表末尾。

C++ 版本的代码使用了 C++ 语言来实现链表节点的删除操作。以下是相关的基础知识：

1. **结构体：** C++ 使用结构体来定义自定义类型。在代码中，`ListNode` 是一个结构体，用于表示链表节点。结构体的成员包括 `val`（节点的值）和 `next`（指向下一个节点的指针）。

2. **指针操作：** C++ 支持指针，可以通过指针来访问和修改变量。在代码中，`dummy` 是一个指向虚拟节点的指针，`first` 和 `second` 是指向链表节点的指针，通过指针操作来进行链表的遍历和删除操作。

3. **循环：** C++ 使用 `for` 和 `while` 循环进行迭代。在代码中，通过 `for` 循环来将 `first` 指针移动 n 步，并在第二个 `while` 循环中，同时移动 `first` 和 `second` 指针直到 `first` 到达链表末尾。

