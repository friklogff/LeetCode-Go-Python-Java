# [31. Next Permutation](https://leetcode.com/problems/next-permutation/)

## 题目

Implement**next permutation**, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending
order).

The replacement must be**[in place](http://en.wikipedia.org/wiki/In-place_algorithm)**and use only constant extra
memory.

**Example 1:**

```
Input: nums = [1,2,3]
Output: [1,3,2]
```

**Example 2:**

```
Input: nums = [3,2,1]
Output: [1,2,3]
```

**Example 3:**

```
Input: nums = [1,1,5]
Output: [1,5,1]
```

**Example 4:**

```
Input: nums = [1]
Output: [1]
```

**Constraints:**

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 100`

## 题目大意

实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。必须
原地 修改，只允许使用额外常数空间。

## 解题思路


Go 版本解题思路：

1. **寻找下一个排列**：首先，我们要找到下一个排列，即重新排列给定数字序列，使其成为字典序中的下一个更大的排列。

2. **寻找较小数的位置**：从右往左遍历整数切片 `nums`，寻找第一个满足 `nums[i] < nums[i+1]` 的下标 `i`。这个位置代表了较小数的位置。

3. **寻找较大数的位置**：如果找到了 `i`，则在下降区间 `[i+1, n)` 中从右往左找到第一个满足 `nums[i] < nums[j]` 的下标 `j`，这个位置代表了较大数的位置。

4. **交换较小数和较大数**：交换 `nums[i]` 和 `nums[j]`，这一步完成后，区间 `[i+1, n)` 一定是一个降序区间。

5. **翻转子数组**：对 `[i+1, n)` 区间内的元素进行原地翻转，使其变为升序，这样才能生成下一个排列。

Python 版本解题思路：

Python 版本的解题思路与 Go 版本相似，只是使用了 Python 的列表和对象。

1. **寻找下一个排列**：与 Go 版本相同，我们首先要找到下一个排列，即重新排列给定数字序列，使其成为字典序中的下一个更大的排列。

2. **寻找较小数的位置**：从右往左遍历整数列表 `nums`，寻找第一个满足 `nums[i] < nums[i+1]` 的下标 `i`，代表了较小数的位置。

3. **寻找较大数的位置**：如果找到了 `i`，则在下降区间 `[i+1, n)` 中从右往左找到第一个满足 `nums[i] < nums[j]` 的下标 `j`，代表了较大数的位置。

4. **交换较小数和较大数**：交换 `nums[i]` 和 `nums[j]`，这一步完成后，区间 `[i+1, n)` 一定是一个降序区间。

5. **翻转子数组**：对 `[i+1, n)` 区间内的元素进行原地翻转，使其变为升序，这样才能生成下一个排列。

Java 版本解题思路：

Java 版本的解题思路与 Go 和 Python 版本相似，只是使用了 Java 的数组和类。

1. **寻找下一个排列**：与其他版本相同，首先要找到下一个排列，即重新排列给定数字序列，使其成为字典序中的下一个更大的排列。

2. **寻找较小数的位置**：从右往左遍历整数数组 `nums`，寻找第一个满足 `nums[i] < nums[i+1]` 的下标 `i`，代表了较小数的位置。

3. **寻找较大数的位置**：如果找到了 `i`，则在下降区间 `[i+1, n)` 中从右往左找到第一个满足 `nums[i] < nums[j]` 的下标 `j`，代表了较大数的位置。

4. **交换较小数和较大数**：交换 `nums[i]` 和 `nums[j]`，这一步完成后，区间 `[i+1, n)` 一定是一个降序区间。

5. **翻转子数组**：对 `[i+1, n)` 区间内的元素进行原地翻转，使其变为升序，这样才能生成下一个排列。

C++ 版本解题思路：

C++ 版本的解题思路与 Go、Python 和 Java 版本相似，只是使用了 C++ 的数组和类。

1. **寻找下一个排列**：与其他版本相同，首先要找到下一个排列，即重新排列给定数字序列，使其成为字典序中的下一个更大的排列。

2. **寻找较小数的位置**：从右往左遍历整数数组 `nums`，寻找第一个满足 `nums[i] < nums[i+1]` 的下标 `i`，代表了较小数的位置。

3. **寻找较大数的位置**：如果找到了 `i`，则在下降区间 `[i+1, n)` 中从右往左找到第一个满足 `nums[i] < nums[j]` 的下标 `j`，代表了较大数的位置。

4. **交换较小数和较大数**：交换 `nums[i]` 和 `nums[j]`，这一步完成后，区间 `[i+1, n)` 一定是一个降序区间。

5. **翻转子数组**：对 `[i+1, n)` 区间内的元素进行原地翻转，使其变为升序，这样才能生成下一个排列。

## 代码

## Go

```Go
// 解法一
// 定义一个函数 nextPermutation，用于生成下一个排列
func nextPermutation(nums []int) {
    // 定义两个变量 i 和 j，并初始化为 0
    i, j := 0, 0
    // 从倒数第二个元素开始向前遍历整数切片 nums，寻找第一个满足 nums[i] < nums[i+1] 的 i
    for i = len(nums) - 2; i >= 0; i-- {
        if nums[i] < nums[i+1] {
            break
        }
    }
    // 如果找到了 i，表示存在下一个排列
    if i >= 0 {
        // 从最后一个元素开始向前遍历整数切片 nums，寻找第一个满足 nums[j] > nums[i] 的 j
        for j = len(nums) - 1; j > i; j-- {
            if nums[j] > nums[i] {
                break
            }
        }
        // 交换 nums[i] 和 nums[j]
        swap(&nums, i, j)
    }
    // 对从 i+1 到末尾的部分进行翻转，以获得下一个排列
    reverse(&nums, i+1, len(nums)-1)
}

// 定义一个函数 reverse，用于翻转整数切片 nums 中从位置 i 到 j 的元素
func reverse(nums *[]int, i, j int) {
    // 使用双指针将元素从两端向中间逐个交换
    for i < j {
        swap(nums, i, j)
        i++
        j--
    }
}

// 定义一个函数 swap，用于交换整数切片 nums 中位置 i 和 j 的元素
func swap(nums *[]int, i, j int) {
    // 使用指针访问和交换切片中的元素值
    (*nums)[i], (*nums)[j] = (*nums)[j], (*nums)[i]
}

```

## Python

```Python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Step 1: Find the first decreasing element from right to left (i)
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # Step 2: Find the first element larger than nums[i] from right to left (j)
        if i >= 0:
            j = len(nums) - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            # Step 3: Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse the subarray to the right of i
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

```

## Java

```Java
class Solution {
    public void nextPermutation(int[] nums) {
        // Step 1: Find the first decreasing element from right to left (i)
        int i = nums.length - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }
        
        // Step 2: Find the first element larger than nums[i] from right to left (j)
        if (i >= 0) {
            int j = nums.length - 1;
            while (j > i && nums[j] <= nums[i]) {
                j--;
            }
            // Step 3: Swap nums[i] and nums[j]
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
        
        // Step 4: Reverse the subarray to the right of i
        int left = i + 1, right = nums.length - 1;
        while (left < right) {
            int temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            left++;
            right--;
        }
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        // Step 1: Find the first decreasing element from right to left (i)
        int i = nums.size() - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }
        
        // Step 2: Find the first element larger than nums[i] from right to left (j)
        if (i >= 0) {
            int j = nums.size() - 1;
            while (j > i && nums[j] <= nums[i]) {
                j--;
            }
            // Step 3: Swap nums[i] and nums[j]
            swap(nums[i], nums[j]);
        }
        
        // Step 4: Reverse the subarray to the right of i
        int left = i + 1, right = nums.size() - 1;
        while (left < right) {
            swap(nums[left], nums[right]);
            left++;
            right--;
        }
    }
};

```
基础知识

Go 版本：

4. **Go 语言基础**: 了解 Go 语言的基本语法、数据类型、函数定义和使用、切片（slice）等相关知识。

5. **指针**: 了解指针的概念以及如何在 Go 中使用指针。

6. **函数**: 理解如何定义和调用函数，以及函数的参数和返回值。

7. **数组切片**: 了解 Go 中的切片概念和切片操作，包括切片的创建和修改。

Python 版本：

4. **Python 基础**: 了解 Python 的基本语法、列表（list）、条件语句和循环。

5. **类和对象**: 理解如何定义类和创建对象（在 Python 类中定义方法）。

6. **列表操作**: 了解如何操作列表，包括索引、切片、迭代和修改列表元素。

Java 版本：

4. **Java 基础**: 熟悉 Java 的基本语法、数组、循环和条件语句。

5. **类和方法**: 了解如何定义类和方法，并且如何在类中使用成员变量和方法。

6. **数组操作**: 熟悉 Java 中数组的创建、遍历和修改操作。

C++ 版本：

4. **C++ 基础**: 了解 C++ 的基本语法、数组、循环和条件语句。

5. **函数**: 理解如何定义和调用函数，以及函数的参数和返回值。

6. **数组操作**: 了解如何操作数组，包括索引、遍历和修改数组元素。

