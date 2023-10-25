# [80. Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

## 题目

Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

```c
Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
```

Example 2:

```c
Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.
```

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

```c
// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```

## 题目大意

给定一个有序数组 nums，对数组中的元素进行去重，使得原数组中的每个元素最多暴露 2 个。最后返回去重以后数组的长度值。

## 解题思路

- 问题提示有序数组，一般最容易想到使用双指针的解法，双指针的关键点：移动两个指针的条件。
- 在该题中移动的条件：快指针从头遍历数组，慢指针指向修改后的数组的末端，当慢指针指向倒数第二个数与快指针指向的数不相等时，才移动慢指针，同时赋值慢指针。
- 处理边界条件：当数组小于两个元素时，不做处理。
以下是每个版本的解题思路：

Go 版本解题思路

1. 在Go版本中，我们使用两个指针：slow和fast。slow指针用于跟踪非重复元素的位置，而fast指针用于遍历整个数组。

2. 我们使用`for`循环和`range`关键字来遍历数组。在每次迭代中，我们检查两个条件：
   - 如果fast小于2（即前两个元素），我们确保这些元素包括在修改后的数组中。
   - 如果`nums[slow-2]`与`nums[fast]`不相等，我们检查当前元素是否与慢指针指向的位置的前两个元素不同，以确保不超过两个重复元素。

3. 如果上述条件成立，我们将当前元素复制到slow指针的位置，并将slow指针向前移动一个位置。

4. 最后，返回slow指针的值，这个值表示修改后的数组的长度，重复元素已经被移除。

Python 版本解题思路

1. 在Python版本中，我们同样使用两个指针：slow和fast，以及`enumerate`函数来遍历数组。

2. 我们使用`for`循环和`enumerate`函数来遍历数组元素，同时获取元素的索引和值。

3. 在每次迭代中，我们检查两个条件：
   - 如果fast小于2（即前两个元素），我们确保这些元素包括在修改后的数组中。
   - 如果`nums[slow-2]`与`nums[fast]`不相等，我们检查当前元素是否与慢指针指向的位置的前两个元素不同，以确保不超过两个重复元素。

4. 如果上述条件成立，我们将当前元素复制到slow指针的位置，并将slow指针向前移动一个位置。

5. 最后，返回slow指针的值，这个值表示修改后的数组的长度，重复元素已经被移除。

Java 版本解题思路

1. 在Java版本中，我们同样使用两个指针：slow和fast。

2. 使用`for`循环遍历整个数组。在每次迭代中，检查两个条件：
   - 如果fast小于2（即前两个元素），确保这些元素包括在修改后的数组中。
   - 如果`nums[slow-2]`与`nums[fast]`不相等，检查当前元素是否与慢指针指向的位置的前两个元素不同，以确保不超过两个重复元素。

3. 如果上述条件成立，将当前元素复制到slow指针的位置，并将slow指针向前移动一个位置。

4. 最后，返回slow指针的值，表示修改后的数组的长度，重复元素已被移除。

C++ 版本解题思路

1. 在C++版本中，同样使用两个指针：slow和fast。

2. 使用`for`循环遍历整个数组。在每次迭代中，检查两个条件：
   - 如果fast小于2（即前两个元素），确保这些元素包括在修改后的数组中。
   - 如果`nums[slow-2]`与`nums[fast]`不相等，检查当前元素是否与慢指针指向的位置的前两个元素不同，以确保不超过两个重复元素。

3. 如果上述条件成立，将当前元素复制到slow指针的位置，并将slow指针向前移动一个位置。

4. 最后，返回slow指针的值，表示修改后的数组的长度，重复元素已被移除。

这些解题思路都基于双指针的概念，遍历有序数组并进行去重操作，确保重复元素最多出现两次。在满足条件的情况下，通过适当地移动指针和复制元素，最终返回修改后的数组的长度。
## 代码

## Go

```Go
func removeDuplicates(nums []int) int {
    slow := 0  // 定义慢指针，用于跟踪非重复元素的位置
    for fast, v := range nums {  // 使用快指针遍历整个数组
        if fast < 2 || nums[slow-2] != v {  // 如果快指针小于2（前两个元素），或者慢指针指向的元素与当前元素不相同
            nums[slow] = v  // 将当前元素复制到慢指针位置
            slow++  // 移动慢指针，指向下一个位置
        }
    }
    return slow  // 返回去重后数组的长度
}

```

## Python

```Python
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0  # 定义慢指针，用于跟踪非重复元素的位置
        for fast, v in enumerate(nums):  # 使用快指针遍历整个数组
            if fast < 2 or nums[slow - 2] != v:  # 如果快指针小于2（前两个元素），或者慢指针指向的元素与当前元素不相同
                nums[slow] = v  # 将当前元素复制到慢指针位置
                slow += 1  # 移动慢指针，指向下一个位置
        return slow  # 返回去重后数组的长度
```

## Java

```Java
class Solution {
    public int removeDuplicates(int[] nums) {
        int slow = 0; // 定义慢指针，用于跟踪非重复元素的位置
        for (int fast = 0; fast < nums.length; fast++) { // 使用快指针遍历整个数组
            if (fast < 2 || nums[slow - 2] != nums[fast]) { // 如果快指针小于2（前两个元素），或者慢指针指向的元素与当前元素不相同
                nums[slow] = nums[fast]; // 将当前元素复制到慢指针位置
                slow++; // 移动慢指针，指向下一个位置
            }
        }
        return slow; // 返回去重后数组的长度
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int slow = 0; // 定义慢指针，用于跟踪非重复元素的位置
        for (int fast = 0; fast < nums.size(); fast++) { // 使用快指针遍历整个数组
            if (fast < 2 || nums[slow - 2] != nums[fast]) { // 如果快指针小于2（前两个元素），或者慢指针指向的元素与当前元素不相同
                nums[slow] = nums[fast]; // 将当前元素复制到慢指针位置
                slow++; // 移动慢指针，指向下一个位置
            }
        }
        return slow; // 返回去重后数组的长度
    }
};

```
理解和实现这个题目的解法需要掌握以下基础知识：



Go 版本

- **切片（Slices）：** 了解如何使用切片来操作数组，包括创建、切片、遍历切片等。在Go中，切片是动态数组，经常用于解决数组长度不确定的情况。

- **for-range 循环：** 了解如何使用 `for` 循环和 `range` 关键字来遍历数组的元素。

Python 版本

- **列表（Lists）：** 了解如何使用列表来操作数组，包括创建、切片、遍历列表等。在Python中，列表是一种灵活的数据结构，用于存储序列数据。

- **enumerate 函数：** 了解如何使用 `enumerate` 函数来同时获取元素的索引和值，这对于在循环中处理数组元素非常有用。

- **类和方法：** 了解如何定义类和方法，尤其是在实现类似面向对象的解决方案时。

Java 版本

- **数组：** 了解如何声明和初始化数组，以及如何使用数组的索引来访问元素。

- **for 循环：** 了解如何使用 `for` 循环来遍历数组，以及如何在循环中处理数组元素。

C++ 版本

- **数组：** 了解如何声明和初始化数组，以及如何使用数组的索引来访问元素。

- **for 循环：** 了解如何使用 `for` 循环来遍历数组，以及如何在循环中处理数组元素。

- **类和方法：** 了解如何定义类和方法，尤其是在实现类似面向对象的解决方案时。

这些基础知识是理解和实现题目解法的关键，无论选择哪种编程语言版本，都需要熟练掌握这些概念。另外，对于特定语言的版本，还需要了解相关语言的语法和特性，如切片、列表、类和方法等。