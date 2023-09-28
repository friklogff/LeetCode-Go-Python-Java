# [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)


## 题目

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Example:**


    Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.


**Follow up:**

If you have figured out the O(*n*) solution, try coding another solution using the divide and conquer approach, which is more subtle.

## 题目大意

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

## 解题思路

- 这一题可以用 DP 求解也可以不用 DP。
- 题目要求输出数组中某个区间内数字之和最大的那个值。`dp[i]` 表示 `[0,i]` 区间内各个子区间和的最大值，状态转移方程是 `dp[i] = nums[i] + dp[i-1] (dp[i-1] > 0)`，`dp[i] = nums[i] (dp[i-1] ≤ 0)`。
## 代码

## Go

```Go
// 定义一个名为 maxSubArray 的函数，接受一个整数数组 nums 作为参数，返回最大子数组和。
func maxSubArray(nums []int) int {
    // 如果数组为空，直接返回 0。
    if len(nums) == 0 {
        return 0
    }
    // 初始化一个临时变量 tmp 和最大子数组和 m，初始值为数组的第一个元素。
    var tmp = 0
    var m = nums[0]
    // 遍历整个数组。
    for i := 0; i < len(nums); i++ {
        // 更新临时变量 tmp，将当前元素加入其中。
        tmp += nums[i]
        // 更新最大子数组和 m，取当前的 m 和 tmp 的较大值。
        m = max(m, tmp)
        // 如果 tmp 小于 0，将 tmp 重置为 0，因为负数不会对最大子数组和产生正面影响。
        tmp = max(tmp, 0)
    }
    // 返回最大子数组和 m。
    return m
}

// 定义一个名为 max 的辅助函数，接受两个整数参数 a 和 b，返回较大的整数。
func max(a, b int) int {
    // 如果 a 大于 b，返回 a，否则返回 b。
    if a > b {
        return a
    }
    return b
}

```

## Python

```Python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 如果数组为空，直接返回0。
        if not nums:
            return 0
        # 初始化一个临时变量 tmp 和最大子数组和 m，初始值为数组的第一个元素。
        tmp = 0
        m = nums[0]
        # 遍历整个数组。
        for num in nums:
            # 更新临时变量 tmp，将当前元素加入其中。
            tmp += num
            # 更新最大子数组和 m，取当前的 m 和 tmp 的较大值。
            m = max(m, tmp)
            # 如果 tmp 小于 0，将 tmp 重置为 0，因为负数不会对最大子数组和产生正面影响。
            tmp = max(tmp, 0)
        # 返回最大子数组和 m。
        return m

```

## Java

```Java
class Solution {
    public int maxSubArray(int[] nums) {
        // 如果数组为空，直接返回0。
        if (nums.length == 0) {
            return 0;
        }
        // 初始化一个临时变量 tmp 和最大子数组和 m，初始值为数组的第一个元素。
        int tmp = 0;
        int m = nums[0];
        // 遍历整个数组。
        for (int i = 0; i < nums.length; i++) {
            // 更新临时变量 tmp，将当前元素加入其中。
            tmp += nums[i];
            // 更新最大子数组和 m，取当前的 m 和 tmp 的较大值。
            m = Math.max(m, tmp);
            // 如果 tmp 小于 0，将 tmp 重置为 0，因为负数不会对最大子数组和产生正面影响。
            tmp = Math.max(tmp, 0);
        }
        // 返回最大子数组和 m。
        return m;
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // 如果数组为空，直接返回0。
        if (nums.empty()) {
            return 0;
        }
        // 初始化一个临时变量 tmp 和最大子数组和 m，初始值为数组的第一个元素。
        int tmp = 0;
        int m = nums[0];
        // 遍历整个数组。
        for (int num : nums) {
            // 更新临时变量 tmp，将当前元素加入其中。
            tmp += num;
            // 更新最大子数组和 m，取当前的 m 和 tmp 的较大值。
            m = max(m, tmp);
            // 如果 tmp 小于 0，将 tmp 重置为 0，因为负数不会对最大子数组和产生正面影响。
            tmp = max(tmp, 0);
        }
        // 返回最大子数组和 m。
        return m;
    }
};

```