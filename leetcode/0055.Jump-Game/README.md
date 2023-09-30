# [55. Jump Game](https://leetcode.com/problems/jump-game/)


## 题目

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

**Example 1**:

```
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Example 2**:

```
Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
```

## 题目大意

给定一个非负整数数组，最初位于数组的第一个位置。数组中的每个元素代表在该位置可以跳跃的最大长度。判断是否能够到达最后一个位置。

## 解题思路

- 给出一个非负数组，要求判断从数组 0 下标开始，能否到达数组最后一个位置。
- 这一题比较简单。如果某一个作为 `起跳点` 的格子可以跳跃的距离是 `n`，那么表示后面 `n` 个格子都可以作为 `起跳点`。可以对每一个能作为 `起跳点` 的格子都尝试跳一次，把 `能跳到最远的距离maxJump` 不断更新。如果可以一直跳到最后，就成功了。如果中间有一个点比 `maxJump` 还要大，说明在这个点和 maxJump 中间连不上了，有些点不能到达最后一个位置。
当然，我来分别介绍每个版本的解题思路：

Go 版本解题思路：

- 题目要求判断是否能够从第一个位置跳跃到最后一个位置。
- 使用一个变量 `maxj` 来表示当前能够跳到的最远位置，初始值为0。
- 遍历数组中的每个元素，对于每个元素，检查是否能够跳到当前位置（`i > maxj` 表示无法跳到当前位置，返回false），然后更新 `maxj` 为当前位置和当前位置能跳跃的最大距离之间的较大值。
- 如果成功遍历完整个数组，说明可以跳到最后一个位置，返回true。

Python 版本解题思路：

- 同样，题目要求判断是否能够从第一个位置跳跃到最后一个位置。
- 使用变量 `max_i` 来表示当前能够跳到的最远位置，初始值为0。
- 使用 `enumerate` 函数遍历列表，`i` 表示当前位置，`jump` 表示当前位置的跳数。
- 如果 `max_i` 大于等于 `i` 并且 `i + jump` 大于 `max_i`，则更新 `max_i` 为 `i + jump`。
- 最后，判断 `max_i` 是否大于等于最后一个位置 `i`，如果是，则返回True，否则返回False。

Java 版本解题思路：

- 题目要求判断是否能够从第一个位置跳跃到最后一个位置。
- 使用变量 `max_i` 来表示当前能够跳到的最远位置，初始值为0。
- 使用 `for` 循环遍历数组，`i` 表示当前位置。
- 如果 `max_i` 大于等于 `i` 并且 `i + nums[i]` 大于 `max_i`，则更新 `max_i` 为 `i + nums[i]`。
- 最后，判断 `max_i` 是否大于等于数组的最后一个位置，如果是，则返回True，否则返回False。

C++ 版本解题思路：

- 同样，题目要求判断是否能够从第一个位置跳跃到最后一个位置。
- 使用变量 `max_i` 来表示当前能够跳到的最远位置，初始值为0。
- 使用 `for` 循环遍历向量，`i` 表示当前位置。
- 如果 `max_i` 大于等于 `i` 并且 `i + nums[i]` 大于 `max_i`，则更新 `max_i` 为 `i + nums[i]`。
- 最后，判断 `max_i` 是否大于等于向量的最后一个位置，如果是，则返回True，否则返回False。

这些解题思路都是基于贪心算法的思想，即不断更新能够跳到的最远位置，最终判断是否能够跳到最后一个位置。希望这些解题思路能够帮助您理解每个版本的解决方案。如果您有更多问题，请随时提出。
## 代码

```go
func canJump(nums []int) bool {
  maxj := 0 // 初始化一个变量 maxj，表示当前能够跳到的最远的位置
  for i := 0; i < len(nums); i++ { // 遍历数组中的每个元素
    if i > maxj { // 如果当前索引 i 大于 maxj，说明无法跳到当前位置
      return false // 返回 false，表示无法跳到末尾
    }
    maxj = max(maxj, nums[i]+i) // 更新 maxj，取当前 maxj 和当前位置能跳到的最远位置的较大值
  }
  return true // 如果成功遍历完数组，说明可以跳到末尾，返回 true
}

func max(a, b int) int {
  if a > b {
    return a
  }
  return b
}

```
## Python

```Python
class Solution:
    def canJump(self, nums) :
        max_i = 0       # 初始化当前能到达最远的位置，开始时为0
        for i, jump in enumerate(nums):   # 使用enumerate函数遍历列表，i为当前位置，jump是当前位置的跳数
            if max_i >= i and i + jump > max_i:  # 如果当前位置能到达，并且当前位置+跳数>最远位置
                max_i = i + jump  # 更新最远能到达位置
        return max_i >= i  # 判断最远能到达位置是否大于等于最后一个位置i，返回True或False
```

## Java

```Java
class Solution {
    public boolean canJump(int[] nums) {
        int max_i = 0;  // 初始化当前能到达最远的位置，开始时为0
        for (int i = 0; i < nums.length; i++) {
            if (max_i >= i && i + nums[i] > max_i) {
                max_i = i + nums[i];  // 更新最远能到达位置
            }
        }
        return max_i >= nums.length - 1;  // 判断最远能到达位置是否大于等于最后一个位置
    }
}


```

## Cpp

```Cpp
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int max_i = 0;  // 初始化当前能到达最远的位置，开始时为0
        for (int i = 0; i < nums.size(); i++) {
            if (max_i >= i && i + nums[i] > max_i) {
                max_i = i + nums[i];  // 更新最远能到达位置
            }
        }
        return max_i >= nums.size() - 1;  // 判断最远能到达位置是否大于等于最后一个位置
    }
};


```
当然，我可以使用中文来详细介绍每个版本的所需基础知识。

Go 版本：

1. **数组和切片**：了解如何声明和使用数组和切片。在Go中，数组是固定长度的，而切片是动态数组。

2. **循环和迭代**：理解`for`循环和如何遍历切片或数组。

3. **函数**：熟悉如何定义和调用函数。在这个示例中，有两个函数，`canJump` 和 `max`。

Python 版本：

1. **列表和迭代**：了解如何声明和操作Python的列表（List）数据结构。列表可以包含不同类型的元素。

2. **enumerate函数**：了解`enumerate`函数，它用于同时遍历列表的索引和值。

3. **条件语句**：理解`if`条件语句的使用，以及如何根据条件执行不同的操作。

Java 版本：

1. **数组和循环**：了解如何声明和操作Java数组。Java中数组的大小是固定的。

2. **for循环**：理解`for`循环的使用，以及如何遍历数组。

3. **条件语句**：熟悉`if`条件语句的使用，以根据条件执行不同的操作。

C++ 版本：

1. **向量（Vector）**：了解如何使用C++的向量容器，它类似于动态数组。向量可以自动调整大小。

2. **for循环**：理解`for`循环的使用，以及如何遍历向量。

3. **条件语句**：熟悉`if`条件语句的使用，以根据条件执行不同的操作。

这些基础知识是理解和编写这些版本中的解决方案所必需的。如果您需要更详细的解释或有其他问题，请随时提出。