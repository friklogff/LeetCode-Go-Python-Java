# [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/)

## 题目

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

```
Input: "()"
Output: true

```

Example 2:

```
Input: "()[]{}"
Output: true

```

Example 3:

```
Input: "(]"
Output: false
```

Example 4:

```
Input: "([)]"
Output: false
```

Example 5:

```
Input: "{[]}"
Output: true
```

## 题目大意

括号匹配问题。

## 解题思路

遇到左括号就进栈push，遇到右括号并且栈顶为与之对应的左括号，就把栈顶元素出栈。最后看栈里面还有没有其他元素，如果为空，即匹配。

需要注意，空字符串是满足括号匹配的，即输出 true。

每个版本解释解题思路。

Go 版本解题思路：

- 创建一个空的 rune 类型切片，用作栈。
- 遍历字符串中的每个字符。
- 如果字符是左括号 `[`, `(`, 或 `{`，则将其压入栈中。
- 如果字符是右括号 `]`, `)`, 或 `}`，且栈非空，且栈顶元素与当前字符匹配，则将栈顶元素弹出，表示找到一对匹配的括号。
- 如果字符不是上述情况之一，说明括号不匹配，返回 `false`。
- 遍历结束后，如果栈为空，表示所有括号都匹配成功，返回 `true`，否则返回 `false`。

Python 版本解题思路：

- 创建一个空列表，用作栈。
- 创建一个映射字典，存储括号的配对关系（例如：`")": "("`）。
- 遍历输入字符串中的每个字符。
- 如果字符是右括号，尝试从栈中弹出一个元素，如果栈为空，将 left 设为空字符串。
- 如果字符是左括号，将其压入栈。
- 遍历结束后，如果栈为空，说明所有括号都匹配成功，返回 `True`，否则返回 `False`。

 ava 版本解题思路：

- 初始化一个字符数组，用于存储下一个应匹配的字符。
- 遍历输入字符串中的每个字符。
- 如果字符是左括号，将相应的右括号压入字符数组。
- 如果字符是右括号，且字符数组非空，尝试与字符数组中的字符匹配。
- 若匹配失败，或字符数组为空，返回 `false`。
- 遍历结束后，如果字符数组为空，则所有括号都匹配成功，返回 `true`，否则返回 `false`。

C++ 版本解题思路：

- 创建一个 `std::stack` 数据结构，用作栈。
- 遍历输入字符串中的每个字符。
- 如果字符是左括号 `(`, `{`, 或 `[`，则将其压入栈。
- 如果字符是右括号 `)`, `}`, 或 `]`，且栈非空，且与栈顶元素匹配，则弹出栈顶元素。
- 如果字符不匹配或栈为空，返回 `false`。
- 遍历结束后，如果栈为空，则所有括号都匹配成功，返回 `true`，否则返回 `false`。

以上是每个版本解题思路的详细描述。不同版本的代码在表达上可能有细微差异，但核心思想都是基于栈的括号匹配。希望这些解题思路能够帮助你更好地理解每个版本的代码。如果你还有任何疑问，欢迎随时提问！

## 代码

## Go

```Go
func isValid(s string) bool {
    // 空字符串直接返回 true
    if len(s) == 0 {
        return true
    }
    stack := make([]rune, 0)  // 创建一个空的 rune 类型切片，用作栈

    // 遍历字符串 s 中的每个字符
    for _, v := range s {
        // 如果字符是 '[', '(', 或者 '{'，则将其压入栈中
        if (v == '[') || (v == '(') || (v == '{') {
            stack = append(stack, v)
        } else if ((v == ']') && len(stack) > 0 && stack[len(stack)-1] == '[') ||
            ((v == ')') && len(stack) > 0 && stack[len(stack)-1] == '(') ||
            ((v == '}') && len(stack) > 0 && stack[len(stack)-1] == '{') {
            // 如果字符是 ']', ')' 或 '}'，并且栈非空，且栈顶元素与当前字符匹配，
            // 则将栈顶元素弹出，表示找到一对匹配的括号
            stack = stack[:len(stack)-1]
        } else {
            // 如果字符不是上述情况之一，则说明括号不匹配，返回 false
            return false
        }
    }
    // 遍历结束后，如果栈为空，则表示所有括号都匹配成功，返回 true，否则返回 false
    return len(stack) == 0
}

```

## Python

```Python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # 创建一个空列表，用作栈

        pair = {
            ")": "(",
            "]": "[",
            "}": "{"
        }  # 创建映射字典，存储括号的配对关系

        for x in s:
            if x in pair:
                left = stack.pop() if stack else ""
                # 如果当前字符是右括号，尝试从栈中弹出一个元素
                # 如果栈为空，将 left 设为空字符串
                if left != pair[x]:
                    return False  # 如果左括号不匹配，返回 False
            else:
                stack.append(x)  # 如果当前字符是左括号，将其压入栈

        if stack:
            return False  # 遍历结束后，如果栈不为空，返回 False，说明括号不匹配
        else:
            return True  # 如果栈为空，返回 True，说明所有括号都匹配成功

```

## Java

```Java
class Solution {
    public boolean isValid(String s) {
        int length = s.length();

        // 如果字符串长度为奇数或者长度小于等于 1，直接返回 false
        if (length <= 1 || length % 2 != 0) {
            return false;
        }

        char[] nextChars = new char[length / 2 + 1]; // 创建字符数组，类似栈，用于存储下一个应匹配的字符
        int nextIndex = 0;

        // 遍历输入字符串中的每个字符
        for (int i = 0; i < length && nextIndex < nextChars.length; i++) {
            char c = s.charAt(i);

            // 如果是左括号，将相应的右括号压入 nextChars 数组
            if (c == '(') {
                nextChars[nextIndex++] = ')';
            } else if (c == '[') {
                nextChars[nextIndex++] = ']';
            } else if (c == '{') {
                nextChars[nextIndex++] = '}';
            } else if (i > 0) {
                // 如果是右括号，且 nextChars 数组非空，尝试与 nextChars 数组中的字符匹配
                nextIndex--;

                // 若匹配失败，或者 nextChars 数组为空，返回 false
                if (nextIndex < 0 || nextChars[nextIndex] != c) {
                    return false;
                }
            }
        }

        // 遍历结束后，如果 nextIndex 为 0，则表示所有括号都匹配成功，返回 true，否则返回 false
        return nextIndex == 0;
    }
}

```

## Cpp

```Cpp
#include <iostream>
#include <stack>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> st; // 创建一个字符类型的栈

        // 遍历输入字符串中的每个字符
        for (auto c : s) {
            if (c == '(' || c == '{' || c == '[') {
                st.push(c); // 如果字符是左括号，压入栈
            } else if (st.empty()) {
                return false; // 如果字符是右括号且栈为空，说明括号不匹配，返回 false
            } else if (abs(st.top() - c) <= 2) {
                st.pop(); // 如果字符是右括号且与栈顶元素匹配，弹出栈顶元素
            } else {
                return false; // 不匹配的情况，返回 false
            }
        }

        // 遍历结束后，如果栈为空，则所有括号都匹配成功，返回 true，否则返回 false
        return st.empty();
    }
};
```
每个版本的代码所需的基础知识。

Go 版本：



- **变量和数据类型：** 了解 Go 中的基本数据类型，如整数、字符、字符串等，以及如何声明和初始化变量。
- **切片（Slices）：** 理解切片是一种动态数组，可以动态增加和减少大小。
- **循环和条件语句：** 熟悉 Go 中的循环和条件判断语句，如 `for` 循环和 `if` 语句。
- **函数：** 知道如何定义和调用函数，以及函数的参数和返回值。
- **数据结构：** 对栈的基本概念有一定了解，知道栈是一种后进先出（LIFO）的数据结构。

Python 版本：


- **基本语法：** 了解 Python 的基本语法，如变量赋值、条件语句、循环语句等。
- **列表和字典：** 知道如何创建和操作列表和字典这两种基本的数据结构。
- **循环和条件语句：** 熟悉 `for` 循环和 `if` 条件语句的使用方法。
- **函数：** 知道如何定义和调用函数，了解函数的参数和返回值。
- **堆栈：** 对堆栈的基本概念有一定了解，知道堆栈是一种后进先出（LIFO）的数据结构。

Java 版本：

- **基本语法：** 了解 Java 的基本语法，包括变量声明、条件语句、循环语句等。
- **数组和集合：** 知道如何创建和使用数组和集合这两种常见的数据结构。
- **循环和条件语句：** 熟悉 `for` 循环和 `if` 条件语句的使用。
- **函数：** 知道如何定义和调用函数，了解函数的参数和返回值。
- **栈：** 对栈的基本概念有一定了解，知道栈是一种后进先出（LIFO）的数据结构。

C++ 版本：

- **基本语法：** 了解 C++ 的基本语法，包括变量声明、条件语句、循环语句等。
- **数组和容器：** 知道如何创建和使用数组以及容器（如 `std::stack`）这两种数据结构。
- **循环和条件语句：** 熟悉 `for` 循环和 `if` 条件语句的使用。
- **函数：** 知道如何定义和调用函数，了解函数的参数和返回值。
- **栈：** 对栈的基本概念有一定了解，知道栈是一种后进先出（LIFO）的数据结构。

