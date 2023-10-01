# [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)

## 题目

Given a collection of intervals, merge all overlapping intervals.

Example 1:  

```
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
```

Example 2:  

```
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

## 题目大意

合并给的多个区间，区间有重叠的要进行区间合并。


## 解题思路


Go 版本:

1. 首先，通过遍历所有区间，找到它们的最大起点和最小终点，以便后续数组的初始化。

2. 创建两个数组 `start` 和 `end`，用于统计每个起始点和结束点的出现次数。

3. 第二次遍历区间列表，将每个区间的起始点和结束点在相应的数组中加一。

4. 使用 `prefix` 变量来记录当前活跃的区间数，通过 `prefix` 的值可以确定是否开始一个新的合并区间。

5. 最后，根据 `prefix` 的值，将合并后的区间加入到答案中。

Python 版本:

1. 首先，通过遍历所有区间，找到它们的最大起点和最小终点，以便后续列表的初始化。

2. 创建两个列表 `start` 和 `end`，用于统计每个起始点和结束点的出现次数。

3. 第二次遍历区间列表，将每个区间的起始点和结束点在相应的列表中加一。

4. 使用 `prefix` 变量来记录当前活跃的区间数，通过 `prefix` 的值可以确定是否开始一个新的合并区间。

5. 最后，根据 `prefix` 的值，将合并后的区间加入到答案中。

Java 版本:

1. 首先，通过遍历所有区间，找到它们的最大起点和最小终点，以便后续数组的初始化。

2. 创建两个数组 `start` 和 `end`，用于统计每个起始点和结束点的出现次数。

3. 第二次遍历区间列表，将每个区间的起始点和结束点在相应的数组中加一。

4. 使用 `prefix` 变量来记录当前活跃的区间数，通过 `prefix` 的值可以确定是否开始一个新的合并区间。

5. 最后，将合并后的区间加入到答案数组中。

C++ 版本:

1. 首先，通过遍历所有区间，找到它们的最大起点和最小终点，以便后续向量的初始化。

2. 创建两个向量 `start` 和 `end`，用于统计每个起始点和结束点的出现次数。

3. 第二次遍历区间列表，将每个区间的起始点和结束点在相应的向量中加一。

4. 使用 `prefix` 变量来记录当前活跃的区间数，通过 `prefix` 的值可以确定是否开始一个新的合并区间。

5. 最后，将合并后的区间加入到答案向量中。

总的来说，这些版本的解决方案都采用了相似的核心思想：先找到区间的最大起点和最小终点，然后统计每个起始点和结束点的出现次数，最后根据这些信息进行合并操作。

## 代码

## Go

```Go
func merge(intervals [][]int) [][]int {
    MAX := math.MinInt
    MIN := math.MaxInt
    left := -1
    prefix := 0
    for _, temp := range intervals {
        x := temp[0]
        y := temp[1]
        if x < MIN {
            MIN = x
        }
        if y > MAX {
            MAX = y
        }
    }

    start := make([]int, MAX+1)
    end := make([]int, MAX+1)

    for i := 0; i < len(intervals); i++ {
        x := intervals[i][0]
        y := intervals[i][1]
        start[x]++
        end[y]++
    }

    var ans [][]int
    size := 0
    for i := MIN; i <= MAX; i++ {
        if start[i] > 0 {
            prefix += start[i]
            if prefix == start[i] {
                left = i
            }
        }
        if end[i] > 0 {
            prefix -= end[i]
            if prefix == 0 {
                ans = append(ans, []int{left, i})
                size++
            }
        }
    }
    return ans
}

```

## Python

```Python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        MAX = float('-inf')
        MIN = float('inf')
        left = -1
        prefix = 0
        for temp in intervals:
            x = temp[0]
            y = temp[1]
            if x < MIN:
                MIN = x
            if y > MAX:
                MAX = y

        start = [0] * (MAX + 1)
        end = [0] * (MAX + 1)
        
        for i in range(len(intervals)):
            x = intervals[i][0]
            y = intervals[i][1]
            start[x] += 1
            end[y] += 1

        ans = []
        size = 0
        for i in range(MIN, MAX + 1):
            if start[i] > 0:
                prefix += start[i]
                if prefix == start[i]:
                    left = i
            if end[i] > 0:
                prefix -= end[i]
                if prefix == 0:
                    ans.append([left, i])
                    size += 1
        
        return ans

```

## Java

```Java
class Solution {
    static int[][] ans = new int[10001][2]; // 创建一个静态二维数组用于存储合并后的区间
    public int[][] merge(int[][] intervals) {
        int MAX = Integer.MIN_VALUE, MIN = Integer.MAX_VALUE, left = -1, prefix = 0;
        for (int[] temp : intervals) {
            int x = temp[0];
            int y = temp[1];
            if (x < MIN) MIN = x;
            if (y > MAX) MAX = y;
        }
        int[] start = new int[MAX+1], end = new int[MAX+1];
        
        // 统计每个起始点和结束点出现的次数
        for (int i = 0; i < intervals.length; i++) {
            int x = intervals[i][0];
            int y = intervals[i][1];
            start[x]++;
            end[y]++;
        }

        int size = 0;
        for (int i = MIN; i <= MAX; i++) {
            if (start[i] > 0) {
                prefix += start[i];
                if (prefix == start[i]) {
                    left = i;
                }
            }
            if (end[i] > 0) {
                prefix -= end[i];
                if (prefix == 0) {
                    ans[size++] = new int[]{left, i}; // 找到一个合并后的区间
                }
            }
        }
        return Arrays.copyOfRange(ans, 0, size); // 返回合并后的结果数组
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        int MAX = INT_MIN;
        int MIN = INT_MAX;
        int left = -1;
        int prefix = 0;
        for (const vector<int>& temp : intervals) {
            int x = temp[0];
            int y = temp[1];
            if (x < MIN) MIN = x;
            if (y > MAX) MAX = y;
        }

        vector<int> start(MAX + 1, 0);
        vector<int> end(MAX + 1, 0);

        for (int i = 0; i < intervals.size(); i++) {
            int x = intervals[i][0];
            int y = intervals[i][1];
            start[x]++;
            end[y]++;
        }

        vector<vector<int>> ans;
        int size = 0;
        for (int i = MIN; i <= MAX; i++) {
            if (start[i] > 0) {
                prefix += start[i];
                if (prefix == start[i]) {
                    left = i;
                }
            }
            if (end[i] > 0) {
                prefix -= end[i];
                if (prefix == 0) {
                    ans.push_back({left, i});
                    size++;
                }
            }
        }
        return ans;
    }
};

```
每个版本的解决方案以及所需的基础知识。

Go 版本：

这个 Go 版本的解决方案使用了以下重要的基础知识：

1. **切片（Slices）和数组（Arrays）：** Go 中的切片和数组是用来存储多个相同类型的数据的数据结构。在这个解决方案中，切片用于存储合并后的区间。

2. **循环（Loop）：** 使用 `for` 循环遍历区间列表和其他数据结构。

3. **条件语句（Conditional Statements）：** 使用条件语句来处理不同的情况，例如合并区间。

4. **切片追加（Slice Append）：** 使用 `append` 函数来动态扩展切片以添加合并后的区间。

Python 版本：

这个 Python 版本的解决方案使用了以下基础知识：

1. **列表（Lists）：** 列表是 Python 中的一种数据结构，用于存储多个对象。在这个解决方案中，列表被用于存储合并后的区间。

2. **循环（Loop）：** 使用 `for` 循环来遍历区间列表和其他数据结构。

3. **条件语句（Conditional Statements）：** 使用条件语句来处理不同的情况，例如合并区间。

4. **列表追加（List Append）：** 使用 `append` 方法来动态扩展列表以添加合并后的区间。

Java 版本：

这个 Java 版本的解决方案使用了以下基础知识：

1. **类和对象（Classes and Objects）：** Java 是面向对象的编程语言，这个解决方案中创建了一个名为 `Solution` 的类来解决问题。

2. **数组（Arrays）：** 使用数组来存储合并后的区间。

3. **循环（Loop）：** 使用 `for` 循环来遍历区间列表和其他数据结构。

4. **条件语句（Conditional Statements）：** 使用条件语句来处理不同的情况，例如合并区间。

5. **静态数组和动态数组（Static and Dynamic Arrays）：** 静态数组是提前定义大小的数组，而动态数组可以根据需要动态分配大小。

C++ 版本：

这个 C++ 版本的解决方案使用了以下基础知识：

1. **类和对象（Classes and Objects）：** C++ 是面向对象的编程语言，这个解决方案中创建了一个名为 `Solution` 的类来解决问题。

2. **向量（Vectors）：** 使用向量来存储合并后的区间。向量是 C++ 标准库提供的动态数组数据结构。

3. **循环（Loop）：** 使用 `for` 循环来遍历区间列表和其他数据结构。

4. **条件语句（Conditional Statements）：** 使用条件语句来处理不同的情况，例如合并区间。

