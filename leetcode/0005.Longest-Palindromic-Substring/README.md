# [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

## 题目

Given a string`s`, return*the longest palindromic substring*in`s`.

**Example 1:**

```
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

```

**Example 2:**

```
Input: s = "cbbd"
Output: "bb"

```

**Example 3:**

```
Input: s = "a"
Output: "a"

```

**Example 4:**

```
Input: s = "ac"
Output: "a"

```

**Constraints:**

- `1 <= s.length <= 1000`
- `s`consist of only digits and English letters (lower-case and/or upper-case),

## 题目大意

给你一个字符串 `s`，找到 `s` 中最长的回文子串。

## 解题思路

- 此题非常经典，并且有多种解法。
- 解法一，动态规划。定义 `dp[i][j]` 表示从字符串第 `i` 个字符到第 `j`
  个字符这一段子串是否是回文串。由回文串的性质可以得知，回文串去掉一头一尾相同的字符以后，剩下的还是回文串。所以状态转移方程是 `dp[i][j] = (s[i] == s[j]) && ((j-i < 3) || dp[i+1][j-1])`
  ，注意特殊的情况，`j - i == 1` 的时候，即只有 2 个字符的情况，只需要判断这 2 个字符是否相同即可。`j - i == 2` 的时候，即只有
  3 个字符的情况，只需要判断除去中心以外对称的 2 个字符是否相等。每次循环动态维护保存最长回文串即可。时间复杂度 O(n^2)
  ，空间复杂度 O(n^2)。
-

解法二，中心扩散法。动态规划的方法中，我们将任意起始，终止范围内的字符串都判断了一遍。其实没有这个必要，如果不是最长回文串，无需判断并保存结果。所以动态规划的方法在空间复杂度上还有优化空间。判断回文有一个核心问题是找到“轴心”。如果长度是偶数，那么轴心是中心虚拟的，如果长度是奇数，那么轴心正好是正中心的那个字母。中心扩散法的思想是枚举每个轴心的位置。然后做两次假设，假设最长回文串是偶数，那么以虚拟中心往
2 边扩散；假设最长回文串是奇数，那么以正中心的字符往 2 边扩散。扩散的过程就是对称判断两边字符是否相等的过程。这个方法时间复杂度和动态规划是一样的，但是空间复杂度降低了。时间复杂度
O(n^2)，空间复杂度 O(1)。

- 解法三，滑动窗口。这个写法其实就是中心扩散法变了一个写法。中心扩散是依次枚举每一个轴心。滑动窗口的方法稍微优化了一点，有些轴心两边字符不相等，下次就不会枚举这些不可能形成回文子串的轴心了。不过这点优化并没有优化时间复杂度，时间复杂度
  O(n^2)，空间复杂度 O(1)。
- 解法四，马拉车算法。这个算法是本题的最优解，也是最复杂的解法。时间复杂度 O(n)，空间复杂度 O(n)。中心扩散法有 2
  处有重复判断，第一处是每次都往两边扩散，不同中心扩散多次，实际上有很多重复判断的字符，能否不重复判断？第二处，中心能否跳跃选择，不是每次都枚举，是否可以利用前一次的信息，跳跃选择下一次的中心？马拉车算法针对重复判断的问题做了优化，增加了一个辅助数组，将时间复杂度从
  O(n^2) 优化到了 O(n)，空间换了时间，空间复杂度增加到 O(n)。

  ![https://img.halfrost.com/Leetcode/leetcode_5_1.png](https://img.halfrost.com/Leetcode/leetcode_5_1.png)

- 首先是预处理，向字符串的头尾以及每两个字符中间添加一个特殊字符 `#`，比如字符串 `aaba` 处理后会变成 `#a#a#b#a#`
  。那么原先长度为偶数的回文字符串 `aa` 会变成长度为奇数的回文字符串 `#a#a#`，而长度为奇数的回文字符串 `aba`
  会变成长度仍然为奇数的回文字符串 `#a#b#a#`，经过预处理以后，都会变成长度为奇数的字符串。**
  注意这里的特殊字符不需要是没有出现过的字母，也可以使用任何一个字符来作为这个特殊字符。**
  这是因为，当我们只考虑长度为奇数的回文字符串时，每次我们比较的两个字符奇偶性一定是相同的，所以原来字符串中的字符不会与插入的特殊字符互相比较，不会因此产生问题。**
  预处理以后，以某个中心扩散的步数和实际字符串长度是相等的。**因为半径里面包含了插入的特殊字符，又由于左右对称的性质，所以扩散半径就等于原来回文子串的长度。

  ![https://img.halfrost.com/Leetcode/leetcode_5_2.png](https://img.halfrost.com/Leetcode/leetcode_5_2.png)

- 核心部分是如何通过左边已经扫描过的数据推出右边下一次要扩散的中心。这里定义下一次要扩散的中心下标是 `i`。如果 `i`
  比 `maxRight` 要小，只能继续中心扩散。如果 `i` 比 `maxRight` 大，这是又分为 3 种情况。三种情况见上图。将上述 3
  种情况总结起来，就是 ：`dp[i] = min(maxRight-i, dp[2*center-i])`，其中，`mirror` 相对于 `center` 是和 `i`
  中心对称的，所以它的下标可以计算出来是 `2*center-i`。更新完 `dp[i]`
  以后，就要进行中心扩散了。中心扩散以后动态维护最长回文串并相应的更新 `center`，`maxRight`
  ，并且记录下原始字符串的起始位置 `begin` 和 `maxLen`。
## 1. Manacher 算法 (基于动态规划)
Manacher 算法是解决最长回文子串问题的高效算法,时间复杂度为 O(n),空间复杂度为 O(n)。它利用了回文串的对称性质,采用了中心扩展法的思想,但是通过一些技巧避免了重复计算,从而大大提高了效率。要理解 Manacher 算法,需要掌握以下基础知识:
- 回文串的性质:理解什么是回文串以及回文串的对称性质是理解 Manacher 算法的基础。
- 中心扩展法:了解如何以某个字符或两个字符为中心,向两边扩展判断回文串。
- 动态规划:理解动态规划的思想和应用场景,Manacher 算法的动态规划部分是核心。
- 数组和字符串操作:熟悉数组和字符串的基本操作,例如索引访问、切片等。
## 2. 滑动窗口方法
滑动窗口方法是一种直观但效率较低的解决方案,时间复杂度为 O(n^2),空间复杂度为 O(1)。该方法通过遍历所有可能的中心点,以中心点为起始,不断扩展窗口并判断回文串。要理解滑动窗口方法,需要掌握以下基础知识:
- 回文串的定义:了解什么是回文串,即正着读和倒着读都一样的字符串。 
- 字符串的基本操作:熟悉字符串的索引访问、切片等基本操作。
- 嵌套循环:理解循环嵌套的概念,以及嵌套循环的时间复杂度。
- 简单的算法思想:了解暴力枚举、遍历等基本的算法思想。
## 3. 中心扩展法 (两种变种)
中心扩展法也是一种直观但效率较低的解决方案,时间复杂度为 O(n^2),空间复杂度为 O(1)。这个方法的思想是以每个字符或两个字符为中心,向两边扩展判断回文串。要理解中心扩展法,需要掌握以下基础知识:
- 回文串的性质:了解回文串的定义和性质,包括对称性质。
- 字符串的基本操作:熟悉字符串的索引访问、切片等基本操作。 
- 嵌套循环:理解循环嵌套的概念,以及嵌套循环的时间复杂度。
- 简单的算法思想:了解暴力枚举、遍历等基本的算法思想。
## 4. 动态规划法 (DP)
动态规划法是一种通用的解决方案,但在解决最长回文子串问题上效率较低,时间复杂度为 O(n^2),空间复杂度为 O(n^2)。这个方法通过构建一个二维数组来记录子问题的解,然后逐步构建更大的回文串。要理解动态规划法,需要掌握以下基础知识:
- 动态规划的基本思想:了解动态规划的核心思想,即将问题拆分为子问题并记忆子问题的解。
- 二维数组的操作:熟悉二维数组的创建、访问、更新等操作。
- 嵌套循环:理解循环嵌套的概念,以及嵌套循环的时间复杂度。
## 代码


## Go

```Go
// 解法一 Manacher's algorithm，时间复杂度 O(n)，空间复杂度 O(n)
func longestPalindrome(s string) string {
    if len(s) < 2 {
        return s
    }
    newS := make([]rune, 0)
    newS = append(newS, '#')
    for _, c := range s {
        newS = append(newS, c)
        newS = append(newS, '#')
    }
    // dp[i]:    以预处理字符串下标 i 为中心的回文半径(奇数长度时不包括中心)
    // maxRight: 通过中心扩散的方式能够扩散的最右边的下标
    // center:   与 maxRight 对应的中心字符的下标
    // maxLen:   记录最长回文串的半径
    // begin:    记录最长回文串在起始串 s 中的起始下标
    dp, maxRight, center, maxLen, begin := make([]int, len(newS)), 0, 0, 1, 0
    for i := 0; i < len(newS); i++ {
        if i < maxRight {
            // 这一行代码是 Manacher 算法的关键所在
            dp[i] = min(maxRight-i, dp[2*center-i])
        }
        // 中心扩散法更新 dp[i]
        left, right := i-(1+dp[i]), i+(1+dp[i])
        for left >= 0 && right < len(newS) && newS[left] == newS[right] {
            dp[i]++
            left--
            right++
        }
        // 更新 maxRight，它是遍历过的 i 的 i + dp[i] 的最大者
        if i+dp[i] > maxRight {
            maxRight = i + dp[i]
            center = i
        }
        // 记录最长回文子串的长度和相应它在原始字符串中的起点
        if dp[i] > maxLen {
            maxLen = dp[i]
            begin = (i - maxLen) / 2 // 这里要除以 2 因为有我们插入的辅助字符 #
        }
    }
    return s[begin : begin+maxLen]
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}
// 解法二 滑动窗口，时间复杂度 O(n^2)，空间复杂度 O(1)
func longestPalindrome(s string) string {
    if len(s) == 0 {
        return ""
    }
    left, right, pl, pr := 0, -1, 0, 0
    for left < len(s) {
        // 移动到相同字母的最右边（如果有相同字母）
        for right+1 < len(s) && s[left] == s[right+1] {
            right++
        }
        // 找到回文的边界
        for left-1 >= 0 && right+1 < len(s) && s[left-1] == s[right+1] {
            left--
            right++
        }
        if right-left > pr-pl {
            pl, pr = left, right
        }
        // 重置到下一次寻找回文的中心
        left = (left+right)/2 + 1
        right = left
    }
    return s[pl : pr+1]
}
// 解法三 中心扩散法，时间复杂度 O(n^2)，空间复杂度 O(1)
func longestPalindrome(s string) string {
    res := ""
    for i := 0; i < len(s); i++ {
        res = maxPalindrome(s, i, i, res)
        res = maxPalindrome(s, i, i+1, res)
    }
    return res
}

func maxPalindrome(s string, i, j int, res string) string {
    sub := ""
    for i >= 0 && j < len(s) && s[i] == s[j] {
        sub = s[i : j+1]
        i--
        j++
    }
    if len(res) < len(sub) {
        return sub
    }
    return res
}
// 解法四 DP，时间复杂度 O(n^2)，空间复杂度 O(n^2)
func longestPalindrome(s string) string {
    res, dp := "", make([][]bool, len(s))
    for i := 0; i < len(s); i++ {
        dp[i] = make([]bool, len(s))
    }
    for i := len(s) - 1; i >= 0; i-- {
        for j := i; j < len(s); j++ {
            dp[i][j] = (s[i] == s[j]) && ((j-i < 3) || dp[i+1][j-1])
            if dp[i][j] && (res == "" || j-i+1 > len(res)) {
                res = s[i : j+1]
            }
        }
    }
    return res
}
```

## Python

```Python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        new_s = ['#']
        for c in s:
            new_s.append(c)
            new_s.append('#')
        dp = [0] * len(new_s)
        max_right = 0
        center = 0
        max_len = 1
        begin = 0
        for i in range(len(new_s)):
            if i < max_right:
                dp[i] = min(max_right - i, dp[2 * center - i])
            left = i - (1 + dp[i])
            right = i + (1 + dp[i])
            while left >= 0 and right < len(new_s) and new_s[left] == new_s[right]:
                dp[i] += 1
                left -= 1
                right += 1
            if i + dp[i] > max_right:
                max_right = i + dp[i]
                center = i
            if dp[i] > max_len:
                max_len = dp[i]
                begin = (i - max_len) // 2
        return s[begin:begin + max_len]


class Solution:
    # 解法二: 滑动窗口法
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""

        left, right, pl, pr = 0, -1, 0, 0

        # 1. 遍历每个字符作为回文中心
        while left < len(s):
            # 2. 找到相同字符的最右边界
            while right + 1 < len(s) and s[left] == s[right + 1]:
                right += 1

            # 3. 扩展回文边界
            while left - 1 >= 0 and right + 1 < len(s) and s[left - 1] == s[right + 1]:
                left -= 1
                right += 1

            # 4. 更新最长回文子串的边界
            if right - left > pr - pl:
                pl, pr = left, right

            # 5. 重置中心，准备下一次寻找
            left = (left + right) // 2 + 1
            right = left

        # 6. 返回结果
        return s[pl: pr + 1]


class Solution:
    # 解法三: 中心扩散法
    def longestPalindrome(self, s: str) -> str:
        res = ""

        # 1. 以每个字符为中心，寻找最长回文子串
        for i in range(len(s)):
            res = self.maxPalindrome(s, i, i, res)  # 处理奇数长度的回文
            res = self.maxPalindrome(s, i, i + 1, res)  # 处理偶数长度的回文

        # 2. 返回结果
        return res

    # 辅助函数：在指定范围内寻找最长回文子串
    def maxPalindrome(self, s: str, i: int, j: int, res: str) -> str:
        sub = ""
        while i >= 0 and j < len(s) and s[i] == s[j]:
            sub = s[i: j + 1]
            i -= 1
            j += 1

        if len(res) < len(sub):
            return sub
        return res


class Solution:

    # 解法四: 动态规划法
    def longestPalindrome(self, s: str) -> str:
        res = ""
        dp = [[False] * len(s) for _ in range(len(s))]

        # 1. 从后往前遍历，填充动态规划表格
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                dp[i][j] = (s[i] == s[j]) and ((j - i < 3) or dp[i + 1][j - 1])

                if dp[i][j] and (not res or j - i + 1 > len(res)):
                    res = s[i: j + 1]

        # 2. 返回结果
        return res

```

## Java

```Java
class Solution {
    public String longestPalindrome(String s) {
        if (s.length() < 2) {
            return s;
        }

        // 解法一: Manacher's 算法
        StringBuilder newS = new StringBuilder("#");
        for (char c : s.toCharArray()) {
            newS.append(c);
            newS.append('#');
        }

        // 初始化变量
        int[] dp = new int[newS.length()];
        int maxRight = 0, center = 0, maxLen = 1, begin = 0;

        // Manacher 算法的核心部分
        for (int i = 0; i < newS.length(); i++) {
            if (i < maxRight) {
                dp[i] = Math.min(maxRight - i, dp[2 * center - i]);
            }

            int left = i - (1 + dp[i]);
            int right = i + (1 + dp[i]);
            while (left >= 0 && right < newS.length() && newS.charAt(left) == newS.charAt(right)) {
                dp[i]++;
                left--;
                right++;
            }

            if (i + dp[i] > maxRight) {
                maxRight = i + dp[i];
                center = i;
            }

            if (dp[i] > maxLen) {
                maxLen = dp[i];
                begin = (i - maxLen) / 2;
            }
        }

        // 返回结果
        return s.substring(begin, begin + maxLen);
    }
}
class Solution {
// 解法二: 滑动窗口法
    public String longestPalindrome(String s) {
        if (s.length() == 0) {
            return "";
        }

        int left = 0, right = -1, pl = 0, pr = 0;

        // 遍历每个字符作为回文中心
        while (left < s.length()) {
            // 找到相同字符的最右边界
            while (right + 1 < s.length() && s.charAt(left) == s.charAt(right + 1)) {
                right++;
            }

            // 扩展回文边界
            while (left - 1 >= 0 && right + 1 < s.length() && s.charAt(left - 1) == s.charAt(right + 1)) {
                left--;
                right++;
            }

            // 更新最长回文子串的边界
            if (right - left > pr - pl) {
                pl = left;
                pr = right;
            }

            // 重置中心，准备下一次寻找
            left = (left + right) / 2 + 1;
            right = left;
        }

        // 返回结果
        return s.substring(pl, pr + 1);
    }
}
class Solution {
    // 解法三: 中心扩散法
    public String longestPalindrome(String s) {
        String res = "";

        // 以每个字符为中心，寻找最长回文子串
        for (int i = 0; i < s.length(); i++) {
            res = maxPalindrome(s, i, i, res);      // 处理奇数长度的回文
            res = maxPalindrome(s, i, i + 1, res);  // 处理偶数长度的回文
        }

        // 返回结果
        return res;
    }

    // 辅助函数：在指定范围内寻找最长回文子串
    private String maxPalindrome(String s, int i, int j, String res) {
        String sub = "";
        while (i >= 0 && j < s.length() && s.charAt(i) == s.charAt(j)) {
            sub = s.substring(i, j + 1);
            i--;
            j++;
        }

        if (sub.length() > res.length()) {
            return sub;
        }

        return res;
    }

}
class Solution {
    // 解法四: 动态规划法
    public String longestPalindrome(String s) {
        String res = "";
        boolean[][] dp = new boolean[s.length()][s.length()];

        // 从后往前遍历，填充动态规划表格
        for (int i = s.length() - 1; i >= 0; i--) {
            for (int j = i; j < s.length(); j++) {
                dp[i][j] = (s.charAt(i) == s.charAt(j)) && ((j - i < 3) || dp[i + 1][j - 1]);

                if (dp[i][j] && (res.isEmpty() || j - i + 1 > res.length())) {
                    res = s.substring(i, j + 1);
                }
            }
        }

        // 返回结果
        return res;
    }

}
```

## Cpp

```Cpp
class Solution {
public:
        string longestPalindrome(string s) {
        if (s.length() < 2) {
            return s;
        }

        // 解法一: Manacher's 算法
        string newS = "#";
        for (char c : s) {
            newS += c;
            newS += '#';
        }

        // 初始化变量
        vector<int> dp(newS.length(), 0);
        int maxRight = 0, center = 0, maxLen = 1, begin = 0;

        // Manacher 算法的核心部分
        for (int i = 0; i < newS.length(); i++) {
            if (i < maxRight) {
                dp[i] = min(maxRight - i, dp[2 * center - i]);
            }

            int left = i - (1 + dp[i]);
            int right = i + (1 + dp[i]);
            while (left >= 0 && right < newS.length() && newS[left] == newS[right]) {
                dp[i]++;
                left--;
                right++;
            }

            if (i + dp[i] > maxRight) {
                maxRight = i + dp[i];
                center = i;
            }

            if (dp[i] > maxLen) {
                maxLen = dp[i];
                begin = (i - maxLen) / 2;
            }
        }

        // 返回结果
        return s.substr(begin, maxLen);
    }

};
class Solution {
public:
    // 解法二: 滑动窗口法
    string longestPalindrome(string s) {
        if (s.length() == 0) {
            return "";
        }

        int left = 0, right = -1, pl = 0, pr = 0;

        // 遍历每个字符作为回文中心
        while (left < s.length()) {
            // 找到相同字符的最右边界
            while (right + 1 < s.length() && s[left] == s[right + 1]) {
                right++;
            }

            // 扩展回文边界
            while (left - 1 >= 0 && right + 1 < s.length() && s[left - 1] == s[right + 1]) {
                left--;
                right++;
            }

            // 更新最长回文子串的边界
            if (right - left > pr - pl) {
                pl = left;
                pr = right;
            }

            // 重置中心，准备下一次寻找
            left = (left + right) / 2 + 1;
            right = left;
        }

        // 返回结果
        return s.substr(pl, pr - pl + 1);
    }

};
class Solution {
public:
    // 解法三: 中心扩散法
    string longestPalindrome(string s) {
        string res = "";

        // 以每个字符为中心，寻找最长回文子串
        for (int i = 0; i < s.length(); i++) {
            res = maxPalindrome(s, i, i, res);      // 处理奇数长度的回文
            res = maxPalindrome(s, i, i + 1, res);  // 处理偶数长度的回文
        }

        // 返回结果
        return res;
    }

    // 辅助函数：在指定范围内寻找最长回文子串
    string maxPalindrome(string s, int i, int j, string res) {
        string sub = "";
        while (i >= 0 && j < s.length() && s[i] == s[j]) {
            sub = s.substr(i, j - i + 1);
            i--;
            j++;
        }

        if (sub.length() > res.length()) {
            return sub;
        }

        return res;
    }
};
class Solution {
public:
    // 解法四: 动态规划法
    string longestPalindrome(string s) {
        string res = "";
        vector<vector<bool>> dp(s.length(), vector<bool>(s.length(), false));

        // 从后往前遍历，填充动态规划表格
        for (int i = s.length() - 1; i >= 0; i--) {
            for (int j = i; j < s.length(); j++) {
                dp[i][j] = (s[i] == s[j]) && ((j - i < 3) || dp[i + 1][j - 1]);

                if (dp[i][j] && (res.empty() || j - i + 1 > res.length())) {
                    res = s.substr(i, j - i + 1);
                }
            }
        }

        // 返回结果
        return res;
    }
};
```

