# [68.Text-Justification](https://leetcode.cn/problems/text-justification/)


## 题目

68. Text-Justification

Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
 

Constraints:

1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth

## 题目大意

给定一个单词数组 words 和一个长度 maxWidth ，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用 “贪心算法” 来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。


## 解题思路

以下是每个版本的解题思路的分别介绍：

 Go 版本
Go 版本使用贪心算法来解决文本两端对齐问题，主要思路如下：

1. 初始化右边界 `right` 和单词总数 `n`。
2. 通过循环遍历每个单词，找到适合当前行的单词，使得当前行的总长度不超过 `maxWidth`。
3. 如果已经处理完了最后一个单词，特殊处理最后一行，左对齐并且不插入额外空格。
4. 如果当前行不只包含一个单词，计算单词间需要插入的空格数，将空格尽可能均匀分配，注意处理额外的空格。
5. 构建当前行的字符串，将其加入结果列表。
6. 重复步骤2-5直到处理完所有单词。

这个思路实现了文本两端对齐的要求，使用贪心算法来尽可能均匀分配空格，以满足每行有 `maxWidth` 字符的条件。

 Python 版本
Python 版本使用贪心算法解决文本两端对齐问题，主要思路如下：

1. 初始化一个空列表 `result`，用于存储最终结果。
2. 初始化一个空列表 `cur_line`，用于存储当前行的单词。
3. 初始化 `cur_width` 为0，表示当前行的宽度。
4. 遍历每个单词，将单词逐个加入 `cur_line`，同时计算当前行的宽度。
5. 如果当前行已满或者不能再加入单词，进行对齐处理，并将当前行加入 `result`。
6. 如果当前行为空，处理最后一行的左对齐。
7. 返回 `result` 列表，包含对齐好的文本。

这个思路实现了文本两端对齐的要求，使用贪心算法来尽可能均匀分配空格，以满足每行有 `maxWidth` 字符的条件。

 Java 版本
Java 版本采用贪心算法解决文本两端对齐问题，主要思路如下：

1. 初始化一个空列表 `res`，用于存储最终结果。
2. 通过循环遍历每个单词，以及跟踪左边界和当前行的长度。
3. 尽可能多地加入单词到当前行，使得长度不超过 `maxWidth`。
4. 如果当前行只有一个单词，左对齐处理。
5. 如果是最后一行，左对齐且单词之间只加一个空格。
6. 否则，尽可能均匀分配单词之间的空格，考虑额外的空格。
7. 构建当前行的字符串，将其加入 `res` 列表。
8. 重复步骤2-7直到处理完所有单词。

这个思路实现了文本两端对齐的要求，使用贪心算法来尽可能均匀分配空格，以满足每行有 `maxWidth` 字符的条件。

 C++ 版本
C++ 版本采用贪心算法解决文本两端对齐问题，主要思路如下：

1. 初始化一些变量，包括计数器、当前行的单词列表、最终结果的列表等。
2. 通过循环遍历每个单词，找到适合当前行的单词，使得当前行的总长度不超过 `maxWidth`。
3. 特殊处理只包含一个单词的情况，左对齐并在单词后面填充额外空格。
4. 特殊处理最后一行，左对齐并在单词之间只加一个空格。
5. 否则，尽可能均匀分配单词之间的空格，考虑额外的空格。
6. 构建当前行的字符串，将其加入结果列表。
7. 重复步骤2-6直到处理完所有单词。

这个思路实现了文本两端对齐的要求，使用贪心算法来尽可能均匀分配空格，以满足每行有 `maxWidth` 字符的条件。
## 代码

## Go

```Go
// blank 返回长度为 n 的由空格组成的字符串
func blank(n int) string {
    return strings.Repeat(" ", n)
}

// fullJustify 实现文本两端对齐
func fullJustify(words []string, maxWidth int) (ans []string) {
    right, n := 0, len(words)  // 初始化右边界和单词总数
    for {
        left := right // 当前行的第一个单词在 words 的位置
        sumLen := 0   // 统计这一行单词长度之和
        // 循环获取适合当前行的单词
        for right < n && sumLen+len(words[right])+right-left <= maxWidth {
            sumLen += len(words[right])
            right++
        }

        // 边界条件，如果已经处理完最后一个单词
        if right == n {
            var s string
            for i := left; i < right; i++ {
                s += words[i] + " "
            }
            // 去掉最后一个单词的多余空格
            ans = append(ans, s[:len(s)-1]+blank(maxWidth-len(s)+1))
            return ans
        }

        // 当前行不只一个单词
        numWords := right - left
        numSpaces := maxWidth - sumLen
        avgSpaces := numSpaces / (numWords - 1)  // 平均空格数
        extraSpaces := numSpaces % (numWords - 1)  // 额外空格数
        s1 := strings.Join(words[left:left+extraSpaces+1], blank(avgSpaces+1)) // 拼接额外加一个空格的单词
        s2 := strings.Join(words[left+extraSpaces+1:right], blank(avgSpaces))  // 拼接其余单词
        ans = append(ans, s1+blank(avgSpaces)+s2)  // 将构建好的当前行加入结果列表
    }
}

```

## Python

```Python
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []  # 存储最终结果的列表
        cur_line = []  # 当前行的单词列表
        cur_width = 0  # 当前行的宽度
        for word in words:  # 遍历每个单词
            if cur_width + len(cur_line) + len(word) <= maxWidth:  # 如果当前行可以容纳该单词
                cur_line.append(word)  # 将单词加入当前行
                cur_width += len(word)  # 更新当前行的宽度
            else:  # 当前行不能容纳该单词
                result.append(self.align(cur_line, cur_width, maxWidth))  # 对当前行进行对齐处理并加入结果列表
                cur_line = [word]  # 初始化下一行
                cur_width = len(word)  # 更新当前行宽度
        if cur_line:  # 处理最后一行
            result.append(' '.join(cur_line).ljust(maxWidth))  # 最后一行左对齐处理
        return result  # 返回最终结果列表

    def align(self, line, cur_width, maxWidth):  # 对齐函数
        if len(line) == 1:  # 如果当前行只有一个单词
            return line[0].ljust(maxWidth)  # 左对齐处理
        total_space = maxWidth - cur_width  # 总空格数
        space_slot = len(line) - 1  # 空格插槽数量
        if space_slot == 0:  # 如果只有一个单词
            return line[0] + ' ' * total_space  # 在单词后面填充剩余空格
        space_between_words, extra_space = divmod(total_space, space_slot)  # 计算平均每个空格数和多余的空格数
        spaces = ' ' * space_between_words  # 构建平均空格
        for i in range(extra_space):  # 分配多余的空格
            line[i] += ' '
        return spaces.join(line)  # 返回对齐后的字符串
```

## Java

```Java
class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> res = new ArrayList<>(); // 存储最终结果的列表
        int n = words.length; // 单词总数
        int i = 0; // 初始化索引
        while (i < n) { // 遍历每个单词
            int len = 0; // 当前行已选单词的长度
            int wordsNum = 0; // 当前行已选单词的数量
            StringBuilder sb = new StringBuilder(); // 用于构建当前行的字符串
            while (i < n && len + words[i].length() + wordsNum <= maxWidth) {
                // 选取单词
                len += words[i].length();
                wordsNum++;
                i++;
            }
            if (wordsNum == 1) { // 如果当前行只有一个单词，左对齐
                sb.append(words[i - wordsNum]);
                for (int j = 0; j < maxWidth - len; j++) {
                    sb.append(" ");
                }
            } else if (i == n) { // 如果是最后一行，左对齐且单词之间只加一个空格
                for (int j = i - wordsNum; j < i; j++) {
                    sb.append(words[j]);
                    if (j < i - 1) {
                        sb.append(" ");
                    }
                }
                for (int j = 0; j < maxWidth - len - (wordsNum - 1); j++) {
                    sb.append(" ");
                }
            } else { // 否则，尽可能均匀分配单词间的空格数量
                int spaces = maxWidth - len;
                int slots = wordsNum - 1;
                int spaceWidth = spaces / slots;
                int remain = spaces % slots;
                for (int j = i - wordsNum; j < i; j++) {
                    sb.append(words[j]);
                    if (j == i - 1) {
                        break;
                    }
                    for (int k = 0; k < spaceWidth; k++) {
                        sb.append(" ");
                    }
                    if (remain > 0) {
                        sb.append(" ");
                        remain--;
                    }
                }
            }
            res.add(sb.toString()); // 将构建好的当前行加入结果列表
        }
        return res; // 返回最终结果列表
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        int n = words.size(), sum = 0, index = 0, countSize = 0;  // 初始化变量
        string str = "";  // 用于构建当前行的字符串
        vector<string> vec1;  // 存储当前行的单词
        vector<string> vec2;  // 存储最终结果
        for (int i = 0; i < n && index < n; ++i)  // 遍历每个单词
        {
            index = i;  // 初始化索引
            while (index < n)  // 在当前行内遍历单词
            {
                if (sum == 0)  // 如果当前行还没有单词
                {
                    str += words[index];  // 将单词添加到当前行
                    sum++;
                    countSize += words[index++].size();  // 更新当前行的字符数
                    vec1.push_back(words[i]);  // 将单词添加到当前行的单词列表
                    continue;
                }
                else if (sum > 0)  // 如果当前行已有单词
                {
                    int tmp = words[index].size() + vec1.size() - 1;  // 计算加入新单词后的字符数
                    if (tmp + countSize < maxWidth)  // 如果加入新单词后不超过最大宽度
                    {
                        countSize += words[index].size();
                        str += " " + words[index];  // 在当前行末尾加入单词
                        vec1.push_back(words[index++]);  // 将单词添加到当前行的单词列表
                        sum++;
                        continue;
                    }
                    else  // 如果加入新单词后超过了最大宽度
                    {
                        int sub = maxWidth - countSize;  // 计算需要填充的空格数
                        if (vec1.size() - 1 > 0)  // 如果当前行单词数大于1
                        {
                            int div = sub / (vec1.size() - 1);  // 平均每个空隙填充的空格数
                            int rem = sub % (vec1.size() - 1);  // 剩余的空格数
                            for (int j = vec1.size() - sum; j < vec1.size() - 1; j++)  // 在单词之间填充空格
                            {
                                int cir = 0;
                                while (cir++ < div)vec1[j] += " ";
                            }

                            for (int k = vec1.size() - sum; k < vec1.size() - sum + rem; k++)  // 在单词之间均匀填充剩余空格
                            {
                                vec1[k] += " ";
                            }

                            str = "";
                            for (int v = vec1.size() - sum; v < vec1.size(); v++)  // 构建当前行的字符串
                            {
                                str += vec1[v];
                            }
                        }
                        else  // 如果只有一个单词
                        {
                            if (countSize > 0)
                            {
                                for (int i = 0; i < maxWidth - countSize; ++i)  // 在单词之后填充剩余的空格
                                {
                                    str += " ";
                                }
                            }
                        }
                        vec2.push_back(str);  // 将构建好的当前行加入结果列表
                        str = "";
                        i += sum - 1;  // 跳过已处理的单词
                        sum = 0, countSize = 0;  // 重置当前行的变量
                        vec1.clear();  // 清空当前行的单词列表
                        break;  // 跳出循环
                    }
                }
            }
        }
        if (countSize > 0)  // 处理最后一行
        {
            for (int i = 0; i < maxWidth - countSize  - (sum - 1); ++i)  // 在最后一行填充剩余的空格
            {
                str += " ";
            }
            vec2.push_back(str);  // 将最后一行加入结果列表
        }
        
        return vec2;  // 返回最终结果列表
    }
};

```
当您用中文进行编程时，了解每个版本的代码所需的基础知识可以帮助您更好地理解和使用这些代码。以下是每个版本的基础知识要点：

 Go 版本
1. **Go 语言**: 您需要了解 Go 编程语言的基础知识，包括变量、函数、数组、切片、字符串处理等。
2. **字符串处理**: 了解如何处理字符串，如字符串连接、重复、判断长度等。
3. **循环与条件语句**: 理解 Go 中的循环和条件语句，以便实现文本两端对齐。
4. **切片**: 了解 Go 中的切片数据结构，用于处理单词列表的添加和删除。
5. **函数和函数调用**: 了解如何定义和调用函数，特别是`fullJustify`函数。
6. **Greedy 贪心算法**: 理解贪心算法的概念，它是解决文本两端对齐问题的核心。

 Python 版本
1. **Python 语言**: 熟悉 Python 编程语言的基础知识，包括变量、列表、字符串、函数等。
2. **列表(List)**: 了解如何使用 Python 的列表来存储和操作单词。
3. **字符串处理**: 了解字符串连接、长度计算、左对齐等字符串处理方法。
4. **循环与条件语句**: 熟悉 Python 的循环和条件语句，用于遍历单词和判断对齐方式。
5. **Greedy 贪心算法**: 了解贪心算法的应用，以便实现文本两端对齐。
6. **类(Class)**: 了解 Python 类的概念，其中定义了 `Solution` 类，包含了文本对齐的方法。

 Java 版本
1. **Java 语言**: 了解 Java 编程语言的基础知识，包括类、数组、字符串处理、循环等。
2. **数组(Array)**: 熟悉 Java 中的数组数据结构，用于存储单词。
3. **字符串处理**: 了解字符串的基本操作，如连接、长度计算、填充等。
4. **循环与条件语句**: 理解 Java 中的循环和条件语句，用于遍历单词和判断对齐方式。
5. **Greedy 贪心算法**: 了解贪心算法的应用，以便实现文本两端对齐。
6. **ArrayList**: 了解 Java 的 `ArrayList` 类，它用于存储每一行的单词。

 C++ 版本
1. **C++ 语言**: 熟悉 C++ 编程语言的基础知识，包括类、向量、字符串处理、循环等。
2. **向量(Vector)**: 了解 C++ 中的向量数据结构，用于存储单词和文本行。
3. **字符串处理**: 了解字符串连接、长度计算、填充等字符串处理方法。
4. **循环与条件语句**: 了解 C++ 中的循环和条件语句，用于遍历单词和判断对齐方式。
5. **Greedy 贪心算法**: 了解贪心算法的应用，以便实现文本两端对齐。
6. **C++ 标准库**: 熟悉 C++ 标准库中的数据结构和函数，如字符串处理函数。

无论您选择哪个版本，理解编程语言的基础知识、数据结构和算法概念都是非常重要的，以便有效地理解和修改代码以满足自己的需求。这些基础知识将帮助您理解文本两端对齐问题的解决方案。
