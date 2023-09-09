# [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)


## 题目

Given an array of integers `nums` sorted in ascending order, find the starting and ending position of a given `target` value.

Your algorithm's runtime complexity must be in the order of *O*(log *n*).

If the target is not found in the array, return `[-1, -1]`.

**Example 1:**

    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]

**Example 2:**

    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]

## 题目大意

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。你的算法时间复杂度必须是 O(log n) 级别。如果数组中不存在目标值，返回 [-1, -1]。


## 解题思路


Go 版本的解题思路：

1. 首先，初始化两个指针 `l_ptr` 和 `r_ptr`，它们分别指向数组的起始位置和结束位置。

2. 初始化一个整数切片 `ans`，用于存储目标值的范围，初始值为 `[-1, -1]`。

3. 使用二分搜索的思想，在循环中不断缩小搜索范围，直到找到目标值的范围或确定目标值不存在。

4. 在每次迭代中，计算中间位置的索引 `mid`。

5. 如果中间位置的元素等于目标值，则更新 `ans[0]` 和 `ans[1]` 为 `mid`。然后，通过循环向左和向右扩展，找到目标值的第一个和最后一个位置。

6. 如果中间位置的元素大于目标值，则将右指针 `r_ptr` 移动到 `mid - 1`，以缩小搜索范围到左半部分。

7. 如果中间位置的元素小于目标值，则将左指针 `l_ptr` 移动到 `mid + 1`，以缩小搜索范围到右半部分。

8. 最终，返回包含目标值范围的 `ans` 数组。

Python 版本的解题思路：

Python 版本的解题思路与 Go 版本类似，但使用了函数和模块的结构来组织代码：

1. 首先，定义了两个辅助函数 `find_left` 和 `find_right`，它们分别用于查找目标值的左边界和右边界。

2. 在主函数 `searchRange` 中，初始化两个整数，用于存储目标值的左边界和右边界。这些值是通过调用辅助函数来找到的。

3. 辅助函数 `find_left` 和 `find_right` 采用二分搜索的思想，不断缩小搜索范围，直到找到目标值的边界或确定目标值不存在。

4. 当找到左边界时，继续向右搜索，找到右边界。

5. 最终，返回包含目标值范围的结果列表。

Java 版本的解题思路：

Java 版本的解题思路与 Go 版本类似，但使用了类和方法的结构来组织代码：

1. 在 `Solution` 类中，定义了一个方法 `searchRange` 来解决问题。

2. 在 `searchRange` 方法中，初始化两个整数，用于存储目标值的左边界和右边界。

3. 使用 `while` 循环，在循环中不断缩小搜索范围，直到找到目标值的范围或确定目标值不存在。

4. 在每次迭代中，计算中间位置的索引 `mid`。

5. 如果中间位置的元素等于目标值，则更新左边界和右边界，然后通过循环向左和向右扩展，找到目标值的第一个和最后一个位置。

6. 如果中间位置的元素大于目标值，则缩小搜索范围到左半部分，将右指针 `r_ptr` 移动到 `mid - 1`。

7. 如果中间位置的元素小于目标值，则缩小搜索范围到右半部分，将左指针 `l_ptr` 移动到 `mid + 1`。

8. 最终，返回包含目标值范围的整数数组。

C++ 版本的解题思路：

C++ 版本的解题思路与 Java 版本类似，但使用了类和方法的结构来组织代码：

1. 在 `Solution` 类中，定义了一个方法 `searchRange` 来解决问题。

2. 在 `searchRange` 方法中，初始化两个整数，用于存储目标值的左边界和右边界。

3. 使用 `while` 循环，在循环中不断缩小搜索范围，直到找到目标值的范围或确定目标值不存在。

4. 在每次迭代中，计算中间位置的索引 `mid`。

5. 如果中间位置的元素等于目标值，则更新左边界和右边界，然后通过循环向左和向右扩展，找到目标值的第一个和最后一个位置。

6. 如果中间位置的元素大于目标值，则缩小搜索范围到左半部分，将右指针 `r_ptr` 移动到 `mid - 1`。

7. 如果中间位置的元素小于目标值，则缩小搜索范围到右半部分，将左指针 `l_ptr` 移动到 `mid`。

8. 最终，返回包含目标值范围的整数数组。

这些是每个版本的解题思路的详细说明，希望这能帮助您更好地理解每个解决方案的工作原理。如果您有任何进一步的问题，请随时提问。
## 代码

## Go

```Go
func searchRange(nums []int, target int) []int {
    // 获取数组的长度
    n := len(nums)
    // 初始化左指针为 0
    l_prt := 0
    // 初始化右指针为数组长度减一
    r_prt := n - 1
    
    // 初始化答案数组，用于存储目标值的范围
    ans := []int{-1, -1}  
    
    // 在左指针小于等于右指针的条件下进行循环
    for l_prt <= r_prt {
        // 计算中间位置的索引
        mid := ((r_prt - l_prt) >> 1) + l_prt
        
        // 如果中间位置的元素等于目标值
        if nums[mid] == target {
            // 更新答案的左边界和右边界为中间位置
            ans[0] = mid
            ans[1] = mid
            
            // 从中间位置向左扩展，找到目标值的第一个位置
            for ans[0] > 0 && nums[ans[0]-1] == target {
                ans[0]--
            }
            
            // 从中间位置向右扩展，找到目标值的最后一个位置
            for ans[1] < n - 1 && nums[ans[1] + 1] == target {
                ans[1]++
            }
            
            // 跳出循环，因为已经找到了目标值的范围
            break
        } else if nums[mid] > target {
            // 如果中间位置的元素大于目标值，缩小搜索范围到左半部分
            r_prt = mid - 1
        } else {
            // 如果中间位置的元素小于目标值，缩小搜索范围到右半部分
            l_prt = mid + 1
        }
    }
    
    // 返回包含目标值范围的答案数组
    return ans
}

```

## Python

```Python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 辅助函数：查找目标值的左边界
        def find_left():
            start, end = 0, len(nums) - 1
            res = -1  # 初始化结果为-1，表示未找到
            while start <= end:
                mid = (start + end) // 2  # 计算中间位置的索引
                
                if nums[mid] < target:
                    start = mid + 1  # 如果中间值小于目标值，缩小搜索范围到右半部分
                
                elif nums[mid] > target:
                    end = mid - 1  # 如果中间值大于目标值，缩小搜索范围到左半部分
                
                else:
                    res = mid  # 找到目标值，更新结果为当前位置
                    end = mid - 1  # 继续向左搜索更左边的位置
            return res
        
        # 辅助函数：查找目标值的右边界
        def find_right():
            start, end = 0, len(nums) - 1
            res = -1  # 初始化结果为-1，表示未找到
            while start <= end:
                mid = (start + end) // 2  # 计算中间位置的索引
                
                if nums[mid] < target:
                    start = mid + 1  # 如果中间值小于目标值，缩小搜索范围到右半部分
                
                elif nums[mid] > target:
                    end = mid - 1  # 如果中间值大于目标值，缩小搜索范围到左半部分
                
                else:
                    res = mid  # 找到目标值，更新结果为当前位置
                    start = mid + 1  # 继续向右搜索更右边的位置
            return res
        
        # 返回包含目标值范围的结果数组，左边界和右边界分别由辅助函数找到
        return [find_left(), find_right()]

```

## Java

```Java
class Solution {
    public int[] searchRange(int[] nums, int target) {
        // 获取数组的长度
        int n = nums.length;
        // 初始化左指针为0
        int l_ptr = 0;
        // 初始化右指针为数组长度减一
        int r_ptr = n - 1;
        
        // 初始化答案数组，用于存储目标值的范围
        int[] ans = {-1, -1};
        
        // 在左指针小于等于右指针的条件下进行循环
        while (l_ptr <= r_ptr) {
            // 计算中间位置的索引
            int mid = (r_ptr - l_ptr) / 2 + l_ptr;
            
            // 如果中间位置的元素等于目标值
            if (nums[mid] == target) {
                // 更新答案的左边界和右边界为中间位置
                ans[0] = mid;
                ans[1] = mid;
                
                // 从中间位置向左扩展，找到目标值的第一个位置
                while (ans[0] > 0 && nums[ans[0] - 1] == target) {
                    ans[0]--;
                }
                
                // 从中间位置向右扩展，找到目标值的最后一个位置
                while (ans[1] < n - 1 && nums[ans[1] + 1] == target) {
                    ans[1]++;
                }
                
                // 跳出循环，因为已经找到了目标值的范围
                break;
            } else if (nums[mid] > target) {
                // 如果中间位置的元素大于目标值，缩小搜索范围到左半部分
                r_ptr = mid - 1;
            } else {
                // 如果中间位置的元素小于目标值，缩小搜索范围到右半部分
                l_ptr = mid + 1;
            }
        }
        
        // 返回包含目标值范围的答案数组
        return ans;
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int ret;  // 用于存储目标值的起始位置
        int l = 0, r = nums.size() - 1;  // 初始化左右指针，表示搜索范围
        
        // 第一个循环：查找目标值的起始位置
        while (l < r) {
            int mid = (l + r) / 2;  // 计算中间位置的索引
            if (nums[mid] < target) {
                l = mid + 1;  // 如果中间值小于目标值，缩小搜索范围到右半部分
            } else {
                r = mid;  // 否则，缩小搜索范围到左半部分
            }
        }
        
        // 如果找到的位置超出数组范围或者该位置的值不等于目标值，返回{-1, -1}
        if (l == nums.size() || nums[l] != target) {
            return {-1, -1};
        }
        
        ret = l;  // 记录目标值的起始位置
        
        l = 0;
        r = nums.size() - 1;
        
        // 第二个循环：查找目标值的结束位置
        while (l < r) {
            int mid = (l + r + 1) / 2;  // 计算中间位置的索引
            if (nums[mid] > target) {
                r = mid - 1;  // 如果中间值大于目标值，缩小搜索范围到左半部分
            } else {
                l = mid;  // 否则，缩小搜索范围到右半部分
            }
        }
        
        // 返回包含目标值范围的结果数组，包括起始位置和结束位置
        return {ret, l};
    }
};

```
每个版本的所需基础知识：

Go 版本的基础知识：

1. **切片（Slices）**：Go 语言中的切片是动态数组，非常常用于处理数组数据。在这个解决方案中，`nums` 是一个整数切片，而 `ans` 也是一个整数切片，用于存储目标值的范围。

2. **循环和条件语句**：解决方案中使用了 `for` 循环和 `if` 条件语句来实现逻辑控制，例如，在二分搜索中不断缩小搜索范围。

3. **二分搜索**：这个问题的关键是使用二分搜索算法。需要了解二分搜索的基本原理，即通过比较中间元素与目标值的大小，将搜索范围缩小一半，直到找到目标或确定目标不存在。

Python 版本的基础知识：

1. **列表（Lists）**：Python 中的列表类似于数组，用于存储一组元素。在这个解决方案中，`nums` 是一个整数列表，而 `ans` 也是一个整数列表，用于存储目标值的范围。

2. **函数和模块**：解决方案中定义了两个辅助函数 `find_left` 和 `find_right`，并使用了函数来组织代码。还需要了解 Python 模块的概念，例如 `List` 类型在 `typing` 模块中的导入。

3. **循环和条件语句**：与 Go 版本一样，Python 版本也使用了 `for` 循环和 `if` 条件语句来实现逻辑控制。

4. **二分搜索**：同样需要了解二分搜索的基本原理和实现方式。

Java 版本的基础知识：

1. **数组**：Java 使用数组来存储一组元素。在这个解决方案中，`nums` 是一个整数数组，而 `ans` 也是一个整数数组，用于存储目标值的范围。

2. **类和方法**：Java 版本使用了一个类 `Solution`，其中包含一个方法 `searchRange` 来解决问题。需要了解如何定义类和方法，并调用它们。

3. **循环和条件语句**：与其他版本一样，Java 版本也使用了 `while` 循环和 `if` 条件语句来实现逻辑控制。

4. **二分搜索**：了解二分搜索的基本原理和实现方式。

C++ 版本的基础知识：

1. **向量（Vectors）**：C++ 中的向量类似于动态数组，用于存储一组元素。在这个解决方案中，`nums` 是一个整数向量，而 `ans` 也是一个整数向量，用于存储目标值的范围。

2. **类和方法**：与 Java 版本一样，C++ 版本也使用了一个类 `Solution`，其中包含一个方法 `searchRange` 来解决问题。需要了解如何定义类和方法，并调用它们。

3. **循环和条件语句**：与其他版本一样，C++ 版本也使用了 `while` 循环和 `if` 条件语句来实现逻辑控制。

4. **二分搜索**：了解二分搜索的基本原理和实现方式。

