# [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)


## 题目

Given a matrix of *m* x *n* elements (*m* rows, *n* columns), return all elements of the matrix in spiral order.

**Example 1:**


    Input:
    [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
    Output: [1,2,3,6,9,8,7,4,5]


**Example 2:**


    Input:
    [
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9,10,11,12]
    ]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]


## 题目大意

给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

## 解题思路

- 给出一个二维数组，按照螺旋的方式输出
- 解法一：需要注意的是特殊情况，比如二维数组退化成一维或者一列或者一个元素。注意了这些情况，基本就可以一次通过了。
- 解法二：提前算出一共多少个元素，一圈一圈地遍历矩阵，停止条件就是遍历了所有元素（count == sum）
**Go版本:**
1. 定义方向向量数组spDir,表示向右、下、左、上的方向
2. 使用visit矩阵标记已访问位置
3. 根据round变量判断方向,初始化为向右
4. 遍历矩阵,每次根据方向向量更新坐标
5. 判断是否到达转角,是则round自增变换方向
6. 判断坐标是否出界
7. 判断该位置是否已访问,未访问则标记并添加到结果 
8. 根据当前方向判断周围是否访问过,是则改变方向


**Python版本:**
1. 定义左右上下边界,表示当前遍历的范围
2. 通过不断改变边界坐标实现螺旋遍历
3. 从左到右遍历上边界,然后上边界下移
4. 从上到下遍历右边界,然后右边界左移 
5. 判断边界是否相遇,相遇则结束
6. 从右到左遍历下边界,然后下边界上移
7. 从下到上遍历左边界,然后左边界右移


**Java版本:**
1. 定义dr、dc数组表示四个方向
2. 使用visited数组标记已访问位置
3. di变量控制方向,每次遍历后自增改变方向
4. 根据方向数组计算下一个遍历位置
5. 如果下个位置合法且未访问过,则移动坐标
6. 否则改变di继续遍历


**C++版本:**
1. 定义方向数组dr、dc
2. 使用visited向量标记已访问位置
3. di变量控制方向,转角时自增di改变方向
4. 根据dr、dc计算下个遍历位置
5. 如果合法且未访问,移动坐标
6. 否则改变方向继续遍历


## 代码

## Go

```Go
// 定义一个螺旋遍历二维矩阵的函数
func spiralOrder(matrix [][]int) []int {
    // 如果矩阵为空,直接返回空切片
    if len(matrix) == 0 { 
       return []int{}
    }
    // 定义一个结果切片
    res := []int{}
    // 如果矩阵只有一行,直接遍历添加到结果切片
    if len(matrix) == 1 {
       for i := 0; i < len(matrix[0]); i++ {
          res = append(res, matrix[0][i])
       }
       return res
    }
    // 如果矩阵只有一列,直接遍历添加到结果切片   
    if len(matrix[0]) == 1 {
       for i := 0; i < len(matrix); i++ {
          res = append(res, matrix[i][0])
       }
       return res
    }
    // 定义一个访问矩阵,标记已访问过的元素
    visit, m, n, round, x, y, spDir := make([][]int, len(matrix)), len(matrix), len(matrix[0]), 0, 0, 0, [][]int{
       []int{0, 1},  // 向右的方向向量
       []int{1, 0},  // 向下的方向向量
       []int{0, -1}, // 向左的方向向量
       []int{-1, 0}, // 向上的方向向量
    }
    // 初始化访问矩阵
    for i := 0; i < m; i++ {
       visit[i] = make([]int, n)
    }
    // 标记当前位置为已访问
    visit[x][y] = 1
    // 将当前位置元素添加到结果切片
    res = append(res, matrix[x][y])
    // 开始遍历矩阵
    for i := 0; i < m*n; i++ {
       // 根据当前方向向量更新x、y坐标 
       x += spDir[round%4][0] 
       y += spDir[round%4][1]
       // 如果遍历到转角,改变方向
       if (x == 0 && y == n-1) || (x == m-1 && y == n-1) || (y == 0 && x == m-1) {
          round++
       }
       // 检查坐标是否出界
       if x > m-1 || y > n-1 || x < 0 || y < 0 {
          return res
       }
       // 如果当前位置未访问过
       if visit[x][y] == 0 {
          // 标记为已访问
          visit[x][y] = 1
          // 添加到结果切片 
          res = append(res, matrix[x][y])
       }
       // 根据当前方向判断是否需要改变方向
       switch round % 4 {
       case 0: // 向右
          if y+1 <= n-1 && visit[x][y+1] == 1 { // 右侧已访问过
             round++ // 改变方向
             continue
          }
       case 1: // 向下
          if x+1 <= m-1 && visit[x+1][y] == 1 { // 下方已访问过
             round++
             continue
          } 
       case 2: // 向左
          if y-1 >= 0 && visit[x][y-1] == 1 { // 左侧已访问过
             round++
             continue
          }
       case 3: // 向上
          if x-1 >= 0 && visit[x-1][y] == 1 { // 上方已访问过
             round++
             continue
          }
       }
    }
    // 返回结果切片
    return res
}
```

## Python

```Python
python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 定义左、上边界
        left, top = 0, 0 
        # 定义右、下边界  
        bottom, right = len(matrix), len(matrix[0])

        # 结果列表
        ans = []

        # 当左右边界未相遇,上下边界未相遇时
        while left < right and top < bottom:
            
            # 从左到右遍历上边界  
            for i in range(left, right):
                ans.append(matrix[top][i])
            # 上边界下移
            top += 1

            # 从上到下遍历右边界
            for i in range(top, bottom):
                ans.append(matrix[i][right - 1])
            # 右边界左移
            right -= 1

            # 如果边界相遇,结束循环
            if left >= right or top >= bottom:
                break

            # 从右到左遍历下边界
            for i in range(right - 1, left - 1, -1):
                ans.append(matrix[bottom - 1][i])
            # 下边界上移
            bottom -= 1

            # 从下到上遍历左边界
            for i in range(bottom - 1, top - 1, -1):
                ans.append(matrix[i][left])
            # 左边界右移
            left += 1

        return ans

```

## Java

```Java

import java.util.ArrayList; 
import java.util.List;

class Solution {
  public List<Integer> spiralOrder(int[][] matrix) {
    
    List<Integer> res = new ArrayList<>();
    
    if(matrix.length == 0) return res;
    
    int m = matrix.length;
    int n = matrix[0].length;
    
    boolean[][] visited = new boolean[m][n];
    
    int[] dr = {0, 1, 0, -1}; // 右、下、左、上 
    int[] dc = {1, 0, -1, 0};
    
    int r = 0, c = 0, di = 0;
    
    for(int i = 0; i < m * n; i++) {
      
      res.add(matrix[r][c]);
      visited[r][c] = true;
      
      int cr = r + dr[di];
      int cc = c + dc[di];
      
      if(0 <= cr && cr < m && 0 <= cc && cc < n && !visited[cr][cc]) {
        r = cr;
        c = cc; 
      }
      else {
        di = (di + 1) % 4; // 改变方向
        r += dr[di]; 
        c += dc[di];
      }
    }
    
    return res;

  }
}

```

## Cpp

```Cpp
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> spiralOrder(vector<vector<int>>& matrix) {

    vector<int> res;
    if (matrix.empty()) return res;

    int m = matrix.size(), n = matrix[0].size();
    vector<vector<bool>> visited(m, vector<bool>(n));

    int dr[4] = {0, 1, 0, -1}; // 右、下、左、上
    int dc[4] = {1, 0, -1, 0};  

    int r = 0, c = 0, di = 0;

    for (int i = 0; i < m * n; i++) {

      res.push_back(matrix[r][c]);
      visited[r][c] = true;

      int cr = r + dr[di], cc = c + dc[di];

      if (0 <= cr && cr < m && 0 <= cc && cc < n && !visited[cr][cc]) {
        r = cr; c = cc;
      }  
      else {
        di = (di + 1) % 4; // 改变方向
        r += dr[di]; c += dc[di]; 
      }
    }

    return res;

  }
};
```
基础知识


1. Go版本
- 使用方向向量控制遍历顺序,根据round变量控制方向
- 使用visit矩阵记录已访问位置,避免重复访问
- 注意处理边界条件,如矩阵只有一行或一列的情况

2. Python版本
- 使用左右上下边界控制遍历范围
- 通过改变边界坐标实现螺旋遍历
- 注意处理边界相遇的情况


3. Java版本
- 使用方向数组dr、dc控制遍历方向
- visited数组记录已访问位置
- 改变di控制方向,转角时di自增实现方向改变


4. C++版本
- 与Java版本类似,使用方向数组dr、dc
- visited向量记录已访问位置 
- 改变di改变方向,转角时自增di


综合来说,螺旋遍历矩阵需要注意边界处理,并通过控制方向实现螺旋遍历顺序。记录已访问位置很重要,避免重复访问。