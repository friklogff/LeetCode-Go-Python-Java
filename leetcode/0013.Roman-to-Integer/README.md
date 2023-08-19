# [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

## 题目

Roman numerals are represented by seven different symbols:`I`,`V`,`X`,`L`,`C`,`D`and`M`.

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, two is written as`II`in Roman numeral, just two one's added together. Twelve is written as,`XII`, which is
simply`X`+`II`. The number twenty seven is written as`XXVII`, which is`XX`+`V`+`II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not`IIII`.
Instead, the number four is written as`IV`. Because the one is before the five we subtract it making four. The same
principle applies to the number nine, which is written as`IX`. There are six instances where subtraction is used:

- `I`can be placed before`V`(5) and`X`(10) to make 4 and 9.
- `X`can be placed before`L`(50) and`C`(100) to make 40 and 90.
- `C`can be placed before`D`(500) and`M`(1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

**Example 1**:

```
Input: "III"
Output: 3
```

**Example 2**:

```
Input: "IV"
Output: 4
```

**Example 3**:

```
Input: "IX"
Output: 9
```

**Example 4**:

```
Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
```

**Example 5**:

```
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

## 题目大意

罗马数字包含以下七种字符:I， V， X， L，C，D 和 M。

```go

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

```

例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做 XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数
5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

- I 可以放在 V(5) 和 X(10) 的左边，来表示 4 和 9。
- X 可以放在 L(50) 和 C(100) 的左边，来表示 40 和 90。- C 可以放在 D(500) 和 M(1000) 的左边，来表示 400 和 900。

给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

## 解题思路

- 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
- 简单题。按照题目中罗马数字的字符数值，计算出对应罗马数字的十进制数即可。

**Go语言版本:**
1. 建立字符到整数的map映射
2. 判断字符串是否为空,为空返回0
3. 定义num, lastNum, total变量初始化为0
4. 从后向前遍历字符串
5. 获取当前字符,在map中找到对应数值
6. 判断当前值与上一个值大小关系:如果小于上一个值,则减去当前值;否则加上当前值
7. 更新lastNum为当前值
8. 遍历结束返回total结果

**Python语言版本:**
1. 建立字符到整数的dict字典
2. 判断字符串是否为空,为空返回0
3. 定义num, last_num, total变量初始化为0
4. 倒序遍历字符串,range从len-1到0
5. 获取当前字符,在dict中找到对应数值
6. 判断当前值与上一个值大小关系:如果小于上一个值,则减去当前值;否则加上当前值
7. 更新last_num为当前值
8. 遍历结束返回total结果

**Java语言版本:**
1. 建立字符到整数的Map映射
2. 判断字符串是否为空,为空返回0
3. 定义num, lastNum, total变量初始化为0 
4. 倒序遍历字符串,i--实现
5. 获取当前字符,在Map中找到对应数值
6. 判断当前值与上一个值大小关系:如果小于上一个值,则减去当前值;否则加上当前值
7. 更新lastNum为当前值
8. 遍历结束返回total结果

**C++语言版本:**
1. 建立字符到整数的map映射
2. 判断字符串是否为空,为空返回0
3. 定义num, lastNum, total变量初始化为0
4. 倒序遍历字符串,i--实现
5. 获取当前字符,在map中找到对应数值
6. 判断当前值与上一个值大小关系:如果小于上一个值,则减去当前值;否则加上当前值 
7. 更新lastNum为当前值
8. 遍历结束返回total结果
## 代码
## Go
```Go
// 定义一个map,映射罗马数字字符到整数值
var roman = map[string]int{ 
    "I": 1,
    "V": 5, 
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}
// 将罗马数字字符串转换为整数的函数
func romanToInt(s string) int {
    // 如果传入空字符串,直接返回0
    if s == "" { 
       return 0
    }
    // 定义num为当前数字值,lastint为上一个数字值,total为结果
    num, lastint, total := 0, 0, 0
    // 从字符串末尾向前遍历
    for i := 0; i < len(s); i++ {
       // 获取当前字符 
       char := s[len(s)-(i+1) : len(s)-i]
       // 在map中找当前字符对应的数字值 
       num = roman[char]
       // 如果当前数字小于上一个数字,则减去当前数字
       if num < lastint {
          total = total - num
       } else {
           // 否则加上当前数字
          total = total + num
       }
       // 更新lastint为当前数字值
       lastint = num
    }
    // 返回最终结果
    return total
}
```
## Python
```Python
class Solution:
    def romanToInt(self, s: str) -> int:
        
        # 定义一个字典,映射罗马数字字符到整数值
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        # 如果传入空字符串,直接返回0
        if not s:
            return 0
        
        # 定义当前数字、上一个数字和结果变量        
        num, last_num, total = 0, 0, 0
        
        # 从字符串末尾向前遍历
        for i in range(len(s)-1, -1, -1):
            
            # 获取当前字符
            char = s[i]
            
            # 在字典中找当前字符对应的数字
            num = roman[char]
            
            # 如果当前数字小于上一个数字,则减去当前数字
            if num < last_num:
                total -= num
            else:
                # 否则加上当前数字
                total += num
                
            # 更新last_num为当前数字
            last_num = num
        
        return total
        

```
## Java
```Java
class Solution {
    public int romanToInt(String s) {
        // 定义一个Map,映射罗马数字字符到整数值
        Map<Character, Integer> roman = new HashMap<>();
        roman.put('I', 1);
        roman.put('V', 5);
        roman.put('X', 10);
        roman.put('L', 50);
        roman.put('C', 100);
        roman.put('D', 500);
        roman.put('M', 1000);

        // 如果传入空字符串,直接返回0
        if (s.isEmpty()) {
            return 0;
        }
        
        // 初始化lastNum为0
        int num, lastNum = 0, total = 0;

        // 从字符串末尾向前遍历
        for (int i = s.length() - 1; i >= 0; i--) {

            // 获取当前字符
            char c = s.charAt(i);

            // 在map中找当前字符对应的数字
            num = roman.get(c);

            // 如果当前数字小于上一个数字,则减去当前数字
            if (num < lastNum) {
                total -= num; 
            } else {
                // 否则加上当前数字
                total += num;
            }

            // 更新lastNum为当前数字
            lastNum = num;
        }
        
        // 返回最终结果
        return total;
    }
}
```
## Cpp
```Cpp
class Solution {
public:
    int romanToInt(string s) {
        
        // 定义一个map,映射罗马数字字符到整数值
        unordered_map<char, int> roman = {{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, 
                                         {'C', 100}, {'D', 500}, {'M', 1000}}; 
        
        // 如果传入空字符串,直接返回0
        if (s.empty()) {
            return 0; 
        }
        
        // 定义当前数字、上一个数字和结果变量
        int num, lastNum = 0, total = 0;
        
        // 从字符串末尾向前遍历
        for (int i = s.length() - 1; i >= 0; i--) {
            
            // 获取当前字符
            char c = s[i];
            
            // 在map中找当前字符对应的数字值
            num = roman[c];
            
            // 如果当前数字小于上一个数字,则减去当前数字
            if (num < lastNum) {
                total -= num;
            } else {
                // 否则加上当前数字
                total += num;
            }
            
            // 更新lastNum为当前数字
            lastNum = num;
        }
        
        return total;
    }
};

```
**Go语言版本:**
- map:Go语言中map是一种键值对的集合,可以用来建立字符和整数之间的映射关系。
- len函数:可以获取字符串的长度。
- 切片:s[start:end]可以提取字符串的一段子串。
- if条件判断和else分支。
- 定义多个变量:num, lastint, total := 0, 0, 0。
- for循环遍历字符串。
-字符串拼接:char := s[len(s)-(i+1) : len(s)-i]。

**Python语言版本:**
- 字典dict:Python中的字典可以建立字符和整数之间的映射关系。
- len函数:可以获取字符串的长度。
-下标索引:s[i] 获取字符串中的字符。
- if条件判断和else分支。
- 定义多个变量:num, last_num, total = 0, 0, 0。
- for循环遍历字符串,range函数生成索引。
- 减一运算:range(len(s)-1, -1, -1)。

**Java语言版本:**
- Map集合:可以建立键值对映射关系。
- isEmpty判断字符串是否为空。
- charAt取字符串指定位置的字符。
- HashMap创建Map集合。
- if条件判断和else分支。
- for循环遍历字符串,i--实现倒序。
- length获取字符串长度。

**C++语言版本:**
- unordered_map映射集合,可以建立字符和整数的映射。
- empty判断字符串是否为空。 
- []访问向量元素。
- if条件判断和else分支。
- 定义多个变量:int num, lastNum = 0, total = 0。
- for循环遍历字符串,i--实现倒序。
- length函数获取字符串长度。