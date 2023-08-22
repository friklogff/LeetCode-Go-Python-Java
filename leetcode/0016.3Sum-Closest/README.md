# [16. 3Sum Closest](https://leetcode.com/problems/3sum-closest/)

## 题目

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

```c
Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```

## 题目大意

给定一个数组，要求在这个数组中找出 3 个数之和离 target 最近。

## 解题思路

当然，我可以为您逐个介绍每个版本的解题思路。以下是对每个版本的解释：

**Go 版本解题思路：**

1. 首先，获取数组的长度，然后对数组进行升序排序，以便于后续的双指针法查找。

2. 初始化一个最小差值 `minDiff` 为整型最大值，并定义一个变量 `ans` 来存储最接近目标的和。

3. 使用循环遍历数组，从第一个元素到倒数第三个元素。在循环中，检查是否需要跳过重复的元素。

4. 尝试以当前元素为基准，计算三个元素的和 `sum`，分情况讨论：
   - 如果 `sum` 大于目标值 `target`，判断差值是否更小，若是则更新 `ans`。
   - 如果 `sum` 小于目标值 `target`，判断差值是否更小，若是则更新 `minDiff`。

5. 如果 `sum` 小于目标值 `target`，使用双指针法在剩余区间内查找最接近目标值的和：
   - 初始化左指针 `j` 为当前元素的下一个元素，右指针 `k` 为数组末尾元素。
   - 在循环中，计算当前和 `sum`，若和等于目标值，直接返回目标值。
   - 若和大于目标值，根据差值是否更小，更新 `ans` 和 `minDiff`，然后左指针右移。
   - 若和小于目标值，根据差值是否更小，更新 `ans` 和 `minDiff`，然后右指针左移。

6. 最后，返回存储最接近目标的和 `ans`。

**Python 版解题思路：**

Python 版本的思路与 Go 版本类似，只是使用了 Python 特有的列表和内置函数，具体如下：

1. 获取列表的长度，然后对列表进行升序排序。

2. 初始化一个最小差值 `minDiff` 为正无穷大，并定义一个变量 `closestSum` 来存储最接近目标的和。

3. 使用循环遍历列表，从第一个元素到倒数第三个元素。在循环中，检查是否需要跳过重复的元素。

4. 尝试以当前元素为基准，计算三个元素的和 `sum_`，分情况讨论：
   - 如果 `sum_` 大于目标值 `target`，判断差值是否更小，若是则更新 `closestSum`。
   - 如果 `sum_` 小于目标值 `target`，判断差值是否更小，若是则更新 `minDiff`。

5. 如果 `sum_` 小于目标值 `target`，使用双指针法在剩余区间内查找最接近目标值的和：
   - 初始化左指针 `j` 为当前元素的下一个元素，右指针 `k` 为列表末尾元素。
   - 在循环中，计算当前和 `sum_`，若和等于目标值，直接返回目标值。
   - 若和大于目标值，根据差值是否更小，更新 `closestSum` 和 `minDiff`，然后右指针左移。
   - 若和小于目标值，根据差值是否更小，更新 `closestSum` 和 `minDiff`，然后左指针右移。

6. 最后，返回存储最接近目标的和 `closestSum`。

**Java 版解题思路：**

Java 版本的解题思路与其他版本类似，同样使用了双指针法和数组，具体如下：

1. 获取数组的长度，然后对数组进行升序排序。

2. 初始化一个最小差值 `minDiff` 为整型最大值，并定义一个变量 `closestSum` 来存储最接近目标的和。

3. 使用循环遍历数组，从第一个元素到倒数第三个元素。在循环中，检查是否需要跳过重复的元素。

4. 尝试以当前元素为基准，计算三个元素的和 `sum`，分情况讨论：
   - 如果 `sum` 大于目标值 `target`，判断差值是否更小，若是则更新 `closestSum`。
   - 如果 `sum` 小于目标值 `target`，判断差值是否更小，若是则更新 `minDiff`。

5. 如果 `sum` 小于目标值 `target`，使用双指针法在剩余区间内查找最接近目标值的和：
   - 初始化左指针 `j` 为当前元素的下一个元素，右指针 `k` 为数组末尾元素。
   - 在循环中，计算当前和 `sum`，若和等于目标值，直接返回目标值。
   - 若和大于目标值，根据差值是否更小，更新 `closestSum` 和 `minDiff`，然后右指针左移。
   - 若和小于目标值，根据差值是否更小，更新 `closestSum` 和 `minDiff`，然后左指针右移。

6. 最后，返回存储最接近目标的和 `closestSum`。


**C++ 版解题思路：**

C++ 版本的解题思路与其他版本类似，同样使用了双指针法和向量（vector），具体如下：

1. 获取向量的长度，然后对向量进行升序排序。

2. 初始化一个最小差值 `minDiff` 为整型最大值，并定义一个变量 `closestSum` 来存储最接近目标的和。

3. 使用循环遍历向量，从第一个元素到倒数第三个元素。在循环中，检查是否需要跳过重复的元素。

4. 尝试以当前元素为基准，计算三个元素的和 `sum`，分情况讨论：
   - 如果 `sum` 大于目标值 `target`，判断差值是否更小，若是则更新 `closestSum`。
   - 如果 `sum` 小于目标值 `target`，判断差值是否更小，若是则更新 `minDiff`。

5. 如果 `sum` 小于目标值 `target`，使用双指针法在剩余区间内查找最接近目标值的和：
   - 初始化左指针 `j` 为当前元素的下一个元素，右指针 `k` 为向量末尾元素。
   - 在循环中，计算当前和 `sum`，若和等于目标值，直接返回目标值。
   - 若和大于目标值，根据差值是否更小，更新 `closestSum` 和 `minDiff`，然后右指针左移。
   - 若和小于目标值，根据差值是否更小，更新 `closestSum` 和 `minDiff`，然后左指针右移。

6. 最后，返回存储最接近目标的和 `closestSum`。

## 代码
## Go
```Go
func threeSumClosest(nums []int, target int) int {
    n := len(nums)             // 获取数组长度
    sort.Ints(nums)            // 对数组进行升序排序
    minDiff := math.MaxInt     // 初始化最小差值为整型最大值
    var ans int                // 用于存储最接近目标的和

    for i := 0; i < n-2; i++ { // 遍历数组，从第一个元素到倒数第三个元素
        if i > 0 && nums[i] == nums[i-1] {
            // 跳过重复的元素，避免重复计算
            continue
        }

        // 尝试以当前元素为基准，计算三个元素的和
        sum := nums[i] + nums[i+1] + nums[i+2]

        if sum > target {
            // 如果和大于目标值，判断差值是否更小，若是则更新结果
            if sum - target < minDiff {
                ans = sum
            }
            break  // 由于数组已经排序，之后的和会更大，不必再继续遍历
        }

        // 尝试以当前元素为基准，和最大的两个元素相加
        sum = nums[i] + nums[n-2] + nums[n-1]

        if sum < target {
            // 如果和小于目标值，判断差值是否更小，若是则更新结果
            if target - sum < minDiff {
                minDiff = target - sum
                ans = sum
            }
            continue  // 继续尝试更大的和
        }

        // 使用双指针法在剩余区间内查找最接近目标值的和
        j, k := i+1, n-1
        for j < k {
            sum = nums[i] + nums[j] + nums[k]
            if sum == target {
                // 如果和等于目标值，直接返回
                return target
            }
            if sum > target {
                // 如果和大于目标值，判断差值是否更小，若是则更新结果
                if sum - target < minDiff {
                    minDiff = sum - target
                    ans = sum
                }
                k--  // 缩小右侧指针的范围
            } else {
                // 如果和小于目标值，判断差值是否更小，若是则更新结果
                if target - sum < minDiff {
                    minDiff = target - sum
                    ans = sum
                }
                j++  // 增大左侧指针的范围
            }
        }
    }
    return ans  // 返回最接近目标值的和
}

```
## Python
```Python
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)                   # 获取数组长度
        nums.sort()                     # 对数组进行升序排序
        minDiff = float('inf')          # 初始化最小差值为正无穷大
        closestSum = 0                  # 用于存储最接近目标的和

        for i in range(n - 2):          # 遍历数组，从第一个元素到倒数第三个元素
            if i > 0 and nums[i] == nums[i - 1]:
                # 跳过重复的元素，避免重复计算
                continue

            sum_ = nums[i] + nums[i + 1] + nums[i + 2]

            if sum_ > target:
                # 如果和大于目标值，判断差值是否更小，若是则更新结果
                if sum_ - target < minDiff:
                    closestSum = sum_
                    minDiff = sum_ - target
                break   # 由于数组已经排序，之后的和会更大，不必再继续遍历

            sum_ = nums[i] + nums[n - 2] + nums[n - 1]

            if sum_ < target:
                # 如果和小于目标值，判断差值是否更小，若是则更新结果
                if target - sum_ < minDiff:
                    closestSum = sum_
                    minDiff = target - sum_
                continue    # 继续尝试更大的和

            j, k = i + 1, n - 1
            while j < k:
                sum_ = nums[i] + nums[j] + nums[k]
                if sum_ == target:
                    # 如果和等于目标值，直接返回
                    return target
                if sum_ > target:
                    # 如果和大于目标值，判断差值是否更小，若是则更新结果
                    if sum_ - target < minDiff:
                        closestSum = sum_
                        minDiff = sum_ - target
                    k -= 1  # 缩小右侧指针的范围
                else:
                    # 如果和小于目标值，判断差值是否更小，若是则更新结果
                    if target - sum_ < minDiff:
                        closestSum = sum_
                        minDiff = target - sum_
                    j += 1  # 增大左侧指针的范围
        return closestSum  # 返回最接近目标值的和

```
## Java
```Java
import java.util.Arrays;

class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int n = nums.length;                    // 获取数组长度
        Arrays.sort(nums);                      // 对数组进行升序排序
        int minDiff = Integer.MAX_VALUE;        // 初始化最小差值为整型最大值
        int closestSum = 0;                     // 用于存储最接近目标的和

        for (int i = 0; i < n - 2; i++) {       // 遍历数组，从第一个元素到倒数第三个元素
            if (i > 0 && nums[i] == nums[i - 1]) {
                // 跳过重复的元素，避免重复计算
                continue;
            }

            int sum = nums[i] + nums[i + 1] + nums[i + 2];

            if (sum > target) {
                // 如果和大于目标值，判断差值是否更小，若是则更新结果
                if (sum - target < minDiff) {
                    closestSum = sum;
                    minDiff = sum - target;
                }
                break;  // 由于数组已经排序，之后的和会更大，不必再继续遍历
            }

            sum = nums[i] + nums[n - 2] + nums[n - 1];

            if (sum < target) {
                // 如果和小于目标值，判断差值是否更小，若是则更新结果
                if (target - sum < minDiff) {
                    closestSum = sum;
                    minDiff = target - sum;
                }
                continue;  // 继续尝试更大的和
            }

            int j = i + 1, k = n - 1;
            while (j < k) {
                sum = nums[i] + nums[j] + nums[k];
                if (sum == target) {
                    // 如果和等于目标值，直接返回
                    return target;
                }
                if (sum > target) {
                    // 如果和大于目标值，判断差值是否更小，若是则更新结果
                    if (sum - target < minDiff) {
                        closestSum = sum;
                        minDiff = sum - target;
                    }
                    k--;  // 缩小右侧指针的范围
                } else {
                    // 如果和小于目标值，判断差值是否更小，若是则更新结果
                    if (target - sum < minDiff) {
                        closestSum = sum;
                        minDiff = target - sum;
                    }
                    j++;  // 增大左侧指针的范围
                }
            }
        }
        return closestSum;  // 返回最接近目标值的和
    }
}

```
## Cpp
```Cpp
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int n = nums.size();                    // 获取数组长度
        sort(nums.begin(), nums.end());         // 对数组进行升序排序
        int minDiff = INT_MAX;                  // 初始化最小差值为整型最大值
        int closestSum = 0;                     // 用于存储最接近目标的和

        for (int i = 0; i < n - 2; i++) {       // 遍历数组，从第一个元素到倒数第三个元素
            if (i > 0 && nums[i] == nums[i - 1]) {
                // 跳过重复的元素，避免重复计算
                continue;
            }

            int sum = nums[i] + nums[i + 1] + nums[i + 2];

            if (sum > target) {
                // 如果和大于目标值，判断差值是否更小，若是则更新结果
                if (sum - target < minDiff) {
                    closestSum = sum;
                    minDiff = sum - target;
                }
                break;  // 由于数组已经排序，之后的和会更大，不必再继续遍历
            }

            sum = nums[i] + nums[n - 2] + nums[n - 1];

            if (sum < target) {
                // 如果和小于目标值，判断差值是否更小，若是则更新结果
                if (target - sum < minDiff) {
                    closestSum = sum;
                    minDiff = target - sum;
                }
                continue;  // 继续尝试更大的和
            }

            int j = i + 1, k = n - 1;
            while (j < k) {
                sum = nums[i] + nums[j] + nums[k];
                if (sum == target) {
                    // 如果和等于目标值，直接返回
                    return target;
                }
                if (sum > target) {
                    // 如果和大于目标值，判断差值是否更小，若是则更新结果
                    if (sum - target < minDiff) {
                        closestSum = sum;
                        minDiff = sum - target;
                    }
                    k--;  // 缩小右侧指针的范围
                } else {
                    // 如果和小于目标值，判断差值是否更小，若是则更新结果
                    if (target - sum < minDiff) {
                        closestSum = sum;
                        minDiff = target - sum;
                    }
                    j++;  // 增大左侧指针的范围
                }
            }
        }
        return closestSum;  // 返回最接近目标值的和
    }
};

```
每个版本的代码所需要的基础知识：

**Go 版本代码所需基础知识：**

1. **基本语法：** 理解 Go 语言的基本语法，包括变量声明、循环、条件语句、函数定义等。

2. **切片和排序：** 了解切片的概念和使用方法，以及如何使用标准库的 `sort` 包对切片进行排序。

3. **双指针法：** 理解双指针法的思想，即使用两个指针来在数组或切片中快速查找或计算。

4. **数学库和常量：** 知道如何使用数学库的常量 `math.MaxInt` 来表示整型最大值。

**Python 版本代码所需基础知识：**

1. **基本语法：** 熟悉 Python 的基本语法，包括变量声明、循环、条件语句、函数定义等。

2. **列表和排序：** 理解列表的概念和使用方法，以及如何使用内置函数 `sorted()` 对列表进行排序。

3. **双指针法：** 了解双指针法的思想，即使用两个指针来在列表中快速查找或计算。

4. **浮点数表示：** 知道如何使用 `float('inf')` 来表示正无穷大。

**Java 版本代码所需基础知识：**

1. **基本语法：** 掌握 Java 的基本语法，包括变量声明、循环、条件语句、方法定义等。

2. **数组和排序：** 理解数组的概念和使用方法，以及如何使用 `Arrays` 类的 `sort()` 方法对数组进行排序。

3. **双指针法：** 熟悉双指针法的思想，即使用两个指针来在数组中快速查找或计算。

4. **常量：** 知道如何使用 `Integer.MAX_VALUE` 来表示整型最大值。

**C++ 版本代码所需基础知识：**

1. **基本语法：** 熟悉 C++ 的基本语法，包括变量声明、循环、条件语句、函数定义等。

2. **向量和排序：** 了解向量（`vector`）的概念和使用方法，以及如何使用标准库的 `sort()` 函数对向量进行排序。

3. **双指针法：** 掌握双指针法的思想，即使用两个指针来在向量中快速查找或计算。

4. **整型常量：** 知道如何使用 `INT_MAX` 来表示整型最大值。

