# [85. Maximal Rectangle](https://leetcode.cn/problems/maximal-rectangle/description/)

## 题目

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

Example 1:

 ![](https://assets.leetcode.com/uploads/2020/09/14/maximal.jpg)

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1
 

Constraints:

rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.

## 题目大意

给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。



## 解题思路

以下是每个版本的解题思路的详细介绍：

Go 版本解题思路:

1. **初始化**: 首先，获取输入矩阵的行数（m）和列数（n），以及创建一个整数切片 `heights` 用于存储每一列的高度。还初始化一个变量 `res` 用于存储最大矩形的面积，以及一个栈 `stack` 用于存储列的索引。

2. **遍历每一行**: 使用两层循环，外层循环遍历每一行，内层循环遍历每一列（包括虚拟的第 n+1 列）。

3. **计算直方图高度**: 对于每一列，如果当前列包含 '1'，则将该列的高度增加；否则，将该列的高度重置为 0。这样，`heights` 数组就表示了每一列的高度。

4. **计算最大矩形面积**: 使用单调栈来依次保存直方图的高度下标。一旦出现高度比栈顶元素小的情况，就取出栈顶元素，单独计算这个栈顶元素的矩形的高度。然后停在这里，继续取出当前最大栈顶的前一个元素，即连续弹出两个最大的，以稍小的一个作为矩形的边，宽就是 2 计算面积。如果停在这里的下标代表的高度一直比栈里面的元素小，就一直弹出，取出最后一个比当前下标大的高度作为矩形的边。宽就是最后一个比当前下标大的高度和当前下标之间的差值。计算出面积以后不断地更新 `maxArea` 即可。

5. **返回结果**: 最后返回 `res`，它包含了最大矩形的面积。

Python 版本解题思路:

1. **初始化**: 首先，获取输入矩阵的行数和列数，并创建一个长度为 n+1 的整数列表 `heights`，用于存储每一列的高度。还初始化一个结果变量 `res` 为 0。

2. **遍历每一行**: 使用两层循环，外层循环遍历每一行，内层循环遍历每一列。

3. **计算直方图高度**: 对于每一列，如果当前列包含 '1'，则将该列的高度增加；否则，将该列的高度重置为 0。这样，`heights` 列表就表示了每一列的高度。

4. **计算最大矩形面积**: 使用一个内部函数 `max_area(heights)` 来计算直方图的最大矩形面积。在这个函数中，使用一个栈来处理直方图的高度和索引。栈帮助找到连续递增高度的部分，并计算最大矩形的面积。

5. **更新结果**: 在每一行处理后，更新 `res` 变量，将其设置为 `res` 和当前直方图行的最大矩形面积中的较大值。

6. **返回结果**: 最后返回 `res`，它包含了最大矩形的面积。

Java 版本解题思路:

1. **初始化**: 首先，检查输入矩阵是否为空或只包含 0，如果是，直接返回 0。然后初始化一个整数数组 `height` 用于存储每一列的高度。

2. **遍历每一行**: 使用外层循环遍历每一行。

3. **重置高度数组**: 对于每一行，遍历每一列，如果当前列包含 '1'，则将该列的高度增加；否则，将该列的高度重置为 0。这样，`height` 数组就表示了每一列的高度。

4. **计算最大矩形面积**: 使用一个内部函数 `largestInLine(height)` 来计算直方图的最大矩形面积。在这个函数中，使用一个栈来处理直方图的高度和索引。栈帮助找到连续递增高度的部分，并计算最大矩形的面积。

5. **更新结果**: 在每一行处理后，更新结果变量 `result`，将其设置为 `result` 和当前直方图行的最大矩形面积中的较大值。

6. **返回结果**: 最后返回 `result`，它包含了最大矩形的面积。

C++ 版本解题思路:

1. **初始化**: 首先，检查输入矩阵是否为空或只包含 0，如果是，直接返回 0。然后初始化一个整数数组 `height` 用于存储每一列的高度。

2. **遍历每一行**: 使用外层循环遍历每一行。

3. **重置高度数组**: 对于每一行，遍历每一列，如果当前列包含 '1'，则将该列的高度增加；否则，将该列的高度重置为 0。这样，`height` 数组就表示了每一列的高度。

4. **计算最大矩形面积**: 使用一个内部函数 `largestRectangleArea(heights)` 来计算直方图的最大矩形面积。在这个函数中，使用一个栈来处理直方图的高度和索引。栈帮助找到连续递增高度的部分，并计算最大矩形的面积。

5. **更新结果**: 在每一行处理后，更新结果变量 `result`，将其设置为 `result` 和当前直方图行的最大矩形面积中的较大值。

6. **返回结果**: 最后返回 `result`，它包含了最大矩形的面积。

## Go

```Go
func maximalRectangle(matrix [][]byte) int {
    m, n := len(matrix), len(matrix[0]) // 获取矩阵的行数 m 和列数 n
    heights := make([]int, n+1) // 创建一个长度为 n+1 的整数数组 heights，用于存储每一列的高度
    res := 0 // 初始化结果变量为 0，用于存储最大矩形的面积
    stack := []int{-1} // 创建一个整数切片 stack，初始化为 [-1]，用于存储列的索引
    max := func(x, y int) int { // 创建一个匿名函数 max，用于返回两个整数中的较大值
        if x > y {
            return x
        }
        return y
    }
    for i := 0; i < m; i++ { // 遍历每一行
        for j := 0; j <= n; j++ { // 遍历每一列（包括虚拟的第 n+1 列）
            if j < n && matrix[i][j] == '1' { // 如果当前列是有效列且包含 '1'
                heights[j]++ // 增加当前列的高度
            } else {
                heights[j] = 0 // 否则，将当前列的高度重置为 0
            }
            top := stack[len(stack)-1] // 获取栈顶元素（最后一个元素）
            for top != -1 && heights[top] >= heights[j] { // 如果栈不为空且栈顶元素的高度大于或等于当前列的高度
                stack = stack[:len(stack)-1] // 出栈
                left := stack[len(stack)-1] // 获取新的栈顶元素，即前一个比当前列高度小的列
                res = max(res, heights[top]*(j-left-1)) // 计算矩形的面积并更新最大面积
                top = left // 更新 top 为左边的栈顶元素，以继续检查更大的矩形
            }
            if j < n { // 如果当前列是有效列
                stack = append(stack, j) // 将当前列的索引入栈
            }
        }
    }
    return res // 返回最大矩形的面积
}


```

## Python

```Python
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        heights = [0] * (n + 1)
        res = 0
        
        def max_area(heights):
            stack = []
            max_rect = 0
            for i, h in enumerate(heights):
                while stack and h < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_rect = max(max_rect, height * width)
                stack.append(i)
            return max_rect
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            res = max(res, max_area(heights))
        
        return res

```

## Java

```Java
class Solution {
    public int maximalRectangle(char[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0)
            return 0;

        int[] height = new int[matrix[0].length];

        // 初始化高度数组，检查第一行的值
        for (int i = 0; i < matrix[0].length; i++) {
            if (matrix[0][i] == '1')
                height[i] = 1;
        }

        int result = largestInLine(height); // 计算第一行的最大矩形面积

        for (int i = 1; i < matrix.length; i++) {
            resetHeight(matrix, height, i); // 重置高度数组
            result = Math.max(result, largestInLine(height)); // 更新最大面积
        }

        return result;
    }

    private void resetHeight(char[][] matrix, int[] height, int idx) {
        // 逐行遍历，记录每列中 '1' 的高度
        for (int i = 0; i < matrix[0].length; i++) {
            if (matrix[idx][i] == '1')
                height[i] += 1;
            else
                height[i] = 0;
        }
    }

    public int largestInLine(int[] height) {
        if (height == null || height.length < 1)
            return 0;

        int[] stack = new int[height.length + 1];
        int len = 0, max = 0;

        // 使用栈来计算每行中的最大矩形面积
        for (int i = 0; i <= height.length; i++) {
            int h = (i == height.length) ? 0 : height[i];
            while (len != 0 && (i == height.length || height[stack[len - 1]] > h)) {
                if (len == 1)
                    max = Math.max(height[stack[--len]] * i, max);
                else
                    max = Math.max(height[stack[--len]] * (i - stack[len - 1] - 1), max);
            }
            stack[len++] = i;
        }

        return max;
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        int h, w;
        if ((h = matrix.size()) == 0 || (w = matrix[0].size()) == 0) {
            return 0;
        }
        int r = 0;
        std::vector<int> heights(w, 0); // 创建一个存储列高度的数组，初始化为0

        for (int i = 0; i < h; ++i) { // 遍历每一行
            for (int j = 0; j < w; ++j) { // 遍历每一列
                if (i == 0) {
                    heights[j] = matrix[i][j] == '0' ? 0 : 1; // 初始化第一行的高度
                } else {
                    heights[j] = matrix[i][j] == '0' ? 0 : (heights[j] + 1); // 更新高度数组
                }
            }
            r = std::max(r, largestRectangleArea(heights)); // 计算并更新最大矩形面积
        }
        return r;
    }

    // 来自LeetCode 84题
    int largestRectangleArea(vector<int> & heights) {
        std::stack<int> ss;
        heights.push_back(0); // 确保在最后清空栈
        int r = 0;
        for (int i = 0; i < heights.size(); ++i) {
            while (!ss.empty() && heights[ss.top()] >= heights[i]) {
                int h = heights[ss.top()];
                ss.pop();
                int w = ss.empty() ? i : i - (ss.top() + 1); // 计算宽度
                r = std::max(r, h * w); // 计算并更新最大面积
            }
            ss.push(i); // 将当前列索引入栈
        }
        return r;
    }
};

```
 
当用不同的编程语言编写解决方案时，你需要掌握一些基础知识和编程概念。以下是每个版本的所需基础知识的详细介绍：

Go 版本:

1. **Go 语言基础**: 你需要了解 Go 语言的基础语法、数据类型、变量声明、控制流程（如循环和条件语句）等。

2. **切片（Slice）**: 在 Go 版本中，使用切片来模拟栈的行为。你需要了解如何创建、添加元素和删除元素等切片操作。

3. **匿名函数**: 代码中使用了匿名函数（闭包）来计算最大值。你需要了解如何声明和使用匿名函数。

4. **循环迭代**: 代码中使用嵌套的循环来遍历二维矩阵的行和列，你需要了解如何正确地使用嵌套循环。

Python 版本:

1. **Python 语言基础**: 你需要了解 Python 的基础语法，包括数据类型、变量、循环、条件语句和列表等。

2. **列表和列表推导式**: Python 使用列表来模拟栈的行为。了解如何创建和操作列表，以及如何使用列表推导式来生成列表。

3. **类和方法**: Python 版本使用类和方法来组织代码。你需要了解如何创建类、方法，以及如何调用方法。

4. **嵌套循环**: 代码中使用嵌套循环来遍历二维矩阵的行和列，你需要了解如何正确使用嵌套循环。

Java 版本:

1. **Java 语言基础**: 你需要了解 Java 的基础语法，包括类、方法、变量声明、循环和条件语句等。

2. **类和方法**: Java 版本使用类和方法来组织代码。了解如何创建类、方法，以及如何调用方法。

3. **堆栈数据结构**: 代码中使用堆栈数据结构（Stack）来处理直方图的高度和索引。你需要了解如何声明和使用堆栈。

4. **嵌套循环**: 代码中使用嵌套循环来遍历二维矩阵的行和列，你需要了解如何正确使用嵌套循环。

C++ 版本:

1. **C++ 语言基础**: 你需要了解 C++ 的基础语法，包括类、函数、变量声明、循环和条件语句等。

2. **类和方法**: C++ 版本使用类和函数来组织代码。了解如何创建类、成员函数，以及如何调用函数。

3. **堆栈数据结构**: 代码中使用堆栈数据结构（std::stack）来处理直方图的高度和索引。你需要了解如何声明和使用堆栈。

4. **嵌套循环**: 代码中使用嵌套循环来遍历二维矩阵的行和列，你需要了解如何正确使用嵌套循环。

不管你选择哪个版本，了解基本的编程概念、语言特性和数据结构都是解决问题的关键。此外，熟悉堆栈数据结构和直方图计算对于理解解决方案的细节也非常重要。