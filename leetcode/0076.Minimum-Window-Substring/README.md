# [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)

## 题目

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

```c
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
```

Note:    

- If there is no such window in S that covers all characters in T, return the empty string "".
- If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

## 题目大意

给定一个源字符串 s，再给一个字符串 T，要求在源字符串中找到一个窗口，这个窗口包含由字符串各种排列组合组成的，窗口中可以包含 T 中没有的字符，如果存在多个，在结果中输出最小的窗口，如果找不到这样的窗口，输出空字符串。

## 解题思路

这一题是滑动窗口的题目，在窗口滑动的过程中不断的包含字符串 T，直到完全包含字符串 T 的字符以后，记下左右窗口的位置和窗口大小。每次都不断更新这个符合条件的窗口和窗口大小的最小值。最后输出结果即可。

以下是每个版本的解题思路的详细介绍：

**Go 版本：**

1. 创建两个数组 `tFreq` 和 `sFreq` 用于记录字符频率，初始化一些变量如 `result`、`left`、`right`、`finalLeft`、`finalRight`、`minW` 和 `count` 。

2. 遍历字符串 `T`，统计每个字符的频率并存储在 `tFreq` 中。

3. 使用滑动窗口来在字符串 `S` 中查找包含所有 `T` 字符的最小窗口。

4. 移动右指针，不断更新 `sFreq` 中字符频率，同时增加 `count` 计数，直到包含所有 `T` 字符。

5. 一旦找到包含 `T` 的子串，计算窗口宽度，并更新 `finalLeft`、`finalRight` 和 `minW`。

6. 移动左指针，不断更新 `sFreq` 中字符频率，同时减少 `count` 计数，缩小窗口。

7. 最终，返回最小窗口的内容。

**Python 版本：**

1. 创建一个字典 `need` 用于存储字符串 `T` 中字符的频率。

2. 初始化变量 `i`、`count` 和 `res`。`i` 用于指示左窗口边界，`count` 用于计算还需要多少个字符，`res` 用于存储最小窗口的起始和结束位置。

3. 遍历字符串 `S`，右指针从左到右移动，统计字符频率，同时减少 `need` 中相应字符的频率。

4. 当 `count` 变为零时，表示找到一个包含 `T` 所有字符的窗口。

5. 移动左指针 `i` 缩小窗口，直到无法再缩小为止。在此过程中，继续更新 `res` 记录最小窗口的范围。

6. 最终，返回最小窗口的内容。

**Java 版本：**

1. 获取字符串 `S` 和 `T` 的长度，并初始化字符频率数组 `count`，以及字符总数 `time`。

2. 遍历字符串 `T`，统计每个字符的频率并增加 `time`。

3. 初始化左指针 `left` 和窗口长度 `len`，以及结果字符串 `ans`。

4. 遍历字符串 `S`，右指针从左到右移动，处理字符频率和计数。

5. 当窗口包含 `T` 中所有字符时，缩小窗口左边界，直到无法再缩小。在此过程中，不断更新 `ans` 记录最小窗口的范围。

6. 最终，返回最小窗口的内容。

**C++ 版本：**

1. 创建两数组 `tFreq` 和 `sFreq` 用于记录字符频率，并初始化一些变量如 `result`、`left`、`right`、`finalLeft`、`finalRight`、`minW` 和 `count`。

2. 遍历字符串 `T`，统计每个字符的频率并存储在 `tFreq` 中。

3. 使用滑动窗口来在字符串 `S` 中查找包含所有 `T` 字符的最小窗口。

4. 移动右指针，不断更新 `sFreq` 中字符频率，同时增加 `count` 计数，直到包含所有 `T` 字符。

5. 一旦找到包含 `T` 的子串，计算窗口宽度，并更新 `finalLeft`、`finalRight` 和 `minW`。

6. 移动左指针，不断更新 `sFreq` 中字符频率，同时减少 `count` 计数，缩小窗口。

7. 最终，返回最小窗口的内容。

这四个版本的解题思路都是使用滑动窗口技巧，通过不断移动左右指针来找到包含所有目标字符的最小窗口。不同编程语言的实现细节和语法略有不同，但基本思路相同。理解这些思路和对应编程语言的基础知识将帮助您更好地理解和修改这些代码。

## 代码

## Go

```Go
func minWindow(s string, t string) string {
	// 如果输入的s或t为空字符串，则直接返回空字符串
	if s == "" || t == "" {
		return ""
	}
	
	// 定义两个数组tFreq和sFreq，用于记录字符频率
	var tFreq, sFreq [256]int
	result, left, right, finalLeft, finalRight, minW, count := "", 0, -1, -1, -1, len(s)+1, 0

	// 遍历字符串t，统计每个字符的频率并存储在tFreq中
	for i := 0; i < len(t); i++ {
		tFreq[t[i]-'a']++
	}

	// 开始滑动窗口操作
	for left < len(s) {
		// 如果右指针在字符串s范围内且字符计数count小于字符串t的长度
		if right+1 < len(s) && count < len(t) {
			// 移动右指针，并更新sFreq中字符频率
			sFreq[s[right+1]-'a']++
			// 如果字符s[right+1]的频率不超过t中的频率，则增加计数count
			if sFreq[s[right+1]-'a'] <= tFreq[s[right+1]-'a'] {
				count++
			}
			right++
		} else {
			// 当找到包含t的子串时，计算窗口宽度
			if right-left+1 < minW && count == len(t) {
				minW = right - left + 1
				finalLeft = left
				finalRight = right
			}
			// 移动左指针，更新sFreq中字符频率
			if sFreq[s[left]-'a'] == tFreq[s[left]-'a'] {
				count--
			}
			sFreq[s[left]-'a']--
			left++
		}
	}
	
	// 如果找到了包含t的子串，根据finalLeft和finalRight提取结果
	if finalLeft != -1 {
		result = string(s[finalLeft : finalRight+1])
	}
	return result
}

```

## Python

```Python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)  # 创建一个用于存储字符串 t 中字符频率的字典
        for c in t:
            need[c] += 1  # 统计字符串 t 中字符的频率
        
        i = 0
        count = len(t)  # 初始化字符计数
        res = (0, len(s))  # 初始化结果的起始位置和结束位置，初始设为整个字符串的范围
        
        for j, c in enumerate(s):
            if need[c] > 0:
                count -= 1  # 当字符 c 在 need 中的频率大于零时，减少计数
            need[c] -= 1  # 减少 need 中字符 c 的频率
            
            if count == 0:  # 当字符计数等于零时，表示找到包含 t 的窗口
                while True:
                    if need[s[i]] == 0:
                        break
                    need[s[i]] += 1
                    i += 1
                
                if (j - i) < (res[1] - res[0]):  # 计算窗口宽度，如果小于当前最小窗口宽度，则更新结果
                    res = (i, j)
                
                need[s[i]] += 1
                count += 1
                i += 1
        
        return "" if res[1] == len(s) else s[res[0]:res[1] + 1]  # 返回最短窗口的内容，如果找不到则返回空字符串

```

## Java

```Java
class Solution {
    public String minWindow(String s, String t) {
        int sLen = s.length();  // 获取字符串 s 的长度
        int tLen = t.length();  // 获取字符串 t 的长度
        if (sLen < tLen) {
            return "";
        }
        int[] count = new int[64];  // 用于记录字符频率的数组
        int time = 0;  // 字符串 t 中字符的总数
        for (char c : t.toCharArray()) {
            count[c - 'A']++;  // 统计字符串 t 中字符的频率
            time++;
        }
        int left = 0, len = 0;  // 初始化左指针和长度
        char[] sArr = s.toCharArray();
        String ans = "";  // 用于存储最短窗口结果的字符串
        for (int i = 0; i < sLen; i++) {
            int index = sArr[i] - 'A';  // 获取当前字符在 count 数组中的索引
            if (count[index] > 0) {
                len++;
            }
            count[index]--;
            while (len == time && count[sArr[left] - 'A'] < 0) {
                count[sArr[left] - 'A']++;
                left++;  // 移动左指针
            }
            if (len == time && (ans == "" || i - left + 1 < ans.length())) {
                ans = s.substring(left, i + 1);  // 更新最短窗口的结果
            }
        }
        return ans;  // 返回最短窗口的内容
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    string minWindow(string s, string t) {
        if (s.empty() || t.empty()) {
            return "";
        }

        vector<int> tFreq(256, 0);
        vector<int> sFreq(256, 0);
        string result = "";
        int left = 0, right = -1, finalLeft = -1, finalRight = -1, minW = s.size() + 1, count = 0;

        for (char c : t) {
            tFreq[c]++;
        }

        while (left < s.size()) {
            if (right + 1 < s.size() && count < t.size()) {
                right++;
                sFreq[s[right]]++;
                if (sFreq[s[right]] <= tFreq[s[right]]) {
                    count++;
                }
            } else {
                if (right - left + 1 < minW && count == t.size()) {
                    minW = right - left + 1;
                    finalLeft = left;
                    finalRight = right;
                }
                if (sFreq[s[left]] == tFreq[s[left]]) {
                    count--;
                }
                sFreq[s[left]]--;
                left++;
            }
        }

        if (finalLeft != -1) {
            result = s.substr(finalLeft, finalRight - finalLeft + 1);
        }
        return result;
    }
};

```

当使用不同编程语言（Go、Python、Java、C++）来解决特定问题时，需要了解每种编程语言的基础知识以理解代码。以下是针对每个版本的详细基础知识介绍：

**Go 版本：**

1. **基本语法和数据类型：** 需要了解 Go 的基本语法，包括变量声明、数据类型（如字符串、整数、数组、切片、映射等）、运算符等。

2. **函数和方法：** 理解函数和方法的声明、调用以及参数传递方式。

3. **数组和切片：** 理解 Go 中的数组和切片，以及它们的使用方式和区别。

4. **循环和条件语句：** 理解 Go 中的循环（如 `for` 循环）和条件语句（如 `if` 语句）的使用。

5. **结构体和方法：** 了解如何定义结构体和关联的方法。

6. **并发和协程：** 了解 Go 中的并发编程概念，如协程（goroutines）和通道（channels）。

**Python 版本：**

1. **基本语法和数据类型：** 理解 Python 的基本语法，包括变量声明、数据类型（如字符串、整数、列表、字典等）、运算符等。

2. **函数：** 了解如何定义函数、函数参数传递、函数的返回值以及函数的作用域。

3. **列表和字典：** 理解 Python 中的列表和字典，以及它们的用途和方法。

4. **循环和条件语句：** 了解 Python 中的循环（如 `for` 循环）和条件语句（如 `if` 语句）的使用。

5. **类和对象：** 了解如何定义类和创建对象，以及类的方法和属性。

6. **文件操作：** 了解如何打开、读取和写入文件。

7. **模块和包：** 了解 Python 中模块和包的概念，以及如何导入和使用它们。

**Java 版本：**

1. **基本语法和数据类型：** 需要了解 Java 的基本语法，包括变量声明、数据类型（如整数、字符串、数组等）、运算符等。

2. **类和对象：** 了解如何定义类和创建对象，以及类的方法和属性。

3. **循环和条件语句：** 理解 Java 中的循环（如 `for` 循环）和条件语句（如 `if` 语句）的使用。

4. **集合和数据结构：** 了解 Java 中的集合框架，如列表、映射、集合等，以及它们的使用。

5. **文件操作：** 了解如何处理文件的读取和写入。

6. **异常处理：** 了解如何捕获和处理异常情况。

7. **多线程和并发：** 了解 Java 中多线程编程和并发编程的基本概念。

**C++ 版本：**

1. **基本语法和数据类型：** 需要了解 C++ 的基本语法，包括变量声明、数据类型（如整数、字符串、数组等）、运算符等。

2. **函数：** 了解如何定义函数、函数参数传递、函数的返回值以及函数的重载。

3. **STL（标准模板库）：** 了解 C++ 中的STL容器（如向量、映射、队列等）和STL算法。

4. **循环和条件语句：** 理解 C++ 中的循环（如 `for` 循环）和条件语句（如 `if` 语句）的使用。

5. **类和对象：** 了解如何定义类和创建对象，以及类的方法和属性。

6. **文件操作：** 了解如何处理文件的读取和写入。

7. **异常处理：** 了解如何捕获和处理异常情况。

8. **指针和内存管理：** 了解 C++ 中指针的使用和内存管理，包括动态内存分配和释放。

以上是每个版本中所需的基本知识要点，您可以根据选择的编程语言深入学习相关主题以更好地理解和修改给出的代码。这将有助于您在解决类似问题时编写自己的代码或进行定制化的开发。