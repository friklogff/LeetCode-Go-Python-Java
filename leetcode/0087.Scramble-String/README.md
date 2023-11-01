# [87. Scramble String](https://leetcode.cn/problems/scramble-string/description/)

## 题目
We can scramble a string s to get a string t using the following algorithm:

If the length of the string is 1, stop.
If the length of the string is > 1, do the following:
Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
Apply step 1 recursively on each of the two substrings x and y.
Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.

 

Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true
Explanation: One possible scenario applied on s1 is:
"great" --> "gr/eat" // divide at random index.
"gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and keep them in order.
"gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both substrings. divide at random index each of them.
"g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring and to keep the second substring in the same order.
"r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide "at" to "a/t".
"r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings in the same order.
The algorithm stops now, and the result string is "rgeat" which is s2.
As one possible scenario led s1 to be scrambled to s2, we return true.
Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false
Example 3:

Input: s1 = "a", s2 = "a"
Output: true
 

Constraints:

s1.length == s2.length
1 <= s1.length <= 30
s1 and s2 consist of lowercase English letters.

## 题目大意

使用下面描述的算法可以扰乱字符串 s 得到字符串 t ：
如果字符串的长度为 1 ，算法停止
如果字符串的长度 > 1 ，执行下述步骤：
在一个随机下标处将字符串分割成两个非空的子字符串。即，如果已知字符串 s ，则可以将其分成两个子字符串 x 和 y ，且满足 s = x + y 。
随机 决定是要「交换两个子字符串」还是要「保持这两个子字符串的顺序不变」。即，在执行这一步骤之后，s 可能是 s = x + y 或者 s = y + x 。
在 x 和 y 这两个子字符串上继续从步骤 1 开始递归执行此算法。
给你两个 长度相等 的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。如果是，返回 true ；否则，返回 false 。
## 解题思路
好的，我将再分别介绍每个版本的解题思路。

Go

Go代码使用递归解决问题。它的基本思路如下：

- 如果两个字符串长度不同，则它们一定不是扰乱字符串。
- 如果两个字符串相等，则它们一定是扰乱字符串。
- 对于一个给定的字符串`s`，我们可以尝试将其拆分成两个子串`t1`和`t2`，然后分别判断这两个子串是否是扰乱字符串。如果两个子串都是扰乱字符串，那么`s`就是扰乱字符串。
- 在上述过程中，需要注意一些特殊情况的处理，例如`t1`和`t2`交换位置之后的情况等。

Python

Python代码也使用递归解决问题，但是在递归过程中使用了缓存机制以避免重复计算。它的基本思路如下：

- 如果两个字符串长度不同，则它们一定不是扰乱字符串。
- 如果两个字符串相等，则它们一定是扰乱字符串。
- 对于一个给定的字符串`s`，我们可以尝试将其拆分成两个子串`t1`和`t2`，然后分别判断这两个子串是否是扰乱字符串。如果两个子串都是扰乱字符串，那么`s`就是扰乱字符串。
- 在上述过程中，使用缓存机制来避免重复计算。

Java

Java代码使用动态规划解决问题。它的基本思路如下：

- 首先定义一个三维数组`dp[i][j][k]`，表示从字符串`s1`的第`i`个字符开始、字符串`s2`的第`j`个字符开始、子串的长度为`k`时，这两个子串是否是扰乱字符串。其中，`i`和`j`的范围为[0,字符串长度]，`k`的范围为[1,字符串长度]。
- 对于任意一对索引`(i,j,k)`，枚举所有可能的拆分点，即将子串`t1`和`t2`分别取自`(i,j,k)`和`(i+k,j+k,len-k)`，然后检查这两个子串是否是扰乱字符串。
- 在上述过程中，需要注意一些边界条件的处理，例如字符串长度为1时的情况等。

C++

C++代码使用分治算法解决问题。它的基本思路如下：

- 如果两个字符串长度不同，则它们一定不是扰乱字符串。
- 如果两个字符串相等，则它们一定是扰乱字符串。
- 对于一个给定的字符串`s`，我们可以尝试将其拆分成两个子串`t1`和`t2`，然后通过比较两个子串的字符出现次数是否相同来判断它们是否是扰乱字符串。如果两个子串都是扰乱字符串，那么`s`就是扰乱字符串。
- 在上述过程中，需要使用位运算来统计字符出现的次数，并对一些特殊情况进行处理。
 
## 代码

## Go

```Go
func isScramble(s1 string, s2 string) bool {
	// 获取字符串s1的长度
	n := len(s1)
	// 定义一个三维数组memo，保存已经处理过的状态
	memo := make([][][]byte, n)
	for i, _ := range memo {
		memo[i] = make([][]byte, n)
		for j, _ := range memo[i] {
			// 初始化memo[i][j]中的每个元素都为0
			memo[i][j] = make([]byte, n+1)
		}
	}
	// 定义函数dp来实现递归计算
	var dp func(int, int, int) bool
	dp = func(i, j, l int) bool {
		if l == 1 {
			return s1[i] == s2[j]
		}
		if v := memo[i][j][l]; v != 0 {
			return v == 1
		}
		result := false
		for s := 1; s <= l-1; s++ {
			// 分别比较s1和s2的左右两部分是否匹配
			if c1, c2 := dp(i, j, s) && dp(i+s, j+s, l-s), dp(i, j+l-s, s) && dp(i+s, j, l-s); c1 || c2 {
				result = true
				break
			}
		}
		// 如果result为true，则将memo[i][j][l]设置为1，表示已经处理过该状态并且是扰乱字符串
		if result {
			memo[i][j][l] = 1
		} else {
			// 否则将memo[i][j][l]设置为2，表示已经处理过该状态但不是扰乱字符串
			memo[i][j][l] = 2
		}
		return result
	}
	// 调用dp函数，并返回结果
	return dp(0, 0, n)
}

```

## Python

```Python
from functools import lru_cache

class Solution:
    @lru_cache(None)  # 使用functools模块中的lru_cache装饰器来开启缓存机制
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n == 0:
            return True
        if n == 1:
            return s1 == s2
        if sorted(s1) != sorted(s2):  # 如果s1和s2的字符集不一样，则一定不是扰乱字符串
            return False
        for i in range(1,n):
            # 比较s1和s2的左右字串以及s1和s2的交叉字串是否都是扰乱字符串
            if self.isScramble(s1[i:],s2[i:]) and self.isScramble(s1[:i],s2[:i]):
                return True
            elif self.isScramble(s1[i:],s2[:-i]) and self.isScramble(s1[:i],s2[-i:]):
                return True
        return False

```

## Java

```Java
class Solution {
    public boolean isScramble(String s1, String s2) {

        char[] chars_s1 = s1.toCharArray(), chars_s2 = s2.toCharArray();
        int index1 = 0, index2 = 0;
        return recursion(chars_s1, 0, chars_s2, 0, chars_s1.length, Forward.all);

    }

    private boolean recursion (char[] chars1, int index1, char[] chars2, int index2, int length, Forward forward) {

        if (length == 0) return true;  // 如果长度为0，则返回true
        if (length == 1) return chars1[index1] == chars2[index2];  // 如果长度为1，则比较两个字符是否相等
        int[] map1 = new int[26], map2 = new int[26];
        int count1 = 0, count2 = 0, end1 = index1 + length - 1, end2 = index2 + length - 1;
        for (int i = 0; i < length - 1; i++) {
            if (forward != Forward.right) {  // 如果没有走到最右边，则尝试以当前位置为分界点进行分割
                if (++map1[chars1[index1 + i] - 'a'] <= 0) count1--;
                else count1++;
                if (--map1[chars2[index2 + i] - 'a'] >= 0) count1--;
                else count1++;
                if (count1 == 0 && recursion(chars1, index1, chars2, index2, i + 1, Forward.right)) {
                    if (recursion(chars1, index1 + i + 1, chars2, index2 + i + 1, length - i - 1, Forward.all)) {
                        return true;
                    }
                }
            }
            if (forward != Forward.left) {  // 如果没有走到最左边，则尝试以当前位置为分界点进行分割
                if (++map2[chars1[index1 + i] - 'a'] <= 0) count2--;
                else count2++;
                if (--map2[chars2[end2 - i] - 'a'] >= 0) count2--;
                else count2++;
                if (count2 == 0 && recursion(chars1, index1, chars2, end2 - i, i + 1, Forward.left)) {
                    return recursion(chars1, index1 + i + 1, chars2, index2, length - i - 1, Forward.all);
                }
            }
        }
        return false;

    }

    enum Forward {
        left, right, all
    }
}

```

## Cpp

```Cpp
#define ALLONE(n) ((1<<(n))-1)

// 窗口状态类，用于记录窗口内字符出现情况
class WindowStatus
{
private:
    int status[2];  // 记录每个字符是否出现过
    int window[2];  // 记录窗口内字符出现情况
    int N;          // 块大小
    int offs;       // 每个块的起始位置

    inline int FirstOne_0b(int number)
    {
        return number & (-number);
    }

    inline int LastOne_0b(int number)
    {
        number |= number >> 1;
		number |= number >> 2;
		number |= number >> 4;
		number |= number >> 8;
		number |= number >> 16;

		return (number + 1) >> 1;
    }
public:
    WindowStatus(int n, int offset):
        N(n),
		offs(offset)
    {
        status[0] = status[1] = 0;
		window[0] = window[1] = 0;
    }

    // 更新窗口顶部的字符出现情况
    void Update_Top(int newpos,int r)
    {
        status[0] |= FirstOne_0b(newpos & ~status[0] & ALLONE(N) << offs);

		window[0] = (status[0] >> offs) % (1 << r);
    }

    // 更新窗口底部的字符出现情况
    void Update_Bot(int newpos,int r)
    {
		status[1] |= LastOne_0b(newpos & ~status[1] & ALLONE(N) << offs);

		window[1] = (status[1] >> offs) & (ALLONE(r) << (N - r));
    }

    // 判断窗口顶部的字符出现情况是否符合要求
    inline bool isOkay_Top(int r)
    {
        return window[0] % (1 << r) == ALLONE(r);
    }

    // 判断窗口底部的字符出现情况是否符合要求
    inline bool isOkay_Bot(int r)
    {
        return (window[1] >> (N - r)) % (1 << r) == ALLONE(r);
    }

    // 判断窗口是否可分离
    inline bool Detachable(int r)
    {
        return isOkay_Top(r) || isOkay_Bot(r);
    }
};
class Solution {
private:
    int pos[26];
    inline int GetHash(const char c)
    {
        return c-'a';
    }
    bool Trial(int start, int n, int offset, const std::string& s1, const std::string& s2)
    {
        if (n <= 0) return false;
		if (n <= 3) return true;

		WindowStatus wStatus(n, offset);
        bool Try[2] = {false,false};

		for (int i = 0;i < n - 1;++i)
		{
			const auto idx = start + i;
			const int r = i + 1;

			if (!Try[0])
			{
				wStatus.Update_Top(pos[GetHash(s2[idx])], i + 1);
				if (wStatus.isOkay_Top(r))
				{
					if (Trial(start, r, offset, s1, s2) 
						&& Trial(idx + 1, n - r, offset + r, s1, s2))
						return true;
					Try[0] = true;
				}
			}
			if (!Try[1])
			{
				wStatus.Update_Bot(pos[GetHash(s2[idx])], i + 1);
				if (wStatus.isOkay_Bot(r))
				{
					if (Trial(start, r, offset + n - r, s1, s2)
						&& Trial(idx + 1, n - r, offset, s1, s2))
						return true;
					Try[1] = true;
				}
			}
			if (Try[0] && Try[1])
			{
				return false;
			}
		}
		return false;
    }
    // 判断两个字符串的字符出现情况是否一致
    bool Check(const std::string& s1, const std::string& s2)
    {
        if (s1.length() != s2.length()) return false;

		int count[2][26];
		memset(count, 0, sizeof(count));

		for (int i = 0;i < s1.length();++i)
		{
			++count[0][GetHash(s1[i])];
			++count[1][GetHash(s2[i])];
		}
		return !memcmp(count[0], count[1], sizeof(count) / 2);
    }
	void InitPos(const std::string& s1, const std::string& s2)
    {
        memset(pos, 0, sizeof(pos));
		for (auto i = 0;i < s1.length();pos[GetHash(s1[i])] |= (1 << i), ++i);
    }
public:
    bool isScramble(string s1, string s2) 
    {
        if (!Check(s1, s2)) return false;
		InitPos(s1, s2);
		return Trial(0, s1.length(), 0, s1, s2);
    }
};

```
每个版本需要掌握的详细基础知识。

Go

在理解Go代码之前，你需要了解以下几个基本概念：

- `string`类型：字符串类型，表示一串字符序列。
- 数组和切片：数组是具有固定长度的数据结构，而切片是一个动态数组，可以根据需要自动增长或缩小。
- 递归函数：递归是一种解决问题的方法，它是通过将问题拆分成更小的子问题来解决大问题的过程。递归函数就是调用自身的函数。
- 动态规划：动态规划是一种算法思想，常用于解决优化问题。它通常采用分治策略，将问题分解为相互重叠和相互依赖的子问题，并将其子问题的解存储起来以避免重复计算。

Python

在理解Python代码之前，你需要了解以下几个基本概念：

- `str`类型：字符串类型，表示一串字符序列。
- 装饰器：装饰器是一种特殊的函数，它可以修改其他函数的行为。在Python中，可以使用`@`符号来应用装饰器。
- 缓存机制：缓存机制是指在计算结果后，将其保存起来以便下次快速访问，从而避免重复计算。这个功能在Python中可以使用`functools`模块中的`lru_cache`装饰器来实现。

Java

在理解Java代码之前，你需要了解以下几个基本概念：

- 字符串：字符串是由一系列字符组成的数据结构，可以用`String`类来表示。
- 递归函数：递归是一种解决问题的方法，它是通过将问题拆分成更小的子问题来解决大问题的过程。递归函数就是调用自身的函数。
- 枚举类型（Enum）：枚举类型是一种特殊的数据类型，它可以定义一组命名的常量值。在Java中，可以使用`enum`关键字来定义一个枚举类型。
- 深度优先搜索（DFS）：深度优先搜索是一种遍历图或树的算法，它从一个节点开始，沿着一条路径一直走到底，然后返回并继续搜索另一条路径。

C++

在理解C++代码之前，你需要了解以下几个基本概念：

- `std::string`类型：字符串类型，表示一串字符序列。
- 数组和指针：数组是具有固定长度的数据结构，而指针是一个指向内存地址的变量。
- 位运算：位运算是对二进制数字进行的运算，包括按位与、按位或、异或等运算。
- 分治算法：分治算法是一种算法思想，常用于解决大规模问题。它通常将问题分解为相互独立的子问题，并对每个子问题进行求解，最终将它们的解合并起来得到整体的解。