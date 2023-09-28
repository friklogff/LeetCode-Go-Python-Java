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
func maxSubArray(nums []int) int {
    if len(nums) == 0 {
        return 0
    }
    var tmp = 0
    var m = nums[0]
    for i:=0; i<len(nums); i++ {
        tmp += nums[i]
        m = max(m, tmp)
        tmp = max(tmp, 0)
    }
    return m
}

func max(a, b int) int{
    if a > b {
        return a
    }
    return b
}
给出完善后带注释完整代码

给出测试输出语句


你能用同样的思路同样数量的解法用Java实现么，以此为开头，给出带注释完整代码
class Solution {
    public int maxSubArray(int[] nums) {

    }
}
你能用同样的思路同样数量的解法用Python实现么，以此为开头，给出带注释完整代码
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
你能用同样的思路同样数量的解法用c++实现么，以此为开头，给出带注释完整代码
class Solution {
public:
    int maxSubArray(vector<int>& nums) {

    }
};
你能用同样的思路同样数量的解法用go实现么，以此为开头，给出带注释完整代码
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSameTree(p *TreeNode, q *TreeNode) bool {

}
我们用中文交流，分开介绍每个版本的所需要掌握的详细基础知识

再分别介绍每个版本的解题思路

git add .
git commit -m "Updated"
git push                                                                                                                                      

```
git config --global user.name "friklogff"
git config --global user.email "374591069@qq.com"
git config user.name
git config user.email
ssh-keygen -t rsa -C '374591069@qq.com'
cat ~/.ssh/id_rsa.pub