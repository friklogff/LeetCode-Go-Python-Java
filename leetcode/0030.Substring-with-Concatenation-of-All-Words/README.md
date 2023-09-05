# [30. Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)

## 题目

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of
substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

```c
Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
```

Example 2:

```c
Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
```

## 题目大意

给定一个源字符串 s，再给一个字符串数组，要求在源字符串中找到由字符串数组各种组合组成的连续串的起始下标，如果存在多个，在结果中都需要输出。

## 解题思路

这一题看似很难，但是有 2 个限定条件也导致这题不是特别难。1. 字符串数组里面的字符串长度都是一样的。2.
要求字符串数组中的字符串都要连续连在一起的，前后顺序可以是任意排列组合。

解题思路，先将字符串数组里面的所有字符串都存到 map
中，并累计出现的次数。然后从源字符串从头开始扫，每次判断字符串数组里面的字符串时候全部都用完了(计数是否为 0)
，如果全部都用完了，并且长度正好是字符串数组任意排列组合的总长度，就记录下这个组合的起始下标。如果不符合，就继续考察源字符串的下一个字符，直到扫完整个源字符串。
下面我将分别介绍每个版本的解题思路：

**Go 版本**：

1. **初始化变量**：
   - 获取输入字符串 `s` 的长度 `ls`，单词数组 `words` 的长度 `m`，以及单词的长度 `n`。
   - 初始化一个空的整数切片 `ans` 用于存储结果。

2. **主循环**：
   - 从字符串 `s` 的前 n 个字符开始，循环遍历起始位置。
   - 创建一个映射 `differ` 用于跟踪当前窗口内每个单词的出现次数。

3. **遍历单词列表 `words`**：
   - 对于单词列表中的每个单词，在 `differ` 中增加其出现次数。
   - 如果出现次数增加后变为 0，从 `differ` 中删除该单词。

4. **主循环**：
   - 从当前起始位置开始，每次移动一个单词的长度 `n`，检查子串是否包含所有单词。
   - 如果不包含，继续移动窗口。
   - 如果 `differ` 中不包含任何单词，说明子串包含了所有单词，将当前起始位置添加到结果中。

5. **返回结果**：返回存储结果的切片 `ans`。

**Python 版本**：

1. **初始化变量**：
   - 初始化一个空列表 `ans` 用于存储结果。
   - 计算单词的长度 `word_len`，单词数组的长度 `total_words`，单词数组的元素计数 `word_count`，以及输入字符串 `s` 的长度 `s_len`。

2. **循环遍历单词的起始位置**：
   - 外层循环迭代单词的起始位置，从 0 到 `word_len-1`。
   - 内部维护两个指针 `left` 和 `j`，以及一个计数器 `count` 和一个单词计数器 `current_count`。

3. **遍历字符串 `s`**：
   - 内部循环遍历字符串 `s` 从当前起始位置开始，每次移动一个单词的长度 `word_len`。
   - 在内部循环中，检查当前子串是否是单词数组的一个有效组合。
   - 如果是有效组合，将起始位置 `left` 添加到结果列表中。

4. **返回结果**：返回存储结果的列表 `ans`。

**Java 版本**：

1. **初始化变量**：
   - 初始化一个空列表 `res` 用于存储结果。
   - 创建一个映射 `map` 用于存储单词以及它们的出现次数。
   - 获取单词数组的长度 `m`。

2. **循环遍历可能的单词起始位置**：
   - 外层循环迭代单词的起始位置，从 0 到 `len(words[0])-1`。

3. **遍历字符串 `s`**：
   - 内部循环遍历字符串 `s`，从当前起始位置开始，每次移动一个单词的长度。
   - 在内部循环中，检查当前子串是否是单词数组的一个有效组合。
   - 如果是有效组合，将起始位置添加到结果列表 `res` 中。

4. **返回结果**：返回存储结果的列表 `res`。

**C++ 版本**：

1. **初始化变量**：
   - 初始化一个空向量 `ans` 用于存储结果。
   - 获取单词数组的长度 `m` 和单词的长度 `wordsize`。
   - 创建一个映射 `mp` 用于存储单词以及它们的出现次数。
   - 获取输入字符串 `s` 的长度 `n`。

2. **循环遍历可能的单词起始位置**：
   - 外层循环迭代单词的起始位置，从 0 到 `wordsize-1`。

3. **遍历字符串 `s`**：
   - 内部循环遍历字符串 `s`，从当前起始位置开始，每次移动一个单词的长度。
   - 在内部循环中，检查当前子串是否是单词数组的一个有效组合。
   - 如果是有效组合，将起始位置添加到结果向量 `ans` 中。

4. **返回结果**：返回存储结果的向量 `ans`。

这些是每个版本的基本解题思路。它们都采用了滑动窗口技巧，从不同的起始位置开始，逐步移动窗口并检查子串是否满足条件。同时，它们还利用了数据结构（如映射或计数器）来统计单词的出现次数以进行比较。不同的编程语言在实现细节上有所不同，但整体思路是一致的。
## 代码

## Go

```Go
func findSubstring(s string, words []string) (ans []int) {
    // 获取输入字符串 `s` 的长度
    ls, m, n := len(s), len(words), len(words[0])

    // 遍历字符串 `s` 的前 n 个字符
    for i := 0; i < n && i+m*n <= ls; i++ {
        // 使用 map `differ` 来跟踪子串中每个单词的出现次数
        differ := map[string]int{}

        // 遍历单词列表 `words`
        for j := 0; j < m; j++ {
            // 将子串中的每个单词加入到 `differ` 中，并统计出现次数
            differ[s[i+j*n:i+(j+1)*n]]++
        }

        // 遍历单词列表 `words`
        for _, word := range words {
            // 减少 `differ` 中对应单词的出现次数
            differ[word]--
            // 如果出现次数减少到 0，从 `differ` 中删除这个单词
            if differ[word] == 0 {
                delete(differ, word)
            }
        }

        // 从当前位置 `i` 开始，每次移动一个单词长度 `n`，检查子串是否包含所有单词
        for start := i; start < ls-m*n+1; start += n {
            if start != i {
                // 更新 `differ`，增加新单词的出现次数，减少旧单词的出现次数
                word := s[start+(m-1)*n : start+m*n]
                differ[word]++
                if differ[word] == 0 {
                    delete(differ, word)
                }
                word = s[start-n : start]
                differ[word]--
                if differ[word] == 0 {
                    delete(differ, word)
                }
            }
            // 如果 `differ` 中不包含任何单词，说明子串包含了所有单词
            if len(differ) == 0 {
                ans = append(ans, start)
            }
        }
    }
    return
}

```

## Python

```Python
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        ans = []
        word_len = len(words[0])
        total_words = len(words)
        word_count = Counter(words)
        s_len = len(s)

        for i in range(word_len):
            left = i
            count = 0
            current_count = Counter()

            for j in range(i, s_len - word_len + 1, word_len):
                word = s[j:j + word_len]
                if word in word_count:
                    current_count[word] += 1
                    count += 1

                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        count -= 1
                        left += word_len

                    if count == total_words:
                        ans.append(left)
                else:
                    current_count.clear()
                    count = 0
                    left = j + word_len

        return ans

```

## Java

```Java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        Map<String, Integer> map = new HashMap<>();
        
        // 将单词数组中的单词以及它们的出现次数存储在 map 中
        for (String str : words) {
            map.put(str, map.getOrDefault(str, 0) + 1);
        }
        
        int len = words[0].length(); // 单词的长度
        List<Integer> res = new ArrayList<>(); // 存储结果的列表
        
        // 遍历字符串 s 中每个可能的起始位置
        for (int i = 0; i < len; i++) {
            Map<String, Integer> newmap = new HashMap<>(); // 存储当前窗口内的单词出现次数
            int count = 0; // 记录窗口内匹配的单词数量
            
            for (int j = i; j <= s.length() - len;) {
                String cur = s.substring(j, j + len); // 当前窗口内的单词
                
                // 如果当前单词在单词数组中且未超出其出现次数限制
                if (map.containsKey(cur) && (!newmap.containsKey(cur) || newmap.get(cur) < map.get(cur))) {
                    newmap.put(cur, newmap.getOrDefault(cur, 0) + 1); // 更新窗口内单词出现次数
                    count++; // 增加匹配的单词数量
                    
                    // 如果窗口内匹配的单词数量等于单词数组的长度，表示找到一个满足条件的子串
                    if (count == words.length) {
                        res.add(j - len * (words.length - 1)); // 记录子串的起始位置
                        count--;
                        String pre = s.substring(j - len * (words.length - 1), j - len * (words.length - 2));
                        newmap.put(pre, newmap.get(pre) - 1); // 更新窗口内单词出现次数
                    }
                    
                    j += len; // 移动窗口
                } 
                // 如果当前单词不在单词数组中
                else if (!map.containsKey(cur)) {
                    count = 0;
                    newmap.clear(); // 清空窗口内的单词记录
                    j += len;
                } 
                // 如果当前单词在单词数组中但超出其出现次数限制
                else {
                    String pre = s.substring(j - len * count, j - len * (count - 1));
                    newmap.put(pre, newmap.get(pre) - 1); // 更新窗口内单词出现次数
                    count--; // 减少匹配的单词数量
                }
            }
        }
        return res; // 返回结果列表
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        const int n = s.length();            // 输入字符串的长度
        const int m = words.size();          // 单词数组的大小
        const int wordsize = words.front().length(); // 单词的长度

        unordered_map<string, int> mp;       // 用于存储单词以及它们的出现次数
        for (auto &word : words)
            mp[word]++;

        vector<int> ans;                     // 存储结果的向量

        for (int i = 0; i < wordsize; ++i) { // 对于每个可能的起始位置
            unordered_map<string, int> cnt;  // 用于存储当前窗口内的单词出现次数
            int start = i;                  // 记录符合条件的字符串的起始位置

            for (int j = i; j < n; j += wordsize) { // 遍历字符串 s 中所有单词
                string word = s.substr(j, wordsize);

                if (!mp.count(word)) {       // 如果遇到不在单词数组中的单词，直接清空前面所有的计数
                    cnt.clear();
                    start = j + wordsize;
                } else {
                    cnt[word] += 1;

                    while (cnt[word] > mp[word]) { // 某个单词的计数超过了在单词数组中的出现次数，从左边减
                        cnt[s.substr(start, wordsize)]--;
                        start += wordsize;
                    }

                    if (j - start == (m - 1) * wordsize) // 如果窗口内匹配的单词数量等于单词数组的长度，表示找到一个满足条件的子串
                        ans.push_back(start);
                }
            }
        }

        return ans;
    }
};

```


每个版本的代码中所需要掌握的基础知识。

**Go 版本**：

1. **Go 语言基础**: 
   - 了解 Go 语言的基本语法，包括变量、循环、条件语句、函数等。

2. **字符串处理**:
   - 了解如何使用字符串切片和字符串拼接操作来处理字符串。
   - 理解字符串长度的计算方法。

3. **映射（map）**:
   - 了解 Go 中的映射数据结构，即 `map`，以及如何向映射中添加、删除和检索元素。
   - 熟悉如何使用映射来实现单词计数和比较。

4. **循环和条件语句**:
   - 了解如何使用 `for` 循环和 `if` 条件语句来实现迭代和条件判断。

5. **切片操作**:
   - 了解如何使用切片来操作数组或字符串的子集。
   - 理解如何通过切片进行迭代。

**Python 版本**：

1. **Python 语言基础**:
   - 熟悉 Python 语言的基本语法，包括变量、循环、条件语句、函数等。

2. **字符串处理**:
   - 了解如何使用字符串切片和字符串拼接操作来处理字符串。
   - 知道如何获取字符串的长度。

3. **Counter 类**:
   - 了解 Python 中的 `collections.Counter` 类，用于统计元素出现的次数。
   - 知道如何使用 `Counter` 对象来进行单词计数。

4. **循环和条件语句**:
   - 理解如何使用 `for` 循环和 `if` 条件语句来实现迭代和条件判断。

5. **列表（List）**:
   - 熟悉 Python 中的列表数据结构，以及如何使用列表来存储和操作数据。

**Java 版本**：

1. **Java 语言基础**:
   - 熟悉 Java 语言的基本语法，包括变量、循环、条件语句、函数等。

2. **字符串处理**:
   - 了解如何使用字符串切片和字符串拼接操作来处理字符串。
   - 知道如何获取字符串的长度。

3. **Map（映射）**:
   - 理解 Java 中的 `java.util.Map` 接口，以及如何使用 `HashMap` 实现映射。
   - 知道如何向映射中添加、删除和检索元素。

4. **循环和条件语句**:
   - 了解如何使用 `for` 循环和 `if` 条件语句来实现迭代和条件判断。

5. **列表（List）**:
   - 熟悉 Java 中的列表数据结构，即 `java.util.List`，以及如何使用列表来存储和操作数据。

**C++ 版本**：

1. **C++ 语言基础**:
   - 理解 C++ 语言的基本语法，包括变量、循环、条件语句、函数等。

2. **字符串处理**:
   - 了解如何使用字符串切片和字符串拼接操作来处理字符串。
   - 知道如何获取字符串的长度。

3. **STL（标准模板库）**:
   - 理解 C++ STL 中的 `std::unordered_map`，用于实现映射。
   - 知道如何向映射中添加、删除和检索元素。

4. **循环和条件语句**:
   - 了解如何使用 `for` 循环和 `if` 条件语句来实现迭代和条件判断。

5. **向量（Vector）**:
   - 熟悉 C++ 中的向量数据结构，即 `std::vector`，以及如何使用向量来存储和操作数据。

这些是理解和编写提供的不同语言版本的代码所需的基本知识。每个版本都使用了相似的算法和数据结构，但具体的语法和库函数可能会有所不同。