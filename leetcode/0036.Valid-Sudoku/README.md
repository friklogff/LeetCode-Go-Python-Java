# [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)


## 题目

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated **according to the following rules**:

1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the 9 `3x3` sub-boxes of the grid must contain the digits `1-9` without repetition.

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/04/12/250px-sudoku-by-l2g-20050714svg.png)

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character `'.'`.

**Example 1:**


    Input:
    [
      ["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    Output: true


**Example 2:**


    Input:
    [
      ["8","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    Output: false
    Explanation: Same as Example 1, except with the 5 in the top left corner being 
        modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


**Note:**

- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.
- The given board contain only digits `1-9` and the character `'.'`.
- The given board size is always `9x9`.

## 题目大意

判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

1. 数字 1-9 在每一行只能出现一次。
2. 数字 1-9 在每一列只能出现一次。
3. 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。


## 解题思路
以下是每个版本的解题思路的详细介绍：

Go 版本解题思路

1. 创建三个二维布尔数组：`rowbuf`、`colbuf`、`boxbuf`，分别用于缓存每行、每列和每个3x3的方框中数字是否已经出现。

2. 遍历数独棋盘，检查每个格子：
   - 如果格子包含字符 `'.'`，则跳过不处理。
   - 如果格子包含数字字符，将其转换为整数并检查是否已经在当前行、列或3x3方框中出现过。
   - 如果已经出现过，则返回 `false`，表示数独无效。
   - 否则，将更新缓存数组，标记该数字已经出现。

3. 如果通过上述检查，返回 `true`，表示数独是有效的。

Python 版本解题思路

1. 创建三个二维布尔数组：`row_used`、`col_used`、`cell_used`，用于记录每行、每列和每个3x3单元格中数字的出现情况。

2. 遍历数独棋盘，检查每个格子：
   - 如果格子包含字符 `'.'`，则跳过不处理。
   - 如果格子包含数字字符，将其转换为整数，并检查是否已经在当前行、列或3x3单元格中出现过。
   - 如果已经出现过，则返回 `false`，表示数独无效。
   - 否则，标记该数字在当前行、列和单元格中已经出现。

3. 如果通过上述检查，返回 `true`，表示数独是有效的。

ava 版本解题思路

1. 创建三个二维布尔数组：`rowbuf`、`colbuf`、`boxbuf`，分别用于缓存每行、每列和每个3x3的方框中数字是否已经出现。

2. 遍历数独棋盘，检查每个格子：
   - 如果格子包含字符 `'.'`，则跳过不处理。
   - 如果格子包含数字字符，将其转换为整数，并检查是否已经在当前行、列或3x3方框中出现过。
   - 如果已经出现过，则返回 `false`，表示数独无效。
   - 否则，将更新缓存数组，标记该数字已经出现。

3. 如果通过上述检查，返回 `true`，表示数独是有效的。

C++ 版本解题思路

1. 创建三个二维整数数组：`row`、`column`、`box`，用于跟踪每行、每列和每个3x3方框中数字的出现情况。

2. 遍历数独棋盘，检查每个格子：
   - 如果格子包含字符 `'.'`，则跳过不处理。
   - 如果格子包含数字字符，将其转换为整数并检查是否已经在当前行、列或3x3方框中出现过。
   - 如果已经出现过，则返回 `false`，表示数独无效。
   - 否则，将更新相应的计数器，标记该数字已经出现。

3. 如果通过上述检查，返回 `true`，表示数独是有效的。

## 代码

## Go

```Go
func isValidSudoku1(board [][]byte) bool {
    // 创建三个二维布尔数组，用于缓存每行、每列和每个3x3的方框中数字是否已经出现
    rowbuf, colbuf, boxbuf := make([][]bool, 9), make([][]bool, 9), make([][]bool, 9)
    for i := 0; i < 9; i++ {
        rowbuf[i] = make([]bool, 9)
        colbuf[i] = make([]bool, 9)
        boxbuf[i] = make([]bool, 9)
    }

    // 遍历一次，添加缓存
    for r := 0; r < 9; r++ {
        for c := 0; c < 9; c++ {
            if board[r][c] != '.' {
                // 将字符数字转换为整数
                num := board[r][c] - '0' - byte(1)
                
                // 检查行、列和3x3方格中是否已经出现相同的数字
                if rowbuf[r][num] || colbuf[c][num] || boxbuf[r/3*3+c/3][num] {
                    return false
                }
                
                // 更新缓存数组，标记数字已经出现
                rowbuf[r][num] = true
                colbuf[c][num] = true
                boxbuf[r/3*3+c/3][num] = true // r,c 转换到box方格中
            }
        }
    }
    
    // 如果通过上述检查，则数独有效
    return true
}

```

## Python

```Python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_used = [[False] * 9 for _ in range(9)]      # 记录每一行出现过的数字
        col_used = [[False] * 9 for _ in range(9)]      # 记录每一列出现过的数字
        cell_used = [[False] * 9 for _ in range(9)]     # 记录每一个单元格出现过的数字
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.': continue     # 不为数字的位置跳过处理
                char_id = int(board[r][c]) - 1      # 获取数字对应的编号（索引）
                
                # 检查当前数字是否已经在当前行、当前列或当前单元格中出现过
                if row_used[r][char_id] or col_used[c][char_id] or cell_used[r // 3 * 3 + c // 3][char_id]:
                    return False    # 如果出现重复，则数独无效
                
                # 否则标记该数字出现过
                row_used[r][char_id], col_used[c][char_id], cell_used[r // 3 * 3 + c // 3][char_id] = True, True, True  

        return True  # 如果通过了所有检查，数独是有效的

```

## Java

```Java
class Solution {
    public boolean isValidSudoku(char[][] board) {
        boolean[][] rowbuf = new boolean[9][9];
        boolean[][] colbuf = new boolean[9][9];
        boolean[][] boxbuf = new boolean[9][9];

        // 遍历一次，添加缓存
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] != '.') {
                    int num = board[r][c] - '1';
                    // 检查行
                    if (rowbuf[r][num]) {
                        return false;
                    }
                    rowbuf[r][num] = true;

                    // 检查列
                    if (colbuf[c][num]) {
                        return false;
                    }
                    colbuf[c][num] = true;

                    // 检查3x3的方框
                    int boxIndex = (r / 3) * 3 + c / 3;
                    if (boxbuf[boxIndex][num]) {
                        return false;
                    }
                    boxbuf[boxIndex][num] = true;
                }
            }
        }

        return true;
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int row[9][9] = {0}; // 用于跟踪每一行中数字的出现次数
        int column[9][9] = {0}; // 用于跟踪每一列中数字的出现次数
        int box[9][9] = {0}; // 用于跟踪每个3x3方框中数字的出现次数

        // 遍历数独棋盘
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                int box_index = i / 3 * 3 + j / 3; // 计算当前单元格属于哪个3x3方框
                int temp = board[i][j] - '0' - 1; // 将字符数字转换为整数，范围是0到8
                if (temp == -1) continue; // 如果是'.'，跳过当前单元格

                // 检查当前数字是否已经在当前行、当前列或当前方框中出现过
                if (row[i][temp] == 1 || column[j][temp] == 1 || box[box_index][temp] == 1) {
                    return false; // 如果出现重复，则数独无效
                }

                // 更新相应的计数器
                ++row[i][temp];
                ++column[j][temp];
                ++box[box_index][temp];
            }
        }

        return true; // 如果通过了所有检查，数独是有效的
    }
};

```
当涉及到不同编程语言版本的解决方案时，你需要了解一些基本概念和语法，以便理解代码的工作原理。以下是每个版本的详细基础知识要点：

Go 版本

- **数组和切片**: Go 中的数组是固定长度的，切片则是可变长度的。在本解决方案中，使用了切片来存储行、列和方框的数字出现情况。

- **二维数组**: Go 支持多维数组，因此可以轻松地创建二维数组来表示数独的棋盘和数字出现情况。

- **循环**: 使用 `for` 循环遍历二维数组中的所有元素，这在解决数独问题时非常有用。

- **条件语句**: 使用 `if` 条件语句来检查数字是否已经出现，并根据条件做出相应的处理。

- **类型转换**: 代码中使用了字符到整数的类型转换，将字符数字转换为整数以进行索引。

Python 版本

- **列表**: Python 中的列表（List）是可变序列，用于存储数独的棋盘和数字出现情况。

- **二维列表**: 通过嵌套列表，可以轻松地表示二维数据结构，例如数独棋盘和数字出现情况。

- **循环**: 使用 `for` 循环遍历二维列表中的所有元素，这在解决数独问题时非常有用。

- **条件语句**: 使用 `if` 条件语句来检查数字是否已经出现，并根据条件做出相应的处理。

- **类型转换**: 代码中使用了字符到整数的类型转换，将字符数字转换为整数以进行索引。

- **面向对象编程**: 解决方案使用了面向对象编程的风格，将检查数独有效性的逻辑封装在一个类中。

ava 版本

- **数组**: Java 中的数组是固定长度的，可以用于存储数独的棋盘和数字出现情况。

- **二维数组**: 使用二维数组来表示数独棋盘和数字出现情况。

- **循环**: 使用 `for` 循环遍历二维数组中的所有元素，这在解决数独问题时非常有用。

- **条件语句**: 使用 `if` 条件语句来检查数字是否已经出现，并根据条件做出相应的处理。

- **类型转换**: 代码中使用了字符到整数的类型转换，将字符数字转换为整数以进行索引。

C++ 版本

- **数组**: C++ 中的数组是固定长度的，可以用于存储数独的棋盘和数字出现情况。

- **二维数组**: 使用二维数组来表示数独棋盘和数字出现情况。

- **循环**: 使用 `for` 循环遍历二维数组中的所有元素，这在解决数独问题时非常有用。

- **条件语句**: 使用 `if` 条件语句来检查数字是否已经出现，并根据条件做出相应的处理。

- **类型转换**: 代码中使用了字符到整数的类型转换，将字符数字转换为整数以进行索引。

了解这些基础知识点可以帮助你理解每个版本的代码是如何实现数独验证的。此外，还需要了解数组和循环的基本概念，以便更好地理解代码的工作原理。