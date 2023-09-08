# [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

## 题目

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`).

You are given a target value to search. If found in the array return its index, otherwise return `-1`.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of *O*(log *n*).

**Example 1:**

    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

**Example 2:**

    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1


## 题目大意

假设按照升序排序的数组在预先未知的某个点上进行了旋转。( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。


## 解题思路

下面将分别介绍每个版本的解题思路：

Go 版本解题思路：

1. 初始化两个指针 `low` 和 `high`，分别指向数组的开头和结尾。
2. 使用二分查找的循环来搜索目标值。
3. 在每次迭代中，计算中间元素的索引 `mid`。
4. 检查中间元素与目标值的关系：
   - 如果中间元素等于目标值，则直接返回中间元素的索引。
   - 如果中间元素大于最左边的元素（说明左半段是有序的），则比较目标值与中间元素的大小关系：
     - 如果目标值大于中间元素且小于等于最右边的元素，说明目标值在右半段有序部分，更新 `low = mid + 1`。
     - 否则，目标值在左半段无序部分，更新 `high = mid - 1`。
   - 如果中间元素小于等于最右边的元素（说明右半段是有序的），则比较目标值与中间元素的大小关系：
     - 如果目标值大于中间元素且小于等于最右边的元素，说明目标值在右半段有序部分，更新 `low = mid + 1`。
     - 否则，目标值在左半段无序部分，更新 `high = mid - 1`。
   - 如果中间元素与最左边的元素相等，说明可能存在重复元素，可以将最左边的指针 `low` 向右移动一位。
   - 如果中间元素与最右边的元素相等，说明可能存在重复元素，可以将最右边的指针 `high` 向左移动一位。
5. 重复步骤 3 和步骤 4，直到 `low` 大于 `high`，此时未找到目标值，返回 -1。

Python 版本解题思路：

1. 初始化两个指针 `low` 和 `high`，分别指向数组的开头和结尾。
2. 使用二分查找的循环来搜索目标值。
3. 在每次迭代中，计算中间元素的索引 `mid`。
4. 检查中间元素与目标值的关系：
   - 如果中间元素等于目标值，则直接返回中间元素的索引。
   - 如果中间元素大于最左边的元素（说明左半段是有序的），则比较目标值与中间元素的大小关系：
     - 如果目标值大于中间元素且小于等于最右边的元素，说明目标值在右半段有序部分，更新 `low = mid + 1`。
     - 否则，目标值在左半段无序部分，更新 `high = mid - 1`。
   - 如果中间元素小于等于最右边的元素（说明右半段是有序的），则比较目标值与中间元素的大小关系：
     - 如果目标值大于中间元素且小于等于最右边的元素，说明目标值在右半段有序部分，更新 `low = mid + 1`。
     - 否则，目标值在左半段无序部分，更新 `high = mid - 1`。
   - 如果中间元素与最左边的元素相等，说明可能存在重复元素，可以将最左边的指针 `low` 向右移动一位。
   - 如果中间元素与最右边的元素相等，说明可能存在重复元素，可以将最右边的指针 `high` 向左移动一位。
5. 重复步骤 3 和步骤 4，直到 `low` 大于 `high`，此时未找到目标值，返回 -1。

Java 版本解题思路：

1. 初始化两个指针 `low` 和 `high`，分别指向数组的开头和结尾。
2. 使用二分查找的循环来搜索目标值。
3. 在每次迭代中，计算中间元素的索引 `mid`。
4. 检查中间元素与目标值的关系：
   - 如果中间元素等于目标值，则直接返回中间元素的索引。
   - 如果中间元素大于最左边的元素（说明左半段是有序的），则比较目标值与中间元素的大小关系：
     - 如果目标值大于中间元素且小于等于最右边的元素，说明目标值在右半段有序部分，更新 `low = mid + 1`。
     - 否则，目标值在左半段无序部分，更新 `high = mid - 1`。
   - 如果中间元素小于等于最右边的元素（说明右半段是有序的），则比较目标值与中间元素的大小关系：
     - 如果目标值大于中间元素且小于等于最右边的元素，说明目标值在右半段有序部分，更新 `low = mid + 1`。
     - 否则，目标值在左半段无序部分，更新 `high = mid - 1`。
   - 如果中间元素与最左边的元素相等，说明可能存在重复元素，可以将最左边的指针 `low` 向右移动一位。
   - 如果中间元素与最右边的元素相等，说明可能存在重复元素，可以将最右边的指针 `high` 向左移动一位。
5. 重复步骤 3 和步骤 4，直到 `low` 大于 `high`，此时未找到目标值，返回 -1。

C++ 版本解题思路：

1. 初始化两个指针 `low` 和 `high`，分别指向数组的开头和结尾。
2. 使用二分查找的循环来搜索目标值。
3. 在每次迭代中，计算中间元素的索引 `mid`。
4. 检查中间元素与目标值的关系：
   - 如果中间元素等于目标值，则直接返回中间元素的索引。
   - 如果中间元素大于最左边的元素（说明左半段是有序的），则比较目标值与中间元素的大小关系：
     - 如果目标值大于中间元素且小于等于最右边的元素，说明目标值在右半段有序部分，更新 `low = mid + 1`。
     - 否则，目标值在左半段无序部分，更新 `high = mid - 1`。
   - 如果中间元素小于等于最右边的元素（说明右半段是有序的），则比较目标值与中间元素的大小关系：
     - 如果目标值大于中间元素且小于等于最右边的元素，说明目标值在右半段有序部分，更新 `low = mid + 1`。
     - 否则，目标值在左半段无序部分，更新 `high = mid - 1`。
   - 如果中间元素与最左边的元素相等，说明可能存在重复元素，可以将最左边的指针 `low` 向右移动一位。
   - 如果中间元素与最右边的元素相等，说明可能存在重复元素，可以将最右边的指针 `high` 向左移动一位。
5. 重复步骤 3 和步骤 4，直到 `low` 大于 `high`，此时未找到目标值，返回 -1。

这四个版本的解题思路基本一致，都是使用二分查找的变种来在旋转有序数组中搜索目标值，关键是正确处理不同情况下指针的更新以及边界条件的处理。算法的时间复杂度是 O(log n)，因为每次迭代都将搜索范围减半。不同版本的代码实现方式有所不同，但核心逻辑相似。
## 代码

## Go

```Go
func search(nums []int, target int) int {
    // 检查数组是否为空，如果是空数组则直接返回-1
    if len(nums) == 0 {
        return -1
    }
    // 初始化两个指针，分别指向数组的开头和结尾
    low, high := 0, len(nums)-1
    // 使用二分查找的循环来搜索目标值
    for low <= high {
        // 计算中间元素的索引
        mid := low + (high-low)>>1
        // 如果中间元素等于目标值，则直接返回中间元素的索引
        if nums[mid] == target {
            return mid
        } else if nums[mid] > nums[low] { // 如果中间元素在数值大的一部分区间里
            // 检查目标值是否在左半部分区间内，如果是则更新高指针
            if nums[low] <= target && target < nums[mid] {
                high = mid - 1
            } else {
                // 否则更新低指针
                low = mid + 1
            }
        } else if nums[mid] < nums[high] { // 如果中间元素在数值小的一部分区间里
            // 检查目标值是否在右半部分区间内，如果是则更新低指针
            if nums[mid] < target && target <= nums[high] {
                low = mid + 1
            } else {
                // 否则更新高指针
                high = mid - 1
            }
        } else {
            // 处理中间元素等于边界元素的情况，移动边界指针以去除重复元素
            if nums[low] == nums[mid] {
                low++
            }
            if nums[high] == nums[mid] {
                high--
            }
        }
    }
    // 如果未找到目标值，则返回-1
    return -1
}

```

## Python

```Python
class Solution:
    def search(self, nums, target: int):
        # 如果数组为空，直接返回-1
        if len(nums) == 0:
            return -1
        # 如果数组只有一个元素，分两种情况判断
        elif len(nums) == 1:
            if nums[0] != target:
                return -1
            else:
                return 0
        
        # 找到旋转点的位置
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                flag = i + 1
                break
        
        # 在旋转点左边进行二分查找
        left = self.binary_search(nums, target, 0, flag - 1)
        if left != -1:
            return left
        else:
            # 如果左边没有找到，就在旋转点右边进行二分查找
            right = self.binary_search(nums, target, flag, len(nums) - 1)
            if right == -1:
                return -1
            else:
                return right
    
    def binary_search(self, nums, target, left, right):
        l, r = left, right
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1

```

## Java

```Java
class Solution {
    public int search(int[] nums, int target) {
        if (nums == null || nums.length == 0) {
            return -1;
        }
        
        int low = 0, high = nums.length - 1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (nums[mid] == target) {
                return mid;
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
        
        return -1;
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    int search(vector<int>& nums, int target) {
        if (nums.empty()) {
            return -1;
        }
        
        int low = 0, high = nums.size() - 1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (nums[mid] == target) {
                return mid;
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
        
        return -1;
    }
};

```
当用不同编程语言实现算法时，需要掌握以下基础知识：

Go 版本：

1. **函数定义与调用**：了解如何定义和调用函数，包括函数的参数和返回值。

2. **数组与切片**：Go 中没有传统的数组，而是使用切片来处理动态数组。需要了解如何声明、初始化和操作切片。

3. **循环与条件语句**：了解如何使用 `for` 和 `if` 语句来实现循环和条件判断。

4. **二分查找**：理解二分查找的原理和实现方法，包括如何计算中间元素的索引和更新指针。

5. **算法复杂度**：理解算法复杂度的概念，包括时间复杂度和空间复杂度，并了解如何分析算法的性能。

Python 版本：

1. **类和方法**：了解如何定义类和类方法，并如何创建类的实例。

2. **列表**：Python 中的列表类似于动态数组，需要了解如何声明、初始化和操作列表。

3. **循环与条件语句**：了解如何使用 `for` 和 `if` 语句来实现循环和条件判断。

4. **二分查找**：理解二分查找的原理和实现方法，包括如何计算中间元素的索引和更新指针。

5. **函数递归**：理解函数递归的概念，以及如何在递归中解决问题。

Java 版本：

1. **类和方法**：了解如何定义类和类方法，并如何创建类的实例。

2. **数组**：Java 中有静态数组，需要了解如何声明、初始化和操作数组。

3. **循环与条件语句**：了解如何使用 `for` 和 `if` 语句来实现循环和条件判断。

4. **二分查找**：理解二分查找的原理和实现方法，包括如何计算中间元素的索引和更新指针。

5. **算法复杂度**：理解算法复杂度的概念，包括时间复杂度和空间复杂度，并了解如何分析算法的性能。

C++ 版本：

1. **类和方法**：了解如何定义类和类方法，并如何创建类的实例。

2. **向量**：C++ 中的向量类似于动态数组，需要了解如何声明、初始化和操作向量。

3. **循环与条件语句**：了解如何使用 `for` 和 `if` 语句来实现循环和条件判断。

4. **二分查找**：理解二分查找的原理和实现方法，包括如何计算中间元素的索引和更新指针。

5. **算法复杂度**：理解算法复杂度的概念，包括时间复杂度和空间复杂度，并了解如何分析算法的性能。

以上是实现搜索旋转排序数组算法所需要掌握的基础知识，包括语言特性、数据结构操作、循环和条件判断、二分查找算法和算法复杂度分析等方面的知识。不同编程语言有不同的语法和库函数，但核心的算法思想和逻辑都是相似的。