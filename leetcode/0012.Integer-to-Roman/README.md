# [12. Integer to Roman](https://leetcode.com/problems/integer-to-roman/)

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

For example,`2`is written as`II`in Roman numeral, just two one's added together.`12`is written as`XII`, which is
simply`X + II`. The number`27`is written as`XXVII`, which is`XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not`IIII`.
Instead, the number four is written as`IV`. Because the one is before the five we subtract it making four. The same
principle applies to the number nine, which is written as`IX`. There are six instances where subtraction is used:

- `I`can be placed before`V`(5) and`X`(10) to make 4 and 9.
- `X`can be placed before`L`(50) and`C`(100) to make 40 and 90.
- `C`can be placed before`D`(500) and`M`(1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.

**Example 1:**

```
Input: num = 3
Output: "III"
```

**Example 2:**

```
Input: num = 4
Output: "IV"
```

**Example 3:**

```
Input: num = 9
Output: "IX"
```

**Example 4:**

```
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
```

**Example 5:**

```
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

**Constraints:**

- `1 <= num <= 3999`

## 题目大意

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数
5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

- I 可以放在 V(5) 和 X(10) 的左边，来表示 4 和 9。
- X 可以放在 L(50) 和 C(100) 的左边，来表示 40 和 90。
- C 可以放在 D(500) 和 M(1000) 的左边，来表示 400 和 900。

给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

## 解题思路

- 依照题意，优先选择大的数字，解题思路采用贪心算法。将 1-3999 范围内的罗马数字从大到小放在数组中，从头选择到尾，即可把整数转成罗马数字。

**Go语言版本:**
1. 定义整型数组values和字符串数组symbols,包含罗马数字的所有组合
2. 初始化结果字符串res为空,索引i为0
3. 使用for循环,当num不为0时循环
4. 在循环内使用if判断,如果当前values中的值大于num,则i递增跳过
5. 从num中减去当前values中的值
6. 将对应的symbols中的字符串连接到res
7. 最后返回res字符串作为结果

**Python语言版本:**
1. 定义值列表values和符号列表symbols,包含罗马数字的所有组合
2. 初始化结果字符串res为空,索引i为0
3. 使用while循环,当num大于0时循环
4. 在循环内使用if判断,如果当前values中的值大于num,则i递增跳过
5. 从num中减去当前values中的值 
6. 将对应的symbols中的字符串连接到res
7. 最后返回res字符串作为结果

**Java语言版本:**
1. 定义整型数组values和字符串数组symbols,包含罗马数字的所有组合
2. 初始化结果字符串res为空,索引i为0
3. 使用while循环,当num大于0时循环
4. 在循环内使用if判断,如果当前values中的值大于num,则i递增跳过
5. 从num中减去当前values中的值
6. 将对应的symbols中的字符串连接到res
7. 最后返回res字符串作为结果

**C++语言版本:**
1. 定义整型数组values和字符串数组symbols,包含罗马数字的所有组合
2. 初始化结果字符串res为空,索引i为0
3. 使用while循环,当num大于0时循环
4. 在循环内使用if判断,如果当前values中的值大于num,则i递增跳过
5. 从num中减去当前values中的值
6. 将对应的symbols中的字符串连接到res
7. 最后返回res字符串作为结果

## 代码

## Go
```Go
func intToRoman(num int) string {
    values := []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1} // 定义一个整数数组,包含罗马数字的基本值
    symbols := []string{"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"} // 定义一个字符串数组,包含对应的罗马符号
    res, i := "", 0 // res为返回的罗马数字字符串,i为values和symbols的索引
    for num != 0 { // 当num不为0时循环
        for values[i] > num { // 如果当前values中的值大于num
            i++ // i增加1
        }
        num -= values[i] // 从num中减去当前values中的值
        res += symbols[i] // 在res中加上对应的罗马符号
    }
    return res // 返回组成的罗马数字字符串
}
```
## Python
```Python
class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1] # 定义值列表
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"] # 符号列表
        res = ""
        i = 0 # 结果字符串和索引
        while num > 0: # 当num大于0时循环
            while values[i] > num: # 如果当前值大于num
                i += 1 # 索引加1
            num -= values[i] # 从num中减去当前值
            res += symbols[i] # 在结果中添加对应的符号
        return res # 返回组成的罗马数字字符串
```
## Java
```Java
class Solution {
    public String intToRoman(int num) {
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}; // 定义整数数组,包含罗马数字的基本值
        String[] symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"}; // 定义字符串数组,包含罗马符号
        String res = "";
        int i = 0; // 结果字符串res,以及values和symbols的索引i
        while(num > 0) { // 当num大于0时循环
            while(values[i] > num) { // 如果当前values中的值大于num
                i++; // i增加1
            }
            num -= values[i]; // 从num中减去当前values中的值
            res += symbols[i]; // 在res中添加对应的罗马符号
        }
        return res; // 返回组成的罗马数字字符串
    }
}
```
## Cpp
```Cpp
class Solution {
public:
    string intToRoman(int num) {
        int values[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}; // 定义整数数组,包含罗马数字的基本值
        string symbols[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"}; // 定义字符串数组,包含罗马符号
        string res;
        int i = 0; // 结果字符串res,以及values和symbols的索引i
        while(num > 0) { // 当num大于0时循环
            while(values[i] > num) { // 如果当前values中的值大于num
                i++; // i增加1
            }
            num -= values[i]; // 从num中减去当前values中的值
            res += symbols[i]; // 在res中添加对应的罗马符号
        }
        return res; // 返回组成的罗马数字字符串
    }
};
```
**Go语言版本:**
- int类型:Go语言中的整型类型,用于表示整数。
- string类型:Go语言中的字符串类型。
- []int和`[]string`:定义整型数组和字符串数组。
- for循环:Go语言的基本循环结构。
- if条件判断:Go语言的条件判断结构。
- +=运算符:字符串或整数的连接赋值运算符。
- 函数定义和返回值:Go语言中定义函数的格式和返回值方式。

**Python语言版本:**
- int类型:Python中的整型类型。
- str类型:Python中的字符串类型。
- list:Python中的列表,相当于数组。
- while循环:Python的基本循环结构。
- if条件判断:Python的条件判断结构。
- +=运算符:字符串的连接赋值运算符。
- def定义函数,return返回值:Python中定义函数和返回值的方式。

**Java语言版本:**
- int类型:Java中的整型。
- String类型:Java中的字符串类。
- int[]和`String[]`:定义整型数组和字符串数组。
- while循环:Java的循环结构。
- if条件判断:Java的条件判断结构。
- +=运算符:字符串的连接赋值运算符。
- 方法定义,return返回值:Java中定义方法和返回值的方式。

**C++语言版本:**
- int类型:C++中的整型。
- string类型:C++中的字符串类。
- int[]和`string[]`:定义整型数组和字符串数组。
- while循环:C++的循环结构。
- if条件判断:C++的条件判断结构。
- +=运算符:字符串的连接赋值运算符。
- 函数定义,return返回值:C++中定义函数和返回值的方式。