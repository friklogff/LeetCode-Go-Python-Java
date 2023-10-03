# [58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/)


## 题目

Given a string `s` consisting of some words separated by some number of spaces, return *the length of the **last** word in the string.*

A **word** is a maximal substring consisting of non-space characters only.

**Example 1:**

```
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

```

**Example 2:**

```
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

```

**Example 3:**

```
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

```

**Constraints:**

- `1 <= s.length <= 104`
- `s` consists of only English letters and spaces `' '`.
- There will be at least one word in `s`.

## 题目大意

给你一个字符串 `s`，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中最后一个单词的长度。**单词** 是指仅由字母组成、不包含任何空格字符的最大子字符串。

## 解题思路

- 先从后过滤掉空格找到单词尾部，再从尾部向前遍历，找到单词头部，最后两者相减，即为单词的长度。
以下是每个版本的解题思路的详细介绍：

Go 版本解题思路：

1. 首先，计算输入字符串的长度，以便后续的操作。

2. 初始化一个变量 `last`，将其设置为字符串的最后一个字符的索引，即 `length - 1`。

3. 从字符串的末尾开始向前遍历，通过逐步减少 `last` 的值来跳过末尾的空格字符，直到找到最后一个单词的末尾。

4. 如果整个字符串都是空格，那么直接返回 0。

5. 接下来，从 `last` 开始向前遍历，找到最后一个单词的开头，通过逐步减少 `first` 的值，直到找到空格字符或达到字符串的开头。

6. 最后，通过计算 `last` 和 `first` 之间的距离，即 `last - first`，得到最后一个单词的长度，然后返回这个长度作为结果。

Python 版本解题思路：

1. 首先，计算输入字符串的长度，以便后续的操作。

2. 初始化一个变量 `last`，将其设置为字符串的最后一个字符的索引，即 `length - 1`。

3. 从字符串的末尾开始向前遍历，通过逐步减少 `last` 的值来跳过末尾的空格字符，直到找到最后一个单词的末尾。

4. 如果整个字符串都是空格，那么直接返回 0。

5. 接下来，从 `last` 开始向前遍历，找到最后一个单词的开头，通过逐步减少 `first` 的值，直到找到空格字符或达到字符串的开头。

6. 最后，通过计算 `last` 和 `first` 之间的距离，即 `last - first`，得到最后一个单词的长度，然后返回这个长度作为结果。

Java 版本解题思路：

1. 首先，计算输入字符串的长度，以便后续的操作。

2. 初始化一个变量 `last`，将其设置为字符串的最后一个字符的索引，即 `length - 1`。

3. 从字符串的末尾开始向前遍历，通过逐步减少 `last` 的值来跳过末尾的空格字符，直到找到最后一个单词的末尾。

4. 如果整个字符串都是空格，那么直接返回 0。

5. 接下来，从 `last` 开始向前遍历，找到最后一个单词的开头，通过逐步减少 `first` 的值，直到找到空格字符或达到字符串的开头。

6. 最后，通过计算 `last` 和 `first` 之间的距离，即 `last - first`，得到最后一个单词的长度，然后返回这个长度作为结果。

C++ 版本解题思路：

1. 首先，计算输入字符串的长度，以便后续的操作。

2. 初始化一个变量 `last`，将其设置为字符串的最后一个字符的索引，即 `length - 1`。

3. 从字符串的末尾开始向前遍历，通过逐步减少 `last` 的值来跳过末尾的空格字符，直到找到最后一个单词的末尾。

4. 如果整个字符串都是空格，那么直接返回 0。

5. 接下来，从 `last` 开始向前遍历，找到最后一个单词的开头，通过逐步减少 `first` 的值，直到找到空格字符或达到字符串的开头。

6. 最后，通过计算 `last` 和 `first` 之间的距离，即 `last - first`，得到最后一个单词的长度，然后返回这个长度作为结果。

总的来说，这四个版本的解题思路都是基本相同的，都是通过从字符串末尾向前遍历来寻找最后一个单词的末尾和开头，然后计算长度并返回。关键是了解如何操作字符串的长度、索引和循环，以及如何处理边界条件。
## 代码

```go
func lengthOfLastWord(s string) int {
	// 获取字符串的最后一个字符的索引
	last := len(s) - 1
	// 循环直到找到字符串末尾不是空格的字符位置
	for last >= 0 && s[last] == ' ' {
		last--
	}
	// 如果字符串全是空格，则返回0
	if last < 0 {
		return 0
	}
	// 从最后一个字符开始，向前查找第一个空格之前的字符
	first := last
	for first >= 0 && s[first] != ' ' {
		first--
	}
	// 返回最后一个单词的长度（最后一个字符的位置 - 第一个字符的位置）
	return last - first
}

```


## Python

```Python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 获取字符串的长度
        length = len(s)
        # 初始化最后一个字符的索引
        last = length - 1
        
        # 从字符串末尾向前查找，跳过末尾的空格字符
        while last >= 0 and s[last] == ' ':
            last -= 1
        
        # 如果字符串全是空格，则返回0
        if last < 0:
            return 0
        
        # 从最后一个字符开始，向前查找第一个空格之前的字符
        first = last
        while first >= 0 and s[first] != ' ':
            first -= 1
        
        # 返回最后一个单词的长度（最后一个字符的位置 - 第一个字符的位置）
        return last - first

```

## Java

```Java
class Solution {
    public int lengthOfLastWord(String s) {
        // 获取字符串的长度
        int length = s.length();
        // 初始化最后一个字符的索引
        int last = length - 1;
        
        // 从字符串末尾向前查找，跳过末尾的空格字符
        while (last >= 0 && s.charAt(last) == ' ') {
            last--;
        }
        
        // 如果字符串全是空格，则返回0
        if (last < 0) {
            return 0;
        }
        
        // 从最后一个字符开始，向前查找第一个空格之前的字符
        int first = last;
        while (first >= 0 && s.charAt(first) != ' ') {
            first--;
        }
        
        // 返回最后一个单词的长度（最后一个字符的位置 - 第一个字符的位置）
        return last - first;
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    int lengthOfLastWord(string s) {
        // 获取字符串的长度
        int length = s.length();
        // 初始化最后一个字符的索引
        int last = length - 1;
        
        // 从字符串末尾向前查找，跳过末尾的空格字符
        while (last >= 0 && s[last] == ' ') {
            last--;
        }
        
        // 如果字符串全是空格，则返回0
        if (last < 0) {
            return 0;
        }
        
        // 从最后一个字符开始，向前查找第一个空格之前的字符
        int first = last;
        while (first >= 0 && s[first] != ' ') {
            first--;
        }
        
        // 返回最后一个单词的长度（最后一个字符的位置 - 第一个字符的位置）
        return last - first;
    }
};

```
每个版本的代码所需的基础知识。

Go 版本：

1. **字符串操作：** 了解如何获取字符串的长度，访问字符串中的字符以及字符串切片操作。

2. **循环和条件语句：** 理解 Go 中的 `for` 和 `if` 条件语句的使用，以及如何在循环中逐步处理字符串。

Python 版本：

1. **字符串操作：** 熟悉字符串的长度计算（使用 `len()` 函数）和字符串索引访问。

2. **字符串遍历：** 了解如何使用 `for` 循环遍历字符串中的字符。

3. **条件语句：** 了解如何使用 `if` 条件语句来进行条件判断。

Java 版本：

1. **字符串操作：** 了解如何获取字符串的长度（使用 `length()` 方法）以及如何使用 `charAt()` 方法访问字符串中的字符。

2. **循环和条件语句：** 理解 Java 中的 `while` 循环和 `if` 条件语句的使用，以及如何在循环中逐步处理字符串。

C++ 版本：

1. **字符串操作：** 熟悉 C++ 中的字符串类（`std::string`）的基本操作，包括获取字符串长度（使用 `length()` 方法）和访问字符串中的字符。

2. **循环和条件语句：** 了解 C++ 中的 `while` 循环和 `if` 条件语句的使用，以及如何在循环中逐步处理字符串。

在这些版本的代码中，最关键的基础知识包括字符串操作、循环和条件语句的使用。同时，还需要了解如何进行字符串的索引访问和遍历，以及如何处理边界条件，例如字符串为空或仅包含空格的情况。这些是解决这个问题所需的基本概念和技能。