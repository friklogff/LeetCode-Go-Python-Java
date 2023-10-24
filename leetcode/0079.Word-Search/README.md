# [79. Word Search](https://leetcode.com/problems/word-search/)


## 题目

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

**Example:**

    board =
    [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
    
    Given word = "ABCCED", return true.
    Given word = "SEE", return true.
    Given word = "ABCB", return false.

## 题目大意

给定一个二维网格和一个单词，找出该单词是否存在于网格中。单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

以下是每个版本的代码的解题思路：

Go 版本解题思路

1. 获取字符矩阵的行数和列数（`m` 和 `n`），以及目标单词的长度（`l`）。

2. 创建一个映射表 `bcnts` 用于统计字符矩阵中每个字符的出现次数。遍历字符矩阵，将每个字符的出现次数记录在 `bcnts` 中。

3. 创建一个映射表 `wcnts` 用于统计目标单词中每个字符的出现次数。遍历目标单词，将每个字符的出现次数记录在 `wcnts` 中。

4. 检查字符矩阵中的字符是否足够组成目标单词。对于每个字符在 `wcnts` 中，检查是否存在于 `bcnts` 中，且其出现次数不小于目标单词中的出现次数。

5. 定义递归函数 `f` 来搜索目标单词的起始位置。该函数接受当前位置 `(x, y)`、目标单词的索引 `idx` 作为参数。

6. 在 `f` 函数中，首先检查是否已经找到了目标单词，即 `idx` 是否等于目标单词的长度 `l`。

7. 然后，检查当前位置 `(x, y)` 是否越界或已经访问过，以及当前字符是否匹配目标单词的当前字符。

8. 如果当前字符匹配目标单词的字符，将当前字符标记为已访问，然后递归搜索上、下、左、右四个方向。

9. 如果在任何方向上找到了目标单词的路径，返回 `true`，否则，将当前字符的标记恢复到原始值，返回 `false`。

10. 在字符矩阵中查找目标单词的起始位置。遍历字符矩阵的每个位置，以该位置为起点调用 `f` 函数。

11. 如果任何搜索路径找到目标单词，返回 `true`，否则返回 `false`，表示未找到目标单词。

Python 版本解题思路

Python 版本的解题思路与 Go 版本基本相同，采用深度优先搜索和递归的方式来查找目标单词。以下是 Python 版本的解题思路：

1. 获取字符矩阵的行数和列数（`m` 和 `n`），以及目标单词的长度（`l`）。

2. 创建一个字典 `bcnts` 用于统计字符矩阵中每个字符的出现次数。遍历字符矩阵，将每个字符的出现次数记录在 `bcnts` 中。

3. 创建一个字典 `wcnts` 用于统计目标单词中每个字符的出现次数。遍历目标单词，将每个字符的出现次数记录在 `wcnts` 中。

4. 检查字符矩阵中的字符是否足够组成目标单词。对于每个字符在 `wcnts` 中，检查是否存在于 `bcnts` 中，且其出现次数不小于目标单词中的出现次数。

5. 定义递归函数 `dfs` 来搜索目标单词的起始位置。该函数接受当前位置 `(x, y)`、目标单词的索引 `idx` 作为参数。

6. 在 `dfs` 函数中，首先检查是否已经找到了目标单词，即 `idx` 是否等于目标单词的长度 `l`。

7. 然后，检查当前位置 `(x, y)` 是否越界或已经访问过，以及当前字符是否匹配目标单词的当前字符。

8. 如果当前字符匹配目标单词的字符，将当前字符标记为已访问，然后递归搜索上、下、左、右四个方向。

9. 如果在任何方向上找到了目标单词的路径，返回 `True`，否则，将当前字符的标记恢复到原始值，返回 `False`。

10. 在字符矩阵中查找目标单词的起始位置。遍历字符矩阵的每个位置，以该位置为起点调用 `dfs` 函数。

11. 如果任何搜索路径找到目标单词，返回 `True`，否则返回 `False`，表示未找到目标单词。

Java 版本解题思路

Java 版本的解题思路与前两个版本相似，同样采用深度优先搜索和递归的方式来查找目标单词。以下是 Java 版本的解题思路：

1. 获取字符矩阵的行数和列数（`m` 和 `n`），以及目标单词的长度（`l`）。

2. 创建一个映射 `bcnts` 用于统计字符矩阵中每个字符的出现次数。遍历字符矩阵，将每个字符的出现次数记录在 `bcnts` 中。

3. 创建一个映射 `wcnts` 用于统计目标单词中每个字符的出现次数。遍历目标单词，将每个字符的出现次数记录在 `wcnts` 中。

4. 检查字符矩阵中的字符是否足够组成目标单词。对于每个字符在 `wcnts` 中，检查是否存在于 `bcnts` 中，且其出现次数不小于目标单词中的出现次数。

5. 创建一个二维布尔数组 `visited` 用于标记字符矩阵中的字符是否已经被访问过。

6. 定义递归函数 `dfs` 来搜索目标单词的起始位置。该函数接受当前位置 `(x, y)`、目标单词的索引 `idx` 和字符矩阵的可能移动方向 `directions` 作为参数。

7. 在 `dfs` 函数中，首先检查是否已经找到了目标单词，即 `idx` 是否等于目标单词的长度 `l`。

8. 然后，检查当前位置 `(x, y)` 是否越界或已经访问过，以及当前字符是否匹配目标单词的当前字符。

9. 如果当前字符匹配目标单词的字符，将当前字符标记为已访问，然后递归搜索可能的移动方向，包括上、下、左、右四个方向。

10. 如果在任何方向上找到了目标单词的路径，返回 `true`，否则，将当前字符的标记恢复到未访问状态，返回 `false`。

11. 在字符矩阵中查找目标单词的起始位置。遍历字符矩阵的每个位置，以该位置为起点调用 `dfs` 函数。

12. 如果任何搜索路径找到目标单词，返回 `true`，否则返回 `false`，表示未找到目标单词。

C++ 版本解题思路

C++ 版本的解题思路与前面的版本相似，同样采用深度优先搜索和递归的方式来查找目标单词。以下是 C++ 版本的解题思路：

1. 获取字符矩阵的行数和列数（`m` 和 `n`），以及目标单词的长度（`l`）。

2. 创建一个映射 `bcnts` 用于统计字符矩阵中每个字符的出现次数。遍历字符矩阵，将每个字符的出现次数记录在 `bcnts` 中。

3. 创建一个映射 `wcnts` 用于统计目标单词中每个字符的出现次数。遍历目标单词，将每个字符的出现次数记录在 `wcnts` 中。

4. 检查字符矩阵中的字符是否足够组成目标单词。对于每个字符在 `wcnts` 中，检查是否存在于 `bcnts` 中，且其出现次数不小于目标单词中的出现次数。

5. 创建一个二维布尔数组 `visited` 用于标记字符矩阵中的字符是否已经被访问过。

6. 定义递归函数 `dfs` 来搜索目标单词的起始位置。该函数接受当前位置 `(x, y)`、目标单词的索引 `idx` 和字符矩阵的可能移动方向 `directions` 作为参数。

7. 在 `dfs` 函数中，首先检查是否已经找到了目标单词，即 `idx` 是否等于目标单词的长度 `l`。

8. 然后，检查当前位置 `(x, y)` 是否越界或已经访问过，以及当前字符是否匹配目标单词的当前字符。

9. 如果当前字符匹配目标单词的字符，将当前字符标记为已访问，然后递归搜索可能的移动方向，包括上、下、左、右四个方向。

10. 如果在任何方向上找到了目标单词的路径，返回 `true`，否则，将当前字符的标记恢复到未访问状态，返回 `false`。

11. 在字符矩阵中查找目标单词的起始位置。遍历字符矩阵的每个位置，以该位置为起点调用 `dfs` 函数。

12. 如果任何搜索路径找到目标单词，返回 `true`，否则返回 `false`，表示未找到目标单词。

## 解题思路

- 在地图上的任意一个起点开始，向 4 个方向分别 DFS 搜索，直到所有的单词字母都找到了就输出 true，否则输出 false。

## 代码

## Go

```Go
func exist(board [][]byte, word string) bool {
    // 获取字符矩阵的行数和列数
    m := len(board)
    n := len(board[0])
    // 获取目标单词的长度
    l := len(word)

    // 创建一个映射表，用于统计字符矩阵中每个字符的出现次数
    bcnts := make(map[byte]int)
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            ch := board[i][j]
            _, exists := bcnts[ch]
            if !exists {
                bcnts[ch] = 0
            }
            bcnts[ch] += 1
        }
    }

    // 创建一个映射表，用于统计目标单词中每个字符的出现次数
    wcnts := make(map[byte]int)
    for i := 0; i < l; i++ {
        _, exists := wcnts[word[i]]
        if !exists {
            wcnts[word[i]] = 0
        }
        wcnts[word[i]] += 1
    }

    // 检查字符矩阵中的字符是否足够组成目标单词
    for ch, wcnt := range wcnts {
        bcnt, exists := bcnts[ch]
        if !exists || bcnt < wcnt {
            return false
        }
    }

    // 定义递归函数来搜索目标单词
    var f func(int, int, int) bool
    f = func(x, y int, idx int) bool {
        if idx == l {
            return true  // 已经找到目标单词
        }

        if x < 0 || x >= m || y < 0 || y >= n {
            return false  // 超出字符矩阵边界
        }

        if board[x][y] == '*' {
            return false  // 已经访问过的字符
        }

        if board[x][y] == word[idx] {
            origin := board[x][y]
            board[x][y] = '*'  // 将字符标记为已访问
            if f(x, y-1, idx+1) || f(x, y+1, idx+1) || f(x-1, y, idx+1) || f(x+1, y, idx+1) {
                return true
            }
            board[x][y] = origin  // 恢复字符原始值
        }
        return false
    }

    // 在字符矩阵中查找目标单词的起始位置
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if f(i, j, 0) {
                return true
            }
        }
    }
    return false  // 未找到目标单词
}

```

## Python

```Python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        l = len(word)

        bcnts = collections.defaultdict(int)
        for i in range(m):
            for j in range(n):
                ch = board[i][j]
                bcnts[ch] += 1

        wcnts = collections.defaultdict(int)
        for i in range(l):
            wcnts[word[i]] += 1

        for ch, wcnt in wcnts.items():
            if ch not in bcnts or bcnts[ch] < wcnt:
                return False

        def dfs(x, y, idx):
            if idx == l:
                return True

            if x < 0 or x >= m or y < 0 or y >= n:
                return False

            if board[x][y] == '*':
                return False

            if board[x][y] == word[idx]:
                origin = board[x][y]
                board[x][y] = '*'
                if (dfs(x, y - 1, idx + 1) or dfs(x, y + 1, idx + 1) or
                    dfs(x - 1, y, idx + 1) or dfs(x + 1, y, idx + 1)):
                    return True
                board[x][y] = origin

            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False

```

## Java

```Java
class Solution {
    public boolean exist(char[][] board, String word) {
        int m = board.length;
        int n = board[0].length;
        int l = word.length();

        Map<Character, Integer> bcnts = new HashMap<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                char ch = board[i][j];
                bcnts.put(ch, bcnts.getOrDefault(ch, 0) + 1);
            }
        }

        Map<Character, Integer> wcnts = new HashMap<>();
        for (int i = 0; i < l; i++) {
            char ch = word.charAt(i);
            wcnts.put(ch, wcnts.getOrDefault(ch, 0) + 1);
        }

        for (Map.Entry<Character, Integer> entry : wcnts.entrySet()) {
            char ch = entry.getKey();
            int wcnt = entry.getValue();
            if (!bcnts.containsKey(ch) || bcnts.get(ch) < wcnt) {
                return false;
            }
        }

        boolean[][] visited = new boolean[m][n];

        int[][] directions = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dfs(board, word, i, j, 0, visited, directions)) {
                    return true;
                }
            }
        }

        return false;
    }

    private boolean dfs(char[][] board, String word, int x, int y, int idx, boolean[][] visited, int[][] directions) {
        int m = board.length;
        int n = board[0].length;
        int l = word.length();

        if (idx == l) {
            return true;
        }

        if (x < 0 || x >= m || y < 0 || y >= n) {
            return false;
        }

        if (visited[x][y] || board[x][y] != word.charAt(idx)) {
            return false;
        }

        visited[x][y] = true;

        for (int[] direction : directions) {
            int newX = x + direction[0];
            int newY = y + direction[1];
            if (dfs(board, word, newX, newY, idx + 1, visited, directions)) {
                visited[x][y] = false;
                return true;
            }
        }

        visited[x][y] = false;

        return false;
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int m = board.size();
        int n = board[0].size();
        int l = word.length();

        unordered_map<char, int> bcnts;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                char ch = board[i][j];
                bcnts[ch]++;
            }
        }

        unordered_map<char, int> wcnts;
        for (int i = 0; i < l; i++) {
            char ch = word[i];
            wcnts[ch]++;
        }

        for (const auto& entry : wcnts) {
            char ch = entry.first;
            int wcnt = entry.second;
            if (bcnts.find(ch) == bcnts.end() || bcnts[ch] < wcnt) {
                return false;
            }
        }

        vector<vector<bool>> visited(m, vector<bool>(n, false));

        vector<vector<int>> directions = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dfs(board, word, i, j, 0, visited, directions)) {
                    return true;
                }
            }
        }

        return false;
    }

private:
    bool dfs(vector<vector<char>>& board, string word, int x, int y, int idx, vector<vector<bool>>& visited, vector<vector<int>>& directions) {
        int m = board.size();
        int n = board[0].size();
        int l = word.length();

        if (idx == l) {
            return true;
        }

        if (x < 0 || x >= m || y < 0 || y >= n) {
            return false;
        }

        if (visited[x][y] || board[x][y] != word[idx]) {
            return false;
        }

        visited[x][y] = true;

        for (const vector<int>& direction : directions) {
            int newX = x + direction[0];
            int newY = y + direction[1];
            if (dfs(board, word, newX, newY, idx + 1, visited, directions)) {
                visited[x][y] = false;
                return true;
            }
        }

        visited[x][y] = false;

        return false;
    }
};
```

当分开介绍每个版本的代码时，我将重点介绍所需的基础知识和概念，以便理解和修改代码。以下是每个版本的详细介绍：

Go 版本

所需基础知识：

1. **基本语法和数据结构**：了解 Go 编程语言的基本语法，如变量、循环、条件语句和数据结构（如切片和映射）。

2. **递归和深度优先搜索 (DFS)**：了解递归的概念和如何使用递归来实现深度优先搜索（DFS）。

3. **数组切片**：了解如何使用数组切片来操作多维数组，以及如何在切片中进行元素的增加和修改。

4. **条件语句**：了解条件语句（如 `if` 语句）的用法，以进行条件检查。

代码解释：

Go 版本的代码使用递归和深度优先搜索来查找目标单词。它使用了两个映射表（`bcnts` 和 `wcnts`）来统计字符矩阵和目标单词中每个字符的出现次数。然后，它使用嵌套的递归函数 `f` 来搜索目标单词的起始位置，并在搜索过程中标记已访问的字符。如果找到目标单词的路径，返回 `true`，否则返回 `false`。

Python 版本

所需基础知识：

1. **基本语法和数据结构**：了解 Python 编程语言的基本语法，如变量、循环、条件语句和数据结构（如列表和字典）。

2. **递归和深度优先搜索 (DFS)**：了解递归的概念和如何使用递归来实现深度优先搜索（DFS）。

3. **列表和字典**：了解如何使用列表和字典来存储和操作数据。

4. **类和对象**（可选）：理解如何创建和使用类和对象，以便组织代码。

代码解释：

Python 版本的代码与 Go 版本相似，使用递归和深度优先搜索来查找目标单词。它使用字典（`collections.defaultdict`）来统计字符矩阵和目标单词中每个字符的出现次数。然后，它使用递归函数 `dfs` 来搜索目标单词的起始位置，标记已访问的字符。如果找到目标单词的路径，返回 `true`，否则返回 `false`。

Java 版本

所需基础知识：

1. **基本语法和数据结构**：了解 Java 编程语言的基本语法，如变量、循环、条件语句和数据结构（如数组和集合）。

2. **递归和深度优先搜索 (DFS)**：了解递归的概念和如何使用递归来实现深度优先搜索（DFS）。

3. **集合框架**：了解 Java 的集合框架，如 `Map` 和 `List`，以便操作数据集合。

4. **二维数组**：了解如何操作二维数组，包括访问元素和遍历。

代码解释：

Java 版本的代码与前两个版本相似，也使用递归和深度优先搜索来查找目标单词。它使用 `Map` 来统计字符矩阵和目标单词中每个字符的出现次数。然后，它使用递归函数 `dfs` 来搜索目标单词的起始位置，标记已访问的字符。如果找到目标单词的路径，返回 `true`，否则返回 `false`。

C++ 版本

所需基础知识：

1. **基本语法和数据结构**：了解 C++ 编程语言的基本语法，如变量、循环、条件语句和数据结构（如向量和映射）。

2. **递归和深度优先搜索 (DFS)**：了解递归的概念和如何使用递归来实现深度优先搜索（DFS）。

3. **STL（标准模板库）**：了解 C++ 中的标准模板库，包括容器和算法，以便操作数据集合。

4. **多维数组**：了解如何操作多维数组，包括访问元素和遍历。

代码解释：

C++ 版本的代码与前面的版本相似，同样使用递归和深度优先搜索来查找目标单词。它使用映射（`unordered_map`）来统计字符矩阵和目标单词中每个字符的出现次数。然后，它使用递归函数 `dfs` 来搜索目标单词的起始位置，标记已访问的字符。如果找到目标单词的路径，返回 `true`，否则返回 `false`。

需要注意的是，不同版本的代码在语法和数据结构上有一些差异，但它们共同使用深度优先搜索和递归来解决相同的问题。您可以选择其中一个版本，根据您熟悉的编程语言来学习和修改代码。