# [72. Edit-Distance](https://leetcode.cn/problems/edit-distance/description/)

## 题目

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character


Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')


Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.

## 题目大意

给你两个单词word1 和word2， 请返回将word1转换成word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
## 解题思路
以下是每个版本的解题思路的详细介绍：

**Go 版本解题思路：**

1. **初始化**：创建一个二维切片 `f`，其中 `f[i][j]` 表示将字符串 `s` 的前 `i` 个字符转换为字符串 `t` 的前 `j` 个字符所需的最小操作数。初始化第一行和第一列，表示从空字符串到各个字符串的编辑距离。

2. **动态规划**：遍历字符串 `s` 和 `t` 的每个字符，逐个比较它们。如果字符相同，`f[i][j]` 等于 `f[i-1][j-1]`；否则，`f[i][j]` 等于 `f[i-1][j]`（删除操作）、`f[i][j-1]`（插入操作）和 `f[i-1][j-1]`（替换操作）中的最小值加一。

3. **返回结果**：最后返回 `f[n][m]`，其中 `n` 和 `m` 是字符串 `s` 和 `t` 的长度。

**Python 版本解题思路：**

1. **初始化**：创建一个二维数组 `f`，其中 `f[i][j]` 表示将字符串 `word1` 的前 `i` 个字符转换为字符串 `word2` 的前 `j` 个字符所需的最小操作数。初始化第一行和第一列，表示从空字符串到各个字符串的编辑距离。

2. **动态规划**：遍历字符串 `word1` 和 `word2` 的每个字符，逐个比较它们。如果字符相同，`f[i][j]` 等于 `f[i-1][j-1]`；否则，`f[i][j]` 等于 `f[i-1][j]`（删除操作）、`f[i][j-1]`（插入操作）和 `f[i-1][j-1]`（替换操作）中的最小值加一。

3. **返回结果**：最后返回 `f[n][m]`，其中 `n` 和 `m` 是字符串 `word1` 和 `word2` 的长度。

**Java 版本解题思路：**

1. **初始化**：将输入的字符串 `word1` 和 `word2` 转换为字符数组 `ch1` 和 `ch2`。创建两个整数数组 `lastRow` 和 `thisRow`，它们用于存储编辑距离计算中的临时结果。

2. **动态规划**：遍历字符数组 `ch1` 和 `ch2`，逐个比较字符。如果字符相同，`thisRow[j]` 等于 `lastRow[j-1]`；否则，`thisRow[j]` 等于 `lastRow[j]`（删除操作）、`thisRow[j-1]`（插入操作）和 `lastRow[j-1]`（替换操作）中的最小值加一。

3. **交替行**：在每次计算后，交换 `lastRow` 和 `thisRow`，以便下一次迭代使用。

4. **返回结果**：最后返回 `lastRow[ch2.length]`，即从 `word1` 到 `word2` 的最小编辑距离。

**C++ 版本解题思路：**

1. **初始化**：获取输入字符串 `word1` 和 `word2` 的长度，创建一个二维数组 `dp` 用于存储编辑距离计算中的临时结果。

2. **动态规划**：遍历字符串 `word1` 和 `word2` 的每个字符，逐个比较它们。如果字符相同，`dp[i][j]` 等于 `dp[i-1][j-1]`；否则，`dp[i][j]` 等于 `dp[i-1][j]`（删除操作）、`dp[i][j-1]`（插入操作）和 `dp[i-1][j-1]`（替换操作）中的最小值加一。

3. **返回结果**：最后返回 `dp[n][m]`，其中 `n` 和 `m` 是字符串 `word1` 和 `word2` 的长度。

在每个版本中，动态规划是主要的解题思路，其中二维数组用于存储中间结果，逐步构建最小编辑距离。最终的目标是得到 `f[n][m]` 或 `dp[n][m]`，即从一个字符串到另一个字符串的最小编辑距离。
 
## 代码

## Go

```Go
func minDistance(s, t string) int {
    n, m := len(s), len(t)   // 获取字符串s和t的长度
    f := make([][]int, n+1)  // 创建一个(n+1) x (m+1)的二维切片f，用于存储编辑距离计算中的临时结果
    for i := range f {       // 初始化f二维切片
        f[i] = make([]int, m+1)
    }
    for j := 1; j <= m; j++ { // 初始化f的第一行，表示从空字符串s到t的编辑距离
        f[0][j] = j
    }
    for i, x := range s {     // 遍历字符串s的字符
        f[i+1][0] = i + 1     // 初始化f的第一列，表示从空字符串t到s的编辑距离
        for j, y := range t { // 遍历字符串t的字符
            if x == y {       // 如果当前字符相同
                f[i+1][j+1] = f[i][j] // 编辑距离不变
            } else {
                f[i+1][j+1] = min(min(f[i][j+1], f[i+1][j]), f[i][j]) + 1
                // 否则，计算替换、插入和删除操作中的最小编辑距离
            }
        }
    }
    return f[n][m] // 返回s到t的最小编辑距离
}

func min(a, b int) int {
    if b < a {
        return b
    }
    return a
}


```

## Python

```Python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        # 创建一个(n+1) x (m+1)的二维数组，用于存储编辑距离计算中的临时结果
        f = [[0] * (m + 1) for _ in range(n + 1)]

        # 初始化第一行和第一列
        for i in range(n + 1):
            f[i][0] = i
        for j in range(m + 1):
            f[0][j] = j

        # 动态规划计算编辑距离
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1

        return f[n][m]

    def min(self, a, b, c):
        return min(a, min(b, c))

```

## Java

```Java
class Solution {
    public int minDistance(String word1, String word2) {
        char[] ch1 = word1.toCharArray(); // 将字符串 word1 转换为字符数组 ch1
        char[] ch2 = word2.toCharArray(); // 将字符串 word2 转换为字符数组 ch2
        int[] lastRow = new int[ch2.length + 1]; // 上一行的编辑距离数组
        int[] thisRow = new int[ch2.length + 1]; // 当前行的编辑距离数组
        int[] temp; // 用于交换 lastRow 和 thisRow 的临时数组
        int tempMin; // 用于暂存最小编辑距离的临时变量

        // 初始化上一行，表示从空字符串 word1 到 word2 的编辑距离
        for (int j = 1; j <= ch2.length; j++) {
            lastRow[j] = lastRow[j - 1] + 1;
        }

        // 遍历字符串 word1 的字符
        for (int i = 1; i <= ch1.length; i++) {
            thisRow[0] = lastRow[0] + 1; // 初始化当前行的第一个元素

            // 遍历字符串 word2 的字符
            for (int j = 1; j <= ch2.length; j++) {
                if (ch1[i - 1] == ch2[j - 1]) {
                    thisRow[j] = lastRow[j - 1]; // 如果字符相同，编辑距离不变
                } else {
                    // 如果字符不同，计算替换、插入和删除操作中的最小编辑距离
                    tempMin = Math.min(lastRow[j], Math.min(thisRow[j - 1], lastRow[j - 1]));
                    thisRow[j] = tempMin + 1;
                }
            }

            // 交换 lastRow 和 thisRow
            temp = lastRow;
            lastRow = thisRow;
            thisRow = temp;
        }

        return lastRow[ch2.length]; // 返回最终的编辑距离
    }
}


```

## Cpp

```Cpp
class Solution {
public:
    int minDistance(string word1, string word2) {
        int n = word1.length();
        int m = word2.length();

        // 如果其中一个字符串为空，返回另一个字符串的长度，这是初始状态
        if (n == 0 || m == 0) return max(n, m);

        int dp[n + 1][m + 1];
        memset(dp, 0, sizeof(dp));

        // 初始化第一行和第一列
        for (int i = 0; i < n + 1; i++) {
            dp[i][0] = i;
        }
        for (int i = 0; i < m + 1; i++) {
            dp[0][i] = i;
        }

        // 动态规划计算编辑距离
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < m + 1; j++) {
                if (word1[i - 1] == word2[j - 1]) {
                    // 如果当前字符相同，不需要执行替换操作
                    dp[i][j] = min(dp[i - 1][j] + 1, min(dp[i][j - 1] + 1, dp[i - 1][j - 1]));
                } else {
                    // 如果当前字符不同，执行替换操作并加1
                    dp[i][j] = min(dp[i - 1][j], min(dp[i][j - 1], dp[i - 1][j - 1])) + 1;
                }
            }
        }
        return dp[n][m]; // 返回编辑距离
    }
};

 
```
以下是每个版本的所需基础知识的详细介绍：

**Go 版本：**

1. **变量和数据类型**：了解 Go 中的基本数据类型（整数、字符串、字符等），以及如何声明和使用变量。

2. **切片和数组**：理解 Go 中的切片和数组，它们在字符串处理中经常用到。

3. **循环和条件语句**：掌握 Go 中的循环和条件语句，用于控制程序流程。

4. **函数**：了解如何定义和调用函数，以及如何传递参数和返回值。

5. **切片操作**：学习如何对切片进行操作，例如添加和删除元素。

6. **动态规划**：理解动态规划的基本思想，包括如何使用二维数组来存储中间结果以解决问题。

**Python 版本：**

1. **变量和数据类型**：了解 Python 中的数据类型（整数、字符串、列表等），以及如何声明和使用变量。

2. **列表**：学会使用列表，因为它们在字符串处理和动态规划中经常用到。

3. **循环和条件语句**：掌握 Python 中的循环和条件语句，用于控制程序流程。

4. **函数**：了解如何定义和调用函数，以及如何传递参数和返回值。

5. **动态规划**：理解动态规划的基本思想，包括如何使用二维数组来存储中间结果以解决问题。

**Java 版本：**

1. **类和对象**：Java 是面向对象的编程语言，所以需要了解类和对象的概念，以及如何创建对象。

2. **字符数组**：了解字符数组的使用，因为字符串操作通常涉及字符数组。

3. **循环和条件语句**：掌握 Java 中的循环和条件语句，用于控制程序流程。

4. **方法**：了解如何定义和调用方法，以及如何传递参数和返回值。

5. **动态规划**：理解动态规划的基本思想，包括如何使用二维数组来存储中间结果以解决问题。

**C++ 版本：**

1. **变量和数据类型**：了解 C++ 中的数据类型（整数、字符串、数组等），以及如何声明和使用变量。

2. **数组**：学会使用数组，因为它们在字符串处理和动态规划中经常用到。

3. **循环和条件语句**：掌握 C++ 中的循环和条件语句，用于控制程序流程。

4. **函数**：了解如何定义和调用函数，以及如何传递参数和返回值。

5. **动态规划**：理解动态规划的基本思想，包括如何使用二维数组来存储中间结果以解决问题。

在每种版本中，你还需要了解动态规划的核心思想，即如何将一个大问题拆分为子问题，以及如何使用中间结果来优化解决方案。这种问题解决方法在编程中非常常见，因此对动态规划的理解至关重要。