# [82. Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)

## 题目

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

```
Input: 1->2->3->3->4->4->5
Output: 1->2->5
```

Example 2:

```
Input: 1->1->1->2->3
Output: 2->3
```

## 题目大意

删除链表中重复的结点，只要是有重复过的结点，全部删除。

## 解题思路

以下是每个版本的解题思路的详细介绍：

**Go版本解题思路**：

1. 创建一个新的头节点 `newHead`，并将其指向原始链表的头节点 `head`。这样可以简化处理边界情况。
2. 使用指针 `cur` 指向当前处理的节点，指针 `last` 指向当前节点的前一个节点，以及指针 `front` 用于遍历链表。
3. 遍历链表，直到 `front` 到达链表末尾。
4. 在遍历过程中，检查当前节点的值是否与前一个节点的值相同，以确定是否有重复节点。
5. 如果当前节点的值与前一个节点的值相同，继续遍历到下一个节点，跳过重复节点。
6. 如果当前节点的值与前一个节点的值不同，根据情况更新指针和连接。如果当前节点与前一个节点之间存在重复节点，将 `last` 指向当前不重复的节点，并更新 `cur` 指向当前节点。如果没有重复节点，正常移动三个指针。
7. 处理链表末尾可能存在的重复节点，确保正确的连接关系。
8. 最后，返回处理后的链表，即 `newHead.Next`。

**Python版本解题思路**：

1. 创建一个虚拟节点 `dummy`，将其 `next` 指向原始链表的头节点 `head`。
2. 遍历链表，同时维护指针 `cur` 指向当前处理的节点。
3. 在循环中，检查当前节点和下一个节点是否有相同的值。
4. 如果有相同的值，继续向下移动，直到找到不同的值。
5. 如果值不同，更新指针 `cur` 到下一个节点，继续遍历。
6. 最后，返回虚拟节点 `dummy` 的下一个节点，这是去除重复元素后的链表。

**Java版本解题思路**：

1. 创建一个新的头节点 `newHead`，并将其指向原始链表的头节点 `head`。这样可以简化处理边界情况。
2. 使用指针 `cur` 指向当前处理的节点，指针 `last` 指向当前节点的前一个节点，以及指针 `front` 用于遍历链表。
3. 遍历链表，直到 `front` 到达链表末尾。
4. 在遍历过程中，检查当前节点的值是否与前一个节点的值相同，以确定是否有重复节点。
5. 如果当前节点的值与前一个节点的值相同，继续遍历到下一个节点，跳过重复节点。
6. 如果当前节点的值与前一个节点的值不同，根据情况更新指针和连接。如果当前节点与前一个节点之间存在重复节点，将 `last.next` 指向当前不重复的节点，并更新 `cur` 指向当前节点。如果没有重复节点，正常移动三个指针。
7. 处理链表末尾可能存在的重复节点，确保正确的连接关系。
8. 最后，返回处理后的链表，即 `newHead.next`。

**C++版本解题思路**：

1. 创建一个新的头节点 `newHead`，并将其指向原始链表的头节点 `head`。这样可以简化处理边界情况。
2. 使用指针 `cur` 指向当前处理的节点，指针 `last` 指向当前节点的前一个节点，以及指针 `front` 用于遍历链表。
3. 遍历链表，直到 `front` 到达链表末尾。
4. 在遍历过程中，检查当前节点的值是否与前一个节点的值相同，以确定是否有重复节点。
5. 如果当前节点的值与前一个节点的值相同，继续遍历到下一个节点，跳过重复节点。
6. 如果当前节点的值与前一个节点的值不同，根据情况更新指针和连接。如果当前节点与前一个节点之间存在重复节点，将 `last->next` 指向当前不重复的节点，并更新 `cur` 指向当前节点。如果没有重复节点，正常移动三个指针。
7. 处理链表末尾可能存在的重复节点，确保正确的连接关系。
8. 最后，返回处理后的链表，即 `newHead->next`。

每个版本的解题思路都涉及创建新头节点、维护多个指针来处理重复节点，以及正确连接不重复节点的关键逻辑。此外，还需要理解链表的基本概念和相应编程语言的语法特性。
## 代码

## Go

```Go
func deleteDuplicates1(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	if head.Next == nil {
		return head
	}
	newHead := &ListNode{Next: head, Val: -999999} // 创建一个新的头节点，值设置为一个不可能出现在链表中的值，以简化边界情况处理
	cur := newHead // cur 指向当前处理的节点
	last := newHead // last 指向当前节点的前一个节点
	front := head // front 用于遍历链表

for front.Next != nil { // 遍历链表直到 front 到达链表末尾
		if front.Val == cur.Val { // 如果当前节点的值与前一个节点的值相同，表示有重复节点
			front = front.Next // 移动到下一个节点
			continue
		} else { // 如果当前节点的值与前一个节点的值不同
			if cur.Next != front { // 如果当前节点与前一个节点之间有重复节点
				last.Next = front // 跳过重复节点，将上一个节点指向当前不重复的节点
				if front.Next != nil && front.Next.Val != front.Val {
					last = front // 更新 last 指针，因为当前节点可能是下一个不同值节点的前一个节点
				}
				cur = front // 更新 cur 指针到当前不重复的节点
				front = front.Next // 移动到下一个节点
			} else { // 常规情况，没有重复节点
				last = cur // 更新 last 指针
				cur = cur.Next // 更新 cur 指针到下一个节点
				front = front.Next // 移动到下一个节点
			}
		}
	}
	if front.Val == cur.Val { // 处理链表末尾可能存在的重复节点
		last.Next = nil // 移除重复节点
	} else {
		if cur.Next != front { // 处理链表末尾的不同值节点
			last.Next = front // 将 last 指向末尾不同值节点
		}
	}
	return newHead.Next // 返回处理后的链表
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 创建一个虚拟节点 dummy，其 next 指向原始链表的头节点 head
        dummy = cur = ListNode(next = head)

        # 遍历链表
        while cur.next and cur.next.next:
            val = cur.next.val

            # 如果当前节点的值与下一个节点的值相同
            if cur.next.val == cur.next.next.val:
                # 移动 cur.next 直到找到不同的值
                while cur.next and cur.next.val == val:
                    cur.next = cur.next.next
            else:
                # 如果当前节点的值与下一个节点的值不同，继续遍历链表
                cur = cur.next

        # 返回虚拟节点的下一个节点，即去除重复元素后的链表
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
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) {
            return null;
        }
        if (head.next == null) {
            return head;
        }
        ListNode newHead = new ListNode(-999999);
        newHead.next = head;
        ListNode cur = newHead;
        ListNode last = newHead;
        ListNode front = head;
        while (front.next != null) {
            if (front.val == cur.val) {
                front = front.next;
                continue;
            } else {
                if (cur.next != front) {
                    last.next = front;
                    if (front.next != null && front.next.val != front.val) {
                        last = front;
                    }
                    cur = front;
                    front = front.next;
                } else {
                    last = cur;
                    cur = cur.next;
                    front = front.next;
                }
            }
        }
        if (front.val == cur.val) {
            last.next = null;
        } else {
            if (cur.next != front) {
                last.next = front;
            }
        }
        return newHead.next;
    }
}
```

## Cpp

```Cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode* next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode* next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head) {
            return nullptr;
        }
        if (!head->next) {
            return head;
        }
        ListNode* newHead = new ListNode(-999999);
        newHead->next = head;
        ListNode* cur = newHead;
        ListNode* last = newHead;
        ListNode* front = head;
        while (front->next) {
            if (front->val == cur->val) {
                front = front->next;
                continue;
            } else {
                if (cur->next != front) {
                    last->next = front;
                    if (front->next && front->next->val != front->val) {
                        last = front;
                    }
                    cur = front;
                    front = front->next;
                } else {
                    last = cur;
                    cur = cur->next;
                    front = front->next;
                }
            }
        }
        if (front->val == cur->val) {
            last->next = nullptr;
        } else {
            if (cur->next != front) {
                last->next = front;
            }
        }
        return newHead->next;
    }
};
```
理解每个版本的代码所需的基础知识可以有所不同，以下是每个版本的详细介绍：

**Go版本**：

- 基本Go语法：了解Go的基本语法，如变量声明、条件语句、循环、函数定义、指针、结构体等。
- 链表：理解链表的概念，包括单链表和节点的结构。了解如何创建、访问和遍历链表。
- 指针：了解Go中的指针操作，包括如何创建指针、访问结构体字段等。
- 循环：理解for循环以及如何在循环中遍历链表。

**Python版本**：

- Python基础语法：了解Python的基本语法，包括变量、条件语句、循环、类和对象、列表等。
- 链表：理解链表的概念，包括单链表和节点的结构。了解如何创建、访问和遍历链表。
- 类和对象：了解Python中如何创建类和对象，以及如何定义类的方法。
- 循环：理解while循环和for循环，以及如何在循环中遍历链表。

**Java版本**：

- Java基础语法：了解Java的基本语法，包括类、方法、变量、条件语句、循环、对象等。
- 链表：理解链表的概念，包括单链表和节点的结构。了解如何创建、访问和遍历链表。
- 类和对象：了解如何创建类和对象，以及如何定义类的构造函数和方法。
- 链表操作：理解Java中如何操作链表，包括创建新节点、更改节点的指针等。

**C++版本**：

- C++基础语法：了解C++的基本语法，包括类、方法、变量、条件语句、循环、指针等。
- 链表：理解链表的概念，包括单链表和节点的结构。了解如何创建、访问和遍历链表。
- 类和对象：了解C++中如何创建类和对象，以及如何定义类的构造函数和方法。
- 指针：了解C++中的指针操作，包括如何创建指针、访问结构体字段等。
- 动态内存分配：了解如何使用`new`和`delete`来进行动态内存分配和释放，以确保内存管理。

每个版本的代码都涉及链表数据结构的操作，以及相应编程语言的语法和特性。因此，理解链表的基本概念以及编程语言的基础知识对于理解和实现这些版本的代码都是必要的。