# [67. Add Binary](https://leetcode.com/problems/add-binary/)


## 题目

Given two binary strings, return their sum (also a binary string).

The input strings are both **non-empty** and contains only characters `1` or `0`.

**Example 1**:

```
Input: a = "11", b = "1"
Output: "100"
```

**Example 2**:

```
Input: a = "1010", b = "1011"
Output: "10101"
```

## 题目大意

给你两个二进制字符串，返回它们的和（用二进制表示）。输入为 非空 字符串且只包含数字 1 和 0。

## 解题思路

- 要求输出 2 个二进制数的和，结果也用二进制表示。
- 简单题。按照二进制的加法规则做加法即可。
继续解释每个版本的代码的思路和实现：

**Go 版本解题思路**：
1. 代码首先检查输入的两个二进制字符串，如果其中一个比另一个长，就进行交换，确保 `a` 永远比 `b` 长。
2. 创建一个结果切片 `res` 用于存储最终结果，长度初始化为 `len(a) + 1`，以容纳可能的最高位进位。
3. 使用三个指针 `i`、`j` 和 `k`，`i` 和 `j` 分别从 `a` 和 `b` 的最低位开始向左遍历，`k` 从 `res` 的最高位开始向左遍历。
4. 在循环中，对应位的值（0 或 1）从 `a` 和 `b` 中提取并与进位 `c` 相加，然后更新 `res[k]` 为该位的结果，并计算新的进位值。
5. 遍历结束后，如果仍有进位，将进位的值 `c` 放入 `res` 的最高位。
6. 最后，使用 `strings.Join` 将结果切片中的字符串元素连接在一起，并返回最终的二进制字符串。

**Python 版本解题思路**：
1. 代码首先检查输入的两个二进制字符串，如果其中一个比另一个长，就进行交换，确保 `a` 永远比 `b` 长。
2. 创建一个结果字符列表 `res` 用于存储最终结果。
3. 使用三个指针 `i`、`j` 和 `k`，`i` 和 `j` 分别从 `a` 和 `b` 的最低位开始向左遍历，`k` 从 `res` 的最高位开始向左遍历。
4. 在循环中，对应位的值（'0' 或 '1'）从 `a` 和 `b` 中提取并与进位 `c` 相加，然后将当前位的结果添加到 `res` 中，并计算新的进位值。
5. 遍历结束后，如果仍有进位，将进位的值 `c` 作为最高位添加到 `res` 中。
6. 最后，将结果字符列表中的字符连接在一起，返回最终的二进制字符串。

**Java 版本解题思路**：
1. 如果两个输入字符串的长度不同，代码会交换它们，以确保 `a` 始终比 `b` 长。
2. 创建一个字符数组用于存储结果，长度为 `a.length() + 1`（以容纳可能的最高位进位）。
3. 从最低位（字符串的末尾）开始逐位相加。
4. 对于每一对相应的位，考虑进位，然后计算当前位的值并更新进位。
5. 将当前位的值（'0' 或 '1'）存储在结果字符数组中。
6. 如果循环结束后仍然有进位，将进位（'0' 或 '1'）放在结果字符数组的最高位。
7. 根据进位情况返回最终的二进制字符串，去掉可能的前导零。

**C++ 版本解题思路**：
1. 如果两个输入字符串的长度不同，代码会交换它们，以确保 `a` 始终比 `b` 长。
2. 创建一个字符串（`std::string`）用于存储结果。
3. 从最低位（字符串的末尾）开始逐位相加。
4. 对于每一对相应的位，考虑进位，然后计算当前位的值并更新进位。
5. 将当前位的值（'0' 或 '1'）添加到结果字符串中。
6. 如果循环结束后仍然有进位，将进位（'0' 或 '1'）添加到结果字符串的最高位。
7. 最后，返回最终的二进制字符串。

在所有版本中，主要思路都是处理进位，逐位相加并生成结果，最后处理可能的前导零。这些实现根据各自编程语言的特性和库函数来操作字符串、数组或切片。
## 代码

```go

package leetcode

import (
	"strconv"
	"strings"
)

func addBinary(a string, b string) string {
	if len(b) > len(a) {
		a, b = b, a
	}

	res := make([]string, len(a)+1)
	i, j, k, c := len(a)-1, len(b)-1, len(a), 0
	for i >= 0 && j >= 0 {
		ai, _ := strconv.Atoi(string(a[i]))
		bj, _ := strconv.Atoi(string(b[j]))
		res[k] = strconv.Itoa((ai + bj + c) % 2)
		c = (ai + bj + c) / 2
		i--
		j--
		k--
	}

	for i >= 0 {
		ai, _ := strconv.Atoi(string(a[i]))
		res[k] = strconv.Itoa((ai + c) % 2)
		c = (ai + c) / 2
		i--
		k--
	}

	if c > 0 {
		res[k] = strconv.Itoa(c)
	}

	return strings.Join(res, "")
}

```
## 代码

## Go

```Go
func addBinary(a string, b string) string {
    m, n := len(a), len(b)
    max := m

    // 确保a和b的长度一致，如果不一致，将短的字符串前面补0，使它们长度相等
    if m > n {
        b = strings.Repeat("0", m-n) + b
    } else if n > m {
        max = n
        a = strings.Repeat("0", n-m) + a
    }

    res := make([]byte, max)
    var carry byte

    // 从最高位开始逐位相加
    for i := max - 1; i >= 0; i-- {
        tmp := a[i] - '0' + b[i] - '0' + carry
        res[i] = tmp % 2
        carry = tmp / 2
    }

    // 如果最高位有进位，添加1到结果的最前面
    if carry > 0 {
        res = append([]byte{1}, res...)
    }

    s := ""
    
    // 将结果转换为字符串
    for i := 0; i < len(res); i++ {
        s += strconv.Itoa(int(res[i]))
    }

    return s
}

```

## Python

```Python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 确保b的长度不大于a，如果b更长，交换它们
        if len(b) > len(a):
            a, b = b, a

        res = [''] * (len(a) + 1)
        i, j, k, c = len(a) - 1, len(b) - 1, len(a), 0

        while i >= 0 and j >= 0:
            ai = int(a[i])
            bj = int(b[j])
            res[k] = str((ai + bj + c) % 2)
            c = (ai + bj + c) // 2
            i -= 1
            j -= 1
            k -= 1

        while i >= 0:
            ai = int(a[i])
            res[k] = str((ai + c) % 2)
            c = (ai + c) // 2
            i -= 1
            k -= 1

        if c > 0:
            res[k] = str(c)

        return ''.join(res)

```

## Java

```Java
class Solution {
    public static String addBinary(String a, String b) {
        // 如果a的长度小于b的长度，交换a和b
        if (a.length() < b.length()) {
            return addBinary(b, a);
        }
        
        // 创建一个字符数组，用于存储相加的结果，长度比a的长度多1
        char[] sum = new char[a.length() + 1];
        
        int indexA = a.length() - 1; // a的索引
        int diffLen = a.length() - b.length(); // a和b的长度差
        char carry = '0'; // 进位初始化为0

        // 从最低位开始逐位相加
        while (indexA > -1) {
            char bitB = indexA - diffLen > -1 ? b.charAt(indexA - diffLen) : '0'; // 获取b的对应位或补0
            if (a.charAt(indexA) == bitB) {
                sum[indexA + 1] = carry;
                carry = bitB;
            } else {
                sum[indexA + 1] = carry == '0' ? '1' : '0';
            }
            indexA--;
        }

        sum[0] = carry; // 设置最高位

        // 根据进位返回最终的二进制字符串，去掉可能的前导零
        return carry == '1' ? new String(sum, 0, a.length() + 1) : new String(sum, 1, a.length());
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    string addBinary(string a, string b) {
        int m = a.length();
        int n = b.length();
        int maxLen = max(m, n);

        // 确保a和b的长度一致，如果不一致，将短的字符串前面补0，使它们长度相等
        if (m > n) {
            b = string(m - n, '0') + b;
…        return res;
    }
};
```
当处理LeetCode问题时，不同的编程语言可能需要不同的基础知识。以下是每个版本的实现需要的基础知识和关键概念的详细介绍：

**Go 版本**：
- **字符串操作**：Go中有许多内置函数和方法用于字符串操作，例如`strings.Repeat`和`strings.Join`。在这个实现中，它们用于处理二进制字符串的填充和拼接。
- **切片（Slices）**：Go中的切片是动态数组，它们用于存储结果。在循环中，切片的长度可能会发生变化，这需要了解如何使用切片来动态管理数据。

**Python 版本**：
- **字符串操作**：Python提供了丰富的字符串操作方法。在这个实现中，您会看到`str`类型的字符串，以及字符串的切片和拼接操作。
- **列表（Lists）**：Python中的列表类似于数组，它们用于存储结果。了解如何创建、修改和迭代列表是很重要的。
- **整数和字符之间的转换**：在实现中，您需要将字符('0' 和 '1')转换为整数，以便进行加法操作。Python提供了`int`和`str`之间的转换方法。

**Java 版本**：
- **字符串操作**：Java中的字符串是不可变的，但在这个实现中，您需要了解如何创建和操作字符数组以构建结果字符串。
- **字符和整数之间的转换**：在实现中，需要将字符（'0' 和 '1'）转换为整数。Java提供了`Character.getNumericValue`方法来执行这种转换。
- **数组**：Java中的数组用于存储结果。了解如何创建、修改和访问数组元素非常重要。

**C++ 版本**：
- **字符串操作**：C++中的字符串可以使用`std::string`来表示，而`std::to_string`函数用于将整数转换为字符串。这在处理二进制字符串的填充和结果字符串的构建中很有用。
- **字符和整数之间的转换**：需要将字符（'0' 和 '1'）转换为整数。C++提供了`std::stoi`函数来执行这种转换。
- **数组（Vectors）**：C++中的`std::vector`类似于动态数组，用于存储结果。了解如何创建、修改和访问`std::vector`元素是很重要的。

在每个版本中，还需要理解循环结构和逻辑控制，以便正确地执行二进制加法。此外，要处理进位和结果的拼接，需要了解位运算和字符串操作的基础知识。

不管使用哪种编程语言，理解二进制加法的规则和位运算是解决这个问题的关键。在实际编码中，根据编程语言的特性，选择合适的数据结构和字符串操作方法来实现算法是很重要的。