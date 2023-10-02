# [57. Insert Interval](https://leetcode.com/problems/insert-interval/)

## 题目

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:  

```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

Example 2:  

```
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```

## 题目大意

这一题是第 56 题的加强版。给出多个没有重叠的区间，然后再给一个区间，要求把如果有重叠的区间进行合并。

## 解题思路

可以分 3 段处理，先添加原来的区间，即在给的 newInterval 之前的区间。然后添加 newInterval ，注意这里可能需要合并多个区间。最后把原来剩下的部分添加到最终结果中即可。
以下是每个版本的解题思路：

Go 版本解题思路：

1. 初始化 `left` 和 `right` 分别为 `newInterval` 的起始和结束值，以及一个 `merged` 标志用于跟踪是否已经合并了 `newInterval`。
2. 使用 `for` 循环遍历原始区间 `intervals`。
3. 对于每个区间，检查三种情况：
   - 如果该区间在 `newInterval` 的右侧且无交集，则将 `newInterval` 添加到结果中，并将 `merged` 设置为 `true`。然后将当前区间添加到结果中。
   - 如果该区间在 `newInterval` 的左侧且无交集，则直接将当前区间添加到结果中。
   - 如果存在交集，更新 `left` 和 `right` 以合并区间。
4. 循环结束后，如果 `newInterval` 没有与任何区间合并（`!merged`），则将其添加到结果中。
5. 返回最终结果。

Python 版本解题思路：

1. 初始化一个空列表 `res` 用于存储合并后的区间。
2. 使用 `for` 循环遍历原始区间列表 `intervals`。
3. 对于每个区间，检查三种情况：
   - 如果当前区间的结束位置小于 `newInterval` 的起始位置，直接将当前区间添加到 `res`。
   - 如果当前区间的起始位置大于 `newInterval` 的结束位置，将 `newInterval` 和后面的区间都添加到 `res`。
   - 否则，合并当前区间和 `newInterval`，更新 `newInterval` 的起始和结束位置。
4. 将 `newInterval` 添加到 `res`。
5. 返回最终结果 `res`。

Java 版本解题思路：

1. 初始化一个 `ArrayList` 类型的结果列表 `ret`。
2. 使用 `for` 循环遍历原始区间数组 `intervals`。
3. 处理三种情况：
   - 左侧区间：如果当前区间的结束位置小于 `newInterval` 的起始位置，将当前区间添加到 `ret`。
   - 区间重叠：如果当前区间与 `newInterval` 有重叠，合并它们并更新 `newInterval` 的起始和结束值。
   - 右侧区间：如果当前区间的起始位置大于 `newInterval` 的结束位置，将当前区间添加到 `ret`。
4. 将 `newInterval` 添加到 `ret`。
5. 将 `ret` 转换为数组形式并返回最终结果。

C++ 版本解题思路：

1. 初始化一个 `vector<vector<int>>` 类型的结果向量 `result`。
2. 使用 `for` 循环遍历原始区间向量 `intervals`。
3. 处理三种情况：
   - 左侧区间：如果当前区间的结束位置小于 `newInterval` 的起始位置，将当前区间添加到 `result`。
   - 区间重叠：如果当前区间与 `newInterval` 有重叠，合并它们并更新 `newInterval` 的起始和结束值。
   - 右侧区间：如果当前区间的起始位置大于 `newInterval` 的结束位置，将当前区间添加到 `result`。
4. 将 `newInterval` 添加到 `result`。
5. 返回最终结果 `result`。

这些解题思路的核心思想是遍历原始区间，处理不同情况下的区间合并和添加操作，最终得到合并后的结果。要解决这个问题，需要理解如何比较区间的位置关系、如何合并区间以及如何使用循环和条件语句来控制程序逻辑。
## 代码

## Go

```Go
func insert(intervals [][]int, newInterval []int) (ans [][]int) {
    left, right := newInterval[0], newInterval[1]
    merged := false
    for _, interval := range intervals {
        if interval[0] > right {
            // 在插入区间的右侧且无交集
            if !merged {
                ans = append(ans, []int{left, right})
                merged = true
            }
            ans = append(ans, interval)
        } else if interval[1] < left {
            // 在插入区间的左侧且无交集
            ans = append(ans, interval)
        } else {
            // 与插入区间有交集，计算它们的并集
            left = min(left, interval[0])
            right = max(right, interval[1])
        }
    }
    if !merged {
        ans = append(ans, []int{left, right})
    }
    return
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```

## Python

```Python
class Solution:
    def insert(self, intervals, newInterval):
        # 初始化结果列表
        res = []
        
        # 遍历区间列表
        for interval in intervals:
            # 如果当前区间的结束位置小于新区间的起始位置，直接将当前区间加入结果
            if interval[1] < newInterval[0]:
                res.append(interval)
            # 如果当前区间的起始位置大于新区间的结束位置，将新区间和后面的区间都加入结果
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                newInterval = interval
            else:
                # 否则，合并当前区间和新区间，更新新区间的起始和结束位置
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        
        # 将新区间加入结果
        res.append(newInterval)
        
        return res
```

## Java

```Java
class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> ret = new ArrayList<>();

        int i = 0;
        int n = intervals.length;

        // 左侧区间：将结束位置小于新区间的起始位置的区间加入结果
        while (i < n && intervals[i][1] < newInterval[0]) {
            ret.add(intervals[i]);
            i++;
        }

        // 区间重叠：合并重叠的区间，更新新区间的起始和结束值
        while (i < n && intervals[i][0] <= newInterval[1] && intervals[i][1] >= newInterval[0]) {
            newInterval[0] = Math.min(intervals[i][0], newInterval[0]);
            newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
            i++;
        }
        ret.add(newInterval);

        // 右侧区间：将起始位置大于新区间的结束位置的区间加入结果
        while (i < n && intervals[i][0] > newInterval[1]) {
            ret.add(intervals[i]);
            i++;
        }

        // 将结果转换为数组形式
        int[][] ans = new int[ret.size()][];
        for (int k = 0; k < ret.size(); ++k) {
            ans[k] = ret.get(k);
        }
        return ans;
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> result;
        int n = intervals.size();
        int i = 0;

        // 左侧区间：将结束位置小于新区间的起始位置的区间加入结果
        while (i < n && intervals[i][1] < newInterval[0]) {
            result.push_back(intervals[i]);
            i++;
        }

        // 区间重叠：合并重叠的区间，更新新区间的起始和结束值
        while (i < n && intervals[i][0] <= newInterval[1] && intervals[i][1] >= newInterval[0]) {
            newInterval[0] = min(intervals[i][0], newInterval[0]);
            newInterval[1] = max(intervals[i][1], newInterval[1]);
            i++;
        }
        result.push_back(newInterval);

        // 右侧区间：将起始位置大于新区间的结束位置的区间加入结果
        while (i < n) {
            result.push_back(intervals[i]);
            i++;
        }

        return result;
    }
};

```
以下是每个版本所需要掌握的详细基础知识：

Go 版本：

1. **Slice（切片）**：Go 中的切片是动态数组，这个版本中使用切片来处理 intervals 和结果集。
2. **For 循环**：了解 Go 中的 `for` 循环语法，它用于遍历切片和执行循环操作。
3. **条件语句**：理解 `if` 和 `else` 条件语句，这里使用条件语句来判断区间的位置关系和重叠。
4. **函数定义和调用**：了解如何定义和调用函数，这里有两个自定义函数 `min` 和 `max`，用于求最小值和最大值。
5. **切片操作**：了解如何使用切片来追加元素，这里使用 `append` 函数将元素添加到结果集中。

Python 版本：

1. **列表（List）**：Python 中的列表是动态数组，这个版本中使用列表来处理 intervals 和结果集。
2. **For 循环**：了解 Python 中的 `for` 循环语法，它用于遍历列表和执行循环操作。
3. **条件语句**：理解 `if` 和 `else` 条件语句，这里使用条件语句来判断区间的位置关系和重叠。
4. **类和方法**：这个版本使用一个类 `Solution`，需要了解如何定义类和类方法，并且如何调用类方法。

Java 版本：

1. **数组**：Java 中的数组是固定大小的数据结构，这个版本中使用二维数组来处理 intervals 和结果集。
2. **For 循环**：了解 Java 中的 `for` 循环语法，它用于遍历数组和执行循环操作。
3. **条件语句**：理解 `if` 和 `else` 条件语句，这里使用条件语句来判断区间的位置关系和重叠。
4. **列表（List）**：Java 中有 `List` 接口和 `ArrayList` 类，但这里没有使用它们。你需要了解如何使用数组来存储和操作数据。
5. **类和方法**：这个版本使用一个类 `Solution`，需要了解如何定义类和类方法，并且如何调用类方法。

C++ 版本：

1. **数组**：C++ 中的数组是固定大小的数据结构，这个版本中使用二维数组来处理 intervals 和结果集。
2. **For 循环**：了解 C++ 中的 `for` 循环语法，它用于遍历数组和执行循环操作。
3. **条件语句**：理解 `if` 和 `else` 条件语句，这里使用条件语句来判断区间的位置关系和重叠。
4. **向量（Vector）**：C++ 中的 `vector` 是动态数组，但这里没有使用它。你需要了解如何使用数组来存储和操作数据。
5. **类和函数**：这个版本没有使用类，但使用了函数。需要了解如何定义函数和如何调用函数。

总体来说，无论你选择哪个版本，你需要了解数组或列表的基本操作、循环和条件语句的使用，以及如何定义和调用函数或方法。此外，不同编程语言有不同的语法和特性，所以你需要熟悉所选语言的语法和特点来理解和修改这些代码。