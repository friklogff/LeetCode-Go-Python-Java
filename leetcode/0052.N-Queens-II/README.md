# [52. N-Queens II](https://leetcode.com/problems/n-queens-ii/)


## 题目

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

![](https://assets.leetcode.com/uploads/2018/10/12/8-queens.png)

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

**Example:**


    Input: 4
    Output: 2
    Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
    [
     [".Q..",  // Solution 1
      "...Q",
      "Q...",
      "..Q."],
    
     ["..Q.",  // Solution 2
      "Q...",
      "...Q",
      ".Q.."]
    ]


## 题目大意

给定一个整数 n，返回 n 皇后不同的解决方案的数量。

## 解题思路

- 这一题是第 51 题的加强版，在第 51 题的基础上累加记录解的个数即可。
- 这一题也可以暴力打表法，时间复杂度为 O(1)。

当然，让我们分别介绍每个版本的解题思路：

Go 版本的解题思路

Go 版本的解决方案采用深度优先搜索（DFS）和回溯法来解决 N 皇后问题。下面是解题思路的关键步骤：

1. 创建并初始化用于记录列、两个对角线是否被占用的布尔数组，以及记录每行皇后位置的整数切片，还有结果的变量。

2. 从第一行开始，递归尝试在每一行放置皇后，直到达到最后一行。每次放置皇后时，需要检查当前列、两个对角线是否被占用。

3. 如果某一行可以放置皇后，将皇后位置记录在整数切片中，并更新列、对角线的占用情况。

4. 继续递归到下一行，重复相同的过程。

5. 当放置完成所有行时，计数结果加1，表示找到了一种解法。

6. 回溯到上一行，撤销当前行的皇后放置，继续尝试下一列。

7. 重复上述步骤，直到找到所有解法。

Python 版本的解题思路

Python 版本的解决方案也采用深度优先搜索（DFS）和回溯法来解决 N 皇后问题。解题思路与 Go 版本基本相同：

1. 创建并初始化用于记录列、两个对角线是否被占用的布尔数组，以及记录每行皇后位置的整数切片。

2. 从第一行开始，递归尝试在每一行放置皇后，直到达到最后一行。每次放置皇后时，需要检查当前列、两个对角线是否被占用。

3. 如果某一行可以放置皇后，将皇后位置记录在整数切片中，并更新列、对角线的占用情况。

4. 继续递归到下一行，重复相同的过程。

5. 当放置完成所有行时，计数结果加1，表示找到了一种解法。

6. 回溯到上一行，撤销当前行的皇后放置，继续尝试下一列。

7. 重复上述步骤，直到找到所有解法。

Java 版本的解题思路

Java 版本的解决方案同样采用深度优先搜索（DFS）和回溯法来解决 N 皇后问题。解题思路如下：

1. 创建并初始化用于记录列、两个对角线是否被占用的布尔数组，以及记录每行皇后位置的整数数组。

2. 从第一行开始，递归尝试在每一行放置皇后，直到达到最后一行。每次放置皇后时，需要检查当前列、两个对角线是否被占用。

3. 如果某一行可以放置皇后，将皇后位置记录在整数数组中，并更新列、对角线的占用情况。

4. 继续递归到下一行，重复相同的过程。

5. 当放置完成所有行时，计数结果加1，表示找到了一种解法。

6. 回溯到上一行，撤销当前行的皇后放置，继续尝试下一列。

7. 重复上述步骤，直到找到所有解法。

C++ 版本的解题思路

C++ 版本的解决方案也使用深度优先搜索（DFS）和回溯法来解决 N 皇后问题。以下是解题思路的关键步骤：

1. 使用位运算来高效地记录列、两个对角线是否被占用。其中，列使用一个整数表示，每一位表示一列是否被占用；两个对角线也分别使用整数来表示。

2. 从第一行开始，递归尝试在每一行放置皇后，直到达到最后一行。在每一行，通过位运算来检查当前列、两个对角线是否被占用。

3. 如果某一行可以放置皇后，使用位运算将皇后位置标记为被占用，并继续递归到下一行。

4. 当放置完成所有行时，计数结果加1，表示找到了一种解法。

5. 回溯到上一行，撤销当前行的皇后放置，继续尝试下一列。

6. 重复上述步骤，直到找到所有解法。

总的来说，这些版本的解题思路都涉及深度优先搜索和回溯，同时使用不同的数据结构和语言特性来实现相同的算法。理解递归、回溯以及位运算对于理解这些解决方案非常重要。
## 代码

## Go

```Go
// 解法二，DFS 回溯法
func totalNQueens(n int) int {
    // 创建并初始化用于记录列、两个对角线是否被占用的布尔数组，
    // 以及记录每行皇后位置的数组，以及结果的变量
    col, dia1, dia2, row, res := make([]bool, n), make([]bool, 2*n-1), make([]bool, 2*n-1), []int{}, 0
    // 调用递归函数放置皇后并计算结果
    putQueen52(n, 0, &col, &dia1, &dia2, &row, &res)
    // 返回结果
    return res
}

// 尝试在一个n皇后问题中, 摆放第index行的皇后位置
func putQueen52(n, index int, col, dia1, dia2 *[]bool, row *[]int, res *int) {
    // 当摆放完成所有行时，计数结果加1
    if index == n {
        *res++
        return
    }

    // 遍历当前行的每一列，尝试放置皇后
    for i := 0; i < n; i++ {
        // 检查当前列、两个对角线是否被占用
        if !(*col)[i] && !(*dia1)[index+i] && !(*dia2)[index-i+n-1] {
            // 如果没有被占用，将皇后放置在当前位置
            (*row) = append((*row), i)
            (*col)[i] = true
            (*dia1)[index+i] = true
            (*dia2)[index-i+n-1] = true
            // 递归放置下一行的皇后
            putQueen52(n, index+1, col, dia1, dia2, row, res)
            // 回溯，撤销当前行的皇后放置，继续尝试下一列
            (*col)[i] = false
            (*dia1)[index+i] = false
            (*dia2)[index-i+n-1] = false
            (*row) = (*row)[:len(*row)-1]
        }
    }
    return
}

```

## Python

```Python
class Solution:
    def totalNQueens(self, n: int) -> int:
        # 计算可以放置皇后的列的位掩码，limit 为一个 n 位的二进制数，所有位都为 1
        limit = (1 << n) - 1
        # 调用 process 函数，初始时传入全0的状态，表示没有皇后被放置
        return self.process(limit, 0, 0, 0)

    def process(self, limit, colLim, leftDiaLim, rightDiaLim):
        # 如果所有列都已经放置了皇后，表示找到了一种解法，返回 1
        if colLim == limit:
            return 1

        mostRight = 0
        # 计算当前行可以放置皇后的位置，pos 为一个二进制数，1 表示可以放置皇后的位置
        pos = limit & (~(colLim | leftDiaLim | rightDiaLim))
        res = 0
        while pos != 0:
            # 取出最右边的 1，表示在该位置放置皇后
            mostRight = pos & (~pos + 1)
            pos = pos - mostRight
            # 递归调用 process 函数，放置下一行的皇后，并累加解的数量
            res += self.process(limit, colLim | mostRight, (leftDiaLim | mostRight) << 1, (rightDiaLim | mostRight) >> 1)
        # 返回总解的数量
        return res

```

## Java

```Java
class Solution {
    public int totalNQueens(int n) {
        boolean[] col = new boolean[n];
        boolean[] dia1 = new boolean[2 * n - 1];
        boolean[] dia2 = new boolean[2 * n - 1];
        int[] row = new int[n];
        int[] res = new int[1];
        putQueen(n, 0, col, dia1, dia2, row, res);
        return res[0];
    }

    private void putQueen(int n, int index, boolean[] col, boolean[] dia1, boolean[] dia2, int[] row, int[] res) {
        if (index == n) {
            res[0]++;
            return;
        }

        for (int i = 0; i < n; i++) {
            if (!col[i] && !dia1[index + i] && !dia2[index - i + n - 1]) {
                row[index] = i;
                col[i] = true;
                dia1[index + i] = true;
                dia2[index - i + n - 1] = true;
                putQueen(n, index + 1, col, dia1, dia2, row, res);
                col[i] = false;
                dia1[index + i] = false;
                dia2[index - i + n - 1] = false;
            }
        }
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    int totalNQueens(int n) {
        // 调用 solve 函数，初始时传入全0的状态，表示没有皇后被放置
        return solve(n, 0, 0, 0, 0);
    }

    int solve(int n, int row, int columns, int diagonals1, int diagonals2) {
        // 如果已经放置了 n 个皇后，表示找到了一种解法，返回 1
        if (row == n) {
            return 1;
        } else {
            int count = 0;
            // 计算当前行可用的位置，通过位运算得到一个二进制数，1 表示可以放置皇后的位置
            int availablePositions = ((1 << n) - 1) & (~(columns | diagonals1 | diagonals2));
            
            // 遍历所有可用的位置
            while (availablePositions != 0) {
                // 取出最低位的 1，表示在该位置放置皇后
                int position = availablePositions & (-availablePositions);
                // 将该位置从可用位置中移除
                availablePositions = availablePositions & (availablePositions - 1);
                // 递归调用 solve 函数，放置下一行的皇后，并累加解的数量
                count += solve(n, row + 1, columns | position, (diagonals1 | position) << 1, (diagonals2 | position) >> 1);
            }
            // 返回总解的数量
            return count;
        }
    }
};

```
当然，让我们分别介绍每个版本的代码以及它们所需的基础知识：

Go 版本

Go 版本的代码是一个使用深度优先搜索（DFS）和回溯法的解决方案，用于解决 N 皇后问题。以下是代码中涉及的基础知识：

1. **数组和切片**：Go 中的数组和切片是重要的数据结构，用于存储和处理数据。在这个问题中，使用了多个布尔数组来跟踪已占用的列和对角线，以及一个整数切片来记录每行的皇后位置。

2. **递归和回溯**：该解决方案使用递归来尝试放置皇后，并通过回溯来撤销不可行的解决方案。递归是解决 N 皇后问题的关键。

3. **位运算**：位运算用于快速检查列、对角线是否被占用，以及在哪里放置皇后。这是该算法的关键部分。

Python 版本

Python 版本的代码也是一个使用深度优先搜索（DFS）和回溯法的解决方案。以下是代码中涉及的基础知识：

1. **递归和回溯**：和 Go 版本一样，Python 版本也使用递归来尝试放置皇后，并通过回溯来撤销不可行的解决方案。递归是解决 N 皇后问题的关键。

2. **位运算**：位运算用于快速检查列、对角线是否被占用，以及在哪里放置皇后。这是该算法的关键部分。

Java 版本

Java 版本的代码也是一个使用深度优先搜索（DFS）和回溯法的解决方案。以下是代码中涉及的基础知识：

1. **数组和列表**：Java 中的数组和列表（ArrayList）用于存储和处理数据。在这个问题中，使用了多个布尔数组来跟踪已占用的列和对角线，以及一个整数数组来记录每行的皇后位置。

2. **递归和回溯**：该解决方案使用递归来尝试放置皇后，并通过回溯来撤销不可行的解决方案。递归是解决 N 皇后问题的关键。

C++ 版本

C++ 版本的代码也是一个使用深度优先搜索（DFS）和回溯法的解决方案。以下是代码中涉及的基础知识：

1. **位运算**：C++ 版本中使用了位运算来快速检查列、对角线是否被占用，以及在哪里放置皇后。这是该算法的关键部分。

2. **递归和回溯**：该解决方案使用递归来尝试放置皇后，并通过回溯来撤销不可行的解决方案。递归是解决 N 皇后问题的关键。

总的来说，无论使用哪种编程语言，解决 N 皇后问题的关键概念包括递归、回溯和位运算。理解这些概念将有助于理解和实现这些代码。