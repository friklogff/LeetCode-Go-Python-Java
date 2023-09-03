# [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

## 题目

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


Example 1:

```c
Input: haystack = "hello", needle = "ll"
Output: 2
```

Example 2:

```c
Input: haystack = "aaaaa", needle = "bba"
Output: -1
```

Clarification:  

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

## 题目大意


实现一个查找 substring 的函数。如果在母串中找到了子串，返回子串在母串中出现的下标，如果没有找到，返回 -1，如果子串是空串，则返回 0 。

## 解题思路



Go 版本

解法一：
1. 使用两个嵌套的循环，在主字符串 `haystack` 中迭代每个字符，外循环从 `i` 开始，内循环从 `j` 开始。
2. 在内循环中，比较 `haystack[i+j]` 和 `needle[j]`，如果不相等，则跳出内循环，继续外循环。
3. 如果内循环完成（即 `j` 等于 `needle` 的长度），则表示找到了匹配的子串，返回 `i`，即匹配子串在 `haystack` 中的起始索引。
4. 如果外循环完成（即 `i+j` 等于 `haystack` 的长度），仍未找到匹配，返回 -1。

解法二：
1. 使用 Go 标准库中的 `strings.Index` 函数，该函数会在主字符串 `haystack` 中查找子串 `needle` 的第一次出现，并返回其索引。
2. 如果找到匹配的子串，则返回索引值；如果未找到，则返回 -1。

Python 版本

解法一：
1. 使用两个嵌套的循环，在主字符串 `haystack` 中迭代每个字符，外循环从 `i` 开始，内循环从 `j` 开始。
2. 在内循环中，比较 `haystack[i+j]` 和 `needle[j]`，如果不相等，则跳出内循环，继续外循环。
3. 如果内循环完成（即 `j` 等于 `needle` 的长度），则表示找到了匹配的子串，返回 `i`，即匹配子串在 `haystack` 中的起始索引。
4. 如果外循环完成（即 `i+j` 等于 `haystack` 的长度），仍未找到匹配，返回 -1。

解法二：
1. 使用 Python 字符串的内置方法 `str.find(needle)`，该方法会在主字符串 `haystack` 中查找子串 `needle` 的第一次出现，并返回其索引。
2. 如果找到匹配的子串，则返回索引值；如果未找到，则返回 -1。

Java 版本

解法一：
1. 使用两个嵌套的循环，在主字符串 `haystack` 中迭代每个字符，外循环从 `i` 开始，内循环从 `j` 开始。
2. 在内循环中，比较 `haystack.charAt(i+j)` 和 `needle.charAt(j)`，如果不相等，则跳出内循环，继续外循环。
3. 如果内循环完成（即 `j` 等于 `needle` 的长度），则表示找到了匹配的子串，返回 `i`，即匹配子串在 `haystack` 中的起始索引。
4. 如果外循环完成（即 `i+j` 等于 `haystack` 的长度），仍未找到匹配，返回 -1。

解法二：
1. 使用 Java 字符串的内置方法 `haystack.indexOf(needle)`，该方法会在主字符串 `haystack` 中查找子串 `needle` 的第一次出现，并返回其索引。
2. 如果找到匹配的子串，则返回索引值；如果未找到，则返回 -1。

C++ 版本

解法一：
1. 使用两个嵌套的循环，在主字符串 `haystack` 中迭代每个字符，外循环从 `i` 开始，内循环从 `j` 开始。
2. 在内循环中，比较 `haystack[i+j]` 和 `needle[j]`，如果不相等，则跳出内循环，继续外循环。
3. 如果内循环完成（即 `j` 等于 `needle` 的长度），则表示找到了匹配的子串，返回 `i`，即匹配子串在 `haystack` 中的起始索引。
4. 如果外循环完成（即 `i+j` 等于 `haystack` 的长度），仍未找到匹配，返回 -1。

解法二：
1. 使用 C++ 字符串的内置方法 `haystack.find(needle)`，该方法会在主字符串 `haystack` 中查找子串 `needle` 的第一次出现，并返回其索引。
2. 如果找到匹配的子串，则返回索引值；如果未找到，则返回 -1。

这些解题思路详细描述了每个版本的代码是如何逐步寻找匹配子串的过程，并在找到匹配时返回相应的索引，或在未找到匹配时返回 -1。


## 代码

## Go

```Go
import "strings"

// 解法一
func strStr(haystack string, needle string) int {
    // 外层循环遍历haystack中的每个字符
    for i := 0; ; i++ {
        // 内层循环遍历needle中的每个字符
        for j := 0; ; j++ {
            // 如果j等于needle的长度，说明needle中的所有字符都已经在haystack中匹配成功
            if j == len(needle) {
                return i // 返回匹配成功的起始索引位置i
            }
            // 如果i+j等于haystack的长度，说明已经遍历完haystack但仍未找到匹配
            if i+j == len(haystack) {
                return -1 // 返回-1表示未找到匹配
            }
            // 如果当前needle中的字符与当前haystack中的字符不相等，跳出内层循环
            if needle[j] != haystack[i+j] {
                break
            }
        }
    }
}

// 解法二
func strStr1(haystack string, needle string) int {
    // 使用标准库strings的Index函数来查找needle在haystack中的位置
    // 如果找到，返回第一次出现的索引位置；如果未找到，返回-1
    return strings.Index(haystack, needle)
}

```

## Python

```Python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 解法一：自己实现的字符串匹配算法
        for i in range(len(haystack) + 1):
            for j in range(len(needle) + 1):
                if j == len(needle):
                    return i
                if i + j == len(haystack):
                    return -1
                if needle[j] != haystack[i + j]:
                    break


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 解法二：使用Python内置函数index
        return haystack.find(needle)

```

## Java

```Java
class Solution {
    public int strStr(String haystack, String needle) {
        // 解法一：自己实现的字符串匹配算法
        for (int i = 0; ; i++) {
            for (int j = 0; ; j++) {
                if (j == needle.length()) {
                    return i;
                }
                if (i + j == haystack.length()) {
                    return -1;
                }
                if (needle.charAt(j) != haystack.charAt(i + j)) {
                    break;
                }
            }
        }
    }
}
class Solution {
    public int strStr(String haystack, String needle) {
        // 解法二：使用Java内置函数indexOf
        return haystack.indexOf(needle);
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    int strStr(string haystack, string needle) {
        // 解法一：自己实现的字符串匹配算法
        for (int i = 0; ; i++) {
            for (int j = 0; ; j++) {
                if (j == needle.length()) {
                    return i;
                }
                if (i + j == haystack.length()) {
                    return -1;
                }
                if (needle[j] != haystack[i + j]) {
                    break;
                }
            }
        }
    }
};
class Solution {
public:
    int strStr(string haystack, string needle) {
        // 解法二：使用C++内置函数find
        size_t index = haystack.find(needle);
        return index != string::npos ? index : -1;
    }
};

```


Go 版本

解法一：
- **字符串操作**：需要了解如何访问字符串的字符，字符串的长度等。
- **循环**：需要熟悉 for 循环，以便在字符串中进行遍历操作。
- **条件语句**：使用条件语句来检查是否匹配子串以及何时返回结果。
- **索引和切片**：可以通过索引访问字符串的单个字符，并使用切片来获取子串。

解法二：
- **字符串操作**：需要了解 Go 标准库中字符串处理函数的用法，例如 `strings.Index`。

Python 版本

解法一：
- **字符串操作**：需要了解如何访问字符串的字符，字符串的长度等。
- **循环**：需要熟悉 for 循环，以便在字符串中进行遍历操作。
- **条件语句**：使用条件语句来检查是否匹配子串以及何时返回结果。

解法二：
- **字符串操作**：需要了解 Python 字符串的一些内置方法，如 `str.find`。

Java 版本

解法一：
- **字符串操作**：需要了解如何访问字符串的字符，字符串的长度等。
- **循环**：需要熟悉 for 循环，以便在字符串中进行遍历操作。
- **条件语句**：使用条件语句来检查是否匹配子串以及何时返回结果。

解法二：
- **字符串操作**：需要了解 Java 字符串的一些内置方法，如 `indexOf`。

C++ 版本

解法一：
- **字符串操作**：需要了解如何访问字符串的字符，字符串的长度等。
- **循环**：需要熟悉 for 循环，以便在字符串中进行遍历操作。
- **条件语句**：使用条件语句来检查是否匹配子串以及何时返回结果。

解法二：
- **字符串操作**：需要了解 C++ 字符串的一些内置方法，如 `find`。
- **数据类型转换**：使用 `static_cast` 进行数据类型转换，因为 `find` 返回的是 `size_t` 类型，而我们需要返回 `int` 类型的结果。



