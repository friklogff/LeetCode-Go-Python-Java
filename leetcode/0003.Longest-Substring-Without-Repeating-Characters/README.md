# [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## 题目

Given a string, find the length of the longest substring without repeating characters.

Example 1:

```c
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
```

Example 2:

```c
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

Example 3:

```c
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

## 题目大意

在一个字符串中寻找没有重复字母的最长子串。

## 解题思路

这一题和第 438 题，第 3 题，第 76 题，第 567 题类似，用的思想都是"滑动窗口"。

滑动窗口的右边界不断的右移，只要没有重复的字符，就持续向右扩大窗口边界。一旦出现了重复字符，就需要缩小左边界，直到重复的字符移出了左边界，然后继续移动滑动窗口的右边界。以此类推，每次移动需要计算当前长度，并判断是否需要更新最大长度，最终最大的值就是题目中的所求。

**Go**

解法一:滑动窗口 + Map
- 使用map[byte]int记录每个字符最后出现的索引
- 初始化左右指针和结果res
- 右指针遍历字符串,若字符的索引大于等于左指针索引,左指针移到重复字符下一位
- 更新字符的索引,计算窗口大小更新结果
- 返回结果

解法二:滑动窗口 + 数组
- 定义int数组记录每个字符的出现频次
- 初始化左右指针和结果res
- 右指针右移,若字符频次为0,加1
- 否则左指针右移,对应频次减1 
- 计算窗口大小更新结果
- 返回结果

解法三:滑动窗口 + Bitmap
- 定义一个数组作为Bitmap
- 初始化左右指针和结果res
- 右指针右移,若该字符已被标记,左指针右移直到标记重置
- 标记右指针字符,计算窗口大小更新结果
- 返回结果

**Python**

解法一:滑动窗口 + 集合
- 使用集合来判断字符是否重复出现过。
- 左右指针初始化在字符串开头。
- 右指针不断右移,若字符已在集合中,则移除左指针位置字符,左指针右移。
- 将右指针字符添加到集合,并计算当前窗口大小,更新结果。
- 返回最大窗口大小。

解法二:滑动窗口 + 字符频次数组
- 定义一个数组记录每个ASCII字符出现的频次。
- 初始化左右指针在字符串开头。
- 右指针右移,若字符频次大于0,表示重复,左指针右移同时对应频次-1。 
- 右指针字符对应频次+1,并更新结果。
- 返回最大窗口大小。

解法三:滑动窗口 + 哈希表
- 使用哈希表存储字符的最近出现下标。
- 初始化左右指针在字符串开头。
- 右指针右移,若字符在表中且下标>=左指针,左指针移到重复字符处。
- 更新字符的最近下标,计算窗口大小并更新结果。
- 返回最大窗口大小。

解法四:位图
- 初始化一个256位的位图,可以映射ASCII字符
- 左右指针初始化在字符串开头
- 右指针右移,如果字符在位图中已被标记,则重置左指针字符,左指针右移
- 将右指针字符在位图中标记
- 计算窗口大小并更新结果
- 返回最大窗口大小

**Java**

解法一:滑动窗口 + 位图
- 使用一个boolean数组作为位图来记录每个字符是否出现
- 定义左右指针和结果res,初始化为0
- 右指针右移,如果对应字符已被标记,左指针右移直到重复字符被重置
- 设置右指针字符在位图中为true
- 计算窗口大小更新结果
- 返回最大窗口大小
解法二:滑动窗口 + 数组
- 定义一个int数组记录每个字符的出现频次 
- 初始化左右指针和结果res
- 右指针右移,如果字符频次为0,频次加1
- 如果频次大于0,左指针右移同时对应频次减1
- 计算窗口大小更新结果
- 返回最大窗口大小
解法三:滑动窗口 + 哈希表
- 使用HashMap存储字符及其最后出现的索引
- 初始化左右指针和结果res
- 左指针遍历字符串,如果字符在表中且索引>=右指针,移动右指针
- 更新字符的最近索引,计算窗口大小更新结果
- 返回最大窗口大小

**C++**

解法一:滑动窗口 + 位图
- 定义一个bool数组作为位图
- 初始化左右指针和结果res
- 右指针遍历,若字符已被标记,左指针右移直到该字符标记重置
- 标记右指针字符,计算窗口大小更新结果 
- 返回结果

解法二:滑动窗口 + 数组
- 定义一个int数组记录每个字符的出现频次
- 初始化左右指针和结果res
- 右指针右移,若字符频次为0,频次加1
- 否则左指针右移,对应频次减1
- 计算窗口大小更新结果
- 返回结果

解法三:滑动窗口 + 哈希表
- 使用unordered_map存储字符及最后出现的索引
- 初始化左右指针和结果res
- 左指针遍历,如果字符在表中且索引>=右指针,右指针移至重复字符下一位
- 更新字符索引,计算窗口大小更新结果
- 返回结果
## Go

```Go
// 解法一 位图
func lengthOfLongestSubstring(s string) int {
    if len(s) == 0 { // 如果传入的字符串长度为0,直接返回0
       return 0
    }
    var bitSet [256]bool // 定义一个256位的布尔数组,用来标记每个字符是否出现过
    result, left, right := 0, 0, 0 // 定义结果、左指针、右指针,初始化为0
    for left < len(s) { 
       // 如果当前右指针指向的字符在位图中被标记为true,说明该字符重复出现过
       // 需要左指针向右移动,直到将重复的字符的对应位标记为false
       if bitSet[s[right]] {  
          bitSet[s[left]] = false
          left++
       } else { // 如果没有重复,将该字符对应位标记为true
          bitSet[s[right]] = true 
          right++
       }
       // 计算当前窗口大小,更新结果
       if result < right-left {
          result = right - left 
       }
       // 如果左指针到达字符串结尾,或者右指针超过了字符串长度,结束循环
       if left+result >= len(s) || right >= len(s) {
          break
       }
    }
    return result // 返回结果
}

// 解法二 滑动窗口
func lengthOfLongestSubstring(s string) int {
    if len(s) == 0 { // 字符串为空,返回0
       return 0
    }
    var freq [127]int // 定义一个数组,记录ASCII字符出现的频率
    result, left, right := 0, 0, -1 

    for left < len(s) {
       // 如果右指针还可以移动,且对应的字符频率为0,右指针右移
       if right+1 < len(s) && freq[s[right+1]] == 0 {  
          freq[s[right+1]]++
          right++

       } else { // 否则左指针右移,对应字符频率减1
          freq[s[left]]--
          left++
       }
       // 计算当前窗口大小,更新结果
       result = max(result, right-left+1)  
    }
    return result
}
func max(a int, b int) int { // 比较两个数大小,返回较大值
    if a > b {
       return a
    }
    return b
}

// 解法三 滑动窗口-哈希桶
func lengthOfLongestSubstring(s string) int {
    right, left, res := 0, 0, 0 // 初始化右指针、左指针和结果
    indexes := make(map[byte]int, len(s)) // map存储每个字符最后出现的index
    for left < len(s) {
       if idx, ok := indexes[s[left]]; ok && idx >= right { // 如果该字符已存在且在窗口中
          right = idx + 1 // 右指针移动到重复字符处
       }
       indexes[s[left]] = left // 更新字符索引
       left++ // 左指针右移
       res = max(res, left-right) // 计算窗口大小,更新结果
    }
    return res
}

func max(a int, b int) int {
    if a > b {
       return a
    }
    return b
}

```

## Python

```Python
# 解法一:滑动窗口 + 集合
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0 # 字符串为空,直接返回0
        
        char_set = set() # 定义一个集合,记录每个字符是否出现过
        l = 0 
        res = 0
        
        for r in range(len(s)):
            while s[r] in char_set: # 如果右指针指向的字符已在集合中
                char_set.remove(s[l]) # 从集合中删除左指针位置字符
                l += 1 # 左指针右移
            char_set.add(s[r]) # 将右指针指向的字符添加到集合
            res = max(res, r-l+1) # 计算当前窗口大小,更新结果
        return res
            
# 解法二:滑动窗口 + 字符频次数组
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: 
            return 0 # 字符串为空,直接返回0
        
        freq = [0] * 128 # 定义数组,记录每个ASCII字符出现的频率
        l = 0
        res = 0
        
        for r in range(len(s)):
            while freq[ord(s[r])] > 0: # 如果右指针字符频率大于0,表示重复
                freq[ord(s[l])] -= 1 # 左指针位置字符频率减1
                l += 1 # 左指针右移
            freq[ord(s[r])] += 1 # 右指针字符频率加1
            res = max(res, r-l+1) # 计算窗口大小,更新结果
        return res
# 解法三:滑动窗口 + 哈希表
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        index = {} # 字典存储字符最后出现的index
        
        for r in range(len(s)):
            if s[r] in index and index[s[r]] >= l: # 字符已存在且在窗口中
                l = index[s[r]] + 1 # 左指针移动到重复字符处
            index[s[r]] = r # 更新字符index
            res = max(res, r-l+1) # 计算窗口大小,更新结果
            
        return res
# 解法四:位图
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        bitmap = [False] * 256 # 初始化一个256位的位图
        l = 0
        res = 0
        
        for r in range(len(s)):
            while bitmap[ord(s[r])]: # 右指针字符已被标记
                bitmap[ord(s[l])] = False # 重置左指针字符
                l += 1 
                
            bitmap[ord(s[r])] = True # 标记右指针字符
            res = max(res, r - l + 1) # 更新结果
            
        return res
```

## Java

```Java
class Solution {
    // 解法一：位图
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0) {
            return 0;
        }
        // 使用一个位图数组来标记字符是否出现过
        boolean[] bitSet = new boolean[256];
        int result = 0;
        int left = 0, right = 0;
        while (left < s.length()) {
            // 如果右侧字符对应的bitSet被标记为true，说明此字符在X位置重复，需要左侧���前移动，直到将X标记为false
            if (bitSet[s.charAt(right)]) {
                bitSet[s.charAt(left)] = false;
                left++;
            } else {
                bitSet[s.charAt(right)] = true;
                right++;
            }
            if (result < right - left) {
                result = right - left;
            }
            // 如果左侧加上结果大于等于字符串长度，或者右侧超过字符串长度，跳出循环
            if (left + result >= s.length() || right >= s.length()) {
                break;
            }
        }
        return result;
    }
}
class Solution {
// 解法二：滑动窗口
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0) {
            return 0;
        }
        int[] freq = new int[127];
        int result = 0, left = 0, right = -1;
        while (left < s.length()) {
            if (right + 1 < s.length() && freq[s.charAt(right + 1)] == 0) {
                freq[s.charAt(right + 1)]++;
                right++;
            } else {
                freq[s.charAt(left)]--;
                left++;
            }
            result = Math.max(result, right - left + 1);
        }
        return result;
    }
}
class Solution {
 // 解法三：滑动窗口-哈希桶
    public int lengthOfLongestSubstring(String s) {
        int right = 0, left = 0, res = 0;
        Map<Character, Integer> indexes = new HashMap<>();
        while (left < s.length()) {
            if (indexes.containsKey(s.charAt(left)) && indexes.get(s.charAt(left)) >= right) {
                right = indexes.get(s.charAt(left)) + 1;
            }
            indexes.put(s.charAt(left), left);
            left++;
            res = Math.max(res, left - right);
        }
        return res;
    }
}
```

## Cpp

```Cpp
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    // 解法一：位图
    int lengthOfLongestSubstring(string s) {
        if (s.length() == 0) {
            return 0;
        }

        // 使用一个位图数组来标记字符是否出现过
        bool bitSet[256] = {false};
        int result = 0;
        int left = 0, right = 0;

        while (left < s.length()) {
            // 如果右侧字符对应的bitSet被标记为true，说明此字符在X位置重复，需要左侧向前移动，直到将X标记为false
            if (bitSet[s[right]]) {
                bitSet[s[left]] = false;
                left++;
            } else {
                bitSet[s[right]] = true;
                right++;
            }

            if (result < right - left) {
                result = right - left;
            }

            // 如果左侧加上结果大于等于字符串长度，或者右侧超过字符串长度，跳出循环
            if (left + result >= s.length() || right >= s.length()) {
                break;
            }
        }

        return result;
    }
};

#include <unordered_map>
#include <algorithm>

class Solution {
public:
// 解法二：滑动窗口
    int lengthOfLongestSubstring(string s) {
        if (s.length() == 0) {
            return 0;
        }

        int freq[127] = {0};
        int result = 0, left = 0, right = -1;

        while (left < s.length()) {
            if (right + 1 < s.length() && freq[s[right + 1]] == 0) {
                freq[s[right + 1]]++;
                right++;
            } else {
                freq[s[left]]--;
                left++;
            }

            result = max(result, right - left + 1);
        }

        return result;
    }
};

#include <unordered_map>
#include <algorithm>

class Solution {
public:
  // 解法三：滑动窗口-哈希桶
    int lengthOfLongestSubstring(string s) {
        int right = 0, left = 0, res = 0;
        unordered_map<char, int> indexes;

        while (left < s.length()) {
            if (indexes.count(s[left]) && indexes[s[left]] >= right) {
                right = indexes[s[left]] + 1;
            }

            indexes[s[left]] = left;
            left++;
            res = max(res, left - right);
        }

        return res;
    }
};
```
四个版本解法所需的基础知识:

**Go**
- Map:
  - 知道内置map的声明方式,及使用make初始化
  - 熟练通过map[key] = val方式设置键值对
  - 理解遍历需要通过range迭代map
- 数组:
  - 完全掌握数组的定义、初始化、读取、修改等操作
  - 注意数组不能负索引,要避免越界访问
- Bitmap:
  - 掌握基于数组实现位图,通过索引设置和读取不同bit
  - 需要掌握位运算在位图中的应用
- 滑动窗口:
  - 理解滑动窗口模板,维护左右指针确定窗口范围
  - 在窗口内需要实现问题的具体逻辑

**Python**
- 字典:
  - 完全掌握字典的初始化、添加、删除、修改键值对
  - 知道in操作可以检查键是否存在
  - 需要掌握遍历字典的items()和keys()方法
- 列表:
  - 熟练列表的定义、索引、切片、遍历等操作
  - 知道append、insert、pop、remove等修改列表的方法
  - 注意索引不能为负,避免索引越界错误
- 位图:
  - 掌握基于列表实现位图,通过索引设置和获取不同bit
  - 需要熟练使用按位与或非来判断位是否置位
- 滑动窗口:
  - 理解模板,使用左右指针维护一个滑动窗口
  - 在窗口范围内实现问题的具体逻辑

**Java**
- HashMap:
  - 了解HashMap的put()方法可以添加键值对,get()方法可以获取键对应的值
  - 知道containsKey()可以检查键是否存在,containsValue()检查值是否存在
  - 需要掌握遍历HashMap的两种方式:使用keySet()或者entrySet()
- 位图:
  - 掌握使用boolean类型的数组可以作为位图,通过索引设置和读取不同位
  - 需要熟练位图的与或非逻辑运算,用于判断一个位是否被设置
- 数组:
  - 完全掌握数组的声明、初始化、读取、修改操作
  - 知道数组边界,避免出现索引越界的异常情况
- 滑动窗口:
  - 掌握滑动窗口的模板,需要维护左右边界指针
  - 理解右指针用于扩大窗口,左指针用于缩小窗口
  - 需要在滑动窗口内完成求解问题的相关逻辑

**C++**
- unordered_map:
  - 知道unordered_map的基本语法,使用[]或者insert()添加元素
  - 了解find()、count()等查询和统计方法
  - 掌握使用迭代器遍历unordered_map
- bitset:
  - 完全掌握bitset的定义方法,以及set(),reset(),flip()等修改位的方法
  - 需要熟练使用[]方式读取位图中的一个位
  - 理解任意位运算,以及与运算判断一个位是否被设置
- 数组:
  - 完全掌握数组的定义、初始化、读取、遍历等各种操作
  - 注意数组访问需要检查边界,避免越界访问异常
- 滑动窗口:
  - 掌握模板,维护左右指针实现窗口的扩大和缩小
  - 需要在滑动窗口逻辑内完成问题的求解


