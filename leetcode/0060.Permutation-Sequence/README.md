# [60. Permutation Sequence](https://leetcode.com/problems/permutation-sequence/)


## 题目

The set `[1,2,3,...,*n*]` contains a total of *n*! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for *n* = 3:

1. `"123"`
2. `"132"`
3. `"213"`
4. `"231"`
5. `"312"`
6. `"321"`

Given *n* and *k*, return the *k*th permutation sequence.

**Note:**

- Given *n* will be between 1 and 9 inclusive.
- Given *k* will be between 1 and *n*! inclusive.

**Example 1:**

```c
Input: n = 3, k = 3
Output: "213"
```

**Example 2:**

```c
Input: n = 4, k = 9
Output: "2314"
```

## 题目大意

给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下："123"，"132"，"213"，"231"，"312"，"321"，给定 n 和 k，返回第 k 个排列。


## 解题思路

下面分别介绍每个版本的解题思路：

**Go 版本解题思路：**
1. 创建一个存储阶乘结果的数组 `factorial`，并初始化第一个元素为 1。
2. 计算从 1 到 n 的阶乘值，并将结果存储在 `factorial` 数组中。
3. 将 k 减去 1，将其转换为从 0 开始的索引，以便在数组中访问。
4. 创建一个空字符串 `ans` 用于存储最终的排列结果。
5. 创建一个 `valid` 数组，用于标记数字是否已经被使用。初始化所有数字为可用（1）。
6. 循环计算每个位置上的数字：
   - 计算当前位置上的数字在当前剩余排列中的顺序（order）。
   - 寻找符合顺序的数字，遍历 `valid` 数组，减去已经使用的数字的数量，找到对应的数字。
   - 将找到的数字添加到 `ans` 中，并将该数字标记为不可用。
   - 更新 k，去除已经确定的数字对应的排列数。
7. 返回 `ans` 作为最终的排列结果。

**Python 版本解题思路：**
1. 计算阶乘数组 `factorial`，其中存储从 1 到 n 的阶乘值。
2. 将 k 减去 1，将其转换为从 0 开始的索引。
3. 创建一个空列表 `ans` 用于存储最终的排列结果。
4. 创建一个 `valid` 列表，用于标记数字是否已经被使用。初始化所有数字为可用。
5. 循环计算每个位置上的数字：
   - 计算当前位置上的数字在当前剩余排列中的顺序（order）。
   - 寻找符合顺序的数字，遍历 `valid` 列表，减去已经使用的数字的数量，找到对应的数字。
   - 将找到的数字添加到 `ans` 中，并将该数字标记为不可用。
   - 更新 k，去除已经确定的数字对应的排列数。
6. 返回 `ans` 作为最终的排列结果。

**Java 版本解题思路：**
1. 计算阶乘数组 `factorial`，其中存储从 1 到 n 的阶乘值。
2. 将 k 减去 1，将其转换为从 0 开始的索引。
3. 创建一个空字符串 `ans` 用于存储最终的排列结果。
4. 创建一个整数数组 `valid`，用于标记数字是否已经被使用。初始化所有数字为可用。
5. 循环计算每个位置上的数字：
   - 计算当前位置上的数字在当前剩余排列中的顺序（order）。
   - 寻找符合顺序的数字，遍历 `valid` 数组，减去已经使用的数字的数量，找到对应的数字。
   - 将找到的数字添加到 `ans` 中，并将该数字标记为不可用。
   - 更新 k，去除已经确定的数字对应的排列数。
6. 返回 `ans` 作为最终的排列结果。

**C++ 版本解题思路：**
1. 计算阶乘数组 `factorial`，其中存储从 1 到 n 的阶乘值。
2. 将 k 减去 1，将其转换为从 0 开始的索引。
3. 创建一个空字符串 `ans` 用于存储最终的排列结果。
4. 创建一个整数数组 `valid`，用于标记数字是否已经被使用。初始化所有数字为可用。
5. 循环计算每个位置上的数字：
   - 计算当前位置上的数字在当前剩余排列中的顺序（order）。
   - 寻找符合顺序的数字，遍历 `valid` 数组，减去已经使用的数字的数量，找到对应的数字。
   - 将找到的数字添加到 `ans` 中，并将该数字标记为不可用。
   - 更新 k，去除已经确定的数字对应的排列数。
6. 返回 `ans` 作为最终的排列结果。

无论使用哪种编程语言版本，核心思路都是相同的，只是具体的语法和数据结构会有所不同。通过理解这些思路，你可以实现解决这个问题的代码。## 代码

## Go

```Go
func getPermutation(n int, k int) string {
    // 创建一个数组 factorial 用于存储阶乘结果
    factorial := make([]int, n)
    factorial[0] = 1

    // 计算 1 到 n 的阶乘值并存储在 factorial 数组中
    for i := 1; i < n; i++ {
        factorial[i] = factorial[i - 1] * i
    }

    k-- // 减去 1，将 k 转换为从 0 开始的索引

    ans := "" // 存储最终的排列结果
    valid := make([]int, n + 1) // 创建一个数组 valid 用于标记数字是否已经被使用
    for i := 0; i < len(valid); i++ {
        valid[i] = 1 // 初始化 valid 数组，所有数字都可用
    }

    // 循环计算每个位置上的数字
    for i := 1; i <= n; i++ {
        // 计算当前位置上的数字在当前剩余排列中的顺序
        order := k / factorial[n - i] + 1
        
        // 寻找符合顺序的数字
        for j := 1; j <= n; j++ {
            order -= valid[j]
            if order == 0 {
                ans += strconv.Itoa(j) // 将找到的数字添加到结果中
                valid[j] = 0 // 将已经使用的数字标记为不可用
                break
            }
        }
        
        k %= factorial[n - i] // 更新 k，去除已经确定的数字对应的排列数
    }

    return ans // 返回最终的排列结果
}

```

## Python

```Python
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 计算阶乘数组
        factorial = [1]
        for i in range(1, n):
            factorial.append(factorial[-1] * i)

        k -= 1  # 将 k 转换为从 0 开始的索引

        ans = []  # 存储最终的排列结果
        valid = [1] * (n + 1)  # 创建一个数组用于标记数字是否已经被使用

        # 循环计算每个位置上的数字
        for i in range(1, n + 1):
            # 计算当前位置上的数字在当前剩余排列中的顺序
            order = k // factorial[n - i] + 1
            
            # 寻找符合顺序的数字
            for j in range(1, n + 1):
                order -= valid[j]
                if order == 0:
                    ans.append(str(j))  # 将找到的数字添加到结果中
                    valid[j] = 0  # 将已经使用的数字标记为不可用
                    break
            
            k %= factorial[n - i]  # 更新 k，去除已经确定的数字对应的排列数

        return ''.join(ans)  # 返回最终的排列结果

```

## Java

```Java
class Solution {
    public String getPermutation(int n, int k) {
        // 计算阶乘数组
        int[] factorial = new int[n];
        factorial[0] = 1;
        for (int i = 1; i < n; i++) {
            factorial[i] = factorial[i - 1] * i;
        }

        k--;  // 将 k 转换为从 0 开始的索引

        StringBuilder ans = new StringBuilder();  // 存储最终的排列结果
        int[] valid = new int[n + 1];
        Arrays.fill(valid, 1);  // 初始化数组，所有数字都可用

        // 循环计算每个位置上的数字
        for (int i = 1; i <= n; i++) {
            // 计算当前位置上的数字在当前剩余排列中的顺序
            int order = k / factorial[n - i] + 1;
            
            // 寻找符合顺序的数字
            for (int j = 1; j <= n; j++) {
                order -= valid[j];
                if (order == 0) {
                    ans.append(j);  // 将找到的数字添加到结果中
                    valid[j] = 0;  // 将已经使用的数字标记为不可用
                    break;
                }
            }
            
            k %= factorial[n - i];  // 更新 k，去除已经确定的数字对应的排列数
        }

        return ans.toString();  // 返回最终的排列结果
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    string getPermutation(int n, int k) {
        // 计算阶乘数组
        vector<int> factorial(n);
        factorial[0] = 1;
        for (int i = 1; i < n; i++) {
            factorial[i] = factorial[i - 1] * i;
        }

        k--;  // 将 k 转换为从 0 开始的索引

        string ans;  // 存储最终的排列结果
        vector<int> valid(n + 1, 1);  // 创建一个数组用于标记数字是否已经被使用

        // 循环计算每个位置上的数字
        for (int i = 1; i <= n; i++) {
            // 计算当前位置上的数字在当前剩余排列中的顺序
            int order = k / factorial[n - i] + 1;
            
            // 寻找符合顺序的数字
            for (int j = 1; j <= n; j++) {
                order -= valid[j];
                if (order == 0) {
                    ans += to_string(j);  // 将找到的数字添加到结果中
                    valid[j] = 0;  // 将已经使用的数字标记为不可用
                    break;
                }
            }
            
            k %= factorial[n - i];  // 更新 k，去除已经确定的数字对应的排列数
        }

        return ans;  // 返回最终的排列结果
    }
};

```
你需要具备以下基础知识：

**Go 版本：**
1. **Go 语言基础：** 理解 Go 语言的基本语法，包括变量声明、循环、条件语句等。
2. **切片（Slice）：** Go 中的切片是一种动态数组，你需要了解如何使用切片来处理和拼接字符串。
3. **函数：** 了解如何声明和调用函数，以及函数参数和返回值的概念。

**Python 版本：**
1. **Python 基础：** 理解 Python 的基本语法，包括变量、列表、循环、条件语句等。
2. **列表（List）：** Python 中的列表是一种常用的数据结构，你需要知道如何处理和操作列表。
3. **字符串操作：** 了解如何连接字符串和将整数转换为字符串。

**Java 版本：**
1. **Java 基础：** 了解 Java 的基本语法，包括类、方法、变量声明和循环。
2. **数组：** Java 中的数组是一种常见的数据结构，你需要知道如何声明、初始化和使用数组。
3. **StringBuilder：** 了解如何使用 `StringBuilder` 类来高效地构建字符串。

**C++ 版本：**
1. **C++ 基础：** 了解 C++ 的基本语法，包括变量、数组、循环、条件语句等。
2. **字符串操作：** 了解如何连接字符串和将整数转换为字符串。在 C++ 中，你可以使用字符串流（`stringstream`）来转换整数为字符串。
3. **类和对象：** 了解如何创建类和对象，以及如何在类中定义成员函数。

不管你选择哪个编程语言版本，你需要理解问题的核心思想，即如何计算第 k 个排列。你还需要了解每个编程语言的语法和特性，以便正确实现算法。不过，问题的核心解决思路在不同版本中是相同的。