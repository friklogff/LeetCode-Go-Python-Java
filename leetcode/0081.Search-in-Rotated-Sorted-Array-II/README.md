# [81. Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)


## 题目

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., `[0,0,1,2,2,5,6]` might become `[2,5,6,0,0,1,2]`).

You are given a target value to search. If found in the array return `true`, otherwise return `false`.

**Example 1:**

    Input: nums = [2,5,6,0,0,1,2], target = 0
    Output: true

**Example 2:**

    Input: nums = [2,5,6,0,0,1,2], target = 3
    Output: false

**Follow up:**

- This is a follow up problem to [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/description/), where `nums` may contain duplicates.
- Would this affect the run-time complexity? How and why?


## 题目大意

假设按照升序排序的数组在预先未知的某个点上进行了旋转。( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

进阶:

- 这是搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
- 这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？


## 解题思路


- 给出一个数组，数组中本来是从小到大排列的，并且数组中有重复数字。但是现在把后面随机一段有序的放到数组前面，这样形成了前后两端有序的子序列。在这样的一个数组里面查找一个数，设计一个 O(log n) 的算法。如果找到就输出 `true`，如果没有找到，就输出 `false` 。
- 这一题是第 33 题的加强版，实现代码完全一样，只不过输出变了。这一题输出 `true` 和 `false` 了。具体思路见第 33 题。

以下是每个版本的解题思路：

**Go 版本：**

1. **初始化指针：** 首先，初始化两个指针 `low` 和 `high`，分别指向数组的第一个元素和最后一个元素。

2. **进入循环：** 使用循环，直到 `low` 大于 `high` 为止。

3. **计算中间索引：** 计算中间索引 `mid`，通过 `(low + (high - low) >> 1)` 来避免整数溢出。

4. **检查中间元素：** 检查中间元素是否等于目标元素，如果是，返回 `true`，因为找到了目标。

5. **处理两部分情况：** 如果中间元素不等于目标，需要根据数组的性质将搜索范围缩小到左半部分或右半部分。

    a. 如果 `nums[mid] > nums[low]`，说明左半部分是有序的。在这种情况下，检查目标是否在 `low` 和 `mid` 之间，如果是，将 `high` 更新为 `mid - 1`，否则将 `low` 更新为 `mid + 1`。

    b. 如果 `nums[mid] < nums[high]`，说明右半部分是有序的。在这种情况下，检查目标是否在 `mid` 和 `high` 之间，如果是，将 `low` 更新为 `mid + 1`，否则将 `high` 更新为 `mid - 1`。

    c. 处理重复的情况：如果 `nums[low]` 等于 `nums[mid]`，将 `low` 指针向右移动一位；如果 `nums[high]` 等于 `nums[mid]`，将 `high` 指针向左移动一位。

6. **返回结果：** 如果循循环结束后仍未找到目标元素，返回 `false`，因为目标不在数组中。

**Python 版本：**

1. **初始化指针和处理边界情况：** 首先，初始化指针 `start` 和 `end` 分别指向数组的第一个元素和最后一个元素。还需要处理特殊情况，例如数组为空或只包含一个元素。

2. **进入循环：** 使用循环，直到 `start` 大于 `end` 为止。

3. **计算中间索引：** 计算中间索引 `half`，通过 `(start + end) // 2` 来找到中间元素的索引。

4. **检查中间元素：** 检查中间元素是否等于目标元素，如果是，返回 `True`，因为找到了目标。

5. **处理两部分情况：** 如果中间元素不等于目标，需要根据数组的性质将搜索范围缩小到左半部分或右半部分。

    a. 如果 `nums[start]` 等于 `nums[half]` 且 `nums[half]` 等于 `nums[end]`，这表示存在重复元素。在这种情况下，将 `start` 向右移动一位，将 `end` 向左移动一位。

    b. 如果 `nums[start]` 小于等于 `nums[half]`，说明左半部分是有序的。检查目标是否在这个有序部分内。如果是，将 `end` 更新为 `half - 1`，否则将 `start` 更新为 `half + 1`。

    c. 如果 `nums[half]` 小于 `nums[end]`，说明右半部分是有序的。检查目标是否在这个有序部分内。如果是，将 `start` 更新为 `half + 1`，否则将 `end` 更新为 `half - 1`。

6. **返回结果：** 如果循环结束后仍未找到目标元素，返回 `False`，因为目标不在数组中。

**Java 版本：**

1. **初始化指针和处理边界情况：** 首先，初始化指针 `low` 和 `high` 分别指向数组的第一个元素和最后一个元素。还需要处理特殊情况，例如数组为空或只包含一个元素。

2. **进入循环：** 使用循环，直到 `low` 大于 `high` 为止。

3. **计算中间索引：** 计算中间索引 `mid`，通过 `(low + (high - low) / 2)` 来找到中间元素的索引。

4. **检查中间元素：** 检查中间元素是否等于目标元素，如果是，返回 `true`，因为找到了目标。

5. **处理两部分情况：** 如果中间元素不等于目标，需要根据数组的性质将搜索范围缩小到左半部分或右半部分。

    a. 如果 `nums[mid] > nums[low]`，说明左半部分是有序的。在这种情况下，检查目标是否在 `low` 和 `mid` 之间，如果是，将 `high` 更新为 `mid - 1`，否则将 `low` 更新为 `mid + 1`。

    b. 如果 `nums[mid] < nums[high]`，说明右半部分是有序的。在这种情况下，检查目标是否在 `mid` 和 `high` 之间，如果是，将 `low` 更新为 `mid + 1`，否则将 `high` 更新为 `mid - 1`。

    c. 处理重复的情况：如果 `nums[low]` 等于 `nums[mid]`，将 `low` 指针向右移动一位；如果 `nums[high]` 等于 `nums[mid]`，将 `high` 指针向左移动一位。

6. **返回结果：** 如果循环结束后仍未找到目标元素，返回 `false`，因为目标不在数组中。

**C++ 版本：**

1. **初始化指针和处理边界情况：** 首先，初始化指针 `low` 和 `high` 分别指向数组的第一个元素和最后一个元素。还需要处理特殊情况，例如数组为空或只包含一个元素。

2. **进入循环：** 使用循环，直到 `low` 大于 `high` 为止。

3. **计算中间索引：** 计算中间索引 `mid`，通过 `(low + (high - low) / 2)` 来找到中间元素的索引。

4. **检查中间元素：** 检查中间元素是否等于目标元素，如果是，返回 `true`，因为找到了目标。

5. **处理两部分情况：** 如果中间元素不等于目标，需要根据数组的性质将搜索范围缩小到左半部分或右半部分。

    a. 如果 `nums[mid] > nums[low]`，说明左半部分是有序的。在这种情况下，检查目标是否在 `low` 和 `mid` 之间，如果是，将 `high` 更新为 `mid - 1`，否则将 `low` 更新为 `mid + 1`。

    b. 如果 `nums[mid] < nums[high]`，说明右半部分是有序的。在这种情况下，检查目标是否在 `mid` 和 `high` 之间，如果是，将 `low` 更新为 `mid + 1`，否则将 `high` 更新为 `mid - 1`。

    c. 处理重复的情况：如果 `nums[low]` 等于 `nums[mid]`，将 `low` 指针向右移动一位；如果 `nums[high]` 等于 `nums[mid]`，将 `high` 指针向左移动一位。

6. **返回结果：** 如果循环结束后仍未找到目标元素，返回 `false`，因为目标不在数组中。

总的来说，这些解题思路都涉及初始化指针，使用二分查找的思想，适应不同编程语言的语法和数据结构，以解决旋转有序数组中的目标查找问题。处理重复元素和边界情况是解题的关键点，同时需要理解二分查找算法的核心思想。
## 代码

## Go

```Go
func search(nums []int, target int) bool {
	if len(nums) == 0 {
		return false
	}
	// 初始化两个指针，low指向数组的第一个元素，high指向数组的最后一个元素
	low, high := 0, len(nums)-1
	// 进入循环，直到low大于high时结束
	for low <= high {
		// 计算中间索引
		mid := low + (high-low)>>1
		// 如果中间元素等于目标元素，则返回true
		if nums[mid] == target {
			return true
		} else if nums[mid] > nums[low] { // 在数值大的一部分区间里
			// 如果目标元素在low和mid之间，缩小搜索范围为low到mid-1
			if nums[low] <= target && target < nums[mid] {
				high = mid - 1
			} else {
				// 否则，缩小搜索范围为mid+1到high
				low = mid + 1
			}
		} else if nums[mid] < nums[high] { // 在数值小的一部分区间里
			// 如果目标元素在mid和high之间，缩小搜索范围为mid+1到high
			if nums[mid] < target && target <= nums[high] {
				low = mid + 1
			} else {
				// 否则，缩小搜索范围为low到mid-1
				high = mid - 1
			}
		} else {
			// 处理重复的情况
			// 如果nums[low]等于nums[mid]，将low指针向右移动一位
			if nums[low] == nums[mid] {
				low++
			}
			// 如果nums[high]等于nums[mid]，将high指针向左移动一位
			if nums[high] == nums[mid] {
				high--
			}
		}
	}
	// 如果循环结束仍未找到目标元素，返回false
	return false
}

```

## Python

```Python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums) - 1

        if len(nums) == 0:
            return False

        if len(nums) == 1:
            return nums[0] == target

        while(start <= end):
            half = (start + end) // 2
            if nums[half] == target:
                return True

            if nums[start] == nums[half] and nums[half] == nums[end]:
                # 处理重复元素的情况
                start += 1
                end -= 1
            elif nums[start] <= nums[half]:
                if nums[start] <= target and nums[half] > target:
                    # 目标值在有序部分
                    end = half - 1
                else:
                    # 目标值在旋转部分
                    start = half + 1
            else:
                if nums[half] < target and nums[end] >= target:
                    # 目标值在有序部分
                    start = half + 1
                else:
                    # 目标值在旋转部分
                    end = half - 1

        return False

```

## Java

```Java
class Solution {
    public boolean search(int[] nums, int target) {
        if (nums.length == 0) {
            return false;
        }
        int low = 0, high = nums.length - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (nums[mid] == target) {
                return true;
            } else if (nums[mid] > nums[low]) {
                if (nums[low] <= target && target < nums[mid]) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            } else if (nums[mid] < nums[high]) {
                if (nums[mid] < target && target <= nums[high]) {
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            } else {
                if (nums[low] == nums[mid]) {
                    low++;
                }
                if (nums[high] == nums[mid]) {
                    high--;
                }
            }
        }
        return false;
    }
}
```

## Cpp

```Cpp
class Solution {
public:
    bool search(vector<int>& nums, int target) {
        if (nums.empty()) {
            return false;
        }
        int low = 0, high = nums.size() - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (nums[mid] == target) {
                return true;
            } else if (nums[mid] > nums[low]) {
                if (nums[low] <= target && target < nums[mid]) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            } else if (nums[mid] < nums[high]) {
                if (nums[mid] < target && target <= nums[high]) {
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            } else {
                if (nums[low] == nums[mid]) {
                    low++;
                }
                if (nums[high] == nums[mid]) {
                    high--;
                }
            }
        }
        return false;
    }
};

```

当使用不同的编程语言来解决算法问题时，需要了解各个语言的基本语法和数据结构。以下是每个版本的需要掌握的基础知识：

**Go 版本：**

1. **数组和切片：** 在 Go 中，数组是固定长度的数据结构，切片则是动态长度的。你需要理解如何声明、初始化和操作数组和切片，因为算法问题通常需要对数据结构进行操作。

2. **循环和条件语句：** 了解 Go 中的 `for` 循环和 `if` 条件语句的用法，因为它们在算法实现中经常用到。

3. **函数：** 熟悉如何定义和调用函数。算法通常被封装为函数，因此需要了解如何传递参数和返回值。

4. **二分查找：** 了解二分查找算法的工作原理，因为这是该问题的关键部分。

**Python 版本：**

1. **列表：** Python 中的列表是动态数组，因此需要知道如何声明、初始化和操作列表。

2. **循环和条件语句：** 了解 Python 中的 `for` 循环和 `if` 条件语句的使用方法，因为它们在算法实现中经常用到。

3. **类和对象：** Python 是一门面向对象的编程语言，了解如何定义类和对象是很有用的，尤其是对于面向对象的编程问题。

4. **二分查找：** 理解二分查找算法的工作原理，因为这是解决问题的核心算法。

**Java 版本：**

1. **数组和列表：** Java 中有数组和 ArrayList 这两种数据结构，需要了解如何声明、初始化和操作它们。

2. **循环和条件语句：** 了解 Java 中的 `for` 循环和 `if` 条件语句的用法，因为它们在算法实现中经常用到。

3. **类和对象：** Java 是一门面向对象的编程语言，需要了解如何定义类和对象，尤其是对于面向对象的编程问题。

4. **二分查找：** 了解二分查找算法的工作原理，因为这是解决问题的核心算法。

**C++ 版本：**

1. **数组和向量：** C++ 中有数组和 vector 这两种数据结构，需要了解如何声明、初始化和操作它们。

2. **循环和条件语句：** 了解 C++ 中的 `for` 循环和 `if` 条件语句的用法，因为它们在算法实现中经常用到。

3. **类和对象：** C++ 是一门支持面向对象编程的语言，需要了解如何定义类和对象，尤其是对于面向对象的编程问题。

4. **二分查找：** 了解二分查找算法的工作原理，因为这是解决问题的核心算法。

总的来说，了解基本的编程概念，掌握循环、条件语句和数据结构的使用，以及理解特定算法的工作原理对解决算法问题非常重要。无论使用哪种编程语言，这些基本知识都是通用的。