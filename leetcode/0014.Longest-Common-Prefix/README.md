# [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

## 题目

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

**Example 1**:

    Input: strs = ["flower","flow","flight"]
    Output: "fl"

**Example 2**:

    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

**Constraints:**

- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lower-case English letters.

## 题目大意

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

## 解题思路

- 对 strs 按照字符串长度进行升序排序，求出 strs 中长度最小字符串的长度 minLen
- 逐个比较长度最小字符串与其它字符串中的字符，如果不相等就返回 commonPrefix,否则就把该字符加入 commonPrefix
### Go版本
1. 将第一个字符串设为prefix
2. 遍历剩余字符串
3. 逐字符比较prefix,如果不相等则减少prefix长度
4. 不断重复步骤3,直到prefix为空或符合所有字符串
5. 返回prefix
主要是利用字符串的遍历和切片操作逐步缩短prefix。
### Python版本
1. 第一个字符串为prefix
2. 循环遍历其余字符串
3. 使用find方法判断是否以prefix开头
4. 如果不符合,减少prefix长度
5. 不断重复步骤3、4,直到prefix为空或符合所有字符串
6. 返回prefix
利用了find方法和切片操作判断并修改prefix。
### Java版本
1. 第一个字符串为prefix
2. 循环遍历其余字符串
3. 使用indexOf判断是否以prefix开头
4. 如果不符合,减少prefix长度
5. 不断重复步骤3、4,直到prefix为空或符合所有字符串 
6. 返回prefix
同样利用了indexOf和substring方法判断并获取子串。
### C++版本
1. 第一个字符串为prefix
2. 循环遍历其余字符串
3. 使用find方法判断是否以prefix开头 
4. 如果不符合,减少prefix长度
5. 不断重复步骤3、4,直到prefix为空或符合所有字符串
6. 返回prefix
依靠find和substr方法判断和获取子串。
## 代码

## Go
```Go
func longestCommonPrefix(strs []string) string {
    prefix := strs[0]

    for i := 1; i < len(strs); i++ {
        for j := 0; j < len(prefix); j++ {
            if len(strs[i]) <= j || strs[i][j] != prefix[j] {
                prefix = prefix[0:j]
                break
            }
        }
    }

    return prefix
}
```
## Python
```Python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:len(prefix)-1]
                if not prefix: return ""
        return prefix
```
## Java
```Java
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) return "";
        String prefix = strs[0];
        for (int i = 1; i < strs.length; i++) {
            while (strs[i].indexOf(prefix) != 0) {
                prefix = prefix.substring(0, prefix.length() - 1);
                if (prefix.isEmpty()) return "";
            }       
        }
        return prefix;
    }
}
```
## Cpp
```Cpp
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";
        string prefix = strs[0];
        for (int i = 1; i < strs.size(); i++) {
            while (strs[i].find(prefix) != 0) {
                prefix = prefix.substr(0, prefix.size()-1);
                if (prefix.empty()) return "";
            }
        }
        return prefix;
    }
};
```
每个版本需要掌握的基础知识:
### Go 版本
- strings包:strings包提供字符串操作相关函数,如Contains、Index等
- 字符串遍历:可以通过for循环遍历字符串的字节
- 字符串切片:可以通过指定开始和结束位置[i:j]来获取子字符串
### Python 版本
- str类型:Python内置的字符串类型
- find方法:查找子字符串在字符串中出现的位置,返回第一个匹配位置的索引,不存在返回-1
- 切片操作:通过指定开始和结束位置[i:j]可以获取子字符串
### Java 版本
- String类:String代表不可变字符串,有索引访问字符和子字符串获取等方法
- indexOf方法:查找子字符串在字符串中出现的位置,返回第一个匹配位置索引,不存在返回-1
- substring方法:获取字符串指定区间的子字符串
### C++版本
- string类:string代表字符串对象,支持遍历、访问单个字符、获取子串等操作
- find方法:查找子串在字符串中首次出现的位置,不存在返回string::npos
- substr方法:获取子字符串中指定范围的字符