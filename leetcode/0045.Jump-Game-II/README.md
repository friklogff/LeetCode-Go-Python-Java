# [45. Jump Game II](https://leetcode.com/problems/jump-game-ii/)


## 题目

Given an array of non-negative integers `nums`, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

**Example 1:**

```
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Example 2:**

```
Input: nums = [2,3,0,1,4]
Output: 2
```

**Constraints:**

- `1 <= nums.length <= 1000`
- `0 <= nums[i] <= 10^5`

## 题目大意

给定一个非负整数数组，你最初位于数组的第一个位置。数组中的每个元素代表你在该位置可以跳跃的最大长度。你的目标是使用最少的跳跃次数到达数组的最后一个位置。

## 解题思路

- 要求找到最少跳跃次数，顺理成章的会想到用贪心算法解题。扫描步数数组，维护当前能够到达最大下标的位置，记为能到达的最远边界，如果扫描过程中到达了最远边界，更新边界并将跳跃次数 + 1。
- 扫描数组的时候，其实不需要扫描最后一个元素，因为在跳到最后一个元素之前，能到达的最远边界一定大于等于最后一个元素的位置，不然就跳不到最后一个元素，到达不了终点了；如果遍历到最后一个元素，说明边界正好为最后一个位置，最终跳跃次数直接 + 1 即可，也不需要访问最后一个元素。

Go 版本解题思路

在Go版本中，解决"Jump Game II"问题的思路如下：

1. 初始化三个变量：`needChoose`（表示需要选择下一步的位置）、`canReach`（表示当前可以到达的最远位置）、`step`（表示跳跃的步数），并将它们都初始化为0。

2. 遍历输入数组 `nums`，使用 `for i, x := range nums` 进行遍历。

3. 在遍历过程中，检查当前位置 `i` 加上能够跳跃的最大距离 `x` 是否大于 `canReach`，如果是的话，更新 `canReach` 为 `i + x`，表示可以到达的更远位置。

4. 如果 `canReach` 已经大于等于数组的最后一个位置 `len(nums)-1`，那么直接返回 `step + 1`，因为已经能够到达终点了。

5. 如果当前位置 `i` 等于 `needChoose` 所指的位置，说明需要选择下一步的位置了。此时，将 `needChoose` 更新为 `canReach`，表示下一步要从 `canReach` 开始跳跃，同时将 `step` 加1，表示跳跃了一步。

6. 最终，返回最小步数 `step`，这就是达到最后一个位置所需的最小跳跃次数。

Python 版本解题思路

在Python版本中，解决"Jump Game II"问题的思路与Go版本类似：

1. 初始化三个变量：`needChoose`（表示需要选择下一步的位置）、`canReach`（表示当前可以到达的最远位置）、`step`（表示跳跃的步数），并将它们都初始化为0。

2. 遍历输入列表 `nums`，使用 `for i in range(len(nums))` 进行遍历。

3. 在遍历过程中，检查当前位置 `i` 加上能够跳跃的最大距离 `nums[i]` 是否大于 `canReach`，如果是的话，更新 `canReach` 为 `i + nums[i]`，表示可以到达的更远位置。

4. 如果 `canReach` 已经大于等于列表的最后一个位置 `len(nums)-1`，那么直接返回 `step + 1`，因为已经能够到达终点了。

5. 如果当前位置 `i` 等于 `needChoose` 所指的位置，说明需要选择下一步的位置了。此时，将 `needChoose` 更新为 `canReach`，表示下一步要从 `canReach` 开始跳跃，同时将 `step` 加1，表示跳跃了一步。

6. 最终，返回最小步数 `step`，这就是达到最后一个位置所需的最小跳跃次数。

Java 版本解题思路

在Java版本中，解决"Jump Game II"问题的思路与Go和Python版本相似：

1. 初始化三个变量：`needChoose`（表示需要选择下一步的位置）、`canReach`（表示当前可以到达的最远位置）、`step`（表示跳跃的步数），并将它们都初始化为0。

2. 遍历输入数组 `nums`，使用 `for (int i = 0; i < nums.length; i++)` 进行遍历。

3. 在遍历过程中，检查当前位置 `i` 加上能够跳跃的最大距离 `nums[i]` 是否大于 `canReach`，如果是的话，更新 `canReach` 为 `i + nums[i]`，表示可以到达的更远位置。

4. 如果 `canReach` 已经大于等于数组的最后一个位置 `nums.length - 1`，那么直接返回 `step + 1`，因为已经能够到达终点了。

5. 如果当前位置 `i` 等于 `needChoose` 所指的位置，说明需要选择下一步的位置了。此时，将 `needChoose` 更新为 `canReach`，表示下一步要从 `canReach` 开始跳跃，同时将 `step` 加1，表示跳跃了一步。

6. 最终，返回最小步数 `step`，这就是达到最后一个位置所需的最小跳跃次数。

C++ 版本解题思路

在C++版本中，解决"Jump Game II"问题的思路与前述版本相似：

1. 初始化三个变量：`needChoose`（表示需要选择下一步的位置）、`canReach`（表示当前可以到达的最远位置）、`step`（表示跳跃的步数），并将它们都初始化为0。

2. 遍历输入向量 `nums`，使用 `for (int i = 0; i < nums.size(); i++)` 进行遍历。

3. 在遍历过程中，检查当前位置 `i` 加上能够跳跃的最大距离 `nums[i]` 是否大于 `canReach`，如果是的话，更新 `canReach` 为 `i + nums[i]`，表示可以到达的更远位置。

4. 如果 `canReach` 已经大于等于向量的最后一个位置 `nums.size() - 1`，那么直接返回 `step + 1`，因为已经能够到达终点了。

5. 如果当前位置 `i` 等于 `needChoose` 所指的位置，说明需要选择下一步的位置了。此时，将 `needChoose` 更新为 `canReach`，表示下一步要从 `canReach` 开始跳跃，同时将 `step` 加1，表示跳跃了一步。

6. 最终，返回最小步数 `step`，这就是达到最后一个位置所需的最小跳跃次数。

这就是各个版本的解题思路
## 代码

```go
func jump(nums []int) int {
    // 如果数组长度为1，无需跳跃，返回0
    if len(nums) == 1 {
        return 0
    }
    // needChoose 表示需要选择下一步的位置，canReach 表示当前可以到达的最远位置，step 表示跳跃的步数
    needChoose, canReach, step := 0, 0, 0
    // 遍历数组
    for i, x := range nums {
        // 如果当前位置加上跳跃力可以到达更远的位置
        if i+x > canReach {
            // 更新 canReach 为更远的位置
            canReach = i + x
            // 如果 canReach 已经可以到达数组末尾，返回步数加1
            if canReach >= len(nums)-1 {
                return step + 1
            }
        }
        // 如果当前位置已经是 needChoose 所指的位置
        if i == needChoose {
            // 更新 needChoose 为 canReach，表示下一步要从 canReach 开始跳跃
            needChoose = canReach
            // 步数加1
            step++
        }
    }
    // 返回最小步数
    return step
}

```


## Python

```Python
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        needChoose, canReach, step = 0, 0, 0
        for i in range(len(nums)):
            if i + nums[i] > canReach:
                canReach = i + nums[i]
                if canReach >= len(nums) - 1:
                    return step + 1
            if i == needChoose:
                needChoose = canReach
                step += 1
        return step

```

## Java

```Java
class Solution {
    public int jump(int[] nums) {
        if (nums.length == 1) {
            return 0;
        }
        int needChoose = 0, canReach = 0, step = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i + nums[i] > canReach) {
                canReach = i + nums[i];
                if (canReach >= nums.length - 1) {
                    return step + 1;
                }
            }
            if (i == needChoose) {
                needChoose = canReach;
                step++;
            }
        }
        return step;
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    int jump(vector<int>& nums) {
        if (nums.size() == 1) {
            return 0;
        }
        int needChoose = 0, canReach = 0, step = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (i + nums[i] > canReach) {
                canReach = i + nums[i];
                if (canReach >= nums.size() - 1) {
                    return step + 1;
                }
            }
            if (i == needChoose) {
                needChoose = canReach;
                step++;
            }
        }
        return step;
    }
};

```

每个版本的代码所需要的基础知识。

Go 版本

- Go（也称为Golang）是一门开源的编程语言，它具有简洁的语法和高效的性能。在这个Go版本的代码中，你需要了解以下基础知识：
  - Go的基本语法，包括变量声明、循环、条件语句等。
  - 切片（slice）和数组（array）的使用，因为题目涉及处理整数数组。
  - 函数的定义和调用，以及函数参数和返回值的处理。
  - 循环结构（for循环）和条件语句（if语句）的使用，因为这些在解决问题时很重要。
  - 切片的操作，如切片扩容、索引访问等，因为这些与跳跃问题相关。

Python 版本

- Python是一门广泛使用的高级编程语言，以其简单易读的语法而闻名。在这个Python版本的代码中，你需要了解以下基础知识：
  - Python的基本语法，包括变量声明、循环、条件语句等。
  - 列表（List）的使用，因为题目涉及处理整数列表。
  - 类和方法的定义，因为代码使用了类来组织解决方案。
  - 循环结构（for循环）和条件语句（if语句）的使用，因为这些在解决问题时很重要。

Java 版本

- Java是一门广泛使用的静态类型编程语言，通常用于构建大型应用程序。在这个Java版本的代码中，你需要了解以下基础知识：
  - Java的基本语法，包括变量声明、循环、条件语句等。
  - 数组的使用，因为题目涉及处理整数数组。
  - 类和方法的定义，因为代码使用了类来组织解决方案。
  - 循环结构（for循环）和条件语句（if语句）的使用，因为这些在解决问题时很重要。

C++ 版本

- C++是一门多范式的编程语言，它结合了高级和低级编程的特性。在这个C++版本的代码中，你需要了解以下基础知识：
  - C++的基本语法，包括变量声明、循环、条件语句等。
  - 向量（Vector）的使用，因为题目涉及处理整数向量。
  - 类和方法的定义，因为代码使用了类来组织解决方案。
  - 循环结构（for循环）和条件语句（if语句）的使用，因为这些在解决问题时很重要。

以上是每个版本代码所需的基础知识概述。如果你需要更详细的解释或有特定问题，欢迎提出。