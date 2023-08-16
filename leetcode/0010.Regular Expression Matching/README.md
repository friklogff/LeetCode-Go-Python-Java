# [10. Regular Expression Matching](https://leetcode.cn/problems/regular-expression-matching/)

## 题目

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 
## 题目大意

给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

## 解题思路

**Go语言:**
1. 使用动态规划求解,定义二维数组f[i][j] 表示s的前i个字符和p的前j个字符是否匹配
2. 初始化f[0][0]为true,表示两字符串为空时匹配
3. 使用双层for循环进行状态转移,考虑当前字符为'*'和非'*'两种情况
4. 当p[j-1]='*'时,分为使用和不使用两种情况讨论
5. 不使用'*',直接继承f[i][j-2]的结果
6. 使用'*',需要校验s[i-1]和p[j-2]是否匹配,如果匹配继承f[i-1][j]
7. 非'*'时,判断s[i-1]和p[j-1]是否匹配,匹配则继承f[i-1][j-1]
8. 返回f[m][n]作为最终结果

**Python语言:**
1. 同样使用动态规划+二维数组f
2. 初始化f[0][0]为true
3. 双层for循环进行状态转移求解
4. 当p[j-1]为'*'时,分不使用和使用两种情况
5. 不使用继承f[i][j-2],使用需要校验s[i-1]和p[j-2]匹配
6. 非'*'时判断s[i-1]和p[j-1]匹配则继承f[i-1][j-1]
7. 返回f[m][n]作为结果

**Java语言:**
思路与上述相同:
1. 动态规划,定义boolean数组f[i][j]
2. 初始化f[0][0]为true
3. 两层for循环做状态转移
4. 分'*'和非'*'情况讨论
5. '*'时考虑不使用和使用两种情况
6. 非'*'判断前一个字符是否匹配
7. 返回f[m][n]作为最终解

**C++语言:**
1. 使用二维vector初始化f,动态规划
2. f[0][0]为true
3. 双层for循环做状态转移
4. 当p[j-1]为'*'分不使用和使用情况
5. 不使用继承f[i][j-2],使用需要校验匹配
6. 否则判断前一个字符是否匹配
7. 返回f[m][n]作为结果

## 代码

## Go
```Go
func isMatch(s string, p string) bool {
    // 定义s和p的长度
    m, n := len(s), len(p)
    // 判断s和p的子串从i和j位置开始是否匹配
    matches := func(i, j int) bool {
        // 如果i为0,说明s为空,返回false
        if i == 0 {
            return false
        }
        // 如果p[j-1]为'.',代表通配符,返回true
        if p[j-1] == '.' {
            return true
        }
        // 否则判断s[i-1]和p[j-1]是否相等
        return s[i-1] == p[j-1]
    }
    // 初始化二维数组f为m+1行n+1列
    f := make([][]bool, m + 1)
    for i := 0; i < len(f); i++ {
        f[i] = make([]bool, n + 1)
    }
    // 边界条件,如果s和p均为空,返回true
    f[0][0] = true
    // 动态规划状态转移
    for i := 0; i <= m; i++ {
        for j := 1; j <= n; j++ {
            // 如果p[j-1]为'*',有两种情况
            if p[j-1] == '*' {
                // 1. 不使用'*',直接继承f[i][j-2]的结果
                f[i][j] = f[i][j] || f[i][j-2]
                // 2. 使用'*',当s[i-1]和p[j-2]匹配时,继承f[i-1][j]的结果
                if matches(i, j - 1) {
                    f[i][j] = f[i][j] || f[i-1][j]
                }
            // 如果s[i-1]和p[j-1]匹配,继承f[i-1][j-1]的结果
            } else if matches(i, j) {
                f[i][j] = f[i][j] || f[i-1][j-1]
            }
        }
    }
    // 返回最终结果f[m][n]
    return f[m][n]
} 
```
## Python
```Python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        f = [[False] * (n+1) for _ in range(m+1)]
        f[0][0] = True
        for i in range(m+1):
            for j in range(1, n+1):
                if p[j-1] == '*':
                    f[i][j] |= f[i][j-2]
                    if self.matches(s, p, i, j-1):
                        f[i][j] |= f[i-1][j]
                else:
                    if self.matches(s, p, i, j):
                        f[i][j] |= f[i-1][j-1]
        return f[m][n]
    def matches(self, s, p, i, j):
        if i == 0:
            return False
        if p[j-1] == '.':
            return True
        return s[i-1] == p[j-1]
```
## Java
```Java
class Solution {
    public boolean isMatch(String s, String p) {
        int m = s.length();
        int n = p.length();
        boolean[][] f = new boolean[m + 1][n + 1];
        f[0][0] = true;
        for (int i = 0; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (p.charAt(j-1) == '*') {
                    f[i][j] = f[i][j-2];
                    if (matches(s, p, i, j-1)) {
                        f[i][j] = f[i][j] || f[i-1][j];
                    }
                } else {
                    if (matches(s, p, i, j)) {
                        f[i][j] = f[i-1][j-1];
                    }
                }
            }
        }
        return f[m][n];
    }
    public boolean matches(String s, String p, int i, int j) {
        if (i == 0) {
            return false;
        }
        if (p.charAt(j-1) == '.') {
            return true;
        }
        return s.charAt(i-1) == p.charAt(j-1);
    }
}
```
## Cpp
```Cpp
class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size();
        int n = p.size();
        vector<vector<bool>> f(m + 1, vector<bool>(n + 1, false));
        f[0][0] = true;
        for (int i = 0; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (p[j-1] == '*') {
                    f[i][j] = f[i][j-2];
                    if (matches(s, p, i, j-1)) {
                        f[i][j] = f[i][j] || f[i-1][j];
                    }
                } else {
                    if (matches(s, p, i, j)) {
                        f[i][j] = f[i-1][j-1];
                    }
                }
            }
        }
        return f[m][n];
    }
    bool matches(string s, string p, int i, int j) {
        if (i == 0) {
            return false;
        }
        if (p[j-1] == '.') {
            return true;
        }
        return s[i-1] == p[j-1];
    }
};
```
**Go语言:**
1. 数组/切片的定义:var arr [n]type, make初始化,len获取长度
2. 字符串访问:s[i]通过索引获取字符
3. 函数定义:func xxx(参数) 返回值类型 {}
4. if条件判断:if 条件 {}  else {}
5. for循环:for 初始化;条件;后续 {}
6. 逻辑或:||
7. 返回值:直接返回,可多值返回

**Python:**
1. 列表生成式:[[0]* n for _ in range(m)]
2. 字符串访问:s[i],索引从0开始
3. 函数定义:def 函数名(参数):
4. 条件判断:if 条件: elif: else:
5. for循环:for 变量 in 集合:
6. 逻辑或:|
7. 返回值:return 直接返回

**Java:**
1. 数组定义:类型[] 数组名 = new 类型[长度]
2. 字符串访问:字符串.charAt(索引)
3. 函数定义:返回值类型 函数名(参数) {}
4. 条件判断:if() {} else {}
5. for循环:for(初始化;条件;递增) {}
6. 逻辑或:||
7. 返回值:return 结果;

**C++:**
1. vector定义:vector<类型> 名称(大小)
2. 字符串访问:字符串[索引]
3. 函数定义:返回值类型 函数名(参数) {}
4. 条件判断:if() {} else {}
5. for循环:for(初始化;条件;递增) {}
6. 逻辑或:||
7. 返回值:return 结果;
