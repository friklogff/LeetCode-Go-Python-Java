# [50. Pow(x, n)](https://leetcode.com/problems/powx-n/)


## 题目

Implement [pow(*x*, *n*)](http://www.cplusplus.com/reference/valarray/pow/), which calculates *x* raised to the power *n* (xn).

**Example 1:**


    Input: 2.00000, 10
    Output: 1024.00000


**Example 2:**


    Input: 2.10000, 3
    Output: 9.26100


**Example 3:**


    Input: 2.00000, -2
    Output: 0.25000
    Explanation: 2-2 = 1/22 = 1/4 = 0.25


**Note:**

- -100.0 < *x* < 100.0
- *n* is a 32-bit signed integer, within the range [−2^31, 2^31− 1]

## 题目大意

实现 pow(x, n) ，即计算 x 的 n 次幂函数。

## 解题思路

- 要求计算 Pow(x, n)
- 这一题用递归的方式，不断的将 n 2 分下去。注意 n 的正负数，n 的奇偶性。
当然，让我们分别介绍每个版本的解题思路：

Go 版本解题思路：

1. **基本情况处理**：首先，检查特殊情况。如果 n 等于 0，直接返回 1，因为任何数的 0 次幂都等于 1。如果 n 等于 1，直接返回 x，因为任何数的 1 次幂都等于它本身。

2. **处理负指数**：如果 n 是负数，将 n 变为其绝对值，同时将 x 变为 1/x。这是因为 x 的负指数等于 1/x 的正指数。

3. **递归计算**：接下来，采用递归的方式计算 x 的 n/2 次幂，将结果存储在 tmp 变量中。这是因为 x^n 可以拆分为 x^(n/2) * x^(n/2)。

4. **处理奇数和偶数**：根据 n 的奇偶性，如果 n 是偶数，返回 tmp 的平方；如果 n 是奇数，返回 tmp 的平方再乘以 x。

Python 版本解题思路：

1. **基本情况处理**：同样，首先检查特殊情况。如果 n 等于 0，返回 1。如果 n 等于 1，返回 x。

2. **处理负指数**：如果 n 是负数，将 n 变为其绝对值，同时将 x 变为 1/x。

3. **递归计算**：使用递归计算 x 的 n/2 次幂，将结果存储在 tmp 变量中。

4. **处理奇数和偶数**：根据 n 的奇偶性，如果 n 是偶数，返回 tmp 的平方；如果 n 是奇数，返回 tmp 的平方再乘以 x。

Java 版本解题思路：

1. **基本情况处理**：同样，首先检查特殊情况。如果 n 等于 0，返回 1。如果 n 等于 1，返回 x。

2. **处理负指数**：如果 n 是负数，将 n 变为其绝对值，同时将 x 变为 1/x。

3. **递归计算**：使用递归计算 x 的 n/2 次幂，将结果存储在 tmp 变量中。

4. **处理奇数和偶数**：根据 n 的奇偶性，如果 n 是偶数，返回 tmp 的平方；如果 n 是奇数，返回 tmp 的平方再乘以 x。

C++ 版本解题思路：

1. **基本情况处理**：同样，首先检查特殊情况。如果 n 等于 0，返回 1。如果 n 等于 1，返回 x。

2. **处理负指数**：如果 n 是负数，将 n 变为其绝对值，同时将 x 变为 1/x。

3. **数据类型转换**：将 n 转换为 long long 类型，以避免整数溢出问题。

4. **递归计算**：使用递归计算 x 的 n/2 次幂，将结果存储在 tmp 变量中。

5. **处理奇数和偶数**：根据 n 的奇偶性，如果 n 是偶数，返回 tmp 的平方；如果 n 是奇数，返回 tmp 的平方再乘以 x。

这些是每个版本中用于解决 Pow(x, n) 问题的主要思路。它们都利用了递归来拆分问题，同时考虑了指数的正负性和奇偶性，以获得最终的结果。
## 代码

## Go

```Go
// 时间复杂度 O(log n), 空间复杂度 O(1)
func myPow(x float64, n int) float64 {
    if n == 0 {
        return 1
    }
    if n == 1 {
        return x
    }
    if n < 0 {
        n = -n
        x = 1 / x
    }
    // 递归计算 x 的 n/2 次幂
    tmp := myPow(x, n/2)
    if n%2 == 0 {
        // 如果 n 为偶数，则返回 tmp 的平方
        return tmp * tmp
    }
    // 如果 n 为奇数，则返回 tmp 的平方再乘以 x
    return tmp * tmp * x
}

```

## Python

```Python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            n = -n
            x = 1 / x
        tmp = self.myPow(x, n // 2)
        if n % 2 == 0:
            return tmp * tmp
        return tmp * tmp * x

```

## Java

```Java
class Solution {
    public double myPow(double x, long n) {
        if (n == 0) {
            return 1;
        }
        if (n == 1) {
            return x;
        }
        if (n < 0) {
            n = -n;
            x = 1 / x;
        }
        double tmp = myPow(x, n / 2);
        if (n % 2 == 0) {
            return tmp * tmp;
        }
        return tmp * tmp * x;
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0) {
            return 1.0;
        }
        if (n == 1) {
            return x;
        }
        long long absN = n; // 将 n 转换为 long long 类型
…};
```
当然，让我们逐个版本介绍并讨论所需的基础知识：

Go 版本：

1. **基本的 Go 语言知识**: 在编写 Go 代码之前，你需要了解 Go 语言的基本语法、数据类型、变量声明、函数定义等基础知识。

2. **递归**: 这个算法使用递归来计算幂函数。了解递归的概念和如何在 Go 中编写递归函数是很重要的。

3. **条件语句**: 代码中使用了条件语句（`if` 和 `if-else`）来处理不同情况，例如 n 的正负性和奇偶性。

Python 版本：

1. **Python 语言基础**: 你需要了解 Python 语言的基础知识，包括变量、函数、条件语句、递归等。

2. **递归**: 和 Go 版本一样，Python 版本也使用递归来计算幂函数。了解递归的概念和如何在 Python 中编写递归函数很重要。

Java 版本：

1. **Java 语言基础**: 你需要熟悉 Java 语言的基础，包括类的定义、方法的声明、条件语句等。

2. **递归**: 与前两个版本一样，Java 版本也使用递归来计算幂函数。了解递归的概念以及如何在 Java 中编写递归函数是必要的。

3. **数据类型转换**: Java 版本中对 n 进行了数据类型转换，将 int 转换为 long。了解数据类型转换的概念在处理数据时非常重要。

C++ 版本：

1. **C++ 语言基础**: 你需要熟悉 C++ 语言的基础知识，包括类的定义、函数的声明、条件语句等。

2. **递归**: 与其他版本一样，C++ 版本也使用递归来计算幂函数。了解递归的概念以及如何在 C++ 中编写递归函数是必要的。

3. **数据类型**: C++ 版本中使用了 long long 数据类型来处理 n，这是为了避免整数溢出问题。了解 C++ 的数据类型和溢出问题是重要的。

这些是每个版本中需要掌握的基础知识要点。如果你对其中任何一个版本有更具体的问题或需要进一步的解释，请随时提问。