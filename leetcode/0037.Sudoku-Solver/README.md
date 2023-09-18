# [37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)

## 题目

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy**all of the following rules**:

1. Each of the digits`1-9`must occur exactly once in each row.
2. Each of the digits`1-9`must occur exactly once in each column.
3. Each of the the digits`1-9`must occur exactly once in each of the 9`3x3`sub-boxes of the grid.

Empty cells are indicated by the character`'.'`.

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/04/12/250px-sudoku-by-l2g-20050714svg.png)

A sudoku puzzle...

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/04/12/250px-sudoku-by-l2g-20050714_solutionsvg.png)

...and its solution numbers marked in red.

**Note:**

- The given board contain only digits`1-9`and the character`'.'`.
- You may assume that the given Sudoku puzzle will have a single unique solution.
- The given board size is always`9x9`.

## 题目大意

编写一个程序，通过已填充的空格来解决数独问题。一个数独的解法需遵循如下规则：

1. 数字 1-9 在每一行只能出现一次。
2. 数字 1-9 在每一列只能出现一次。
3. 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

空白格用 '.'表示。

## 解题思路


Go版本解题思路：

1. **定义结构体和数据结构**：首先，定义一个结构体 `position` 用于表示数独中的位置（行和列）。创建一个空的 `position` 切片，用于存储待填入数字的位置信息。还需要定义一个布尔变量 `find` 用于表示是否找到解。

2. **遍历数独格子**：遍历数独的每个格子，如果当前格子是'.'，表示需要填入数字，将其位置信息加入 `position` 切片。

3. **DFS暴力回溯枚举**：使用深度优先搜索（DFS）进行暴力回溯枚举。在每个空格位置，尝试填入数字1到9，然后检查是否符合数独规则。如果符合规则，继续递归填充下一个位置。如果找到解，将 `find` 设置为 `true` 并返回。

4. **检查数独规则**：在每个位置填入数字时，需要检查以下三个规则是否满足：
   - 横行是否有重复数字
   - 竖行是否有重复数字
   - 九宫格是否有重复数字

5. **回溯和重置**：如果在当前位置填入数字后没有找到解，需要将该位置重置为'.'，继续尝试下一个数字。

6. **完成解题**：当找到一组解时，设置 `find` 为 `true` 并返回。此时不需要继续回溯。

Python版本解题思路：

Python版本的解题思路与Go版本类似，主要区别在于语法和数据结构的表示方式。具体解题思路如下：

1. **定义类和方法**：使用Python的类和方法来组织代码。定义一个类 `Solution` 用于解决数独问题。

2. **递归解法**：采用深度优先搜索（DFS）的递归解法。创建 `dfs` 方法，其中主要逻辑与Go版本相似。

3. **位运算**：使用位运算来检查数字的合法性，如按位与、按位或、按位异或等。

4. **列表（List）**：Python中使用列表（List）来存储待填入数字的位置信息和进行判断。

5. **回溯和重置**：当在当前位置填入数字后没有找到解时，需要将该位置重置为'.'，继续尝试下一个数字。

Java版本解题思路：

Java版本的解题思路与Python版本类似，主要区别在于语法和数据结构的表示方式。具体解题思路如下：

1. **定义类和方法**：Java是面向对象编程语言，因此使用类和方法的方式来组织代码。定义一个类 `Solution` 用于解决数独问题。

2. **递归解法**：采用深度优先搜索（DFS）的递归解法。创建 `dfs` 方法，其中主要逻辑与Python版本相似。

3. **位运算**：使用位运算来检查数字的合法性，如按位与、按位或、按位异或等。

4. **列表（List）**：Java中使用List来存储待填入数字的位置信息和进行判断。

5. **回溯和重置**：当在当前位置填入数字后没有找到解时，需要将该位置重置为'.'，继续尝试下一个数字。

C++版本解题思路：

C++版本的解题思路与Go、Python、Java版本类似，主要区别在于语法和数据结构的表示方式。具体解题思路如下：

1. **定义类和函数**：C++使用类和函数的方式来组织代码。定义一个类 `Solution` 用于解决数独问题。

2. **递归解法**：采用深度优先搜索（DFS）的递归解法。创建 `dfs` 方法，其中主要逻辑与其他版本相似。

3. **位运算**：使用位运算来检查数字的合法性，如按位与、按位或、按位异或等。

4. **向量（Vector）**：C++中使用向量（Vector）来存储待填入数字的位置信息和进行判断。

5. **回溯和重置**：当在当前位置填入数字后没有找到解时，需要将该位置重置为'.'，继续尝试下一个数字。

总的来说，无论使用哪种编程语言，解数独问题的基本思路是使用深度优先搜索（DFS）进行回溯枚举，同时利用位运算和合适的数据结构来检查和记录数字的合法性。这些思路在不同编程语言中都是通用的，只需根据语言的特点进行相应的实现。
## 代码

## Go

```Go
// 定义一个结构体 position，表示数独中的位置（行和列）
type position struct {
    x int // 行
    y int // 列
}

// 主函数，用于解数独
func solveSudoku(board [][]byte) {
    // 创建一个空的 position 切片，用于存储待填入数字的位置信息
    pos, find := []position{}, false

    // 遍历数独的每个格子
    for i := 0; i < len(board); i++ {
        for j := 0; j < len(board[0]); j++ {
            // 如果当前格子是'.'，表示需要填入数字，将其位置信息加入 pos 切片
            if board[i][j] == '.' {
                pos = append(pos, position{x: i, y: j})
            }
        }
    }

    // 调用 putSudoku 函数来填充数独
    putSudoku(&board, pos, 0, &find)
}

// 递归函数，用于填充数独
func putSudoku(board *[][]byte, pos []position, index int, succ *bool) {
    // 如果已经成功找到解决方案，则返回
    if *succ == true {
        return
    }
    // 如果已经遍历完了所有待填入的位置，则表示找到了解决方案
    if index == len(pos) {
        *succ = true
        return
    }
    // 尝试填入数字 1 到 9
    for i := 1; i < 10; i++ {
        // 检查当前位置是否可以填入数字 i，同时确保还没有找到解决方案
        if checkSudoku(board, pos[index], i) && !*succ {
            // 填入数字 i
            (*board)[pos[index].x][pos[index].y] = byte(i) + '0'
            // 递归调用 putSudoku 函数，继续填充下一个位置
            putSudoku(board, pos, index+1, succ)
            // 如果已经找到解决方案，返回
            if *succ == true {
                return
            }
            // 如果在当前位置填入数字 i 后没有找到解决方案，则将其重置为'.'，继续尝试下一个数字
            (*board)[pos[index].x][pos[index].y] = '.'
        }
    }
}

// 检查当前位置是否可以填入指定的数字
func checkSudoku(board *[][]byte, pos position, val int) bool {
    // 判断横行是否有重复数字
    for i := 0; i < len((*board)[0]); i++ {
        if (*board)[pos.x][i] != '.' && int((*board)[pos.x][i]-'0') == val {
            return false
        }
    }
    // 判断竖行是否有重复数字
    for i := 0; i < len((*board)); i++ {
        if (*board)[i][pos.y] != '.' && int((*board)[i][pos.y]-'0') == val {
            return false
        }
    }
    // 判断九宫格是否有重复数字
    posx, posy := pos.x-pos.x%3, pos.y-pos.y%3
    for i := posx; i < posx+3; i++ {
        for j := posy; j < posy+3; j++ {
            if (*board)[i][j] != '.' && int((*board)[i][j]-'0') == val {
                return false
            }
        }
    }
    // 如果以上条件都不满足，说明可以填入该数字
    return true
}

```

## Python

```Python
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # 定义翻转位的函数，用于更新行、列和块的状态
        def flip(i: int, j: int, digit: int):
            line[i] ^= (1 << digit)
            column[j] ^= (1 << digit)
            block[i // 3][j // 3] ^= (1 << digit)

        # 深度优先搜索函数
        def dfs(pos: int):
            nonlocal valid
            if pos == len(spaces):  # 如果所有空格都填满了，找到了解
                valid = True
                return

            i, j = spaces[pos]  # 获取当前空格的坐标
            # 计算当前可以填入的数字的掩码
            mask = ~(line[i] | column[j] | block[i // 3][j // 3]) & 0x1ff
            while mask:
                digitMask = mask & (-mask)  # 获取最低位的1
                digit = bin(digitMask).count("0") - 1  # 计算数字
                flip(i, j, digit)  # 更新状态
                board[i][j] = str(digit + 1)  # 填入数字
                dfs(pos + 1)  # 递归下一个空格
                flip(i, j, digit)  # 恢复状态
                mask &= (mask - 1)  # 去掉最低位的1
                if valid:
                    return

        line = [0] * 9  # 记录每一行的数字状态
        column = [0] * 9  # 记录每一列的数字状态
        block = [[0] * 3 for _ in range(3)]  # 记录每个块的数字状态
        valid = False  # 记录是否找到解
        spaces = list()  # 记录所有空格的坐标

        # 遍历数独，初始化状态
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    digit = int(board[i][j]) - 1
                    flip(i, j, digit)

        # 不断尝试填充数字，直到不能再填充为止
        while True:
            modified = False
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        mask = ~(line[i] | column[j] | block[i // 3][j // 3]) & 0x1ff
                        if not (mask & (mask - 1)):  # 如果mask中只有一个1，即只有一种可能的数字
                            digit = bin(mask).count("0") - 1
                            flip(i, j, digit)
                            board[i][j] = str(digit + 1)
                            modified = True
            if not modified:
                break  # 如果没有发生改变，说明无法再填充了

        # 找到所有空格的坐标
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    spaces.append((i, j))

        dfs(0)  # 开始深度优先搜索，填充剩余的空格

```

## Java

```Java
class Solution {
    private int[] line = new int[9];  // 记录每一行的数字状态
    private int[] column = new int[9];  // 记录每一列的数字状态
    private int[][] block = new int[3][3];  // 记录每个块的数字状态
    private boolean valid = false;  // 记录是否找到解
    private List<int[]> spaces = new ArrayList<int[]>();  // 记录所有空格的坐标

    public void solveSudoku(char[][] board) {
        // 初始化行、列和块的状态
        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                if (board[i][j] != '.') {
                    int digit = board[i][j] - '0' - 1;
                    flip(i, j, digit);
                }
            }
        }

        // 不断尝试填充数字，直到不能再填充为止
        while (true) {
            boolean modified = false;
            for (int i = 0; i < 9; ++i) {
                for (int j = 0; j < 9; ++j) {
                    if (board[i][j] == '.') {
                        int mask = ~(line[i] | column[j] | block[i / 3][j / 3]) & 0x1ff;
                        if ((mask & (mask - 1)) == 0) {  // 如果mask中只有一个1，即只有一种可能的数字
                            int digit = Integer.bitCount(mask - 1);
                            flip(i, j, digit);
                            board[i][j] = (char) (digit + '0' + 1);
                            modified = true;
                        }
                    }
                }
            }
            if (!modified) {
                break;  // 如果没有发生改变，说明无法再填充了
            }
        }

        // 找到所有空格的坐标
        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                if (board[i][j] == '.') {
                    spaces.add(new int[]{i, j});
                }
            }
        }

        dfs(board, 0);  // 开始深度优先搜索，填充剩余的空格
    }

    public void dfs(char[][] board, int pos) {
        if (pos == spaces.size()) {  // 如果所有空格都填满了，找到了解
            valid = true;
            return;
        }

        int[] space = spaces.get(pos);
        int i = space[0], j = space[1];
        int mask = ~(line[i] | column[j] | block[i / 3][j / 3]) & 0x1ff;
        for (; mask != 0 && !valid; mask &= (mask - 1)) {
            int digitMask = mask & (-mask);
            int digit = Integer.bitCount(digitMask - 1);
            flip(i, j, digit);
            board[i][j] = (char) (digit + '0' + 1);
            dfs(board, pos + 1);
            flip(i, j, digit);
        }
    }

    public void flip(int i, int j, int digit) {
        line[i] ^= (1 << digit);
        column[j] ^= (1 << digit);
        block[i / 3][j / 3] ^= (1 << digit);
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        vector<int> line(9, 0);  // 记录每一行的数字状态
        vector<int> column(9, 0);  // 记录每一列的数字状态
        vector<vector<int>> block(3, vector<int>(3, 0));  // 记录每个块的数字状态
        bool valid = false;  // 记录是否找到解
        vector<pair<int, int>> spaces;  // 记录所有空格的坐标

        // 初始化行、列和块的状态
        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                if (board[i][j] != '.') {
                    int digit = board[i][j] - '0' - 1;
                    flip(line, column, block, i, j, digit);
                }
            }
        }

        // 不断尝试填充数字，直到不能再填充为止
        while (true) {
            bool modified = false;
            for (int i = 0; i < 9; ++i) {
                for (int j = 0; j < 9; ++j) {
                    if (board[i][j] == '.') {
                        int mask = ~(line[i] | column[j] | block[i / 3][j / 3]) & 0x1ff;
                        if ((mask & (mask - 1)) == 0) {  // 如果mask中只有一个1，即只有一种可能的数字
                            int digit = __builtin_popcount(mask - 1);
                            flip(line, column, block, i, j, digit);
                            board[i][j] = digit + '0' + 1;
                            modified = true;
                        }
                    }
                }
            }
            if (!modified) {
                break;  // 如果没有发生改变，说明无法再填充了
            }
        }

        // 找到所有空格的坐标
        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                if (board[i][j] == '.') {
                    spaces.push_back({i, j});
                }
            }
        }

        dfs(board, line, column, block, spaces, 0, valid);  // 开始深度优先搜索，填充剩余的空格
    }

    void dfs(vector<vector<char>>& board, vector<int>& line, vector<int>& column, vector<vector<int>>& block, vector<pair<int, int>>& spaces, int pos, bool& valid) {
        if (pos == spaces.size()) {  // 如果所有空格都填满了，找到了解
            valid = true;
            return;
        }

        pair<int, int> space = spaces[pos];
        int i = space.first, j = space.second;
        int mask = ~(line[i] | column[j] | block[i / 3][j / 3]) & 0x1ff;
        for (; mask != 0 && !valid; mask &= (mask - 1)) {
            int digitMask = mask & -mask;
            int digit = __builtin_ctz(digitMask);
            flip(line, column, block, i, j, digit);
            board[i][j] = digit + '0' + 1;
            dfs(board, line, column, block, spaces, pos + 1, valid);
            flip(line, column, block, i, j, digit);
        }
    }

    void flip(vector<int>& line, vector<int>& column, vector<vector<int>>& block, int i, int j, int digit) {
        line[i] ^= (1 << digit);
        column[j] ^= (1 << digit);
        block[i / 3][j / 3] ^= (1 << digit);
    }
};

```
这里分别介绍了Go、Python、Java和C++版本的知识要点：

Go版本：

1. **结构体（Struct）**：在Go中，你会看到使用结构体（Struct）来表示数独中的位置信息，如行和列。

2. **递归**：解决数独问题的主要算法是深度优先搜索（DFS）递归。你需要理解递归的概念和如何在Go中实现递归函数。

3. **切片（Slice）**：你会使用切片来存储待填入数字的位置信息和进行判断。

4. **位运算**：位运算是判断数字是否合法的关键。你需要了解Go中的位运算，如按位与、按位或、按位异或等操作，以及如何使用它们来检查数字的合法性。

Python版本：

1. **类和方法**：Python中使用类和方法的方式来组织代码。你需要了解如何定义类、方法，以及如何在类中进行数据操作。

2. **递归**：Python版本也使用深度优先搜索（DFS）递归来解决数独问题。了解递归的概念和如何在Python中实现递归函数是必要的。

3. **位运算**：位运算在Python中同样是关键，用于检查数字的合法性。你需要了解Python中的位运算操作，如按位与、按位或、按位异或等。

4. **列表（List）**：Python中的列表用于存储待填入数字的位置信息和进行判断。

Java版本：

1. **类和方法**：Java是一种面向对象编程语言，你需要了解如何定义类、方法，以及如何在类中进行数据操作。

2. **递归**：Java版本同样使用深度优先搜索（DFS）递归来解决数独问题。了解递归的概念和如何在Java中实现递归函数是必要的。

3. **位运算**：位运算在Java中同样是关键，用于检查数字的合法性。你需要了解Java中的位运算操作，如按位与、按位或、按位异或等。

4. **列表（List）**：Java中的List用于存储待填入数字的位置信息和进行判断。你需要了解如何操作List。

C++版本：

1. **类和函数**：C++使用类和函数的方式来组织代码。你需要了解如何定义类、函数，以及如何在类中进行数据操作。

2. **递归**：C++版本同样使用深度优先搜索（DFS）递归来解决数独问题。了解递归的概念和如何在C++中实现递归函数是必要的。

3. **位运算**：位运算在C++中同样是关键，用于检查数字的合法性。你需要了解C++中的位运算操作，如按位与、按位或、按位异或等。

4. **向量（Vector）**：C++中的向量（Vector）类似于动态数组，用于存储待填入数字的位置信息和进行判断。你需要了解如何操作向量。

总的来说，无论你使用哪种编程语言，掌握递归、数据结构（如切片、列表、向量）的使用，以及位运算的基本概念和操作，都是解决数独问题的关键。此外，了解如何在特定编程语言中实现这些概念和操作也是必要的。