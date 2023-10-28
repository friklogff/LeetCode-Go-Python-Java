## 代码

## Go

```Go

```

## Python

```Python

```

## Java

```Java

```

## Cpp

```Cpp

```

## Prompt

```Prompt
我们用中文交流，你能理解这段代码么，逐行加上注释
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
    if head == nil || head.Next == nil{
        return head
    }
    head.Next = deleteDuplicates(head.Next)
    if head.Val == head.Next.Val{
        head = head.Next
    }
    return head
}

给出测试输出语句
你能用同样的思路同样数量的解法用go实现么，以此为开头，给出带注释完整代码
func combine(n int, k int) [][]int {

}
你能用同样的思路同样数量的解法用Python实现么，以此为开头，给出带注释完整代码
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
你能用同样的思路同样数量的解法用Java实现么，以此为开头，给出带注释完整代码
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

    }
}
你能用同样的思路同样数量的解法用c++实现么，以此为开头，给出带注释完整代码
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

    }
};
我们用中文交流，分开介绍每个版本的所需要掌握的详细基础知识

再分别介绍每个版本的解题思路

git add .
git commit -m "Updated"
git push                                                                                                                                      

```

git config --global user.name "friklogff"
git config --global user.email "@qq.com"
git config user.name
git config user.email
ssh-keygen -t rsa -C '@qq.com'
cat ~/.ssh/id_rsa.pub