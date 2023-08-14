# [8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)


## 题目

Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer (similar to C/C++'s `atoi` function).

The algorithm for `myAtoi(string s)` is as follows:

1. Read in and ignore any leading whitespace.
2. Check if the next character (if not already at the end of the string) is `'-'` or `'+'`. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
3. Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.
4. Convert these digits into an integer (i.e. `"123" -> 123`, `"0032" -> 32`). If no digits were read, then the integer is `0`. Change the sign as necessary (from step 2).
5. If the integer is out of the 32-bit signed integer range `[-231, 231 - 1]`, then clamp the integer so that it remains in the range. Specifically, integers less than `231` should be clamped to `231`, and integers greater than `231 - 1` should be clamped to `231 - 1`.
6. Return the integer as the final result.

**Note:**

- Only the space character `' '` is considered a whitespace character.
- **Do not ignore** any characters other than the leading whitespace or the rest of the string after the digits.

**Example 1:**

```
Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.

```

**Example 2:**

```
Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.

```

**Example 3:**

```
Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-231, 231 - 1], the final result is 4193.

```

**Example 4:**

```
Input: s = "words and 987"
Output: 0
Explanation:
Step 1: "words and 987" (no characters read because there is no leading whitespace)
         ^
Step 2: "words and 987" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "words and 987" (reading stops immediately because there is a non-digit 'w')
         ^
The parsed integer is 0 because no digits were read.
Since 0 is in the range [-231, 231 - 1], the final result is 0.

```

**Example 5:**

```
Input: s = "-91283472332"
Output: -2147483648
Explanation:
Step 1: "-91283472332" (no characters read because there is no leading whitespace)
         ^
Step 2: "-91283472332" ('-' is read, so the result should be negative)
          ^
Step 3: "-91283472332" ("91283472332" is read in)
                     ^
The parsed integer is -91283472332.
Since -91283472332 is less than the lower bound of the range [-231, 231 - 1], the final result is clamped to -231 = -2147483648.
```

**Constraints:**

- `0 <= s.length <= 200`
- `s` consists of English letters (lower-case and upper-case), digits (`0-9`), `' '`, `'+'`

## 题目大意

请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。

函数 myAtoi(string s) 的算法如下：

- 读入字符串并丢弃无用的前导空格
- 检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
- 读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
- 将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
- 如果整数数超过 32 位有符号整数范围 [−231,  231 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231 的整数应该被固定为 −231 ，大于 231 − 1 的整数应该被固定为 231 − 1 。
- 返回整数作为最终结果。

注意：

- 本题中的空白字符只包括空格字符 ' ' 。
- 除前导空格或数字后的其余字符串外，请勿忽略 任何其他字符。

## 解题思路

- 这题是简单题。题目要求实现类似 `C++` 中 `atoi` 函数的功能。这个函数功能是将字符串类型的数字转成 `int` 类型数字。先去除字符串中的前导空格，并判断记录数字的符号。数字需要去掉前导 `0` 。最后将数字转换成数字类型，判断是否超过 `int` 类型的上限 `[-2^31, 2^31 - 1]`，如果超过上限，需要输出边界，即 `-2^31`，或者 `2^31 - 1`。


每种语言版本的解题思路:

**Go语言**
1. strings.TrimSpace()删除前导空格
2. strings.Split()分割字符串成数字字符数组
3. for range迭代字符数组
4. strconv.Atoi()逐个字符转整数
5. 将整数append到数组中
6. 切片运算取前100个数的平方和

**Python**
1. isspace()判断空格,isdigit()判断数字字符
2. int()强转字符为整数,try-except捕获溢出
3. append()将数字添加到数组
4. itertools.islice()取前100个元素 
5. sum()求和,pow()求平方

**Java**
1. replaceAll()替换空格,split()分割字符串
2. Character.isDigit()判断数字字符 
3. Integer.parseInt()解析成整数
4. ArrayList存储整数,subList()取前100个
5. Stream流式处理,mapToInt().sum()求和

**C++** 
1. isspace()判断空格,isdigit()判断数字
2. stoi()将字符转整数
3. vector存储数字,resize()调整大小
4. accumulate求和,transform求平方 
5. 取vector前100个元素进行处理
## 代码
## Go
```Go
func myAtoi(s string) int {
    // 定义最大整数值,是否允许符号,是否允许空白,符号,数字数组
    maxInt, signAllowed, whitespaceAllowed, sign, digits := int64(2<<30), true, true, 1, []int{}
    for _, c := range s {
      // 如果是空格且允许空白,继续
      if c == ' ' && whitespaceAllowed {
         continue
      }
      // 如果允许符号
      if signAllowed {
         // 如果是加号,不再允许符号和空白
         if c == '+' {
            signAllowed = false
            whitespaceAllowed = false
            continue
         } else if c == '-' { // 如果是减号,置符号为-1
            sign = -1
            signAllowed = false
            whitespaceAllowed = false
            continue
         }
      }
      // 如果不是数字,跳出循环
      if c < '0' || c > '9' {
         break
      }
      // 不再允许符号和空白
      whitespaceAllowed, signAllowed = false, false
      // 将字符转换为整数并加入数字数组 
      digits = append(digits, int(c-48))
    }
    // 定义返回值相关变量
    var num, place int64
    place, num = 1, 0
    // 记录最后一个前导0的索引
    lastLeading0Index := -1
    // 找到最后一个前导0
    for i, d := range digits {
       if d == 0 {
          lastLeading0Index = i
       } else {
          break
       }
    }
    // 如果有前导0,去掉前导0
    if lastLeading0Index > -1 {
       digits = digits[lastLeading0Index+1:]
    }
    // 定义正负数最大返回值
    var rtnMax int64
    if sign > 0 {
       rtnMax = maxInt - 1
    } else {
       rtnMax = maxInt
    }
    // 计算数字总位数
    digitsCount := len(digits)
    // 从低位到高位计算数值
    for i := digitsCount - 1; i >= 0; i-- {
       num += int64(digits[i]) * place
       place *= 10
       // 如果超出范围,返回最大值
       if digitsCount-i > 10 || num > rtnMax {
          return int(int64(sign) * rtnMax)
       }
    }
    // 加上符号
    num *= int64(sign)
    return int(num)
}
```
## Python
```Python
class Solution:
    def myAtoi(self, s: str) -> int:
        max_int = 2**31 - 1
        min_int = -2**31
        sign = 1 # 符号默认为正
        result = 0 # 结果初始化为0
        index = 0
        n = len(s)
        # 去掉前导空格
        while index < n and s[index] == ' ':
            index += 1
        # 判断符号   
        if index < n and s[index] == '+':
            sign = 1
            index += 1
        elif index < n and s[index] == '-':
            sign = -1
            index += 1
        # 将后续数字字符转换为整数累加
        while index < n and s[index].isdigit():
            digit = int(s[index])
            result = result * 10 + digit
            index += 1
            # 每次处理一个数字后检查是否越界
            if result * sign <= min_int:
                return min_int
            if result * sign >= max_int:
                return max_int
        return sign * result
```
## Java
```Java
class Solution {
    public int myAtoi(String s) {
        // 定义变量
        long maxInt = Integer.MAX_VALUE; 
        long minInt = Integer.MIN_VALUE;
        boolean signAllowed = true;
        boolean whitespaceAllowed = true;
        int sign = 1;
        List<Integer> digits = new ArrayList<>();

        for(char c : s.toCharArray()) {
            // 处理空格
            if(c == ' ' && whitespaceAllowed) continue;

            // 处理正负号
            if(signAllowed) {
                if(c == '+') {
                    signAllowed = false;
                    whitespaceAllowed = false;
                    continue;
                } else if(c == '-') {
                    sign = -1;
                    signAllowed = false;
                    whitespaceAllowed = false;
                    continue;
                }
            }

            // 非数字则跳出
            if(c < '0' || c > '9') break;

            // 记录数字
            signAllowed = false;
            whitespaceAllowed = false;
            digits.add(c - '0');
        }

        // 处理前导0
        int lastLeading0 = -1;
        for(int i = 0; i < digits.size(); i++) {
            if(digits.get(i) == 0) lastLeading0 = i;
            else break;
        }
        if(lastLeading0 > -1) {
            digits = digits.subList(lastLeading0+1, digits.size());
        }

        // 计算数值
        long num = 0;
        for(int i = digits.size()-1; i >= 0; i--) {
            num += digits.get(i) * Math.pow(10, digits.size()-1-i);
            
            // 处理越界
            if(sign == 1 && num > maxInt) return (int)maxInt;
            if(sign == -1 && -num < minInt) return (int)minInt;
        }
        
        return (int)(sign * num);
    }
}

```
## Cpp
```Cpp
#include <iostream>
#include <string>
#include <limits>

class Solution {
public:
    int myAtoi(std::string s) {
        int i = 0;
        int sign = 1;
        int result = 0;

        if (s.empty()) {
            return 0;
        }

        // 跳过空格
        while (i < s.size() && s[i] == ' ') {
            i++;
        }

        // 处理正负号
        if (i < s.size() && (s[i] == '+' || s[i] == '-')) {
            sign = (s[i] == '-') ? -1 : 1;
            i++;
        }

        // 转换数字并检查溢出
        while (i < s.size() && isdigit(s[i])) {
            int digit = s[i] - '0';
            if (result > (std::numeric_limits<int>::max() - digit) / 10) {
                return (sign == 1) ? std::numeric_limits<int>::max() : std::numeric_limits<int>::min();
            }
            result = result * 10 + digit;
            i++;
        }

        return result * sign;
    }
};
```
每个语言版本的基础知识点:

**Go语言**
- strings包:strings.TrimSpace()可以删除字符串前导空格,strings.Contains()判断子串
- strconv包:strconv.Atoi()字符串转整数,strconv.Itoa()整数转字符串
- 数组和切片:数字存储在数组中,可以用append()添加,切片操作取子串
- for range遍历:可以直接遍历字符串,通过下标或者rune类型访问字符
- 类型转换:需要int和int64类型转换,用类型强转实现

**Python**
- str方法:isspace()判断空格,isdigit()判断数字等
- int强转:直接int()可以将字符串转整数
- try-except:可以用try-except捕获整数转换溢出异常
- 数学模块:提供pow()求幂等辅助方法

**Java**
- 包装类:Integer, Long等箱装类提供数值范围常量
- ArrayList:可以动态添加数字,subList()取子串
- Math类:提供求幂等数学函数
- 类型强转:需要处理int和long之间转换

**C++**
- 头文件:需要imits等定义数值边界
- isdigit()判断数字字符
- string处理:substr()取子串等
- 异常:可以用异常代替手动边界判断
- 类型转换:静态强转或stoi,to_string等函数
