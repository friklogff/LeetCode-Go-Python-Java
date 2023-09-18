# [43. Multiply Strings](https://leetcode.com/problems/multiply-strings/)

## 题目

Given two non-negative integers`num1`and`num2`represented as strings, return the product of`num1`and`num2`, also
represented as a string.

**Note:**You must not use any built-in BigInteger library or convert the inputs to integer directly.

**Example 1:**

```
Input: num1 = "2", num2 = "3"
Output: "6"
```

**Example 2:**

```
Input: num1 = "123", num2 = "456"
Output: "56088"
```

**Constraints:**

- `1 <= num1.length, num2.length <= 200`
- `num1`and`num2`consist of digits only.
- Both`num1`and`num2`do not contain any leading zero, except the number`0`itself.

## 题目大意

给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

## 解题思路

- 用数组模拟乘法。创建一个数组长度为 `len(num1) + len(num2)`
  的数组用于存储乘积。对于任意 `0 ≤ i < len(num1)`，`0 ≤ j < len(num2)`，`num1[i] * num2[j]` 的结果位于 `tmp[i+j+1]`
  ，如果 `tmp[i+j+1]≥10`，则将进位部分加到 `tmp[i+j]`。最后，将数组 `tmp` 转成字符串，如果最高位是 0 则舍弃最高位。
下面分别介绍每个版本的解题思路：

Go 版本解题思路

1. 首先，检查输入的 `num1` 和 `num2` 是否为 "0"，如果其中一个是 "0"，则返回 "0"，因为任何数乘以 0 都等于 0。

2. 创建一个整数切片 `tmp`，其长度为 `len(num1) + len(num2)`，用于存储乘法的中间结果。

3. 使用嵌套循环遍历 `num1` 和 `num2` 的每个字符，将对应位置的数字相乘，并将结果累加到 `tmp` 中合适的位置。

4. 处理进位：从右向左遍历 `tmp`，将每一位的进位加到前一位上，并将当前位取模 10 以保持在 0 到 9 的范围内。

5. 如果 `tmp` 的最高位为 0，则去除最高位的 0。

6. 将 `tmp` 切片中的数字转换为字符，并构建结果字符串。

7. 返回结果字符串。

Python 版本解题思路

1. 首先，检查输入的 `num1` 和 `num2` 是否为 "0"，如果其中一个是 "0"，则返回 "0"，因为任何数乘以 0 都等于 0。

2. 使用内置的 `int()` 函数将 `num1` 和 `num2` 转换为整数，然后将它们相乘，得到整数结果。

3. 将整数结果转换为字符串，并返回。

Java 版本解题思路

1. 首先，检查输入的 `num1` 和 `num2` 是否为 "0"，如果其中一个是 "0"，则返回 "0"，因为任何数乘以 0 都等于 0。

2. 将 `num1` 和 `num2` 转换为字符数组 `b1` 和 `b2`。

3. 创建一个整数数组 `tmp`，其长度为 `num1.length() + num2.length()`，用于存储乘法的中间结果。

4. 使用嵌套循环遍历 `b1` 和 `b2` 的每个字符，将对应位置的数字相乘，并将结果累加到 `tmp` 中合适的位置。

5. 处理进位：从右向左遍历 `tmp`，将每一位的进位加到前一位上，并将当前位取模 10 以保持在 0 到 9 的范围内。

6. 如果 `tmp` 的最高位为 0，则去除最高位的 0。

7. 构建结果字符串，将 `tmp` 数组中的数字转换为字符。

8. 返回结果字符串。

C++ 版本解题思路

1. 首先，检查输入的 `num1` 和 `num2` 是否为 "0"，如果其中一个是 "0"，则返回 "0"，因为任何数乘以 0 都等于 0。

2. 将 `num1` 和 `num2` 转换为字符数组 `b1` 和 `b2`。

3. 创建一个整数数组 `tmp`，其长度为 `num1.length() + num2.length()`，用于存储乘法的中间结果。

4. 使用嵌套循环遍历 `b1` 和 `b2` 的每个字符，将对应位置的数字相乘，并将结果累加到 `tmp` 中合适的位置。

5. 处理进位：从右向左遍历 `tmp`，将每一位的进位加到前一位上，并将当前位取模 10 以保持在 0 到 9 的范围内。

6. 如果 `tmp` 的最高位为 0，则去除最高位的 0。

7. 构建结果字符串，将 `tmp` 数组中的数字转换为字符。

8. 返回结果字符串。

总体来说，这些版本的解题思路都是类似的，都是模拟手工乘法的过程，将每一位的乘积存储在中间数组中，然后处理进位并构建最终的结果字符串。不同的编程语言具有不同的语法和数据结构，但基本思路是一致的。
## 代码

## Go

```Go
func multiply(num1 string, num2 string) string {
    if num1 == "0" || num2 == "0" {
        return "0"
    }

    // 将输入的两个字符串转换为字节数组
    b1, b2, tmp := []byte(num1), []byte(num2), make([]int, len(num1)+len(num2))

    // 使用嵌套循环遍历两个输入字符串的每一位数字进行相乘，结果存储在 tmp 数组中
    for i := 0; i < len(b1); i++ {
        for j := 0; j < len(b2); j++ {
            tmp[i+j+1] += int(b1[i]-'0') * int(b2[j]-'0')
        }
    }

    // 处理进位，将 tmp 数组中的每一位数字都保留在 0 到 9 的范围内
    for i := len(tmp) - 1; i > 0; i-- {
        tmp[i-1] += tmp[i] / 10
        tmp[i] = tmp[i] % 10
    }

    // 如果最高位是0，则去除最高位的0
    if tmp[0] == 0 {
        tmp = tmp[1:]
    }

    // 将结果从整数数组转换回字符串
    res := make([]byte, len(tmp))
    for i := 0; i < len(tmp); i++ {
        res[i] = '0' + byte(tmp[i])
    }
    return string(res)
}

```

## Python

```Python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))
```

## Java

```Java
class Solution {
    public String multiply(String num1, String num2) {
        if (num1.equals("0") || num2.equals("0")) {
            return "0";
        }

        char[] b1 = num1.toCharArray();
        char[] b2 = num2.toCharArray();
        int[] tmp = new int[num1.length() + num2.length()];

        for (int i = 0; i < b1.length; i++) {
            for (int j = 0; j < b2.length; j++) {
                tmp[i + j + 1] += (b1[i] - '0') * (b2[j] - '0');
            }
        }

        for (int i = tmp.length - 1; i > 0; i--) {
            tmp[i - 1] += tmp[i] / 10;
            tmp[i] = tmp[i] % 10;
        }

        if (tmp[0] == 0) {
            tmp = Arrays.copyOfRange(tmp, 1, tmp.length);
        }

        StringBuilder result = new StringBuilder();
        for (int num : tmp) {
            result.append(num);
        }

        return result.toString();
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    string multiply(string num1, string num2) {
        if (num1 == "0" || num2 == "0") {
            return "0";
        }

        vector<char> b1(num1.begin(), num1.end());
        vector<char> b2(num2.begin(), num2.end());
        vector<int> tmp(num1.length() + num2.length(), 0);

        for (int i = 0; i < b1.size(); i++) {
            for (int j = 0; j < b2.size(); j++) {
                tmp[i + j + 1] += (b1[i] - '0') * (b2[j] - '0');
            }
        }

        for (int i = tmp.size() - 1; i > 0; i--) {
            tmp[i - 1] += tmp[i] / 10;
            tmp[i] = tmp[i] % 10;
        }

        if (tmp[0] == 0) {
            tmp.erase(tmp.begin());
        }

        string result;
        for (int num : tmp) {
            result += to_string(num);
        }

        return result;
    }
};

```

当使用不同的编程语言实现同一个算法时，你需要掌握与该语言相关的基础知识和语法。以下是每个版本的基础知识要求的详细介绍：

Go 版本

1. **数据类型和变量**: 了解 Go 中的基本数据类型，如整数、字符串和数组。了解如何声明和使用变量。

2. **切片 (Slice)**: Go 中的切片是动态数组，你需要了解如何创建、操作和使用切片来处理字符数组。

3. **循环**: 了解 Go 中的 `for` 循环语句，以便在两个字符串的字符上执行嵌套循环。

4. **条件语句**: 了解 Go 中的 `if` 条件语句，以处理特殊情况，如乘数为 "0" 时的情况。

5. **数组和切片操作**: 理解如何访问数组和切片的元素，以及如何进行数组和切片的迭代。

Python 版本

1. **数据类型和变量**: 了解 Python 中的基本数据类型，如整数、字符串和列表。了解如何声明和使用变量。

2. **字符串操作**: Python 中具有强大的字符串处理功能，需要了解如何访问字符串的字符、切片字符串以及将字符串转换为整数。

3. **循环**: 了解 Python 中的 `for` 循环和 `while` 循环语句，以便在两个字符串的字符上执行嵌套循环。

4. **条件语句**: 了解 Python 中的 `if` 条件语句，以处理特殊情况，如乘数为 "0" 时的情况。

5. **列表 (List)**: 了解如何创建、操作和使用 Python 中的列表数据结构，以存储中间结果。

Java 版本

1. **类和对象**: Java 是面向对象编程语言，需要了解如何创建类和对象，以组织代码。

2. **数据类型和变量**: 了解 Java 中的基本数据类型，如整数、字符串和字符数组。了解如何声明和使用变量。

3. **字符数组操作**: 了解如何创建字符数组，以便在其中存储字符串的字符，并进行字符之间的操作。

4. **循环**: 了解 Java 中的 `for` 循环和 `while` 循环语句，以便在两个字符数组的字符上执行嵌套循环。

5. **条件语句**: 了解 Java 中的 `if` 条件语句，以处理特殊情况，如乘数为 "0" 时的情况。

6. **字符串操作**: Java 提供了许多字符串处理方法，需要了解如何访问字符串的字符、将字符串转换为整数，以及如何使用 `StringBuilder` 类构建结果字符串。

C++ 版本

1. **数据类型和变量**: 了解 C++ 中的基本数据类型，如整数、字符串和数组。了解如何声明和使用变量。

2. **字符数组操作**: 了解如何创建字符数组，以便在其中存储字符串的字符，并进行字符之间的操作。

3. **循环**: 了解 C++ 中的 `for` 循环和 `while` 循环语句，以便在两个字符数组的字符上执行嵌套循环。

4. **条件语句**: 了解 C++ 中的 `if` 条件语句，以处理特殊情况，如乘数为 "0" 时的情况。

5. **字符串操作**: C++ 提供了许多字符串处理函数，需要了解如何访问字符串的字符、将字符串转换为整数，以及如何使用 `stringstream` 构建结果字符串。

无论选择哪个版本，都需要熟悉基本的数据类型、变量声明、循环、条件语句以及与字符串和字符数组相关的操作。此外，了解如何处理特殊情况（例如，一个乘数为 "0"）以及如何将结果从其他数据类型转换为字符串也是解决此问题的关键要点。