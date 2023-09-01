# [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

## 题目

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

```c
Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
```

Example 2:

```c
Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

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

给定一个有序数组 nums，对数组中的元素进行去重，使得原数组中的每个元素只有一个。最后返回去重以后数组的长度值。

## 解题思路

Go 版本解题思路：

1. 初始化一个指针 `i`，用于指向当前不重复元素的位置。
2. 使用两个指针，`i` 和 `j`，其中 `i` 指向当前不重复元素的位置，而 `j` 用于遍历数组。
3. 从数组的第二个元素开始，遍历数组。比较当前元素和前一个元素是否相等。
4. 如果当前元素不等于前一个元素，说明找到了一个新的不重复元素，将指针 `i` 向前移动一位，然后将当前不重复的元素放置在指针 `i` 的位置。
5. 重复步骤 3 和 4，直到遍历完整个数组。
6. 返回不重复元素的数量（长度），需要加 1，因为数组下标从 0 开始。

Python 版本解题思路：

1. 初始化一个指针 `i`，用于指向当前不重复元素的位置。
2. 使用两个指针，`i` 和 `j`，其中 `i` 指向当前不重复元素的位置，而 `j` 用于遍历列表。
3. 从列表的第二个元素开始，遍历列表。比较当前元素和前一个元素是否相等。
4. 如果当前元素不等于前一个元素，说明找到了一个新的不重复元素，将指针 `i` 向前移动一位，然后将当前不重复的元素放置在指针 `i` 的位置。
5. 重复步骤 3 和 4，直到遍历完整个列表。
6. 返回不重复元素的数量（长度），需要加 1，因为列表下标从 0 开始。

Java 版本解题思路：

1. 初始化一个指针 `i`，用于指向当前不重复元素的位置。
2. 使用两个指针，`i` 和 `j`，其中 `i` 指向当前不重复元素的位置，而 `j` 用于遍历数组。
3. 从数组的第二个元素开始，遍历数组。比较当前元素和前一个元素是否相等。
4. 如果当前元素不等于前一个元素，说明找到了一个新的不重复元素，将指针 `i` 向前移动一位，然后将当前不重复的元素放置在指针 `i` 的位置。
5. 重复步骤 3 和 4，直到遍历完整个数组。
6. 返回不重复元素的数量（长度），需要加 1，因为数组下标从 0 开始。

C++ 版本解题思路：

1. 初始化一个指针 `i`，用于指向当前不重复元素的位置。
2. 使用两个指针，`i` 和 `j`，其中 `i` 指向当前不重复元素的位置，而 `j` 用于遍历向量。
3. 从向量的第二个元素开始，遍历向量。比较当前元素和前一个元素是否相等。
4. 如果当前元素不等于前一个元素，说明找到了一个新的不重复元素，将指针 `i` 向前移动一位，然后将当前不重复的元素放置在指针 `i` 的位置。
5. 重复步骤 3 和 4，直到遍历完整个向量。
6. 返回不重复元素的数量（长度），需要加 1，因为向量下标从 
## 代码
## Go
```Go
// 定义一个函数，用于从排序后的整数数组中去除重复元素，并返回新数组的长度
func removeDuplicates(nums []int) int {
    // 如果数组为空，直接返回0
    if len(nums) == 0 {
        return 0
    }

    // 初始化一个指针i，用于指向当前不重复元素的位置
    i := 0
    // 遍历数组，从第二个元素开始
    for j := 1; j < len(nums); j++ {
        // 如果当前元素不等于前一个元素，说明找到了一个新的不重复元素
        if nums[i] != nums[j] {
            // 将指针i向前移动一位
            i++
            // 将当前不重复的元素放置在指针i的位置
            nums[i] = nums[j]
        }
    }

    // 返回不重复元素的数量（长度），需要加1，因为数组下标从0开始
    return i + 1
}

```
## Python
```Python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 如果数组为空，直接返回0
        if not nums:
            return 0
        
        # 初始化一个指针i，用于指向当前不重复元素的位置
        i = 0
        # 遍历数组，从第二个元素开始
        for j in range(1, len(nums)):
            # 如果当前元素不等于前一个元素，说明找到了一个新的不重复元素
            if nums[i] != nums[j]:
                # 将指针i向前移动一位
                i += 1
                # 将当前不重复的元素放置在指针i的位置
                nums[i] = nums[j]
        
        # 返回不重复元素的数量（长度），需要加1，因为数组下标从0开始
        return i + 1
```
## Java
```Java
class Solution {
    public int removeDuplicates(int[] nums) {
        // 如果数组为空，直接返回0
        if (nums.length == 0) {
            return 0;
        }

        // 初始化一个指针i，用于指向当前不重复元素的位置
        int i = 0;
        // 遍历数组，从第二个元素开始
        for (int j = 1; j < nums.length; j++) {
            // 如果当前元素不等于前一个元素，说明找到了一个新的不重复元素
            if (nums[i] != nums[j]) {
                // 将指针i向前移动一位
                i++;
                // 将当前不重复的元素放置在指针i的位置
                nums[i] = nums[j];
            }
        }

        // 返回不重复元素的数量（长度），需要加1，因为数组下标从0开始
        return i + 1;
    }
}

```
## Cpp
```Cpp
#include <vector>

class Solution {
public:
    int removeDuplicates(std::vector<int>& nums) {
        // 如果数组为空，直接返回0
        if (nums.empty()) {
            return 0;
        }

        // 初始化一个指针i，用于指向当前不重复元素的位置
        int i = 0;
        // 遍历数组，从第二个元素开始
        for (int j = 1; j < nums.size(); j++) {
            // 如果当前元素不等于前一个元素，说明找到了一个新的不重复元素
            if (nums[i] != nums[j]) {
                // 将指针i向前移动一位
                i++;
                // 将当前不重复的元素放置在指针i的位置
                nums[i] = nums[j];
            }
        }

        // 返回不重复元素的数量（长度），需要加1，因为数组下标从0开始
        return i + 1;
    }
};

```

Go 版本解法所需基础知识：

1. **切片（Slices）和数组（Arrays）：** Go 中的切片是动态数组，可以根据需要动态调整大小。在本题中，我们使用切片来操作数组。
2. **循环和迭代：** 你需要理解 `for` 循环和如何迭代数组的元素。
3. **指针：** `i` 是一个指向数组元素的指针，你需要了解指针的概念和如何使用它来修改数组元素。

Python 版本解法所需基础知识：

1. **列表（Lists）：** Python 中的列表类似于数组，可以包含多个元素。在本题中，我们使用列表来操作数组。
2. **循环和迭代：** 你需要理解 `for` 循环和如何迭代列表的元素。
3. **索引和切片：** 你需要了解如何使用索引来访问列表元素，以及如何使用切片来修改和操作列表。

Java 版本解法所需基础知识：

1. **数组：** Java 中的数组是一组相同类型的元素的集合。在本题中，我们使用数组来存储和操作元素。
2. **循环和迭代：** 你需要理解 `for` 循环和如何迭代数组的元素。
3. **数组索引：** 你需要了解如何使用索引来访问数组元素，并理解数组索引从 0 开始的概念。

C++ 版本解法所需基础知识：

1. **向量（Vectors）：** C++ 中的向量类似于数组，是一种动态数组容器。在本题中，我们使用向量来存储和操作元素。
2. **循环和迭代：** 你需要理解 `for` 循环和如何迭代向量的元素。
3. **数组索引：** 你需要了解如何使用索引来访问向量元素，并理解数组索引从 0 开始的概念。

