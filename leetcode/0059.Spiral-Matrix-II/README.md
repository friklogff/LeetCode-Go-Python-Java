# [59. Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/)


## 题目

Given a positive integer *n*, generate a square matrix filled with elements from 1 to *n*2 in spiral order.

**Example:**


    Input: 3
    Output:
    [
     [ 1, 2, 3 ],
     [ 8, 9, 4 ],
     [ 7, 6, 5 ]
    ]


## 题目大意

给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。


## 解题思路
题目要求生成一个正方形矩阵，矩阵的元素按照螺旋顺序从1到n^2依次填充。

首先，我们需要初始化一个n×n的矩阵，并定义四个方向，分别是向右、向下、向左、向上。然后按照螺旋顺序依次填充矩阵。

具体步骤如下：

定义一个n×n的矩阵，初始化所有元素为0。
定义四个方向的偏移量，分别是向右、向下、向左、向上，用来控制填充顺序。
根据题目要求，依次填充矩阵中的元素，同时更新当前位置和下一个位置的坐标，以及判断是否需要改变方向。
继续填充直到所有位置都被填充。


这些版本的解题思路共同点是通过模拟螺旋填充的过程，依次填充矩阵的每个位置。在填充的过程中，根据规定的螺旋顺序不断更新坐标，并在达到边界或已访问过的位置时改变填充方向。
## 代码

## Go

```Go
// 定义一个名为 generateMatrix 的函数，接收一个整数参数 n，表示要生成的螺旋矩阵的大小
func generateMatrix(n int) [][]int {
    // 如果 n 为 0，返回一个空的二维整数数组
    if n == 0 {
        return [][]int{}
    }
    // 如果 n 为 1，返回一个包含元素 1 的二维整数数组
    if n == 1 {
        return [][]int{[]int{1}}
    }
    
    // 初始化结果矩阵 res，访问标记矩阵 visit，螺旋方向 round，以及当前坐标 x 和 y
    res, visit, round, x, y, spDir := make([][]int, n), make([][]int, n), 0, 0, 0, [][]int{
        []int{0, 1},  // 朝右
        []int{1, 0},  // 朝下
        []int{0, -1}, // 朝左
        []int{-1, 0}, // 朝上
    }
    
    // 初始化结果矩阵和访问标记矩阵
    for i := 0; i < n; i++ {
        visit[i] = make([]int, n)
        res[i] = make([]int, n)
    }
    
    // 标记起始点已访问
    visit[x][y] = 1
    res[x][y] = 1
    
    // 循环填充矩阵
    for i := 0; i < n*n; i++ {
        // 根据当前螺旋方向更新坐标
        x += spDir[round%4][0]
        y += spDir[round%4][1]
        
        // 检查是否需要改变螺旋方向
        if (x == 0 && y == n-1) || (x == n-1 && y == n-1) || (y == 0 && x == n-1) {
            round++
        }
        
        // 如果坐标越界，返回结果矩阵
        if x > n-1 || y > n-1 || x < 0 || y < 0 {
            return res
        }
        
        // 如果当前坐标未被访问过，标记为已访问并填充值
        if visit[x][y] == 0 {
            visit[x][y] = 1
            res[x][y] = i + 2
        }
        
        // 根据当前螺旋方向检查下一个位置是否已经访问，如果访问过则改变方向
        switch round % 4 {
        case 0:
            if y+1 <= n-1 && visit[x][y+1] == 1 {
                round++
                continue
            }
        case 1:
            if x+1 <= n-1 && visit[x+1][y] == 1 {
                round++
                continue
            }
        case 2:
            if y-1 >= 0 && visit[x][y-1] == 1 {
                round++
                continue
            }
        case 3:
            if x-1 >= 0 && visit[x-1][y] == 1 {
                round++
                continue
            }
        }
    }
    
    // 返回生成的螺旋矩阵
    return res
}

```

## Python

```Python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 初始化结果矩阵和访问标记矩阵
        result = [[0] * n for _ in range(n)]
        visited = [[False] * n for _ in range(n)]
        
        # 定义方向数组，表示右、下、左、上四个方向
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        x, y, direction = 0, 0, 0
        
        for num in range(1, n * n + 1):
            result[x][y] = num
            visited[x][y] = True
            
            # 计算下一个坐标
            next_x, next_y = x + directions[direction][0], y + directions[direction][1]
            
            # 如果下一个坐标越界或已访问过，则改变方向
            if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n or visited[next_x][next_y]:
                direction = (direction + 1) % 4
                next_x, next_y = x + directions[direction][0], y + directions[direction][1]
            
            x, y = next_x, next_y
        
        return result

```

## Java

```Java
class Solution {
    public int[][] generateMatrix(int n) {
        // 初始化结果矩阵和访问标记矩阵
        int[][] result = new int[n][n];
        boolean[][] visited = new boolean[n][n];
        
        // 定义方向数组，表示右、下、左、上四个方向
        int[][] directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        
        int x = 0, y = 0, direction = 0;
        
        for (int num = 1; num <= n * n; num++) {
            result[x][y] = num;
            visited[x][y] = true;
            
            // 计算下一个坐标
            int nextX = x + directions[direction][0];
            int nextY = y + directions[direction][1];
            
            // 如果下一个坐标越界或已访问过，则改变方向
            if (nextX < 0 || nextX >= n || nextY < 0 || nextY >= n || visited[nextX][nextY]) {
                direction = (direction + 1) % 4;
                nextX = x + directions[direction][0];
                nextY = y + directions[direction][1];
            }
            
            x = nextX;
            y = nextY;
        }
        
        return result;
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        // 初始化结果矩阵和访问标记矩阵
        vector<vector<int>> result(n, vector<int>(n, 0));
        vector<vector<bool>> visited(n, vector<bool>(n, false));
        
        // 定义方向数组，表示右、下、左、上四个方向
        vector<vector<int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        
        int x = 0, y = 0, direction = 0;
        
        for (int num = 1; num <= n * n; num++) {
            result[x][y] = num;
            visited[x][y] = true;
            
            // 计算下一个坐标
            int nextX = x + directions[direction][0];
            int nextY = y + directions[direction][1];
            
            // 如果下一个坐标越界或已访问过，则改变方向
            if (nextX < 0 || nextX >= n || nextY < 0 || nextY >= n || visited[nextX][nextY]) {
                direction = (direction + 1) % 4;
                nextX = x + directions[direction][0];
                nextY = y + directions[direction][1];
            }
            
            x = nextX;
            y = nextY;
        }
        
        return result;
    }
};

```
好的，我会分别介绍每个版本的代码涉及的基础知识和算法思路。

Go 版本
基础知识：
1. **函数定义与调用**: `func generateMatrix(n int) [][]int` 定义了一个接受整数参数 `n` 的函数。
2. **条件判断**: 使用 `if` 条件判断语句进行不同情况的处理。
3. **数组操作**: 使用二维数组表示矩阵，通过数组索引进行访问和修改。


Python 版本
基础知识：
1. **类和方法**: 使用 `class Solution` 定义一个类，其中的 `generateMatrix` 方法是解决问题的主要逻辑。
2. **列表（List）操作**: 使用列表表示矩阵，通过索引访问和修改元素。
3. **循环与条件判断**: 使用 `for` 循环和 `if` 条件判断进行逻辑控制。


Java 版本
基础知识：
1. **类和方法**: 使用 `class Solution` 定义一个类，其中的 `generateMatrix` 方法是解决问题的主要逻辑。
2. **二维数组操作**: 使用二维数组表示矩阵，通过数组索引进行访问和修改。
3. **循环与条件判断**: 使用 `for` 循环和 `if` 条件判断进行逻辑控制。


C++ 版本
基础知识：
1. **类和方法**: 使用 `class Solution` 定义一个类，其中的 `generateMatrix` 方法是解决问题的主要逻辑。
2. **二维数组操作**: 使用二维数组表示矩阵，通过数组索引进行访问和修改。
3. **循环与条件判断**: 使用 `for` 循环和 `if` 条件判断进行逻辑控制。
