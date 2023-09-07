# [32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)

## 题目

Given a string containing just the characters`'('`and`')'`, find the length of the longest valid (well-formed)
parentheses substring.

**Example 1:**

```
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
```

**Example 2:**

```
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
```

**Example 3:**

```
Input: s = ""
Output: 0
```

**Constraints:**

- `0 <= s.length <= 3 * 104`
- `s[i]`is`'('`, or`')'`.

## 题目大意

给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

## 解题思路

以下是每个版本的解题思路的详细介绍：

Go 版本解题思路：

Go 版本的解题思路是利用栈来处理括号匹配问题，并采用了双指针的方法来计算最长有效括号子串的长度。主要步骤如下：

1. 定义一个辅助函数 `max(a, b int) int` 用于返回两个整数中的较大值。

2. 初始化 `left`、`right` 和 `maxLength` 变量，它们分别用于记录左括号数量、右括号数量和最长有效括号子串的长度，初始值都为 0。

3. 遍历输入字符串 `s`，从左到右：
   - 如果当前字符是 '(', 则增加 `left` 计数器。
   - 如果当前字符是 ')', 则增加 `right` 计数器。
   - 如果 `left` 和 `right` 计数器相等，说明找到了一个有效的括号子串，计算当前有效括号子串的长度，并更新 `maxLength`。
   - 如果 `right` 大于 `left`，则重置 `left` 和 `right` 计数器为 0，因为当前的括号串无法匹配。

4. 重置 `left`、`right` 和 `maxLength` 变量为 0，再进行一次从右到左的遍历，处理右括号数量多于左括号数量的情况。

5. 返回 `maxLength`，它表示最长有效括号子串的长度。

Python 版本解题思路：

Python 版本的解题思路与 Go 版本相似，也是利用栈来处理括号匹配问题，并采用了双指针的方法来计算最长有效括号子串的长度。主要步骤如下：

1. 定义一个辅助函数 `max(a, b)` 用于返回两个数中的较大值。

2. 初始化 `left`、`right` 和 `maxLength` 变量，它们分别用于记录左括号数量、右括号数量和最长有效括号子串的长度，初始值都为 0。

3. 遍历输入字符串 `s`，从左到右：
   - 如果当前字符是 '(', 则增加 `left` 计数器。
   - 如果当前字符是 ')', 则增加 `right` 计数器。
   - 如果 `left` 和 `right` 计数器相等，说明找到了一个有效的括号子串，计算当前有效括号子串的长度，并更新 `maxLength`。
   - 如果 `right` 大于 `left`，则重置 `left` 和 `right` 计数器为 0，因为当前的括号串无法匹配。

4. 重置 `left`、`right` 和 `maxLength` 变量为 0，再进行一次从右到左的遍历，处理右括号数量多于左括号数量的情况。

5. 返回 `maxLength`，它表示最长有效括号子串的长度。

Java 版本解题思路：

Java 版本的解题思路与 Go 和 Python 版本相似，也是利用栈来处理括号匹配问题，并采用了双指针的方法来计算最长有效括号子串的长度。主要步骤如下：

1. 初始化 `left`、`right` 和 `maxLength` 变量，它们分别用于记录左括号数量、右括号数量和最长有效括号子串的长度，初始值都为 0。

2. 遍历输入字符串 `s`，从左到右：
   - 如果当前字符是 '(', 则增加 `left` 计数器。
   - 如果当前字符是 ')', 则增加 `right` 计数器。
   - 如果 `left` 和 `right` 计数器相等，说明找到了一个有效的括号子串，计算当前有效括号子串的长度，并更新 `maxLength`。
   - 如果 `right` 大于 `left`，则重置 `left` 和 `right` 计数器为 0，因为当前的括号串无法匹配。

3. 重置 `left`、`right` 和 `maxLength` 变量为 0，再进行一次从右到左的遍历，处理右括号数量多于左括号数量的情况。

4. 返回 `maxLength`，它表示最长有效括号子串的长度。

C++ 版本解题思路：

C++ 版本的解题思路与 Go、Python 和 Java 版本相似，也是利用栈来处理括号匹配问题，并采用了双指针的方法来计算最长有效括号子串的长度。主要步骤如下：

1. 初始化 `left`、`right` 和 `maxLength` 变量，它们分别用于记录左括号数量、右括号数量和最长有效括号子串的长度，初始值都为 0。

2. 遍历输入字符串 `s`，从左到右：
   - 如果当前字符是 '(', 则增加 `left` 计数器。
   - 如果当前字符是 ')', 则增加 `right` 计数器。
   - 如果 `left` 和 `right` 计数器相等，说明找到了一个有效的括号子串，计算当前有效括号子串的长度，并更新 `maxLength`。
   - 如果 `right` 大于 `left`，则重置 `left` 和 `right` 计数器为 0，因为当前的括号串无法匹配。

3. 重置 `left`、`right` 和 `maxLength` 变量为 0，再进行一次从右到左的遍历，处理右括号数量多于左括号数量的情况。

4. 返回 `maxLength`，它表示最长有效括号子串的长度。

## 代码

## Go

```Go
func max(a, b int) int {
    // 返回两个整数中的较大值
    if a > b {
        return a
    }
    return b
}

// 解法二 双指针
func longestValidParentheses(s string) int {
    // 初始化左右指针和最大有效括号子串长度
    left, right, maxLength := 0, 0, 0
    for i := 0; i < len(s); i++ {
        // 如果当前字符是左括号 '('，增加左括号计数
        if s[i] == '(' {
            left++
        } else {
            // 如果当前字符是右括号 ')'，增加右括号计数
            right++
        }
        // 如果左右括号计数相等，说明找到了一个有效的括号子串
        if left == right {
            // 计算当前有效括号子串的长度并更新最大长度
            maxLength = max(maxLength, 2*right)
        } else if right > left {
            // 如果右括号计数大于左括号计数，重置左右指针
            left, right = 0, 0
        }
    }
    // 重置左右指针
    left, right = 0, 0
    for i := len(s) - 1; i >= 0; i-- {
        // 从右向左遍历字符串，处理与上面相同的逻辑
        if s[i] == '(' {
            left++
        } else {
            right++
        }
        if left == right {
            maxLength = max(maxLength, 2*left)
        } else if left > right {
            left, right = 0, 0
        }
    }
    // 返回最大有效括号子串的长度
    return maxLength
}

```

## Python

```Python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def max(a, b):
            return a if a > b else b

        left, right, maxLength = 0, 0, 0

        # 从左向右遍历字符串
        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1

            if left == right:
                maxLength = max(maxLength, 2 * right)
            elif right > left:
                left, right = 0, 0

        left, right = 0, 0

        # 从右向左遍历字符串
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            if char == '(':
                left += 1
            else:
                right += 1

            if left == right:
                maxLength = max(maxLength, 2 * left)
            elif left > right:
                left, right = 0, 0

        return maxLength

```

## Java

```Java
class Solution {
    public int longestValidParentheses(String s) {
        int left = 0, right = 0, maxLength = 0;

        // 从左向右遍历字符串
        for (char c : s.toCharArray()) {
            if (c == '(') {
                left++;
            } else {
                right++;
            }

            if (left == right) {
                maxLength = Math.max(maxLength, 2 * right);
            } else if (right > left) {
                left = 0;
                right = 0;
            }
        }

        left = 0;
        right = 0;

        // 从右向左遍历字符串
        for (int i = s.length() - 1; i >= 0; i--) {
            char c = s.charAt(i);
            if (c == '(') {
                left++;
            } else {
                right++;
            }

            if (left == right) {
                maxLength = Math.max(maxLength, 2 * left);
            } else if (left > right) {
                left = 0;
                right = 0;
            }
        }

        return maxLength;
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    int longestValidParentheses(string s) {
        int left = 0, right = 0, maxLength = 0;

        // 从左向右遍历字符串
        for (char c : s) {
            if (c == '(') {
                left++;
            } else {
                right++;
            }

            if (left == right) {
                maxLength = max(maxLength, 2 * right);
            } else if (right > left) {
                left = 0;
                right = 0;
            }
        }

        left = 0;
        right = 0;

        // 从右向左遍历字符串
        for (int i = s.length() - 1; i >= 0; i--) {
            char c = s[i];
            if (c == '(') {
                left++;
            } else {
                right++;
            }

            if (left == right) {
                maxLength = max(maxLength, 2 * left);
            } else if (left > right) {
                left = 0;
                right = 0;
            }
        }

        return maxLength;
    }
};

```


Go 版本：

1. **Go 语言基础**：
   - 变量声明和初始化
   - 循环（for 循环）
   - 条件语句（if-else）
   - 函数声明和调用
   - 数组和切片（slices）的基本操作

2. **栈的概念**：
   - Go 中可以使用切片（slices）来模拟栈的行为

Python 版本：

1. **Python 语言基础**：
   - 变量声明和初始化
   - 循环（for 循环）
   - 条件语句（if-else）
   - 函数声明和调用
   - 字符串的基本操作

2. **栈的概念**：
   - Python 中可以使用列表（list）来模拟栈的行为

Java 版本：

1. **Java 语言基础**：
   - 类和对象的概念
   - 方法声明和调用
   - 循环（for 循环）
   - 条件语句（if-else）
   - 字符串的基本操作

2. **栈的概念**：
   - Java 中可以使用集合类（如 ArrayList 或 LinkedList）来模拟栈的行为

C++ 版本：

1. **C++ 语言基础**：
   - 变量声明和初始化
   - 函数声明和调用
   - 循环（for 循环）
   - 条件语句（if-else）
   - 字符串的基本操作

2. **栈的概念**：
   - C++ 中可以使用标准库中的容器（如 std::vector 或 std::deque）来模拟栈的行为
