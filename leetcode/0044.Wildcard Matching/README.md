# [44.Wildcard Matching](https://leetcode.com/problems/wildcard-matching/)


Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
 

Constraints:

0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.
## 题目大意

给你一个输入字符串 (s) 和一个字符模式 (p) ，请你实现一个支持 '?' 和 '*' 匹配规则的通配符匹配：
'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符序列（包括空字符序列）。
判定匹配成功的充要条件是：字符模式必须能够 完全匹配 输入字符串（而不是部分匹配）。
## 解题思路
当讨论每个版本的解题思路时，我们将详细介绍每个版本的算法步骤。以下是每个版本的解题思路：

Go版本：

Go版本的解题思路是使用双指针和回溯法来匹配字符串和模式。主要步骤如下：

1. 首先，使用一个循环来处理模式`p`末尾的连续`*`字符。这是为了跳过模式中的多余`*`。

2. 接着进入一个循环，同时遍历字符串`s`和模式`p`：
   - 如果当前模式字符是`*`，记录当前字符串`s`和模式`p`的位置，并将模式指针`p`向后移动一位。
   - 如果当前字符匹配或者是`?`通配符，将字符串和模式指针同时向后移动一位。
   - 如果字符不匹配且有可回溯的位置，回溯到上一个`*`的位置，并更新字符串和模式指针。

3. 循环结束后，检查是否还有未处理的`*`字符在模式`p`中。

4. 最后，检查模式`p`是否已经完全匹配字符串`s`。如果模式指针`p`到达了模式的末尾，表示匹配成功。

Python版本：

Python版本的解题思路与Go版本类似，也是使用双指针和回溯法。主要步骤如下：

1. 首先，使用一个循环来处理模式`p`末尾的连续`*`字符。这是为了跳过模式中的多余`*`。

2. 接着进入一个循环，同时遍历字符串`s`和模式`p`：
   - 如果当前模式字符是`*`，记录当前字符串`s`和模式`p`的位置，并将模式指针`p`向后移动一位。
   - 如果当前字符匹配或者是`?`通配符，将字符串和模式指针同时向后移动一位。
   - 如果字符不匹配且有可回溯的位置，回溯到上一个`*`的位置，并更新字符串和模式指针。

3. 循环结束后，检查是否还有未处理的`*`字符在模式`p`中。

4. 最后，检查模式`p`是否已经完全匹配字符串`s`。如果模式指针`p`到达了模式的末尾，表示匹配成功。

Java版本：

Java版本的解题思路也是使用双指针和回溯法。主要步骤如下：

1. 首先，使用一个循环来处理模式`p`末尾的连续`*`字符。这是为了跳过模式中的多余`*`。

2. 接着进入一个循环，同时遍历字符串`s`和模式`p`：
   - 如果当前模式字符是`*`，记录当前字符串`s`和模式`p`的位置，并将模式指针`p`向后移动一位。
   - 如果当前字符匹配或者是`?`通配符，将字符串和模式指针同时向后移动一位。
   - 如果字符不匹配且有可回溯的位置，回溯到上一个`*`的位置，并更新字符串和模式指针。

3. 循环结束后，检查是否还有未处理的`*`字符在模式`p`中。

4. 最后，检查模式`p`是否已经完全匹配字符串`s`。如果模式指针`p`到达了模式的末尾，表示匹配成功。

C++版本：

C++版本的解题思路与其他版本相似，也是使用双指针和回溯法。主要步骤如下：

1. 首先，使用一个循环来处理模式`p`末尾的连续`*`字符。这是为了跳过模式中的多余`*`。

2. 接着进入一个循环，同时遍历字符串`s`和模式`p`：
   - 如果当前模式字符是`*`，记录当前字符串`s`和模式`p`的位置，并将模式指针`p`向后移动一位。
   - 如果当前字符匹配或者是`?`通配符，将字符串和模式指针同时向后移动一位。
   - 如果字符不匹配且有可回溯的位置，回溯到上一个`*`的位置，并更新字符串和模式指针。

3. 循环结束后，检查是否还有未处理的`*`字符在模式`p`中。

4. 最后，检查模式`p`是否已经完全匹配字符串`s`。如果模式指针`p`到达了模式的末尾，表示匹配成功。

总的来说，无论使用哪种编程语言，解决方案的核心思路都是双指针和回溯法，用于匹配字符串和模式，同时处理通配符`*`和`?`。


## 代码

```go
func isMatch(s string, p string) bool {
    // 进入循环，只要s和p非空且p的最后一个字符不是'*'
    for len(s) > 0 && len(p) > 0 && p[len(p)-1] != '*' {
        // 如果字符匹配或者p的最后一个字符是'?'，则从s和p的末尾去掉一个字符
        if charMatch(s[len(s)-1], p[len(p)-1]) {
            s = s[:len(s)-1]
            p = p[:len(p)-1]
        } else {
            // 如果字符不匹配，返回false
            return false
        }
    }
    // 如果p为空，返回s是否也为空
    if len(p) == 0 {
        return len(s) == 0
    }
    // 初始化索引和记录变量
    sIndex, pIndex := 0, 0
    sRecord, pRecord := -1, -1
    // 开始循环，sIndex小于s的长度且pRecord小于p的长度
    for sIndex < len(s) && pRecord < len(p) {
        // 如果p的当前字符是'*'，将p的索引向后移动，记录s和p的位置
        if p[pIndex] == '*' {
            pIndex++
            sRecord, pRecord = sIndex, pIndex
        } else if charMatch(s[sIndex], p[pIndex]) {
            // 如果字符匹配，将s和p的索引都向后移动
            sIndex++
            pIndex++
        } else if sRecord != -1 && sRecord + 1 < len(s) {
            // 如果字符不匹配，但是有记录的位置可用，并且sRecord+1小于s的长度，更新sIndex和pIndex
            sRecord++
            sIndex, pIndex = sRecord, pRecord
        } else {
            // 如果没有符合的情况，返回false
            return false
        }
    }
    // 最后，检查p中是否只包含'*'
    return allStars(p, pIndex, len(p))
}

// 辅助函数，检查字符串中是否都是'*'
func allStars(str string, left, right int) bool {
    for i := left; i < right; i++ {
        if str[i] != '*' {
            return false
        }
    }
    return true
}

// 辅助函数，检查两个字符是否匹配
func charMatch(u, v byte) bool {
    return u == v || v == '?'
}

```


## Python

```Python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 进入循环，只要s和p非空且p的最后一个字符不是'*'
        while s and p and p[-1] != '*':
            # 如果字符匹配或者p的最后一个字符是'?'，则从s和p的末尾去掉一个字符
            if self.charMatch(s[-1], p[-1]):
                s = s[:-1]
                p = p[:-1]
            else:
                # 如果字符不匹配，返回false
                return False
        # 如果p为空，返回s是否也为空
        if not p:
            return not s
        # 初始化索引和记录变量
        sIndex, pIndex = 0, 0
        sRecord, pRecord = -1, -1
        # 开始循环，sIndex小于s的长度且pRecord小于p的长度
        while sIndex < len(s) and pRecord < len(p):
            # 如果p的当前字符是'*'，将p的索引向后移动，记录s和p的位置
            if p[pIndex] == '*':
                pIndex += 1
                sRecord, pRecord = sIndex, pIndex
            elif self.charMatch(s[sIndex], p[pIndex]):
                # 如果字符匹配，将s和p的索引都向后移动
                sIndex += 1
                pIndex += 1
            elif sRecord != -1 and sRecord + 1 < len(s):
                # 如果字符不匹配，但是有记录的位置可用，并且sRecord+1小于s的长度，更新sIndex和pIndex
                sRecord += 1
                sIndex, pIndex = sRecord, pRecord
            else:
                # 如果没有符合的情况，返回false
                return False
        # 最后，检查p中是否只包含'*'
        return self.allStars(p, pIndex, len(p))

    # 辅助函数，检查字符串中是否都是'*'
    def allStars(self, s, left, right):
        for i in range(left, right):
            if s[i] != '*':
                return False
        return True

    # 辅助函数，检查两个字符是否匹配
    def charMatch(self, u, v):
        return u == v or v == '?'

```

## Java

```Java
class Solution {
    public boolean isMatch(String s, String p) {
        // 进入循环，只要s和p非空且p的最后一个字符不是'*'
        while (s.length() > 0 && p.length() > 0 && p.charAt(p.length() - 1) != '*') {
            // 如果字符匹配或者p的最后一个字符是'?'，则从s和p的末尾去掉一个字符
            if (charMatch(s.charAt(s.length() - 1), p.charAt(p.length() - 1))) {
                s = s.substring(0, s.length() - 1);
                p = p.substring(0, p.length() - 1);
            } else {
                // 如果字符不匹配，返回false
                return false;
            }
        }
        // 如果p为空，返回s是否也为空
        if (p.length() == 0) {
            return s.length() == 0;
        }
        // 初始化索引和记录变量
        int sIndex = 0, pIndex = 0;
        int sRecord = -1, pRecord = -1;
        // 开始循环，sIndex小于s的长度且pRecord小于p的长度
        while (sIndex < s.length() && pRecord < p.length()) {
            // 如果p的当前字符是'*'，将p的索引向后移动，记录s和p的位置
            if (p.charAt(pIndex) == '*') {
                pIndex++;
                sRecord = sIndex;
                pRecord = pIndex;
            } else if (charMatch(s.charAt(sIndex), p.charAt(pIndex))) {
                // 如果字符匹配，将s和p的索引都向后移动
                sIndex++;
                pIndex++;
            } else if (sRecord != -1 && sRecord + 1 < s.length()) {
                // 如果字符不匹配，但是有记录的位置可用，并且sRecord+1小于s的长度，更新sIndex和pIndex
                sRecord++;
                sIndex = sRecord;
                pIndex = pRecord;
            } else {
                // 如果没有符合的情况，返回false
                return false;
            }
        }
        // 最后，检查p中是否只包含'*'
        return allStars(p, pIndex, p.length());
    }

    // 辅助函数，检查字符串中是否都是'*'
    private boolean allStars(String str, int left, int right) {
        for (int i = left; i < right; i++) {
            if (str.charAt(i) != '*') {
                return false;
            }
        }
        return true;
    }

    // 辅助函数，检查两个字符是否匹配
    private boolean charMatch(char u, char v) {
        return u == v || v == '?';
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    bool isMatch(string s, string p) {
        int lens = s.size(); // 获取字符串s的长度
        int lenp = p.size(); // 获取模式p的长度
        int scur = 0; // 初始化字符串s的当前指针
        int sstar = -1; // 初始化字符串s的'*'的位置记录
        int pcur = 0; // 初始化模式p的当前指针
        int pstar = -1; // 初始化模式p的'*'的位置记录
        
        while (scur < lens) { // 循环处理字符串s
            if (pcur < lenp && p[pcur] == '*') { // 如果模式p当前字符是'*'
                sstar = scur; // 记录当前字符串s的位置
                pstar = ++pcur; // 记录当前模式p的位置，同时将模式p指针向后移动
            } else {
                if (pcur < lenp && (p[pcur] == '?' || p[pcur] == s[scur])) {
                    // 如果模式p当前字符是'?'或者与字符串s当前字符相匹配
                    scur++; // 移动字符串s的指针
                    pcur++; // 移动模式p的指针
                } else {
                    if (sstar < 0) return false; // 如果没有'*'的位置记录，返回false
                    scur = ++sstar; // 回溯到'*'的位置的下一个字符
                    pcur = pstar; // 恢复模式p的指针到'*'的位置的下一个字符
                }
            }
        }
        
        while (pcur < lenp && p[pcur] == '*') pcur++; // 处理模式p中多余的'*'
        
        return pcur == lenp; // 返回是否模式p已经处理完毕
    }
};

```
当讨论每个版本的解决方案时，我们将详细介绍所需的基础知识。首先，我们将使用Go、Python、Java和C++的版本进行分析。

Go版本：

1. **基本语法和数据类型**: 在Go中，你需要了解基本的语法和数据类型，包括变量声明、循环、条件语句等。

2. **字符串操作**: 你需要了解如何处理字符串，包括字符串的切片操作和获取字符串的长度。

3. **循环和条件语句**: 代码中使用了循环和条件语句来遍历字符串和执行不同的操作，所以你需要了解这些控制结构。

4. **切片操作**: 在Go中，切片操作是处理字符串和数组的关键操作之一。你需要了解如何截取和操作切片。

Python版本：

1. **基本语法和数据类型**: 在Python中，你需要了解基本的语法和数据类型，包括变量、列表、字符串、循环、条件语句等。

2. **字符串操作**: Python提供了丰富的字符串操作方法，包括切片、拼接、长度等。你需要了解这些操作。

3. **循环和条件语句**: 代码中使用了循环和条件语句来遍历字符串和执行不同的操作，所以你需要了解这些控制结构。

4. **面向对象编程 (OOP)**: 尽管在代码中没有使用类和对象，但Python是一种面向对象的编程语言，因此你需要了解OOP的基本概念。

Java版本：

1. **基本语法和数据类型**: 在Java中，你需要了解基本的语法和数据类型，包括变量声明、列表、字符串、循环、条件语句等。

2. **字符串操作**: Java提供了处理字符串的类和方法，你需要了解如何使用`String`类的方法来操作字符串。

3. **循环和条件语句**: 代码中使用了循环和条件语句来遍历字符串和执行不同的操作，所以你需要了解这些控制结构。

4. **面向对象编程 (OOP)**: Java是一种面向对象的编程语言，你需要了解OOP的基本概念，即类、对象、继承等。

C++版本：

1. **基本语法和数据类型**: 在C++中，你需要了解基本的语法和数据类型，包括变量声明、数组、字符串、循环、条件语句等。

2. **字符串操作**: C++提供了处理字符串的标准库，你需要了解如何使用标准库中的字符串函数来操作字符串。

3. **循环和条件语句**: 代码中使用了循环和条件语句来遍历字符串和执行不同的操作，所以你需要了解这些控制结构。

4. **指针和引用**: C++中涉及了指针和引用的概念，尤其是在处理字符串时，你需要了解如何使用指针和引用来操作数据。

总的来说，无论你选择哪种编程语言版本，都需要掌握基本的编程概念、控制结构、字符串操作方法，并根据具体的语言特性来理解和实现算法。每个版本都使用了循环、条件语句、字符串操作等基本编程知识来解决通配符匹配问题。