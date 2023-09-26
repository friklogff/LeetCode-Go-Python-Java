# [51. N-Queens](https://leetcode.com/problems/n-queens/)

## 题目

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

![](https://assets.leetcode.com/uploads/2018/10/12/8-queens.png)

Given an integer*n*, return all distinct solutions to the*n*-queens puzzle.

Each solution contains a distinct board configuration of the*n*-queens' placement, where`'Q'`and`'.'`both indicate a
queen and an empty space respectively.

**Example:**

    Input: 4
    Output: [
     [".Q..",  // Solution 1
      "...Q",
      "Q...",
      "..Q."],
    
     ["..Q.",  // Solution 2
      "Q...",
      "...Q",
      ".Q.."]
    ]
    Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

## 题目大意

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.'
分别代表了皇后和空位。

## 解题思路

- 求解 n 皇后问题
- 利用 col 数组记录列信息，col 有 `n` 列。用 dia1，dia2 记录从左下到右上的对角线，从左上到右下的对角线的信息，dia1 和 dia2
  分别都有 `2*n-1` 个。
- dia1 对角线的规律是 `i + j 是定值`，例如[0,0]，为 0；[1,0]、[0,1] 为 1；[2,0]、[1,1]、[0,2] 为 2；
- dia2 对角线的规律是 `i - j 是定值`，例如[0,7]，为 -7；[0,6]、[1,7] 为 -6；[0,5]、[1,6]、[2,7] 为 -5；为了使他们从 0 开始，i -
  j + n - 1 偏移到 0 开始，所以 dia2 的规律是 `i - j + n - 1 为定值`。
-

还有一个位运算的方法，每行只能选一个位置放皇后，那么对每行遍历可能放皇后的位置。如何高效判断哪些点不能放皇后呢？这里的做法毕竟巧妙，把所有之前选过的点按照顺序存下来，然后根据之前选的点到当前行的距离，就可以快速判断是不是会有冲突。举个例子:
假如在 4 皇后问题中，如果第一二行已经选择了位置 [1, 3]，那么在第三行选择时，首先不能再选 1, 3 列了，而对于第三行， 1
距离长度为2，所以它会影响到 -1, 3 两个列。同理，3 在第二行，距离第三行为 1，所以 3 会影响到列 2, 4。由上面的结果，我们知道 -1,
4 超出边界了不用去管，别的不能选的点是 1, 2, 3，所以第三行就只能选 0。在代码实现中，可以在每次遍历前根据之前选择的情况生成一个
occupied 用来记录当前这一行，已经被选了的和由于之前皇后攻击范围所以不能选的位置，然后只选择合法的位置进入到下一层递归。另外就是预处理了一个皇后放不同位置的字符串，这样这些字符串在返回结果的时候是可以在内存中复用的，省一点内存。
当然，让我们分别介绍每个版本的解题思路：

Go 版本解题思路：

1. **递归回溯法**：Go
   版本的解决方法采用了递归回溯法。从第一行开始，尝试在每一行的每一列放置皇后，然后递归进入下一行。如果在某一行找到一个可行的皇后位置，就继续下一行的放置。如果找不到合适的位置，就回溯到上一行，尝试其他列的位置，直到找到所有可能的解。

2. **布尔数组**：为了确保皇后不会互相攻击，使用了布尔数组 `col`、`dia1` 和 `dia2`
   来跟踪哪些列和对角线已被占用。这些数组的索引表示列号和对角线编号，值为 `true` 表示已被占用，值为 `false` 表示可用。

3. **生成棋盘**：在找到一个解之后，使用 `generateBoard` 函数生成棋盘，将皇后位置标记为 'Q'，并将棋盘添加到结果中。

Python 版本解题思路：

1. **递归回溯法**：Python 版本的解决方法也采用了递归回溯法，与 Go
   版本相似。从第一行开始，尝试在每一行的每一列放置皇后，然后递归进入下一行。如果在某一行找到一个可行的皇后位置，就继续下一行的放置。如果找不到合适的位置，就回溯到上一行，尝试其他列的位置，直到找到所有可能的解。

2. **布尔列表**：为了确保皇后不会互相攻击，使用了布尔列表 `col`、`dia1` 和 `dia2`
   来跟踪哪些列和对角线已被占用。这些列表的索引表示列号和对角线编号，值为 `True` 表示已被占用，值为 `False` 表示可用。

3. **生成棋盘**：在找到一个解之后，使用 `generateBoard` 函数生成棋盘，将皇后位置标记为 'Q'，并将棋盘添加到结果中。

Java 版本解题思路：

1. **递归回溯法**：Java
   版本的解决方法同样采用了递归回溯法。从第一行开始，尝试在每一行的每一列放置皇后，然后递归进入下一行。如果在某一行找到一个可行的皇后位置，就继续下一行的放置。如果找不到合适的位置，就回溯到上一行，尝试其他列的位置，直到找到所有可能的解。

2. **布尔数组**：为了确保皇后不会互相攻击，使用了布尔数组 `col`、`dia1` 和 `dia2`
   来跟踪哪些列和对角线已被占用。这些数组的索引表示列号和对角线编号，值为 `true` 表示已被占用，值为 `false` 表示可用。

3. **生成棋盘**：在找到一个解之后，使用 `generateBoard` 函数生成棋盘，将皇后位置标记为 'Q'，并将棋盘添加到结果中。

C++ 版本解题思路：

1. **递归回溯法**：C++
   版本的解决方法也采用了递归回溯法，与其他版本相似。从第一行开始，尝试在每一行的每一列放置皇后，然后递归进入下一行。如果在某一行找到一个可行的皇后位置，就继续下一行的放置。如果找不到合适的位置，就回溯到上一行，尝试其他列的位置，直到找到所有可能的解。

2. **布尔向量**：为了确保皇后不会互相攻击，使用了布尔向量 `col`、`dia1` 和 `dia2`
   来跟踪哪些列和对角线已被占用。这些向量的索引表示列号和对角线编号，值为 `true` 表示已被占用，值为 `false` 表示可用。

3. **生成棋盘**：在找到一个解之后，使用 `generateBoard` 函数生成棋盘，将皇后位置标记为 'Q'，并将棋盘添加到结果中。

这些解题思路的核心都是使用递归回溯法来尝试不同的皇后放置方式，并使用布尔数组/列表/向量来跟踪哪些位置已被占用，以确保皇后不互相攻击。同时，使用字符串处理来生成和表示棋盘。

## 代码

## Go

```Go
// 解法一 DFS
func solveNQueens(n int) [][]string {
    col, dia1, dia2, row, res := make([]bool, n), make([]bool, 2*n-1), make([]bool, 2*n-1), []int{}, [][]string{}
    putQueen(n, 0, &col, &dia1, &dia2, &row, &res) // 调用putQueen函数来找到解
    return res
}

// 尝试在一个n皇后问题中, 摆放第index行的皇后位置
func putQueen(n, index int, col, dia1, dia2 *[]bool, row *[]int, res *[][]string) {
    if index == n { // 所有皇后都已经成功摆放，得到一个解
        *res = append(*res, generateBoard(n, row)) // 生成棋盘并添加到结果集中
        return
    }
    for i := 0; i < n; i++ {
        // 尝试将第index行的皇后摆放在第i列
        if !(*col)[i] && !(*dia1)[index+i] && !(*dia2)[index-i+n-1] {
            *row = append(*row, i)          // 在当前行的row中记录皇后位置
            (*col)[i] = true                // 在列col中标记为占用
            (*dia1)[index+i] = true         // 在对角线dia1中标记为占用
            (*dia2)[index-i+n-1] = true     // 在对角线dia2中标记为占用
            putQueen(n, index+1, col, dia1, dia2, row, res) // 递归下一行
            (*col)[i] = false               // 回溯：取消占用
            (*dia1)[index+i] = false        // 回溯：取消占用
            (*dia2)[index-i+n-1] = false    // 回溯：取消占用
            *row = (*row)[:len(*row)-1]    // 回溯：移除上一行的皇后位置
        }
    }
    return
}

// 生成一个N皇后问题的棋盘
func generateBoard(n int, row *[]int) []string {
    board := []string{}
    res := ""
    for i := 0; i < n; i++ {
        res += "."
    }
    for i := 0; i < n; i++ {
        board = append(board, res) // 初始化棋盘为全"."
    }
    for i := 0; i < n; i++ {
        tmp := []byte(board[i])    // 将当前行转换为字节切片以修改皇后位置
        tmp[(*row)[i]] = 'Q'        // 在皇后位置处添加"Q"表示皇后
        board[i] = string(tmp)
    }
    return board // 返回表示棋盘的字符串切片
}

```

## Python

```Python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        col = [False] * n
        dia1 = [False] * (2 * n - 1)
        dia2 = [False] * (2 * n - 1)
        row = [0] * n
        self.putQueen(n, 0, col, dia1, dia2, row, result)
        return result

    def putQueen(self, n, index, col, dia1, dia2, row, result):
        if index == n:
            result.append(self.generateBoard(n, row))
            return
        for i in range(n):
            if not col[i] and not dia1[index + i] and not dia2[index - i + n - 1]:
                row[index] = i
                col[i] = True
                dia1[index + i] = True
                dia2[index - i + n - 1] = True
                self.putQueen(n, index + 1, col, dia1, dia2, row, result)
                col[i] = False
                dia1[index + i] = False
                dia2[index - i + n - 1] = False

    def generateBoard(self, n, row):
        board = []
        for i in range(n):
            row_str = ['.' for _ in range(n)]
            row_str[row[i]] = 'Q'
            board.append(''.join(row_str))
        return board

```

## Java

```Java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> result = new ArrayList<>();
        boolean[] col = new boolean[n];
        boolean[] dia1 = new boolean[2 * n - 1];
        boolean[] dia2 = new boolean[2 * n - 1];
        int[] row = new int[n];
        putQueen(n, 0, col, dia1, dia2, row, result);
        return result;
    }

    private void putQueen(int n, int index, boolean[] col, boolean[] dia1, boolean[] dia2, int[] row, List<List<String>> result) {
        if (index == n) {
            result.add(generateBoard(n, row));
            return;
        }
        for (int i = 0; i < n; i++) {
            if (!col[i] && !dia1[index + i] && !dia2[index - i + n - 1]) {
                row[index] = i;
                col[i] = true;
                dia1[index + i] = true;
                dia2[index - i + n - 1] = true;
                putQueen(n, index + 1, col, dia1, dia2, row, result);
                col[i] = false;
                dia1[index + i] = false;
                dia2[index - i + n - 1] = false;
            }
        }
    }

    private List<String> generateBoard(int n, int[] row) {
        List<String> board = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append('.');
        }
        for (int i = 0; i < n; i++) {
            char[] chars = sb.toString().toCharArray();
            chars[row[i]] = 'Q';
            board.add(new String(chars));
        }
        return board;
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> result;
        vector<bool> col(n, false);
        vector<bool> dia1(2 * n - 1, false);
        vector<bool> dia2(2 * n - 1, false);
        vector<int> row(n, 0);
        putQueen(n, 0, col, dia1, dia2, row, result);
        return result;
    }

    void putQueen(int n, int index, vector<bool>& col, vector<bool>& dia1, vector<bool>& dia2, vector<int>& row, vector<vector<string>>& result) {
        if (index == n) {
            result.push_back(generateBoard(n, row));
            return;
        }
        for (int i = 0; i < n; i++) {
            if (!col[i] && !dia1[index + i] && !dia2[index - i + n - 1]) {
                row[index] = i;
                col[i] = true;
                dia1[index + i] = true;
                dia2[index - i + n - 1] = true;
                putQueen(n, index + 1, col, dia1, dia2, row, result);
                col[i] = false;
                dia1[index + i] = false;
                dia2[index - i + n - 1] = false;
            }
        }
    }

    vector<string> generateBoard(int n, vector<int>& row) {
        vector<string> board(n, string(n, '.'));
        for (int i = 0; i < n; i++) {
            board[i][row[i]] = 'Q';
        }
        return board;
    }
};

```

当然，让我们分别介绍每个版本的代码中所需要的基础知识：

Go 版本：

1. **切片 (Slices)**：Go 使用切片来处理动态数组。在代码中，使用 `[]string` 表示一个字符串切片，用于存储每个皇后的位置。

2. **递归 (Recursion)**：解决 N-Queens 问题的关键是递归。代码中使用递归来尝试在每一行中放置皇后，同时进行回溯，以寻找所有可能的解。

3. **布尔数组 (Boolean Arrays)**：使用布尔数组来跟踪哪些列和对角线已被占用，以确保皇后不互相攻击。

Python 版本：

1. **列表 (Lists)**：Python 使用列表来处理动态数组，类似于 Go 中的切片。在代码中，使用 `List[List[str]]`
   表示一个字符串列表的列表，用于存储棋盘的不同解。

2. **递归 (Recursion)**：与 Go 版本类似，Python 版本也使用递归来尝试在每一行中放置皇后，并进行回溯。

3. **布尔列表 (Boolean Lists)**：Python 使用布尔列表来跟踪哪些列和对角线已被占用，以确保皇后不互相攻击。

4. **列表推导式 (List Comprehension)**：在生成棋盘时，使用列表推导式将字符串列表转换为包含皇后位置的字符串。

Java 版本：

1. **ArrayList**：Java 中使用 `ArrayList` 来处理动态数组，类似于 Go 的切片和 Python
   的列表。在代码中，使用 `List<List<String>>` 表示一个字符串列表的列表。

2. **递归 (Recursion)**：与 Go 和 Python 版本类似，Java 版本也使用递归来尝试在每一行中放置皇后，并进行回溯。

3. **布尔数组 (Boolean Arrays)**：Java 使用布尔数组来跟踪哪些列和对角线已被占用，以确保皇后不互相攻击。

4. **字符串处理**：Java 使用 `StringBuilder` 来处理字符串的可变性，以便在棋盘上放置皇后。

C++ 版本：

1. **向量 (Vectors)**：C++ 使用向量来处理动态数组，类似于 Go 的切片、Python 的列表和 Java 的
   ArrayList。在代码中，使用 `vector<vector<string>>` 表示一个字符串向量的向量。

2. **递归 (Recursion)**：与其他版本类似，C++ 版本也使用递归来尝试在每一行中放置皇后，并进行回溯。

3. **布尔向量 (Boolean Vectors)**：C++ 使用布尔向量来跟踪哪些列和对角线已被占用，以确保皇后不互相攻击。

4. **字符串处理**：C++ 使用字符串向量和字符数组来表示和处理棋盘，将皇后位置添加到合适的位置。

这些基础知识包括切片、列表、递归、布尔数组/列表、字符串处理等，是理解和编写解决 N-Queens
问题的关键要素。如果您对其中的任何概念有更具体的疑问，或者需要更深入的解释，请随时提出。