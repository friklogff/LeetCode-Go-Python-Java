# [63. Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)


## 题目

A robot is located at the top-left corner of a *m* x *n* grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

![](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

An obstacle and empty space is marked as `1` and `0` respectively in the grid.

**Note:** *m* and *n* will be at most 100.

**Example 1:**

    Input:
    [
      [0,0,0],
      [0,1,0],
      [0,0,0]
    ]
    Output: 2
    Explanation:
    There is one obstacle in the middle of the 3x3 grid above.
    There are two ways to reach the bottom-right corner:
    1. Right -> Right -> Down -> Down
    2. Down -> Down -> Right -> Right

## 题目大意

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？


## 解题思路

- 这一题是第 62 题的加强版。也是一道考察 DP 的简单题。
- 这一题比第 62 题增加的条件是地图中会出现障碍物，障碍物的处理方法是 `dp[i][j]=0`。
- 需要注意的一种情况是，起点就是障碍物，那么这种情况直接输出 0 。

每个版本的解题思路：

Go 版本解题思路：

1. 首先，检查输入网格是否为空或者起始格子就是障碍物，如果是则返回0，因为没有有效的路径。

2. 获取网格的行数和列数，分别存储在 `m` 和 `n` 变量中。

3. 创建一个二维数组 `dp` 用于存储路径数，初始化为0，其大小为 `m x n`。

4. 设置起始格子的路径数为1，因为只有一种方式可以到达起始格子。

5. 初始化第一行，如果前一个格子的路径数不为0且当前格子不是障碍物，则路径数为1。

6. 初始化第一列，如果上一个格子的路径数不为0且当前格子不是障碍物，则路径数为1。

7. 计算其余格子的路径数，如果当前格子不是障碍物，则路径数为上方格子和左方格子的路径数之和。

8. 返回右下角格子的路径数，即从左上角到右下角的不同路径数。

Python 版本解题思路：

1. 首先，检查输入网格是否为空或者起始格子就是障碍物，如果是则返回0，因为没有有效的路径。

2. 获取网格的行数和列数，分别存储在 `m` 和 `n` 变量中。

3. 创建一个二维列表 `dp` 用于存储路径数，初始化为0，其大小为 `m x n`。

4. 设置起始格子的路径数为1，因为只有一种方式可以到达起始格子。

5. 初始化第一行，如果前一个格子的路径数不为0且当前格子不是障碍物，则路径数为1。

6. 初始化第一列，如果上一个格子的路径数不为0且当前格子不是障碍物，则路径数为1。

7. 计算其余格子的路径数，如果当前格子不是障碍物，则路径数为上方格子和左方格子的路径数之和。

8. 返回右下角格子的路径数，即从左上角到右下角的不同路径数。

Java 版本解题思路：

1. 首先，检查输入网格是否为空或者起始格子就是障碍物，如果是则返回0，因为没有有效的路径。

2. 获取网格的行数和列数，分别存储在 `m` 和 `n` 变量中。

3. 创建一个二维数组 `dp` 用于存储路径数，初始化为0，其大小为 `m x n`。

4. 设置起始格子的路径数为1，因为只有一种方式可以到达起始格子。

5. 初始化第一行，如果前一个格子的路径数不为0且当前格子不是障碍物，则路径数为1。

6. 初始化第一列，如果上一个格子的路径数不为0且当前格子不是障碍物，则路径数为1。

7. 计算其余格子的路径数，如果当前格子不是障碍物，则路径数为上方格子和左方格子的路径数之和。

8. 返回右下角格子的路径数，即从左上角到右下角的不同路径数。

C++ 版本解题思路：

1. 首先，检查输入网格是否为空或者起始格子就是障碍物，如果是则返回0，因为没有有效的路径。

2. 获取网格的行数和列数，分别存储在 `m` 和 `n` 变量中。

3. 创建一个二维向量 `dp` 用于存储路径数，初始化为0，其大小为 `m x n`。

4. 设置起始格子的路径数为1，因为只有一种方式可以到达起始格子。

5. 初始化第一行，如果前一个格子的路径数不为0且当前格子不是障碍物，则路径数为1。

6. 初始化第一列，如果上一个格子的路径数不为0且当前格子不是障碍物，则路径数为1。

7. 计算其余格子的路径数，如果当前格子不是障碍物，则路径数为上方格子和左方格子的路径数之和。

8. 返回右下角格子的路径数，即从左上角到右下角的不同路径数。

这些解题思路都遵循动态规划的原理，通过填充一个二维数组来记录每个格子的路径数，最终计算出从起始点到目标点的不同路径数。
## 代码

## Go

```Go
func uniquePathsWithObstacles(obstacleGrid [][]int) int {
    // 检查输入网格是否为空或者起始格子就是障碍物，如果是则返回0
    if len(obstacleGrid) == 0 || obstacleGrid[0][0] == 1 {
        return 0
    }
    
    // 获取网格的行数和列数
    m, n := len(obstacleGrid), len(obstacleGrid[0])
    
    // 创建一个二维数组 dp 用于存储路径数，初始化为0
    dp := make([][]int, m)
    for i := 0; i < m; i++ {
        dp[i] = make([]int, n)
    }
    
    // 设置起始格子的路径数为1，因为只有一种方式可以到达起始格子
    dp[0][0] = 1
    
    // 初始化第一行，如果前一个格子的路径数不为0且当前格子不是障碍物，则路径数为1
    for i := 1; i < n; i++ {
        if dp[0][i-1] != 0 && obstacleGrid[0][i] != 1 {
            dp[0][i] = 1
        }
    }
    
    // 初始化第一列，如果上一个格子的路径数不为0且当前格子不是障碍物，则路径数为1
    for i := 1; i < m; i++ {
        if dp[i-1][0] != 0 && obstacleGrid[i][0] != 1 {
            dp[i][0] = 1
        }
    }
    
    // 计算其余格子的路径数，如果当前格子不是障碍物，则路径数为上方格子和左方格子的路径数之和
    for i := 1; i < m; i++ {
        for j := 1; j < n; j++ {
            if obstacleGrid[i][j] != 1 {
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            }
        }
    }
    
    // 返回右下角格子的路径数，即从左上角到右下角的不同路径数
    return dp[m-1][n-1]
}

```

## Python

```Python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        for i in range(1, n):
            if dp[0][i-1] != 0 and obstacleGrid[0][i] != 1:
                dp[0][i] = 1
        
        for i in range(1, m):
            if dp[i-1][0] != 0 and obstacleGrid[i][0] != 1:
                dp[i][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]

```

## Java

```Java
class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if (obstacleGrid == null || obstacleGrid[0][0] == 1) {
            return 0;
        }
        
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        
        int[][] dp = new int[m][n];
        dp[0][0] = 1;
        
        for (int i = 1; i < n; i++) {
            if (dp[0][i-1] != 0 && obstacleGrid[0][i] != 1) {
                dp[0][i] = 1;
            }
        }
        
        for (int i = 1; i < m; i++) {
            if (dp[i-1][0] != 0 && obstacleGrid[i][0] != 1) {
                dp[i][0] = 1;
            }
        }
        
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (obstacleGrid[i][j] != 1) {
                    dp[i][j] = dp[i-1][j] + dp[i][j-1];
                }
            }
        }
        
        return dp[m-1][n-1];
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        if (obstacleGrid.empty() || obstacleGrid[0][0] == 1) {
            return 0;
        }
        
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        
        vector<vector<int>> dp(m, vector<int>(n, 0));
        dp[0][0] = 1;
        
        for (int i = 1; i < n; i++) {
            if (dp[0][i-1] != 0 && obstacleGrid[0][i] != 1) {
                dp[0][i] = 1;
            }
        }
        
        for (int i = 1; i < m; i++) {
            if (dp[i-1][0] != 0 && obstacleGrid[i][0] != 1) {
                dp[i][0] = 1;
            }
        }
        
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (obstacleGrid[i][j] != 1) {
                    dp[i][j] = dp[i-1][j] + dp[i][j-1];
                }
            }
        }
        
        return dp[m-1][n-1];
    }
};

```
基础知识。

Go 版本：

1. **基本语法和数据结构**：了解 Go 的基本语法、变量声明、条件语句（if）、循环语句（for）、数组和切片的使用。

2. **二维数组**：理解如何声明和使用二维数组，以表示网格。

3. **动态规划（DP）**：了解动态规划的基本概念，包括如何使用DP数组解决问题以及如何进行状态转移。

4. **条件语句**：理解如何使用条件语句（if）来处理特殊情况，例如检查输入是否为空或者起始点是否是障碍物。

Python 版本：

1. **基本语法**：了解 Python 的基本语法，包括变量声明、条件语句（if）、循环语句（for）等。

2. **列表和二维列表**：掌握 Python 中列表和二维列表的使用，用于表示网格和DP数组。

3. **动态规划（DP）**：了解动态规划的概念和原理，包括如何定义状态和状态转移方程。

4. **类和方法**：Python 版本的解法使用了类和方法，了解如何定义类和实现方法。

Java 版本：

1. **基本语法**：掌握 Java 的基本语法，包括变量声明、条件语句（if）、循环语句（for）等。

2. **二维数组**：了解如何声明和使用二维数组，以表示网格。

3. **动态规划（DP）**：理解动态规划的概念，包括如何定义DP数组和状态转移。

4. **类和方法**：Java 版本的解法使用了类和方法，了解如何定义类和实现方法。

C++ 版本：

1. **基本语法**：了解 C++ 的基本语法，包括变量声明、条件语句（if）、循环语句（for）等。

2. **二维向量**：了解如何使用 C++ 的二维向量（vector<vector<int>>) 来表示网格和DP数组。

3. **动态规划（DP）**：理解动态规划的概念，包括如何定义DP数组和状态转移。

4. **类和方法**：C++ 版本的解法没有使用类，但了解如何定义和使用函数是有帮助的。

以上是每个版本解法所需要的基础知识，但不必担心一开始完全掌握所有这些概念。通过学习和实践，逐渐积累经验和技能，能够更好地理解和编写这些代码。如果需要深入了解任何特定概念，可以参考相关的编程教程和文档。