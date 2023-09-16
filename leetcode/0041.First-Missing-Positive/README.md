# [41. First Missing Positive](https://leetcode.com/problems/first-missing-positive/description/)

## 题目

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:  

```
Input: [1,2,0]  
Output: 3  
```

Example 2:  

```
Input: [3,4,-1,1]  
Output: 2  
```

Example 3:  

```
Input: [7,8,9,11,12]  
Output: 1  
```

Note:  

Your algorithm should run in O(n) time and uses constant extra space.

## 题目大意

找到缺失的第一个正整数。

## 解题思路

**Go解决方案**：

这个解决方案的思路如下：

1. 首先，遍历数组，将正整数放置到它们应该在的位置上。具体做法是，对于数组中的每个元素 `nums[i]`，如果它是一个正整数并且在有效范围内（1 到 n），则将它放置到索引为 `nums[i] - 1` 的位置上。这样，数组中的正整数应该在的位置就被正确标记了。

2. 然后，再次遍历数组，找到第一个不在正确位置上的正整数，即缺失的第一个正整数。如果在遍历的过程中找到了这样的正整数，就返回它。如果遍历完数组都没有找到，说明数组中包含了所有的正整数，那么返回 `len(nums) + 1`，即下一个正整数。

3. 这个解决方案还包括一个递归函数 `changeArray`，用于处理交换元素的过程。

**Python解决方案**：

这个解决方案的思路如下：

1. 首先，将数组中的所有元素存储到一个集合（set）中，以便快速查找。

2. 然后，从1开始逐个检查正整数。如果某个正整数不在集合中，即为缺失的第一个正整数，直接返回它。

3. 如果遍历完所有正整数都没有找到缺失的正整数，说明数组中包含了所有正整数，返回 `n + 1`，其中 `n` 是数组的长度。

**Java解决方案**：

这个解决方案的思路如下：

1. 创建一个布尔数组 `numExists`，用于标记正整数的存在情况，数组长度为 `nums.length + 1`。初始化时，所有元素都为 `false`。

2. 遍历数组 `nums`，将数组中的正整数对应的 `numExists` 中的位置标记为 `true`。

3. 再次遍历 `numExists` 数组，找到第一个未标记为 `true` 的位置，即为缺失的第一个正整数。

4. 如果遍历完 `numExists` 数组都没有找到，说明数组中包含了所有正整数，返回 `nums.length + 1`。

**C++解决方案**：

这个解决方案的思路如下：

1. 首先，遍历数组，将正整数放置到它们应该在的位置上。具体做法是，对于数组中的每个元素 `nums[i]`，如果它是一个正整数并且在有效范围内（1 到 n），则将它放置到索引为 `nums[i] - 1` 的位置上。这样，数组中的正整数应该在的位置就被正确标记了。

2. 然后，再次遍历数组，找到第一个不在正确位置上的正整数，即缺失的第一个正整数。如果在遍历的过程中找到了这样的正整数，就返回它。如果遍历完数组都没有找到，说明数组中包含了所有正整数，那么返回 `n + 1`，即下一个正整数。

## 代码

## Go

```Go
func firstMissingPositive(nums []int) int {
    for i := 0; i < len(nums); i++ {
        if nums[i] > 0 && nums[i] <= len(nums) && nums[i] != i+1 {
            tmp := nums[nums[i]-1]
            nums[nums[i]-1] = nums[i]
            if tmp == i+1 || tmp <= 0 || tmp > len(nums) {
                nums[i] = tmp
            } else {
                if tmp > 0 && tmp <= len(nums) && tmp != nums[tmp-1] {
                    tmp = changeArray(nums, tmp)
                } else {
                    nums[i] = tmp
                }
            }
        }
    }
    
    for i := 0; i < len(nums); i++ {
        if nums[i] != i+1 {
            return i + 1
        }
    }
    
    return len(nums) + 1
}

func changeArray(nums []int, tmp int) int {
    if tmp <= 0 || tmp > len(nums) || tmp == nums[tmp-1] {
        return tmp
    }
    nextTmp := nums[tmp-1]
    nums[tmp-1] = tmp
    return changeArray(nums, nextTmp)
}

```

## Python

```Python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 使用集合来存储数组中的元素，以便快速查找
        s = set(nums)
        n = len(nums)
        
        # 从1开始逐个检查正整数，如果某个正整数不在集合中，即为缺失的第一个正整数
        for i in range(1, n + 1):
            if i not in s:
                return i
        
        # 如果数组中包含所有正整数，则返回 n+1
        return n + 1

```

## Java

```Java
class Solution {
    public int firstMissingPositive(int[] nums) {
        // 创建一个映射（数组），用于存储正整数的存在情况
        boolean[] numExists = new boolean[nums.length + 1];
        
        // 将数组中的正整数标记在映射中
        for (int num : nums) {
            if (num > 0 && num <= nums.length) {
                numExists[num] = true;
            }
        }
        
        // 从1开始逐个检查映射，找到第一个未标记的正整数即为缺失的第一个正整数
        for (int i = 1; i < numExists.length; i++) {
            if (!numExists[i]) {
                return i;
            }
        }
        
        // 如果数组中包含所有正整数，则返回数组长度加1作为缺失的第一个正整数
        return nums.length + 1;
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();

        // 遍历数组，将每个正整数 nums[i] 放置到其应该在的位置 nums[nums[i]-1]
        for (int i = 0; i < n; ) {
            // 检查 nums[i] 是否是一个有效的正整数，并且是否不在正确的位置上
            if (nums[i] > 0 && nums[i] < n && nums[i] != nums[nums[i] - 1]) {
                swap(nums[i], nums[nums[i] - 1]); // 将 nums[i] 放置到正确的位置
            } else {
                i++;
            }
        }

        // 再次遍历数组，找到第一个不在正确位置上的正整数，返回它
        for (int i = 0; i < n; i++) {
            if (nums[i] != i + 1) {
                return i + 1;
            }
        }

        // 如果数组中包含所有正整数，则返回 n+1
        return n + 1;
    }
};

```
每个版本的解决方案所需的详细基础知识。

**Go解决方案**：

1. **基本语法**: 熟悉Go编程语言的基本语法，包括变量声明、循环、条件语句等。

2. **切片（Slices）**: 了解Go中切片的概念和用法，因为该解决方案使用了切片来操作数组元素。

3. **函数声明**: 理解Go函数的声明和调用方式，包括函数参数和返回值。

4. **数组和切片操作**: 了解如何访问和修改数组和切片的元素。

5. **循环和条件语句**: 理解for循环和if条件语句的使用，因为该解决方案使用了这些控制结构。

6. **递归**: 该解决方案中使用了递归函数来处理数组元素的交换，因此了解递归的概念和实现方式也很重要。

**Python解决方案**：

1. **基本语法**: 熟悉Python编程语言的基本语法，包括变量声明、列表、循环、条件语句等。

2. **列表（Lists）**: 了解Python中列表的概念和用法，因为该解决方案使用了列表来存储数组元素。

3. **函数定义**: 理解如何定义和调用Python函数，包括函数参数和返回值。

4. **集合（Sets）**: 了解Python中集合的概念和用法，因为该解决方案使用了集合来检查元素是否存在。

5. **循环和条件语句**: 了解for循环和if条件语句的使用，因为该解决方案使用了这些控制结构。

**Java解决方案**：

1. **基本语法**: 熟悉Java编程语言的基本语法，包括变量声明、数组、循环、条件语句等。

2. **数组**: 了解Java中数组的概念和用法，因为该解决方案使用了数组来标记正整数的存在情况。

3. **函数声明**: 理解如何定义和调用Java方法，包括方法参数和返回值。

4. **布尔数组**: 了解如何使用布尔数组来标记元素的存在情况，并了解如何遍历数组。

5. **循环和条件语句**: 理解for循环和if条件语句的使用，因为该解决方案使用了这些控制结构。

**C++解决方案**：

1. **基本语法**: 熟悉C++编程语言的基本语法，包括变量声明、数组、循环、条件语句等。

2. **数组和向量（Vectors）**: 了解C++中数组和向量的概念和用法，因为该解决方案使用了数组来处理正整数。

3. **函数声明**: 理解如何定义和调用C++函数，包括函数参数和返回值。

4. **递归**: 了解递归的概念和实现方式，因为该解决方案中使用了递归函数。

5. **循环和条件语句**: 了解for循环和if条件语句的使用，因为该解决方案使用了这些控制结构。

