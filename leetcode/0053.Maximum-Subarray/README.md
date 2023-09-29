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
**Go版本:**
1. 定义maxSubArray函数,参数为nums切片。
2. 定义tmp和m变量,分别表示当前子数组之和和最大子数组之和。m初始化为nums[0]。
3. 遍历nums,用tmp累加当前元素。
4. 比较m和tmp,通过max函数取较大值赋给m。
5. 如果tmp<0,通过max函数将tmp赋为0。
6. 循环结束后返回m。


**Python版本:**
1. 定义maxSubArray函数,参数为nums列表。
2. 定义tmp和m变量,分别表示当前子数组之和和最大子数组之和。m初始化为nums[0]。
3. 遍历nums,用tmp累加当前元素。
4. 比较m和tmp,通过内置max函数取较大值赋给m。
5. 如果tmp<0,通过max函数将tmp赋为0。
6. 循环结束后返回m。


**Java版本:**
1. 定义maxSubArray方法,参数为nums数组。
2. 定义tmp和m变量,分别表示当前子数组之和和最大子数组之和。m初始化为nums[0]。
3. 遍历nums,用tmp累加当前元素。
4. 比较m和tmp,通过Math.max取较大值赋给m。
5. 如果tmp<0,通过Math.max将tmp赋为0。
6. 循环结束后返回m。


**C++版本:**
1. 定义maxSubArray方法,参数为nums向量。
2. 定义tmp和m变量,分别表示当前子数组之和和最大子数组之和。m初始化为nums[0]。
3. 遍历nums,用tmp累加当前元素。
4. 比较m和tmp,通过max方法取较大值赋给m。
5. 如果tmp<0,通过max方法将tmp赋为0。
6. 循环结束后返回m。


核心思路都是一样的,主要区别在语法细节上,利用本地语言特性进行优化。
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
基础知识


对于Go版本:
- 函数定义:Go语言中使用func关键字定义函数,括号内参数列表,大括号内函数体。
- 返回值:Go函数可以只返回一个值,使用return语句。
- 切片操作:nums []int定义一个int切片,len(nums)获取切片长度,nums[i]访问切片元素。
- if条件判断:if a > b {} else {}。
- for循环:for i := 0; i < len(nums); i++ {}。
- 变量定义:var tmp int 定义临时变量。
- 取最大值:调用max函数比较a,b大小返回较大值。


对于Python版本:
- 函数定义:使用def定义函数,参数列表中的self代表类内方法。  
- 返回值:使用 return 语句返回值。
- 列表操作:nums作为列表参数,len(nums)获取长度,num遍历列表元素。
- if条件判断:if not nums: 判断空列表。
- 取最大值:调用内置max函数比较两个值。


对于Java版本:
- 方法定义:public类型说明方法访问权限,int返回值类型。
- 数组操作:nums.length获取数组长度,nums[i]访问元素。
- if条件判断:if(nums.length == 0)。
- for循环:for(初始化;条件;迭代)。
- 取最大值:Math.max(a, b)调用工具类方法。


对于C++版本:
- 方法定义:class内定义,int返回类型。
- 向量操作:nums作为向量参数,empty()判断空,num遍历。
- if条件判断:if(nums.empty())。
- for循环:for(元素类型 元素:容器)。
- 取最大值:调用max方法比较两个值。
主要就是函数/方法定义,基础数据结构的操作,流程控制语言(if/for)的使用,数值比较取最大值。掌握了这些基础语法,就可以编写出算法代码。