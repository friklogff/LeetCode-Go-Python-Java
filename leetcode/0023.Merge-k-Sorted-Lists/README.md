# [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

## 题目

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.



Example :

```
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

```

## 题目大意

合并 K 个有序链表

## 解题思路


Go 版本解法：

这个解法使用了分治的思想来合并 k 个有序链表。首先，判断输入的链表数组的长度：

- 如果长度为 0，返回 `nil`。
- 如果长度为 1，直接返回该链表。

对于长度大于 1 的情况，将链表数组分成两半，然后递归地合并左半部分和右半部分，最后将两部分合并。合并的过程是通过一个辅助函数来实现的，比较两个链表的当前节点值，选择较小的节点连接到合并后的链表。

Python 版本解法：

这个解法使用了优先队列（堆）来合并 k 个有序链表。首先，将每个链表的头节点及其值和索引放入优先队列中。然后，循环从优先队列中弹出最小值的节点，将其连接到合并链表的末尾。如果弹出的节点还有下一个节点，将下一个节点入队。

这样，通过不断弹出最小节点，不断将下一个节点入队，就能够逐步构建合并后的链表。

Java 版本解法：

这个解法也是使用了优先队列（堆）来合并 k 个有序链表。与 Python 版本类似，首先将每个链表的头节点及其值和索引放入优先队列中。然后，循环从优先队列中弹出最小值的节点，将其连接到合并链表的末尾。如果弹出的节点还有下一个节点，将下一个节点入队。

这个过程会不断弹出最小节点，不断将下一个节点入队，从而构建合并后的链表。

C++ 版本解法：

这个解法使用了分治的思想来合并 k 个有序链表。首先，定义了一个辅助函数 `merge`，用来合并两个有序链表。然后，使用递归的分治方法，将 k 个链表分成两半，递归地合并左半部分和右半部分，最后将两部分合并。

在合并的过程中，辅助函数 `merge` 会比较两个链表的当前节点值，选择较小的节点连接到合并后的链表。

以上就是各个版本的解题思路，它们都是通过合并有序链表来实现的，但采用了不同的数据结构和算法来达到相同的目标。## 代码
## Go
```Go
/**
 * 定义单链表节点结构
 * type ListNode struct {
 *     Val int           // 当前节点的值
 *     Next *ListNode    // 指向下一个节点的指针
 * }
 */
func mergeKLists(lists []*ListNode) *ListNode {
    // 获取输入链表数组的长度
    len := len(lists)

    // 根据不同情况进行合并操作
    switch len {
    case 0:
        return nil    // 如果没有链表，返回 nil
    case 1:
        return lists[0]    // 如果只有一个链表，直接返回这个链表
    default:
        mid := len / 2    // 将链表数组分成两半
        left := mergeKLists(lists[:mid])    // 递归地合并左半部分
        right := mergeKLists(lists[mid:])   // 递归地合并右半部分
        return merge(left, right)    // 合并左右两部分链表
    }
}

func merge(list1 *ListNode, list2 *ListNode) *ListNode {
    dummy := &ListNode{}    // 创建一个哑节点作为合并后的链表的起始节点
    cur := dummy    // 创建一个当前节点指针，初始指向哑节点

    // 比较两个链表的节点值，逐个选择较小的节点连接到合并后的链表
    for list1 != nil && list2 != nil {
        if list1.Val < list2.Val {
            cur.Next = list1
            list1 = list1.Next
        } else {
            cur.Next = list2
            list2 = list2.Next
        }
        cur = cur.Next
    }

    // 将剩余的 list1 链接到合并后的链表
    for list1 != nil {
        cur.Next = list1
        list1 = list1.Next
        cur = cur.Next
    }

    // 将剩余的 list2 链接到合并后的链表
    for list2 != nil {
        cur.Next = list2
        list2 = list2.Next
        cur = cur.Next
    }

    return dummy.Next    // 返回合并后链表的起始节点
}

```
## Python
```Python
import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []  # 使用一个最小堆来存储当前每个链表的头节点
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))  # 将链表头节点的值、链表索引和链表头节点元组入堆
        
        dummy = ListNode()  # 创建哑节点作为合并后链表的起始节点
        cur = dummy  # 创建一个当前节点指针，初始指向哑节点
        
        while heap:
            val, idx, node = heapq.heappop(heap)  # 弹出堆顶元素，即最小值的节点
            cur.next = node  # 将最小节点接到合并链表的末尾
            cur = cur.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))  # 将下一个节点入堆，保持堆的有序性
        
        return dummy.next  # 返回合并后链表的起始节点

```
## Java
```Java
import java.util.*;
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
    public ListNode mergeKLists(ListNode[] lists) {
        // 创建一个最小堆，并根据节点值进行比较
        PriorityQueue<ListNode> minHeap = new PriorityQueue<>((a, b) -> a.val - b.val);
        
        // 将所有链表的头节点加入堆
        for (ListNode node : lists) {
            if (node != null) {
                minHeap.offer(node);
            }
        }
        
        ListNode dummy = new ListNode();  // 创建哑节点作为合并后链表的起始节点
        ListNode cur = dummy;  // 创建一个当前节点指针，初始指向哑节点
        
        while (!minHeap.isEmpty()) {
            ListNode minNode = minHeap.poll();  // 弹出堆顶元素，即最小值的节点
            cur.next = minNode;  // 将最小节点接到合并链表的末尾
            cur = cur.next;
            
            if (minNode.next != null) {
                minHeap.offer(minNode.next);  // 将下一个节点加入堆，保持堆的有序性
            }
        }
        
        return dummy.next;  // 返回合并后链表的起始节点
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
    // 递归合并两个有序链表
    ListNode* merge(ListNode* list1, ListNode* list2) {
        if (!list1) return list2;
        if (!list2) return list1;
        
        if (list1->val <= list2->val) {
            list1->next = merge(list1->next, list2);
            return list1;
        } else {
            list2->next = merge(list1, list2->next);
            return list2;
        }
    }
    
    // 使用分治法逐步合并 K 个链表
    ListNode* quick(vector<ListNode*>& lists, int l, int r) {
        if (l > r) return nullptr;
        if (l == r) return lists[l];
        
        int mid = (l + r) >> 1;
        return merge(quick(lists, l, mid), quick(lists, mid + 1, r));
    }
    
    // 主函数，合并 K 个有序链表
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        return quick(lists, 0, lists.size() - 1);
    }
};

```
每个版本的详细基础知识。

Go 版本解法：

1. **链表数据结构：** 你需要理解 `ListNode` 结构的定义，它是一个表示链表节点的结构体，包括一个整数值 `Val` 和指向下一个节点的指针 `Next`。

2. **递归：** 这个解法使用了递归来实现分治合并。你需要了解递归的工作原理，即一个函数调用自身以解决更小规模的问题。

3. **切片（Slices）：** Go 中的切片是动态数组，用于存储多个相同类型的元素。解法中用切片进行了链表的分割和合并。

Python 版本解法：

1. **优先队列（堆）：** `heapq` 是 Python 中的堆操作库，它提供了优先队列的实现。你需要了解如何使用堆来维护最小元素，以及堆的基本操作。

2. **链表数据结构：** 你需要理解 `ListNode` 结构的定义，类似于 Go 版本的链表数据结构。

3. **类和对象：** Python 是面向对象的语言，解法中使用了类来定义 `Solution` 类，以及链表节点的构造。

4. **循环：** 解法中使用了循环来遍历链表、优先队列等。

Java 版本解法：

1. **优先队列（堆）：** Java 中的优先队列也是通过堆实现的，你需要了解如何使用 `PriorityQueue` 类来创建和操作优先队列。

2. **链表数据结构：** 你需要理解 `ListNode` 结构的定义，与其他版本类似。

3. **类和对象：** Java 也是面向对象的语言，你需要理解类的定义和使用。

4. **循环：** 解法中使用了循环来遍历链表、优先队列等。

C++ 版本解法：

1. **优先队列（堆）：** C++ 中的 `priority_queue` 类用于实现优先队列，你需要了解如何使用它来维护最小元素。

2. **链表数据结构：** 你需要理解 `ListNode` 结构的定义，与其他版本类似。

3. **递归：** 解法中使用了递归来实现分治合并，你需要理解递归的概念和用法。

4. **类和对象：** C++ 是面向对象的语言，解法中使用了类来定义 `Solution` 类和链表节点。

