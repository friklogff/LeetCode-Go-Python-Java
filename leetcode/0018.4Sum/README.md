# [18. 4Sum](https://leetcode.com/problems/4sum/)

## 题目

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c +
d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

```c
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
```

## 题目大意

给定一个数组，要求在这个数组中找出 4 个数之和为 0 的所有组合。

## 解题思路

用 map 提前计算好任意 3 个数字之和，保存起来，可以将时间复杂度降到 O(n^3)
。这一题比较麻烦的一点在于，最后输出解的时候，要求输出不重复的解。数组中同一个数字可能出现多次，同一个数字也可能使用多次，但是最后输出解的时候，不能重复。例如 [-1，1，2, -2]
和 [2, -1, -2, 1]、[-2, 2, -1, 1] 这 3 个解是重复的，即使 -1, -2 可能出现 100 次，每次使用的 -1, -2 的数组下标都是不同的。

这一题是第 15 题的升级版，思路都是完全一致的。这里就需要去重和排序了。map 记录每个数字出现的次数，然后对 map 的 key
数组进行排序，最后在这个排序以后的数组里面扫，找到另外 3 个数字能和自己组成 0 的组合。

第 15 题和第 18 题的解法一致。
当解释每个版本的解题思路时，我们将专注于每个版本中使用的方法和算法。

Go 版本的解题思路

1. **双指针法：** 这个解法主要使用了双指针法，通过对数组进行排序，然后使用指针来确定数组中的元素。通过设置两个指针，一个指向当前元素，另一个指向数组的末尾，逐步移动指针以找到满足条件的四元组。

2. **通用的 kSum 解法：** 除了双指针法，这个解法还使用了一个通用的 kSum 解法。这个解法基于递归，将问题逐步转化为更小规模的 k-1 Sum 问题，直到最终转化为 2 Sum 问题，然后再使用双指针法来解决。这种通用性的解法可以用于解决不同规模的 kSum 问题。

Python 版本的解题思路

1. **双指针法：** 这个版本的解法主要使用了双指针法。通过对数组进行排序，然后设置两个指针，一个从数组起始位置向后移动，另一个从数组末尾位置向前移动，根据当前指针指向的元素之和与目标值的比较结果，决定指针的移动方向，从而找到满足条件的四元组。

Java 版本的解题思路

1. **双指针法：** 这个版本的解法同样使用了双指针法。通过对数组进行排序，然后设置两个指针，一个从数组起始位置向后移动，另一个从数组末尾位置向前移动，根据当前指针指向的元素之和与目标值的比较结果，决定指针的移动方向，从而找到满足条件的四元组。

2. **封装 nSum 函数：** 这个版本的解法将 nSum 问题的求解封装在一个单独的函数中，这样可以在 3Sum 和 4Sum 问题中重复使用。nSum 函数会根据传入的参数来决定是计算 2Sum、3Sum 还是其他的 nSum 问题。

C++ 版本的解题思路

1. **双指针法：** 这个版本的解法同样使用了双指针法。通过对向量进行排序，然后设置两个指针，一个从向量起始位置向后移动，另一个从向量末尾位置向前移动，根据当前指针指向的元素之和与目标值的比较结果，决定指针的移动方向，从而找到满足条件的四元组。


## 代码

## Go

```Go
import "sort"  // 导入排序库

// 解法一 双指针
func fourSum(nums []int, target int) (quadruplets [][]int) {
    sort.Ints(nums)  // 对输入数组进行排序
    n := len(nums)
    for i := 0; i < n-3 && nums[i]+nums[i+1]+nums[i+2]+nums[i+3] <= target; i++ {
        // 跳过重复的起始数字，或者如果当前四个最小数之和已经大于目标值，也跳过
        if i > 0 && nums[i] == nums[i-1] || nums[i]+nums[n-3]+nums[n-2]+nums[n-1] < target {
            continue
        }
        for j := i + 1; j < n-2 && nums[i]+nums[j]+nums[j+1]+nums[j+2] <= target; j++ {
            // 跳过重复的第二个数字，或者如果当前四个数最小和大于目标值，也跳过
            if j > i+1 && nums[j] == nums[j-1] || nums[i]+nums[j]+nums[n-2]+nums[n-1] < target {
                continue
            }
            // 使用双指针查找剩下的两个数字
            for left, right := j+1, n-1; left < right; {
                if sum := nums[i] + nums[j] + nums[left] + nums[right]; sum == target {
                    quadruplets = append(quadruplets, []int{nums[i], nums[j], nums[left], nums[right]})
                    // 跳过重复的数字
                    for left++; left < right && nums[left] == nums[left-1]; left++ {
                    }
                    for right--; left < right && nums[right] == nums[right+1]; right-- {
                    }
                } else if sum < target {
                    left++
                } else {
                    right--
                }
            }
        }
    }
    return
}

// 解法二 kSum
func fourSum1(nums []int, target int) [][]int {
    res, cur := make([][]int, 0), make([]int, 0)
    sort.Ints(nums)
    kSum(nums, 0, len(nums)-1, target, 4, cur, &res)
    return res
}

// 通用的 kSum 函数，用于计算 k 个数之和等于目标值
func kSum(nums []int, left, right int, target int, k int, cur []int, res *[][]int) {
    if right-left+1 < k || k < 2 || target < nums[left]*k || target > nums[right]*k {
        return
    }
    if k == 2 {
        // 2 sum
        twoSum(nums, left, right, target, cur, res)
    } else {
        for i := left; i < len(nums); i++ {
            if i == left || (i > left && nums[i-1] != nums[i]) {
                next := make([]int, len(cur))
                copy(next, cur)
                next = append(next, nums[i])
                kSum(nums, i+1, len(nums)-1, target-nums[i], k-1, next, res)
            }
        }
    }
}

// 计算两数之和为目标值的函数
func twoSum(nums []int, left, right int, target int, cur []int, res *[][]int) {
    for left < right {
        sum := nums[left] + nums[right]
        if sum == target {
            cur = append(cur, nums[left], nums[right])
            temp := make([]int, len(cur))
            copy(temp, cur)
            *res = append(*res, temp)
            // 恢复 cur 到之前状态
            cur = cur[:len(cur)-2]
            left++
            right--
            // 跳过重复的数字
            for left < right && nums[left] == nums[left-1] {
                left++
            }
            for left < right && nums[right] == nums[right+1] {
                right--
            }
        } else if sum < target {
            left++
        } else {
            right--
        }
    }
}

```

## Python

```Python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # 对输入数组进行排序
        ans = []  # 存储结果的列表
        n = len(nums)

        for a in range(n - 3):
            x = nums[a]  # 第一个数
            if a and x == nums[a - 1]:  # 避免重复解
                continue
            if x + nums[a + 1] + nums[a + 2] + nums[a + 3] > target:  # 剪枝，如果最小的四个数之和大于目标值，退出循环
                break
            if x + nums[-3] + nums[-2] + nums[-1] < target:  # 剪枝，如果最大的三个数和当前数的和小于目标值，继续下一个数
                continue
            for b in range(a + 1, n - 2):
                y = nums[b]  # 第二个数
                if b > a + 1 and y == nums[b - 1]:  # 避免重复解
                    continue
                if x + y + nums[b + 1] + nums[b + 2] > target:  # 剪枝，如果最小的三个数和当前数的和大于目标值，退出循环
                    break
                if x + y + nums[-2] + nums[-1] < target:  # 剪枝，如果最大的两个数和当前数的和小于目标值，继续下一个数
                    continue
                c = b + 1
                d = n - 1
                while c < d:
                    s = x + y + nums[c] + nums[d]  # 四数之和
                    if s > target:
                        d -= 1
                    elif s < target:
                        c += 1
                    else:  # s == target，找到满足条件的四元组
                        ans.append([x, y, nums[c], nums[d]])
                        c += 1
                        while c < d and nums[c] == nums[c - 1]:  # 跳过重复数字
                            c += 1
                        d -= 1
                        while d > c and nums[d] == nums[d + 1]:  # 跳过重复数字
                            d -= 1
        return ans

```

## Java

```Java
// 导入需要的 Java 类
import java.util.AbstractList;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

// 定义一个名为 Solution 的类
class Solution {
    // 定义一个方法用于解决 3Sum 问题
    public List<List<Integer>> threeSum(int[] nums) {
        return nSum(nums, 3, 0);  // 调用 nSum 方法来解决问题
    }

    // 定义一个方法用于解决 4Sum 问题
    public List<List<Integer>> fourSum(int[] nums, int target) {
        return nSum(nums, 4, target);  // 调用 nSum 方法来解决问题
    }

    // nSum 方法实现了通用的 nSum 问题解决方案
    List<List<Integer>> nSum(int[] a, int n, long target) {
        return new AbstractList<List<Integer>>() {
            final List<List<Integer>> res = new ArrayList<>();  // 存储结果的列表
            final List<Integer> path = new ArrayList<>();       // 存储路径的列表

            @Override
            public int size() {
                init();  // 初始化并计算结果
                return res.size();  // 返回结果列表的大小
            }

            @Override
            public List<Integer> get(int index) {
                init();  // 初始化并计算结果
                return res.get(index);  // 返回指定索引处的结果列表
            }

            // 初始化函数，在结果为空时进行计算
            void init() {
                if (res.isEmpty()) {
                    Arrays.sort(a);  // 对输入数组进行排序
                    dfs(a, 0, a.length - 1, n, target);  // 调用深度优先搜索来计算结果
                }
            }

            // 深度优先搜索函数，计算 nSum 的结果
            void dfs(int[] a, int i, int j, int n, long target) {
                if (n == 2) {
                    two(a, i, j, target);  // 如果 n 为 2，调用 two 函数计算结果
                } else if (n > 2) {
                    hit(a, i, j, n, target);  // 如果 n 大于 2，调用 hit 函数计算结果
                }
            }

            // 计算 twoSum 的结果
            void two(int[] a, int i, int j, long target) {
                if (i >= j) {
                    return;
                }
                long max = 0;
                long min = 0;
                for (int k = 0; k < 2; k++) {
                    min += a[i + k];
                    max += a[j - k];
                }
                if (target < min || target > max) {
                    return;
                }
                while (j > i) {
                    long sum = a[i] + a[j];
                    if (sum < target) {
                        i++;
                    } else if (sum > target) {
                        j--;
                    } else {
                        path.add(a[i]);
                        path.add(a[j]);
                        res.add(new ArrayList<>(path));
                        path.remove(path.size() - 1);
                        path.remove(path.size() - 1);
                        while (j > i && a[i] == a[i + 1]) {
                            i++;
                        }
                        while (j > i && a[i] == a[j - 1]) {
                            j--;
                        }
                        i++;
                        j--;
                    }
                }
            }

            // 计算 nSum（n > 2）的结果
            void hit(int[] a, int i, int j, int n, long target) {
                int begin = i;
                int end = j;
                if (i + n - 2 >= j) {
                    return;
                }
                long max = 0;
                long min = 0;
                for (int k = 0; k < n; k++) {
                    min += a[i + k];
                    max += a[j - k];
                }
                if (target < min || target > max) {
                    return;
                }
                while (j > i + n - 2) {
                    long sufMax = 0;
                    long preMin = 0;
                    for (int k = 0; k < n - 1; k++) {
                        preMin += a[i + k];
                        sufMax += a[j - k];
                    }
                    preMin += a[j];
                    sufMax += a[i];
                    if (sufMax < target) {
                        i++;
                    } else if (preMin > target) {
                        j--;
                    } else {
                        while (i != begin && j > i + n - 2 && a[i] == a[i - 1]) {
                            i++;
                        }
                        while (j != end && j > i + n - 2 && a[j] == a[j + 1]) {
                            j--;
                        }
                        path.add(a[i]);
                        dfs(a, i + 1, j, n - 1, target - a[i]);
                        path.remove(path.size() - 1);
                        i++;
                    }
                }
            }
        };
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());  // 对输入数组进行排序
        vector<vector<int>> result;  // 存储结果的二维向量
        int n = nums.size();
        
        for (int i = 0; i < n - 3; ++i) {
            if (i > 0 && nums[i] == nums[i - 1])  // 避免重复解
                continue;

            for (int j = i + 1; j < n - 2; ++j) {
                if (j > i + 1 && nums[j] == nums[j - 1])  // 避免重复解
                    continue;

                int left = j + 1;
                int right = n - 1;

                while (left < right) {
                    long long sum = static_cast<long long>(nums[i]) + nums[j] + nums[left] + nums[right];

                    if (sum < target) {
                        ++left;
                    } else if (sum > target) {
                        --right;
                    } else {
                        result.push_back({nums[i], nums[j], nums[left], nums[right]});
                        
                        while (left < right && nums[left] == nums[left + 1])
                            ++left;
                        while (left < right && nums[right] == nums[right - 1])
                            --right;

                        ++left;
                        --right;
                    }
                }
            }
        }

        return result;
    }
};

```

Go 版本的基础知识

- **基本语法：** 熟悉 Go 语言的基本语法，包括变量声明、循环、条件语句等。
- **切片和数组：** 了解切片和数组的使用方式，它们在 Go 中用于存储数据。
- **排序：** 了解如何使用 `sort` 包来对切片进行排序。
- **递归：** 理解递归的概念和用法，因为 kSum 解法使用了递归。

Python 版本的基础知识

- **基本语法：** 熟悉 Python 的基本语法，包括变量声明、循环、条件语句等。
- **列表和数组：** 了解列表的使用方式，它在 Python 中常用于存储数据。
- **排序：** 了解如何使用内置的 `sorted()` 函数来对列表进行排序。
- **双指针法：** 理解双指针法的基本思想，它在这个问题的解决中起到了关键作用。

Java 版本的基础知识

- **基本语法：** 熟悉 Java 的基本语法，包括变量声明、循环、条件语句等。
- **集合和列表：** 了解集合和列表的使用方式，Java 中的 `ArrayList` 和 `List` 接口在这个代码中被使用。
- **排序：** 了解如何使用 `Arrays.sort()` 方法来对数组进行排序。
- **类和对象：** 对 Java 中的类和对象有基本的了解，因为代码中定义了一个名为 `Solution` 的类。

C++ 版本的基础知识

- **基本语法：** 熟悉 C++ 的基本语法，包括变量声明、循环、条件语句等。
- **向量和数组：** 了解向量的使用方式，它在 C++ 中常用于存储数据。
- **排序：** 了解如何使用 `std::sort()` 函数来对向量进行排序。
- **双指针法：** 理解双指针法的基本思想，它在这个问题的解决中起到了关键作用。

