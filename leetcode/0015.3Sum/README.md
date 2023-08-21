# [15. 3Sum](https://leetcode.com/problems/3sum/)

## 题目

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

```c
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

## 题目大意

给定一个数组，要求在这个数组中找出 3 个数之和为 0 的所有组合。

## 解题思路
**解题思路（Go 版本）：**
1. 对输入的数组进行排序，这样相同的数字会相邻排列。
2. 遍历数组，将当前元素作为三元组的第一个元素（`a`），将问题转化为在剩余数组中查找两个数之和等于 `-a` 的问题。
3. 使用双指针技巧，在剩余数组中查找满足条件的两个数，左指针从当前元素的下一个位置开始，右指针从数组末尾开始，逐步向中间移动。
4. 如果当前三个数的和为 0，则将这个三元组添加到结果中。同时，为了避免重复解，需要跳过重复的元素。
5. 移动左右指针，继续查找其他可能的解。

**解题思路（Python 版本）：**
1. 使用字典（`counts`）来记录每个数字的出现次数。
2. 对输入数组进行排序，然后遍历排序后的数组。
3. 对于每个数字，考虑三种情况：
   - 如果数字出现次数大于1，检查是否满足条件的三元组。
   - 如果数字是 0，检查是否满足条件的三元组。
   - 如果数字为负数，使用双指针技巧在剩余数组中查找满足条件的两个数。
4. 使用双指针技巧，左指针从当前数字的下一个位置开始，右指针从数组末尾开始，逐步向中间移动。
5. 如果找到满足条件的两个数，将这个三元组添加到结果中。为了避免重复解，需要跳过重复的元素。
6. 移动左右指针，继续查找其他可能的解。

**解题思路（Java 版本）：**
1. 对输入的数组进行排序，这样相同的数字会相邻排列。
2. 遍历数组，将当前元素作为三元组的第一个元素（`a`），将问题转化为在剩余数组中查找两个数之和等于 `-a` 的问题。
3. 使用双指针技巧，在剩余数组中查找满足条件的两个数，左指针从当前元素的下一个位置开始，右指针从数组末尾开始，逐步向中间移动。
4. 如果当前三个数的和为 0，则将这个三元组添加到结果中。同时，为了避免重复解，需要跳过重复的元素。
5. 移动左右指针，继续查找其他可能的解。

**解题思路（C++ 版本）：**
1. 对输入的数组进行排序，这样相同的数字会相邻排列。
2. 遍历数组，将当前元素作为三元组的第一个元素（`a`），将问题转化为在剩余数组中查找两个数之和等于 `-a` 的问题。
3. 使用双指针技巧，在剩余数组中查找满足条件的两个数，左指针从当前元素的下一个位置开始，右指针从数组末尾开始，逐步向中间移动。
4. 如果当前三个数的和为 0，则将这个三元组添加到结果中。同时，为了避免重复解，需要跳过重复的元素。
5. 移动左右指针，继续查找其他可能的解。

## 代码


## Go
```Go
func threeSum(nums []int) [][]int {
    var ans [][]int  // 存储结果的二维切片
    sort.Ints(nums)  // 对切片进行排序
    
    for i := 0; i < len(nums)-2; i++ {
        // 避免重复的情况
        if i > 0 && nums[i] == nums[i-1] {
            continue
        }
        
        target := -nums[i]  // 目标值，找到两个数使得它们的和等于目标值
        left := i + 1
        right := len(nums) - 1
        
        for left < right {
            sum := nums[left] + nums[right]
            
            if sum == target {
                ans = append(ans, []int{nums[i], nums[left], nums[right]})
                // 避免重复的情况
                for left < right && nums[left] == nums[left+1] {
                    left++
                }
                for left < right && nums[right] == nums[right-1] {
                    right--
                }
                left++
                right--
            } else if sum < target {
                left++
            } else {
                right--
            }
        }
    }
    
    return ans  // 返回结果二维切片
}

```
## Python
```Python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []  # 存储结果的列表
        counts = {}  # 用于记录每个数字出现次数的字典
        for i in nums:
            counts[i] = counts.get(i, 0) + 1  # 统计数字出现次数

        nums = sorted(counts)  # 对数字进行排序
        print(counts, nums)  # 打印数字出现次数和排序后的数字列表
        for i, num in enumerate(nums):
            if counts[num] > 1:  # 如果数字出现次数大于1
                if num == 0:
                    if counts[num] > 2:
                        ans.append([0, 0, 0])  # 若数字是0且出现次数大于2，添加[0, 0, 0]到结果列表
                        continue
                else:
                    if -num * 2 in counts:  # 如果两倍的负值在字典中存在
                        ans.append([num, num, -2 * num])  # 添加[num, num, -2*num]到结果列表
            if num < 0:
                two_sum = -num  # 计算需要找到的两个数的和
                # 在排序后的数字列表中寻找合适的数
                left = bisect.bisect_left(nums, (two_sum - nums[-1]), i + 1)
                # 寻找满足条件的 j 值，使得 num + j + k = 0
                for j in nums[left: bisect.bisect_right(nums, (two_sum // 2), left)]:
                    k = two_sum - j
                    if k in counts and k != j:
                        ans.append([num, j, k])  # 添加[num, j, k]到结果列表

        return ans  # 返回结果列表

```
## Java
```Java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();  // 存储结果的列表
        Arrays.sort(nums);  // 对数组进行排序
        
        for (int i = 0; i < nums.length - 2; i++) {
            // 避免重复的情况
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            
            int target = -nums[i];  // 目标值，找到两个数使得它们的和等于目标值
            int left = i + 1;
            int right = nums.length - 1;
            
            while (left < right) {
                int sum = nums[left] + nums[right];
                
                if (sum == target) {
                    ans.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    // 避免重复的情况
                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                    }
                    while (left < right && nums[right] == nums[right - 1]) {
                        right--;
                    }
                    left++;
                    right--;
                } else if (sum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        
        return ans;  // 返回结果列表
    }
}

```
## Cpp
```Cpp
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;  // 存储结果的二维向量
        sort(nums.begin(), nums.end());  // 对数组进行排序
        
        for (int i = 0; i < nums.size() - 2; i++) {
            // 避免重复的情况
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            
            int target = -nums[i];  // 目标值，找到两个数使得它们的和等于目标值
            int left = i + 1;
            int right = nums.size() - 1;
            
            while (left < right) {
                int sum = nums[left] + nums[right];
                
                if (sum == target) {
                    ans.push_back({nums[i], nums[left], nums[right]});
                    // 避免重复的情况
                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                    }
                    while (left < right && nums[right] == nums[right - 1]) {
                        right--;
                    }
                    left++;
                    right--;
                } else if (sum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        
        return ans;  // 返回结果二维向量
    }
};

```
所需要掌握的基础知识。

**Go 版本：**

1. **切片（Slice）：** 在 Go 中，切片是动态数组，是一种常见的数据结构。你需要了解如何创建切片、访问切片元素、切片的长度和容量等基本操作。

2. **排序（Sorting）：** Go 提供了排序函数 `sort.Ints` 来对整数切片进行排序。了解如何使用排序函数对切片进行排序。

3. **循环和条件语句：** 掌握 Go 中的 `for` 循环和 `if` 条件语句，以及如何在循环中使用 `continue` 和 `break`。

4. **切片的添加元素：** 学习如何使用 `append` 函数在切片末尾添加元素。

5. **双指针技巧：** 了解如何使用双指针技巧来解决查找问题，例如在本问题中的左右指针用法。

**Python 版本：**

1. **列表（List）：** 在 Python 中，列表是一种动态数组。你需要了解如何创建列表、访问列表元素、列表的方法和属性等。

2. **字典（Dictionary）：** 字典是键值对的集合，类似于其他编程语言中的哈希表或映射。了解如何使用字典存储数字出现次数。

3. **排序：** 学习如何使用内置函数 `sorted` 对列表进行排序。

4. **循环和条件语句：** 掌握在 Python 中的 `for` 循环和 `if` 条件语句，以及如何在循环中使用 `continue` 和 `break`。

5. **双指针技巧：** 学习如何使用双指针技巧来解决问题，例如在本问题中的左右指针用法。

**Java 版本：**

1. **数组（Array）：** 了解如何创建数组、访问数组元素以及数组的属性。

2. **排序：** 掌握如何使用 Java 中的 `Arrays.sort` 方法对数组进行排序。

3. **循环和条件语句：** 学习在 Java 中的 `for` 循环和 `if` 条件语句，以及如何使用 `break` 和 `continue` 控制循环。

4. **列表（List）：** Java 中的 `List` 是一种常见的数据结构，类似于动态数组。了解如何使用 `List` 存储数据。

5. **双指针技巧：** 掌握在 Java 中如何使用双指针技巧来解决问题，例如在本问题中的左右指针用法。

**C++ 版本：**

1. **向量（Vector）：** C++ 中的 `vector` 类似于其他编程语言中的动态数组。了解如何创建向量、访问向量元素以及向量的方法。

2. **排序：** 学习如何使用 `sort` 函数对向量进行排序。

3. **循环和条件语句：** 掌握在 C++ 中的 `for` 循环和 `if` 条件语句，以及如何使用 `break` 和 `continue` 控制循环。

4. **向量的添加元素：** 了解如何使用 `push_back` 函数在向量末尾添加元素。

5. **双指针技巧：** 学习如何使用双指针技巧来解决问题，例如在本问题中的左右指针用法。


