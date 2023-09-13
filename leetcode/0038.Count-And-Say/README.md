# [38. Count-And-Say](https://leetcode.com/problems/sudoku-solver/)

## 题目

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

For example, the saying and conversion for digit string "3322251":

![](https://assets.leetcode.com/uploads/2020/10/23/countandsay.jpg)

Given a positive integer n, return the nth term of the count-and-say sequence.

 

Example 1:

Input: n = 1
Output: "1"
Explanation: This is the base case.
Example 2:

Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
 

Constraints:

1 <= n <= 30

## 题目大意

给定一个正整数 n ，输出外观数列的第 n 项。

「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。

你可以将其视作是由递归公式定义的数字字符串序列：

countAndSay(1) = "1"
countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。
前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
第一项是数字 1 
描述前一项，这个数是 1 即 “ 一 个 1 ”，记作 "11"
描述前一项，这个数是 11 即 “ 二 个 1 ” ，记作 "21"
描述前一项，这个数是 21 即 “ 一 个 2 + 一 个 1 ” ，记作 "1211"
描述前一项，这个数是 1211 即 “ 一 个 1 + 一 个 2 + 二 个 1 ” ，记作 "111221"
要 描述 一个数字字符串，首先要将字符串分割为 最小 数量的组，每个组都由连续的最多 相同字符 组成。然后对于每个组，先描述字符的数量，然后描述字符，形成一个描述组。要将描述转换为数字字符串，先将每组中的字符数量用数字替换，再将所有描述组连接起来。

例如，数字字符串 "3322251" 的描述如下图：


 

示例 1：

输入：n = 1
输出："1"
解释：这是一个基本样例。
示例 2：

输入：n = 4
输出："1211"
解释：
countAndSay(1) = "1"
countAndSay(2) = 读 "1" = 一 个 1 = "11"
countAndSay(3) = 读 "11" = 二 个 1 = "21"
countAndSay(4) = 读 "21" = 一 个 2 + 一 个 1 = "12" + "11" = "1211"
 

提示：

1 <= n <= 30
## 解题思路

以下是每个版本的解题思路：

Go 版本解题思路

1. **justify 函数**：这个函数用于生成下一个 count-and-say 序列。它遍历输入字符串 `s`，统计连续相同字符的个数，并将个数和字符按规则拼接成新的字符串。

2. **countAndSay 函数**：这个函数是主函数，它生成 count-and-say 序列的第 `n` 项。它从第一项开始，依次调用 `justify` 函数来生成下一项的字符串，重复这个过程 `n-1` 次，最后返回第 `n` 项的字符串。

Python 版本解题思路

1. **countAndSay 函数**：这是主函数，用于生成 count-and-say 序列的第 `n` 项。如果 `n` 为 1，直接返回 "1"，否则递归调用 `countAndSay(n-1)` 获取前一项的字符串。

2. **doSay 函数**：这个函数负责生成当前项的 count-and-say 序列。它遍历输入字符串 `sn`，统计相邻相同字符的个数，并按规则拼接成新的字符串。

Java 版本解题思路

1. **justify 方法**：这个方法用于生成下一个 count-and-say 序列。它遍历输入字符串，统计连续相同字符的个数，并将个数和字符按规则拼接成新的字符串。

2. **countAndSay 方法**：这是主方法，用于生成 count-and-say 序列的第 `n` 项。它从第一项开始，依次调用 `justify` 方法来生成下一项的字符串，重复这个过程 `n-1` 次，最后返回第 `n` 项的字符串。

C++ 版本解题思路

1. **solution 函数**：这个函数用于生成下一个 count-and-say 序列。它遍历输入字符串 `s`，统计连续相同字符的个数，并将个数和字符按规则拼接成新的字符串。

2. **countAndSay 函数**：这是主函数，用于生成 count-and-say 序列的第 `n` 项。它从第一项开始，依次调用 `solution` 函数来生成下一项的字符串，重复这个过程 `n-1` 次，最后返回第 `n` 项的字符串。

无论使用哪个版本，核心思路都是递归生成 count-and-say 序列，其中每一项都依赖于前一项，并按照规则进行字符计数和拼接。每个版本都采用了不同的编程语言和字符串处理方法，但解题思路是相同的。
## 代码

## Go

```Go
func justify(s string) string {
    var result []byte
    i := 0

    for i < len(s) {
        c := s[i]
        count := 1

        // 统计连续相同字符的个数
        for i+1 < len(s) && s[i] == s[i+1] {
            count++
            i++
        }

        // 将统计结果添加到结果字符串中
        result = append(result, []byte(strconv.Itoa(count))...)
        result = append(result, c)

        i++
    }

    return string(result)
}

func countAndSay(n int) string {
    sequence := "1"

    for i := 1; i < n; i++ {
        sequence = justify(sequence)
    }

    return sequence
}

```

## Python

```Python
class Solution:
    def countAndSay(self, n: int) -> str:
        # 基础情况：n=1时返回'1'
        if n == 1:
            return '1'
        
        # 递归调用，生成前一个序列
        prev_sequence = self.countAndSay(n - 1)
        
        # 调用doSay函数生成当前序列
        return self.doSay(prev_sequence)
    
    def doSay(self, sn):
        counts = []  # 存储相邻相同字符的个数
        digits = []  # 存储相邻相同字符
        n = len(sn)
        c = 1  # 初始化字符计数为1
        d = sn[0]  # 初始化当前字符为第一个字符

        for i in range(1, n):
            if sn[i] == sn[i - 1]:
                c += 1  # 如果当前字符与前一个字符相同，增加计数
            else:
                counts.append(c)  # 如果不同，将计数和字符添加到对应的列表中
                digits.append(d)
                c = 1  # 重置计数为1
                d = sn[i]  # 更新当前字符为新字符
        
        # 处理最后一组相同字符
        counts.append(c)
        digits.append(d)
        
        # 使用列表解析将计数和字符组合成字符串
        return ''.join([f'{x}{y}' for x, y in zip(counts, digits)])

```

## Java

```Java
class Solution {
    // 定义一个方法，用于将输入的字符串进行报数
    public String justify(String s) {
        // 创建一个 StringBuilder 对象，用于存储结果
        StringBuilder result = new StringBuilder();
        // 遍历输入的字符串
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i); // 获取当前字符
            int sum = 1; // 初始化计数器为 1，表示至少有一个当前字符

            // 如果当前字符是输入字符串的最后一个字符或者与下一个字符不同
            if (i + 1 >= s.length() || c != s.charAt(i + 1)) {
                result.append(sum); // 将计数器的值追加到结果中
                result.append(c);   // 将当前字符追加到结果中
                return String.valueOf(result); // 返回结果的字符串表示
            }

            // 如果当前字符与下一个字符相同，继续遍历并增加计数器
            while (c == s.charAt(i + 1)) {
                sum++;
                i++;

                // 如果当前字符是输入字符串的最后一个字符，将计数器的值和字符追加到结果中，并返回
                if (i + 1 >= s.length()) {
                    result.append(sum);
                    result.append(c);
                    return String.valueOf(result);
                }
            }

            // 将计数器的值和字符追加到结果中
            result.append(sum);
            result.append(c);
        }

        // 返回结果的字符串表示
        return String.valueOf(result);
    }

    // 定义一个方法，根据输入的 n 返回第 n 个报数序列
    public String countAndSay(int n) {
        String[] list = new String[n];
        list[0] = "1"; // 第一个序列是固定的 "1"
        
        // 生成第 2 到第 n 个序列
        for (int i = 1; i < n; i++) {
            String s = list[i - 1]; // 获取前一个序列
            list[i] = justify(s); // 生成当前序列并保存
        }
        
        // 返回第 n 个序列
        return list[n - 1];
    }
}

```

## Cpp

```Cpp
#include <iostream>
#include <string>

class Solution {
public:
    string countAndSay(int n) {
        string s = "1"; // 初始序列为 "1"
        for (int i = 1; i < n; ++i) {
            solution(s); // 调用 solution 函数生成下一个序列
            std::cout << "s:" << s << std::endl; // 可选：打印当前序列，用于调试
        }
        return s; // 返回第 n 个报数序列
    }

    void solution(string &s) {
        string ans; // 用于存储生成的下一个序列
        int l = 0, r = 0; // 左右指针，用于统计相同字符的个数

        while (r < s.size()) {
            if (s[r] == s[l]) {
                r++; // 同字符，右指针移动
                continue;
            }

            int cnt = r - l; // 统计相同字符的个数
            ans.push_back(cnt + '0'); // 将个数添加到结果字符串
            ans.push_back(s[l]); // 添加字符本身
            l = r; // 左指针移到右指针位置
        }

        int cnt = r - l; // 处理末尾相同字符
        ans.push_back(cnt + '0');
        ans.push_back(s[l]);

        s = ans; // 更新原始字符串为下一个序列
    }
};

```
当我们用不同的编程语言来解决同一个问题时，需要了解每种语言的特定语法和库函数，但在解决这个特定问题时，需要掌握一些共同的基础知识。以下是对每个版本的详细基础知识的介绍：

Go 版本
- **函数声明与调用**：了解如何声明和调用函数，以及函数的参数和返回值。
- **字符串处理**：Go中字符串是不可变的，因此需要了解如何在不可变字符串上执行操作，以及如何将字符串转换为字节数组和反之。
- **循环和条件语句**：了解如何使用循环和条件语句来控制程序的流程。
- **切片（Slice）**：切片是动态数组，需要了解如何创建和操作切片。
- **整数转字符串**：Go中将整数转换为字符串的方法。

Python 版本
- **类与方法**：Python是面向对象的语言，了解如何定义类和方法。
- **递归**：在解决这个问题中，使用递归来生成序列的下一项。
- **字符串操作**：Python提供了丰富的字符串操作方法，如索引、切片和字符串拼接。
- **列表解析**：Python中的列表解析是一种快速生成列表的方式，对于处理字符计数和字符拼接很有用。

Java 版本
- **类与方法**：Java是面向对象的语言，了解如何定义类和方法，并且如何使用它们来组织代码。
- **递归**：与Python版本一样，Java版本也使用递归来生成序列。
- **字符串操作**：Java提供了各种字符串操作方法，如charAt、length等。
- **StringBuilder类**：在Java中，使用StringBuilder类来构建和操作可变字符串，以提高性能。

C++ 版本
- **类与方法**：C++也支持面向对象编程，了解如何定义类和成员函数。
- **递归**：与Python和Java版本一样，C++版本也使用递归来生成序列。
- **字符串操作**：C++提供了标准库中的string类，了解如何使用它来处理字符串。
- **字符转换**：使用字符转换函数将整数转换为字符。

