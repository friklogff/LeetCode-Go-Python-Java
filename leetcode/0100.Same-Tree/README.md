# [100. Same Tree](https://leetcode.com/problems/same-tree/)

## 题目


Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:


```c
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
```

Example 2:

```c
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
```

Example 3:

```c
Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
```

## 题目大意

这一题要求判断 2 颗树是否是完全相等的。


## 解题思路

递归判断即可。


## 代码

## Go

```Go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func isSameTree(p *TreeNode, q *TreeNode) bool {
    // 如果两棵树都为空，认为它们相同
    if p == nil && q == nil {
        return true
    }
    // 如果只有其中一棵树为空，认为它们不相同
    if p == nil || q == nil {
        return false
    }
    // 如果当前节点的值相同，递归比较左子树和右子树是否相同
    if p.Val == q.Val {
        return isSameTree(p.Left, q.Left) && isSameTree(p.Right, q.Right)
    }
    // 如果当前节点的值不同，认为这两棵树不相同
    return false
}

```

## Python

```Python
# Definition for a binary tree node.
# 定义二叉树节点的类
class TreeNode:
    def __init__(self, x):
        self.val = x  # 保存节点的值
        self.left = None  # 左子树
        self.right = None  # 右子树

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True  # 如果两棵树都为空，认为它们相同
        elif not p or not q:
            return False  # 如果只有其中一棵树为空，认为它们不相同
        elif p.val == q.val:
            # 如果当前节点的值相同，递归比较左子树和右子树是否相同
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False  # 如果当前节点的值不同，认为这两棵树不相同

```

## Java

```Java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        // 如果两棵树都为空，认为它们相同
        if (p == null && q == null) {
            return true;
        }
        // 如果只有其中一棵树为空，认为它们不相同
        if (p == null || q == null) {
            return false;
        }
        // 如果当前节点的值相同，递归比较左子树和右子树是否相同
        if (p.val == q.val) {
            return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
        }
        // 如果当前节点的值不同，认为这两棵树不相同
        return false;
    }
}

```

## Cpp

```Cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        // 如果两棵树都为空，认为它们相同
        if (!p && !q) {
            return true;
        }
        // 如果只有其中一棵树为空，认为它们不相同
        if (!p || !q) {
            return false;
        }
        // 如果当前节点的值相同，递归比较左子树和右子树是否相同
        if (p->val == q->val) {
            return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
        }
        // 如果当前节点的值不同，认为这两棵树不相同
        return false;
    }
};

```