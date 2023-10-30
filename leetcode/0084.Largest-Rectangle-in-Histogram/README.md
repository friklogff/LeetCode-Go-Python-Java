# [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)

## 题目

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

 ![](https://assets.leetcode.com/uploads/2018/10/12/histogram.png)


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

![](https://assets.leetcode.com/uploads/2018/10/12/histogram_area.png)


The largest rectangle is shown in the shaded area, which has area = 10 unit.

 

Example:

```c
Input: [2,1,5,6,2,3]
Output: 10
```


## 题目大意

给出每个直方图的高度，要求在这些直方图之中找到面积最大的矩形，输出矩形的面积。


## 解题思路

用单调栈依次保存直方图的高度下标，一旦出现高度比栈顶元素小的情况就取出栈顶元素，单独计算一下这个栈顶元素的矩形的高度。然后停在这里(外层循环中的 i--，再 ++，就相当于停在这里了)，继续取出当前最大栈顶的前一个元素，即连续弹出 2 个最大的，以稍小的一个作为矩形的边，宽就是 2 计算面积…………如果停在这里的下标代表的高度一直比栈里面的元素小，就一直弹出，取出最后一个比当前下标大的高度作为矩形的边。宽就是最后一个比当前下标大的高度和当前下标 i 的差值。计算出面积以后不断的更新 maxArea 即可。
## 代码

## Go

```Go
func largestRectangleArea(heights []int) int {
	maxArea := 0  // 初始化最大矩形面积为0
	n := len(heights) + 2  // 计算直方图的长度，并在两端各添加一个哨兵节点
	// 添加一个函数getHeight，用于获取某个位置的高度，如果是哨兵节点则返回0
	getHeight := func(i int) int {
		if i == 0 || n-1 == i {
			return 0
		}
		return heights[i-1]
	}
	st := make([]int, 0, n/2)  // 创建一个用于保存直方图高度索引的栈
	for i := 0; i < n; i++ {
		for len(st) > 0 && getHeight(st[len(st)-1]) > getHeight(i) {
			// 如果栈不为空且栈顶高度大于当前高度，则出栈
			idx := st[len(st)-1]  // 获取栈顶索引
			st = st[:len(st)-1]  // 出栈
			maxArea = max(maxArea, getHeight(idx)*(i-st[len(st)-1]-1))  // 计算矩形面积并更新最大面积
		}
		// 将当前索引入栈
		st = append(st, i)
	}
	return maxArea  // 返回最大矩形面积
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

```

## Python

```Python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_h=max(heights)
        min_h=min(heights)
        if max_h==min_h:
            return max_h*len(heights)
        stack = [-1]
        heights.append(0)
        mxarea = 0
        for i, v in enumerate(heights):
            while heights[stack[-1]] > v:
                mid = stack.pop()
                area = heights[mid] * (i - 1 - stack[-1])
                if area > mxarea: mxarea = area
            stack.append(i)
        return mxarea
```

## Java

```Java
class Solution {
    public int largestRectangleArea(int[] heights) {
        //也很经典
        int n = heights.length;
        int[] stack = new int[n + 1];
        int top = 0;
        int res = 0;
        for (int i = 0; i < n; i++) {
            while (top > 0 && heights[i] <= heights[stack[top]]) {
                int temp = stack[top--];
                res = Math.max(res, (i - (top == 0 ? -1 : stack[top]) - 1)  * heights[temp]);
            }
            stack[++top] = i;
        }
        while (top > 0) {
            int temp = stack[top--];
            res = Math.max(res, (n - (top == 0 ? -1 : stack[top]) - 1) * heights[temp]);
        }
        return res;
    }
}
```

## Cpp

```Cpp
#define let     const auto
int pos[100005];

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        heights.push_back(0);
        const int n = heights.size();
        int sp = -1;
        int ans = 0;
        for(int i = 0; i < n; ++i) {
            let t = heights[i];
            for(; sp >= 0; --sp) {
                let h = heights[ pos[sp] ];
                if(h < t) {
                    break;
                }
                let b = sp ? pos[sp - 1] : -1;
                ans = max(ans, h * (i - 1 - b));
            }
            ++sp;
            pos[sp] = i;
        }
        return ans;
    }
};

struct IoBooster {
    IoBooster() {
        ios::sync_with_stdio(0);
        cin.tie(0);
    }
}iob;
```
理解不同编程语言版本的解决方案需要一些基础知识。以下是针对不同版本的详细介绍：

Go 版本：

1. **Slice（切片）**：Go 中的切片是动态数组，类似于其他语言中的数组或列表。了解如何声明、初始化和操作切片是编写 Go 代码的基本要求。

2. **栈（Stack）**：Go 版本使用一个切片来模拟栈的数据结构，实现了单调栈的功能。了解栈的基本操作，如入栈、出栈以及栈的初始化和访问方式。

3. **闭包（Closure）**：Go 版本使用了匿名函数（闭包）来定义一个用于获取某个位置的高度的函数。了解如何创建和使用闭包在这个解决方案中非常有帮助。

4. **哨兵节点（Sentinel Node）**：了解在算法中使用哨兵节点的目的，以及如何在 Go 中将哨兵节点添加到切片中。

5. **循环**：理解 Go 中的 `for` 循环，以及如何使用循环迭代数组和切片中的元素。

6. **条件语句和算术运算符**：理解 Go 中的条件语句（如 `if`）和算术运算符（如 `+`、`-`、`*` 等），以便计算矩形的面积。

Python 版本：

1. **列表（List）**：Python 中的列表类似于动态数组，用于存储一系列的元素。了解如何创建、操作和访问列表。

2. **栈（Stack）**：Python 版本使用一个列表来模拟栈的数据结构，实现了单调栈的功能。了解栈的基本操作，如入栈、出栈以及栈的初始化和访问方式。

3. **条件语句和算术运算符**：理解 Python 中的条件语句（如 `if`）和算术运算符（如 `+`、`-`、`*` 等），以便计算矩形的面积。

4. **类和方法**：Python 版本使用了类和方法，包括 `__init__` 初始化方法和 `largestRectangleArea` 方法。了解如何定义和使用类及其方法。

5. **列表迭代**：了解如何使用 `for` 循环迭代列表中的元素，以及如何获取元素的索引和值。

6. **条件表达式（List Comprehension）**：Python 版本使用列表推导来计算最大面积。了解列表推导的基本语法。

Java 版本：

1. **数组（Array）**：Java 中的数组用于存储一系列的元素。了解如何声明、初始化和操作数组是 Java 编程的基础知识。

2. **栈（Stack）**：Java 版本使用数组来模拟栈的数据结构，实现了单调栈的功能。了解栈的基本操作，如入栈、出栈以及栈的初始化和访问方式。

3. **循环**：理解 Java 中的 `for` 循环，以及如何使用循环迭代数组和数组中的元素。

4. **条件语句和算术运算符**：理解 Java 中的条件语句（如 `if`）和算术运算符（如 `+`、`-`、`*` 等），以便计算矩形的面积。

5. **类和方法**：Java 版本使用了类和方法，包括 `largestRectangleArea` 方法。了解如何定义和使用类及其方法。

6. **数组索引和长度**：了解如何访问数组元素的索引和获取数组的长度。

C++ 版本：

1. **数组（Array）**：C++ 中的数组用于存储一系列的元素。了解如何声明、初始化和操作数组是 C++ 编程的基础知识。

2. **栈（Stack）**：C++ 版本使用数组来模拟栈的数据结构，实现了单调栈的功能。了解栈的基本操作，如入栈、出栈以及栈的初始化和访问方式。

3. **条件语句和算术运算符**：理解 C++ 中的条件语句（如 `if`）和算术运算符（如 `+`、`-`、`*` 等），以便计算矩形的面积。

4. **数组索引和长度**：了解如何访问数组元素的索引和获取数组的长度。

5. **类和方法**：C++ 版本使用了类和方法，包括 `largestRectangleArea` 方法。了解如何定义和使用类及其方法。

6. **算法设计**：理解如何设计算法来解决问题，包括使用栈数据结构来查找最大矩形的面积。

