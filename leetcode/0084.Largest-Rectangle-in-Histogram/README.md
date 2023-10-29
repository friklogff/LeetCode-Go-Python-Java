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
