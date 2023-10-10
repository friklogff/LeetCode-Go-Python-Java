# [65. Valid Number](https://leetcode.com/problems/valid-number/)


## 题目

A **valid number** can be split up into these components (in order):

   1. A **decimal number** or an integer. 
   2. (Optional) An 'e' or 'E', followed by an **integer.**
   
A **decimal number** can be split up into these components (in order):

   1. (Optional) A sign character (either '+' or '-').
   2. One of the following formats:
        1. One or more digits, followed by a dot '.'.
        2. One or more digits, followed by a dot '.', followed by one or more digits.
        3. A dot '.', followed by one or more digits.
        
An **integer** can be split up into these components (in order):

   1. (Optional) A sign character (either '+' or '-').
   2. One or more digits.
   
For example, all the following are valid numbers: `["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]`, while the following are not valid numbers: `["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].`

Given a string s, return true if s is a **valid number.**

**Example:**

    Input: s = "0"
    Output: true
    
    Input: s = "e"
    Output: false

## 题目大意

给定一个字符串S，请根据以上的规则判断该字符串是否是一个有效的数字字符串。


## 解题思路

- 用三个变量分别标记是否出现过数字、是否出现过'.'和 是否出现过 'e/E'
- 从左到右依次遍历字符串中的每一个元素
    - 如果是数字，则标记数字出现过
    - 如果是 '.', 则需要 '.'没有出现过，并且 'e/E' 没有出现过，才会进行标记
    - 如果是 'e/E', 则需要 'e/E'没有出现过，并且前面出现过数字，才会进行标记
    - 如果是 '+/-', 则需要是第一个字符，或者前一个字符是 'e/E'，才会进行标记，并重置数字出现的标识
    - 最后返回时，需要字符串中至少出现过数字，避免下列case: s == '.' or 'e/E' or '+/e' and etc...
好的，让我再详细介绍每个版本的解题思路：

Go 版本解题思路

1. **标志位设置：** 用三个布尔型变量 `numFlag`、`dotFlag`、`eFlag` 分别标记是否出现过数字、是否出现过小数点、是否出现过指数符号。

2. **遍历字符串：** 从左到右遍历字符串的每个字符。

3. **条件判断：**
   - 如果是数字，将 `numFlag` 置为 true。
   - 如果是小数点，需要确保小数点之前未出现过，并且指数符号未出现过，然后将 `dotFlag` 置为 true。
   - 如果是指数符号，需要确保指数符号之前未出现过，并且之前出现过数字，然后将 `eFlag` 置为 true，并重置 `numFlag`。
   - 如果是正负号，需要是第一个字符，或者前一个字符是指数符号，然后进行标记，并重置数字出现的标识 `numFlag`。
   - 如果是其他字符，返回 false。

4. **返回结果：** 最后需要确保字符串中至少出现过数字，以避免类似字符串为 "." 或 "e" 的特殊情况。

Python 版本解题思路

1. **标志位设置：** 用三个布尔型变量 `numFlag`、`dotFlag`、`eFlag` 分别标记是否出现过数字、是否出现过小数点、是否出现过指数符号。

2. **遍历字符串：** 从左到右遍历字符串的每个字符。

3. **条件判断：**
   - 如果是数字，将 `numFlag` 置为 true。
   - 如果是小数点，需要确保小数点之前未出现过，并且指数符号未出现过，然后将 `dotFlag` 置为 true。
   - 如果是指数符号，需要确保指数符号之前未出现过，并且之前出现过数字，然后将 `eFlag` 置为 true，并重置 `numFlag`。
   - 如果是正负号，需要是第一个字符，或者前一个字符是指数符号，然后进行标记，并重置数字出现的标识 `numFlag`。
   - 如果是其他字符，返回 false。

4. **返回结果：** 最后需要确保字符串中至少出现过数字，以避免类似字符串为 "." 或 "e" 的特殊情况。

Java 版本解题思路

1. **标志位设置：** 用三个布尔型变量 `numFlag`、`dotFlag`、`eFlag` 分别标记是否出现过数字、是否出现过小数点、是否出现过指数符号。

2. **遍历字符串：** 从左到右遍历字符串的每个字符。

3. **条件判断：**
   - 如果是数字，将 `numFlag` 置为 true。
   - 如果是小数点，需要确保小数点之前未出现过，并且指数符号未出现过，然后将 `dotFlag` 置为 true。
   - 如果是指数符号，需要确保指数符号之前未出现过，并且之前出现过数字，然后将 `eFlag` 置为 true，并重置 `numFlag`。
   - 如果是正负号，需要是第一个字符，或者前一个字符是指数符号，然后进行标记，并重置数字出现的标识 `numFlag`。
   - 如果是其他字符，返回 false。

4. **返回结果：** 最后需要确保字符串中至少出现过数字，以避免类似字符串为 "." 或 "e" 的特殊情况。

C++ 版本解题思路

1. **标志位设置：** 用三个布尔型变量 `numFlag`、`dotFlag`、`eFlag` 分别标记是否出现过数字、是否出现过小数点、是否出现过指数符号。

2. **遍历字符串：** 从左到右遍历字符串的每个字符。

3. **条件判断：**
   - 如果是数字，将 `numFlag` 置为 true。
   - 如果是小数点，需要确保小数点之前未出现过，并且指数符号未出现过，然后将 `dotFlag` 置为 true。
   - 如果是指数符号，需要确保指数符号之前未出现过，并且之前出现过数字，然后将 `eFlag` 置为 true，并重置 `numFlag`。
   - 如果是正负号，需要是第一个字符，或者前一个字符是指数符号，然后进行标记，并重置数字出现的标识 `numFlag`。
   - 如果是其他字符，返回 false。

4. **返回结果：** 最后需要确保字符串中至少出现过数字，以避免类似字符串为 "." 或 "e" 的特殊情况。

这些解题思路基本上都是利用标志位来记录数字、小数点和指数符号的出现情况，然后通过条件判断来验证字符串是否是一个有效的数字。希望这样的详细介绍能够帮助理解这些代码的思路。
## 代码

```go


func isNumber(s string) bool {
	numFlag, dotFlag, eFlag := false, false, false // 用于跟踪数字、小数点和指数标志的布尔变量初始化为false
	for i := 0; i < len(s); i++ { // 循环遍历输入字符串的每个字符
		if '0' <= s[i] && s[i] <= '9' { // 如果当前字符是数字0-9之间的字符
			numFlag = true // 设置数字标志为true
		} else if s[i] == '.' && !dotFlag && !eFlag { // 如果当前字符是小数点，且之前未出现小数点且未出现指数符号
			dotFlag = true // 设置小数点标志为true
		} else if (s[i] == 'e' || s[i] == 'E') && !eFlag && numFlag { // 如果当前字符是指数符号 'e' 或 'E'，且之前未出现指数符号且之前出现过数字
			eFlag = true // 设置指数标志为true
			numFlag = false // 重置数字标志以在指数符号后重新判断整数部分
		} else if (s[i] == '+' || s[i] == '-') && (i == 0 || s[i-1] == 'e' || s[i-1] == 'E') {
			// 如果当前字符是正号 '+' 或负号 '-'，且该符号在字符串开头或在指数符号 'e' 或 'E' 的后面
			continue // 继续循环，不执行其他操作
		} else {
			return false // 如果当前字符不满足上述任何条件，则字符串不是有效数字，返回false
		}
	}
	// 避免特殊情况: s == '.' 或 'e/E' 或 '+/-' 等等...
	// 字符串 s 必须包含数字
	return numFlag // 返回数字标志，如果为true，则表示字符串是有效数字，否则为false
}

```

## Python

```Python
class Solution:
    def isNumber(self, s: str) -> bool:
        numFlag, dotFlag, eFlag = False, False, False
        for i in range(len(s)):
            if '0' <= s[i] <= '9':
                numFlag = True
            elif s[i] == '.' and not dotFlag and not eFlag:
                dotFlag = True
            elif (s[i] == 'e' or s[i] == 'E') and not eFlag and numFlag:
                eFlag = True
                numFlag = False
            elif (s[i] == '+' or s[i] == '-') and (i == 0 or s[i-1] == 'e' or s[i-1] == 'E'):
                continue
            else:
                return False
        return numFlag

```

## Java

```Java
class Solution {
    public boolean isNumber(String s) {
        boolean numFlag = false, dotFlag = false, eFlag = false;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) >= '0' && s.charAt(i) <= '9') {
                numFlag = true;
            } else if (s.charAt(i) == '.' && !dotFlag && !eFlag) {
                dotFlag = true;
            } else if ((s.charAt(i) == 'e' || s.charAt(i) == 'E') && !eFlag && numFlag) {
                eFlag = true;
                numFlag = false;
            } else if ((s.charAt(i) == '+' || s.charAt(i) == '-') && (i == 0 || s.charAt(i-1) == 'e' || s.charAt(i-1) == 'E')) {
                continue;
            } else {
                return false;
            }
        }
        return numFlag;
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    bool isNumber(string s) {
        bool numFlag = false, dotFlag = false, eFlag = false;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] >= '0' && s[i] <= '9') {
                numFlag = true;
            } else if (s[i] == '.' && !dotFlag && !eFlag) {
                dotFlag = true;
            } else if ((s[i] == 'e' || s[i] == 'E') && !eFlag && numFlag) {
                eFlag = true;
                numFlag = false;
            } else if ((s[i] == '+' || s[i] == '-') && (i == 0 || s[i-1] == 'e' || s[i-1] == 'E')) {
                continue;
            } else {
                return false;
            }
        }
        return numFlag;
    }
};

```
每个版本的代码所需要的基础知识：

Go 版本

1. **基础数据类型：** 代码中对数字、布尔类型进行了处理，所以需要了解 Go 语言的基础数据类型，包括整数和浮点数。

2. **字符串操作：** 对字符串进行了遍历和字符比较操作，需要了解 Go 语言中字符串的基本操作。

3. **循环和条件语句：** 代码使用了 `for` 循环和 `if` 条件语句，因此需要了解 Go 中的循环和条件语句的使用。

Python 版本

1. **基础数据类型：** 代码中同样对数字、布尔类型进行了处理，因此需要了解 Python 的基础数据类型，包括整数和浮点数。

2. **字符串操作：** 对字符串进行了遍历和字符比较操作，需要了解 Python 中字符串的基本操作。

3. **循环和条件语句：** 代码使用了 `for` 循环和 `if` 条件语句，因此需要了解 Python 中的循环和条件语句的使用。

Java 版本

1. **基础数据类型：** 代码中同样对数字、布尔类型进行了处理，因此需要了解 Java 的基础数据类型，包括整数和浮点数。

2. **字符串操作：** 对字符串进行了遍历和字符比较操作，需要了解 Java 中字符串的基本操作。

3. **循环和条件语句：** 代码使用了 `for` 循环和 `if` 条件语句，因此需要了解 Java 中的循环和条件语句的使用。

C++ 版本

1. **基础数据类型：** 代码中同样对数字、布尔类型进行了处理，因此需要了解 C++ 的基础数据类型，包括整数和浮点数。

2. **字符串操作：** 对字符串进行了遍历和字符比较操作，需要了解 C++ 中字符串的基本操作。

3. **循环和条件语句：** 代码使用了 `for` 循环和 `if` 条件语句，因此需要了解 C++ 中的循环和条件语句的使用。

总体来说，这些代码都涉及到了基本的数据类型、字符串操作、循环和条件语句。如果你对这些方面有一定的了解，应该能够理解和修改这些代码。如果有具体的问题，欢迎提出。