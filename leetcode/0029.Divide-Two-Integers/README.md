# [29. Divide Two Integers](https://leetcode.com/problems/divide-two-integers/)

## 题目

Given two integers`dividend`and`divisor`, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing`dividend`by`divisor`.

The integer division should truncate toward zero.

**Example 1:**

    Input: dividend = 10, divisor = 3
    Output: 3

**Example 2:**

    Input: dividend = 7, divisor = -3
    Output: -2

**Note:**

- Both dividend and divisor will be 32-bit signed integers.
- The divisor will never be 0.
- Assume we are dealing with an environment which could only store integers within the 32-bit signed integer
  range: [−2^31, 2^31 − 1]. For the purpose of this problem, assume that your function returns 2^31 − 1 when the
  division result overflows.

## 题目大意

给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。返回被除数 dividend 除以除数
divisor 得到的商。

说明:

- 被除数和除数均为 32 位有符号整数。
- 除数不为 0。
- 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 2^31 − 1。

## 解题思路

- 给出除数和被除数，要求计算除法运算以后的商。注意值的取值范围在 [−2^31, 2^31 − 1] 之中。超过范围的都按边界计算。
- 这一题可以用二分搜索来做。要求除法运算之后的商，把商作为要搜索的目标。商的取值范围是 [0, dividend]，所以从 0
  到被除数之间搜索。利用二分，找到(商 + 1 ) * 除数 > 被除数并且 商 * 除数 ≤ 被除数 或者 (商+1)* 除数 ≥ 被除数并且商 *
  除数 < 被除数的时候，就算找到了商，其余情况继续二分即可。最后还要注意符号和题目规定的 Int32 取值范围。
- 二分的写法常写错的 3 点：
    1. low ≤ high (注意二分循环退出的条件是小于等于)
    2. mid = low + (high-low)>>1 (防止溢出)
    3. low = mid + 1 ; high = mid - 1 (注意更新 low 和 high 的值，如果更新不对就会死循环)
以下是每个版本的解题思路的详细介绍：

Go 版本

Go 版本的解题思路如下：

1. 首先，处理特殊情况，包括被除数（dividend）等于 0，除数（divisor）等于 1，以及避免溢出的情况（例如，被除数为math.MinInt32，除数为-1）。

2. 确定最终结果的符号（正数或负数），并将被除数和除数都转换为正数，以便进行位运算。

3. 使用二分搜索来找到商。二分搜索的目标是找到一个整数 x，使得 `(x + 1) * divisor > dividend` 且 `x * divisor ≤ dividend`，或者 `(x + 1) * divisor ≥ dividend` 且 `x * divisor < dividend`。这个 x 就是我们要找的商。

4. 在二分搜索的过程中，确保更新搜索的范围和值，同时处理可能的溢出情况。

5. 最后，根据符号和边界情况返回最终的商。

Python 版本

Python 版本的解题思路如下：

1. 处理特殊情况，包括被除数等于 0，除数等于 1，以及避免溢出的情况（例如，被除数为-2^31，除数为-1）。

2. 确定最终结果的符号（正数或负数），并将被除数和除数都转换为正数，以便进行位运算。

3. 使用递归的二分搜索方法来找到商。递归函数的目标是找到一个整数 x，使得 `(x + 1) * divisor > dividend` 且 `x * divisor ≤ dividend`，或者 `(x + 1) * divisor ≥ dividend` 且 `x * divisor < dividend`。这个 x 就是我们要找的商。

4. 在递归的过程中，确保更新搜索的范围和值，同时处理可能的溢出情况。

5. 最后，根据符号和边界情况返回最终的商。

Java 版本

Java 版本的解题思路如下：

1. 处理特殊情况，包括被除数等于 0，除数等于 1，以及避免溢出的情况（例如，被除数为Integer.MIN_VALUE，除数为-1）。

2. 确定最终结果的符号（正数或负数），并将被除数和除数都转换为正数，以便进行位运算。

3. 使用递归的二分搜索方法来找到商。递归函数的目标是找到一个整数 x，使得 `(x + 1) * divisor > dividend` 且 `x * divisor ≤ dividend`，或者 `(x + 1) * divisor ≥ dividend` 且 `x * divisor < dividend`。这个 x 就是我们要找的商。

4. 在递归的过程中，确保更新搜索的范围和值，同时处理可能的溢出情况。

5. 最后，根据符号和边界情况返回最终的商。

C++ 版本

C++ 版本的解题思路如下：

1. 处理特殊情况，包括被除数等于 0，除数等于 1，以及避免溢出的情况（例如，被除数为INT_MIN，除数为-1）。

2. 确定最终结果的符号（正数或负数），并将被除数和除数都转换为正数，以便进行位运算。

3. 使用递归的二分搜索方法来找到商。递归函数的目标是找到一个整数 x，使得 `(x + 1) * divisor > dividend` 且 `x * divisor ≤ dividend`，或者 `(x + 1) * divisor ≥ dividend` 且 `x * divisor < dividend`。这个 x 就是我们要找的商。

4. 在递归的过程中，确保更新搜索的范围和值，同时处理可能的溢出情况。

5. 最后，根据符号和边界情况返回最终的商。

总之，这些解决方案的核心思想都是使用二分搜索来找到商，同时处理特殊情况和溢出情况，以确保最终的计算结果正确。递归函数在实现中被广泛用于搜索过程。
## 代码

## Go

```Go
func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}

// 解法一 递归版的二分搜索
func divide(dividend int, divisor int) int {
    sign, res := -1, 0
    // low, high := 0, abs(dividend)
    if dividend == 0 {
        return 0
    }
    if divisor == 1 {
        return dividend
    }
    if dividend == math.MinInt32 && divisor == -1 {
        return math.MaxInt32
    }
    if dividend > 0 && divisor > 0 || dividend < 0 && divisor < 0 {
        sign = 1
    }
    if dividend > math.MaxInt32 {
        dividend = math.MaxInt32
    }

    // 调用二分搜索函数计算商
    res = binarySearchQuotient(0, abs(dividend), abs(divisor), abs(dividend))

    // 处理溢出情况
    if res > math.MaxInt32 {
        return sign * math.MaxInt32
    }
    if res < math.MinInt32 {
        return sign * math.MinInt32
    }
    return sign * res
}

// 二分搜索函数，用于计算商
func binarySearchQuotient(low, high, val, dividend int) int {
    quotient := low + (high-low)>>1
    if ((quotient+1)*val > dividend && quotient*val <= dividend) || ((quotient+1)*val >= dividend && quotient*val < dividend) {
        if (quotient+1)*val == dividend {
            return quotient + 1
        }
        return quotient
    }
    if (quotient+1)*val > dividend && quotient*val > dividend {
        return binarySearchQuotient(low, quotient-1, val, dividend)
    }
    if (quotient+1)*val < dividend && quotient*val < dividend {
        return binarySearchQuotient(quotient+1, high, val, dividend)
    }
    return 0
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}



// 解法二 非递归版的二分搜索
func divide(dividend int, divisor int) int {
    if dividend == math.MinInt32 && divisor == -1 {
        return math.MaxInt32
    }
    result := 0
    sign := -1
    if dividend > 0 && divisor > 0 || dividend < 0 && divisor < 0 {
        sign = 1
    }
    dividendAbs, divisorAbs := abs(dividend), abs(divisor)
    for dividendAbs >= divisorAbs {
        temp := divisorAbs
        multiplier := 1
        for temp<<1 <= dividendAbs {
            temp <<= 1
            multiplier <<= 1
        }
        dividendAbs -= temp
        result += multiplier
    }
    return sign * result
}
```

## Python

```Python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 递归版
        def recursive_divide(dividend, divisor):
            if dividend < divisor:
                return 0
            quotient = 1
            div = divisor
            while (div + div) <= dividend:
                div += div
                quotient += quotient
            return quotient + recursive_divide(dividend - div, divisor)

        if dividend == 0:
            return 0
        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1

        sign = 1 if (dividend > 0) == (divisor > 0) else -1
        dividend, divisor = abs(dividend), abs(divisor)

        result = recursive_divide(dividend, divisor)
        return sign * result


class Solution:

    # 非递归版
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1

        sign = 1 if (dividend > 0) == (divisor > 0) else -1
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0

        while dividend >= divisor:
            temp, m = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                m <<= 1
            dividend -= temp
            result += m

        return sign * result
```

## Java

```Java
class Solution {
    public int divide(int dividend, int divisor) {
        // 递归版
        if (dividend == 0) {
            return 0;
        }
        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        }

        int sign = (dividend > 0) == (divisor > 0) ? 1 : -1;
        long dvd = Math.abs((long) dividend);
        long dvs = Math.abs((long) divisor);

        int result = recursiveDivide(dvd, dvs);
        return sign * result;
    }

    private int recursiveDivide(long dividend, long divisor) {
        if (dividend < divisor) {
            return 0;
        }
        int quotient = 1;
        long div = divisor;
        while ((div + div) <= dividend) {
            div += div;
            quotient += quotient;
        }
        return quotient + recursiveDivide(dividend - div, divisor);
    }

}
class Solution {

    // 非递归版
    public int divide(int dividend, int divisor) {
        if (dividend == 0) {
            return 0;
        }
        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        }

        int sign = (dividend > 0) == (divisor > 0) ? 1 : -1;
        long dvd = Math.abs((long) dividend);
        long dvs = Math.abs((long) divisor);

        int result = 0;

        while (dvd >= dvs) {
            long temp = dvs;
            int m = 1;
            while (dvd >= (temp << 1)) {
                temp <<= 1;
                m <<= 1;
            }
            dvd -= temp;
            result += m;
        }

        return sign * result;
    }
}
```

## Cpp

```Cpp
class Solution {
public:
    int divide(int dividend, int divisor) {
        // 处理特殊情况
        if (dividend == 0) {
            return 0;
        }
        if (divisor == 1) {
            return dividend;
        }
        if (dividend == INT_MIN && divisor == -1) {
            return INT_MAX;
        }
        
        int sign = (dividend > 0 && divisor > 0) || (dividend < 0 && divisor < 0) ? 1 : -1;
        
        // 处理溢出情况
        if (dividend > INT_MAX) {
            dividend = INT_MAX;
        }
        
        return sign * binarySearchQuotient(0, abs((long)dividend), abs((long)divisor), abs((long)dividend));
    }
    
private:
    int binarySearchQuotient(long low, long high, long val, long dividend) {
        long quotient = low + (high - low) / 2;
        if (((quotient + 1) * val > dividend && quotient * val <= dividend) || 
            ((quotient + 1) * val >= dividend && quotient * val < dividend)) {
            if ((quotient + 1) * val == dividend) {
                return quotient + 1;
            }
            return quotient;
        }
        if ((quotient + 1) * val > dividend && quotient * val > dividend) {
            return binarySearchQuotient(low, quotient - 1, val, dividend);
        }
        if ((quotient + 1) * val < dividend && quotient * val < dividend) {
            return binarySearchQuotient(quotient + 1, high, val, dividend);
        }
        return 0;
    }
};

class Solution {
public:
    int divide(int dividend, int divisor) {
        // 处理特殊情况
        if (dividend == INT_MIN && divisor == -1) {
            return INT_MAX;
        }
        
        int result = 0;
        int sign = (dividend > 0 && divisor > 0) || (dividend < 0 && divisor < 0) ? 1 : -1;
        long dvd = abs((long)dividend);
        long dvs = abs((long)divisor);
        
        while (dvd >= dvs) {
            long temp = dvs;
            long m = 1;
            while (temp << 1 <= dvd) {
                temp <<= 1;
                m <<= 1;
            }
            dvd -= temp;
            
            // 处理溢出情况
            if (result > INT_MAX - m) {
                return sign == 1 ? INT_MAX : INT_MIN;
            }
            result += m;
        }
        
        return sign * result;
    }
};

```
当讨论每个版本的解决方案时，我将分开介绍所需的详细基础知识。

Go 版本

1. **Go 语言基础**: 在理解 Go 版本的解决方案之前，您需要熟悉 Go 语言的基础知识，包括变量、函数、条件语句、循环等。

2. **递归**: Go 版本的解决方案中使用了递归来实现二分搜索，因此需要了解递归的概念和用法。

3. **位运算**: Go 版本中使用位运算来处理细节，如符号、边界情况等。因此，您需要了解 Go 中的位运算操作符（如`<<`、`>>`）和位运算的基本原理。

4. **边界情况处理**: 了解如何处理边界情况是解决这个问题的关键之一，因为输入和输出受到了限制。需要考虑最小和最大的 32 位有符号整数。

Python 版本

1. **Python 语言基础**: 您需要熟悉 Python 语言的基础知识，包括变量、函数、条件语句、循环以及整数溢出处理。

2. **递归**: Python 版本中的递归解决方案使用了递归函数来实现二分搜索。您需要了解如何编写递归函数以及递归的工作原理。

3. **位运算**: 位运算在 Python 版本中也被用于处理符号和边界情况。了解 Python 中的位运算操作符（如`<<`、`>>`）和位运算的基本原理将有助于理解解决方案。

Java 版本

1. **Java 语言基础**: 在理解 Java 版本的解决方案之前，您需要熟悉 Java 语言的基础知识，包括类、方法、条件语句、循环以及整数溢出处理。

2. **递归**: Java 版本的解决方案使用了递归函数来实现二分搜索。您需要了解如何编写递归函数以及递归的工作原理。

3. **位运算**: 位运算在 Java 版本中用于处理符号和边界情况。了解 Java 中的位运算操作符（如`<<`、`>>`）和位运算的基本原理将有助于理解解决方案。

4. **整数溢出处理**: Java 版本考虑了整数溢出情况，并采取了措施来防止溢出。您需要了解 Java 中整数溢出的特点以及如何处理它。

C++ 版本

1. **C++ 语言基础**: 在理解 C++ 版本的解决方案之前，您需要熟悉 C++ 语言的基础知识，包括类、函数、条件语句、循环以及整数溢出处理。

2. **递归**: C++ 版本的解决方案使用了递归函数来实现二分搜索。您需要了解如何编写递归函数以及递归的工作原理。

3. **位运算**: 位运算在 C++ 版本中用于处理符号和边界情况。了解 C++ 中的位运算操作符（如`<<`、`>>`）和位运算的基本原理将有助于理解解决方案。

4. **整数溢出处理**: C++ 版本考虑了整数溢出情况，并采取了措施来防止溢出。您需要了解 C++ 中整数溢出的特点以及如何处理它。

总之，理解每个版本的解决方案需要对编程语言的基础知识、递归、位运算和整数溢出处理有一定的了解。此外，了解问题的特殊要求和边界情况也是解决这个问题的关键。