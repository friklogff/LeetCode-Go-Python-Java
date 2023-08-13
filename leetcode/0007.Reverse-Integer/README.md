# [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/)


## 题目

Given a 32-bit signed integer, reverse digits of an integer.

**Example 1:**

    Input: 123
    Output: 321

**Example 2:**

    Input: -123
    Output: -321

**Example 3:**

    Input: 120
    Output: 21

**Note:**Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

## 题目大意

给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。注意:假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。



## 解题思路


- 这一题是简单题，要求反转 10 进制数。类似的题目有第 190 题。
- 这一题只需要注意一点，反转以后的数字要求在 [−2^31, 2^31 − 1]范围内，超过这个范围的数字都要输出 0 。
### Go 版本
1. 定义变量 tmp 来保存反转后的结果,初始化为 0
2. 使用 for 循环,当 x 不等于 0 时执行循环
3. 在循环内,通过 x 对 10 求余(x%10)获取末位数字,并将其乘以 10 加到 tmp 后面
4. 通过 x 整除 10(x/10)去掉 x 的末位数字
5. 循环直至 x 为 0
6. 判断 tmp 是否超出 int32 范围,如果是返回 0
7. 最后返回 tmp 作为结果
### Python 版本
1. 定义 result 变量,初始化为 0
2. 判断 x 是否为负数,是则将符号设为 -1,并将 x 转正
3. 使用 while 循环,当 x 不等于 0 时执行循环
4. 在循环内,获取 x 对 10 求余的末位数字,累加到 result 末尾
5. 将 x 整除 10 删除末位数字
6. 循环直至 x 为 0
7. 根据符号将 result 还原为负数
8. 判断 result 是否越界,是则返回 0
9. 返回 result
### Java 版本
1. 定义 result 变量,初始化为 0
2. 判断 x 是否为负数,是则将 x 转为正数
3. 使用 while 循环,当 x 不等于 0 时循环
4. 在循环内,获取 x 对 10 求余的末位数字,累加到 result 末尾
5. 将 x 整除 10 删除末位数字
6. 循环直至 x 为 0
7. 在循环中判断是否越界,是则返回 0
8. 如果为负数,将 result 变为负数
9. 返回 result
### C++版本
1. 定义 result 变量,初始化为 0
2. 判断 x 是否为负数,是则将 x 转为正数
3. 检查是否为最小值,是则直接返回 0
4. 使用 while 循环,当 x 不等于 0 时循环
5. 在循环内,获取 x 对 10 求余的末位数字,累加到 result 末尾
6. 将 x 整除 10 删除末位数字
7. 在循环中判断是否越界,是则返回 0
8. 如果为负数,将 result 变为负数
9. 返回 result

## Go
```Go
func reverse(x int) int {
    tmp := 0 // 定义一个临时变量tmp,初始化为0
    for x != 0 { // 当x不等于0时,进行循环
       tmp = tmp*10 + x%10 // 将x对10取余,加到tmp末尾,实现逆序
       x = x / 10 // x整除10,去掉末尾数字
    }
    if tmp > 1<<31-1 || tmp < -(1<<31) { // 检查tmp是否超出int范围
       return 0 // 如果超出范围,返回0
    }
    return tmp // 返回tmp
}

```
## Python
```Python
class Solution:
    def reverse(self, x: int) -> int:
        result = 0 # 结果初始化为0
        if x < 0: # 判断x是否为负数
            symbol = -1 # 如果x为负数,符号设为-1
            x = -x # 将x变正
        else:
            symbol = 1 # 否则符号为1
        while x != 0:
            result = result * 10 + x % 10 # 取x的末尾数字,加到result末尾
            x = x // 10 # x去掉末尾数字
        result = result * symbol # 恢复result的符号
        if result >= 2**31 or result < -2**31: # 判断是否越界
            return 0
        else:
            return result
```
## Java
```Java
class Solution {
    public int reverse(int x) {
        int result = 0; // 结果初始化为0
        boolean isNegative = x < 0; // 判断x是否为负数
        if(isNegative) {
            x = -x; // 如果为负数,将x变为正数
        }
        while(x != 0) {
            int pop = x % 10; // x对10取余,获取末位数字
            x /= 10; // x除以10,删除末位数字
            if (result > Integer.MAX_VALUE/10 || (result == Integer.MAX_VALUE / 10 && pop > 7)) {
                return 0; // 检查是否越上界
            }
            if (result < Integer.MIN_VALUE/10 || (result == Integer.MIN_VALUE / 10 && pop < -8)) {
                return 0; // 检查是否越下界
            }
            result = result * 10 + pop; // 结果乘10后加上末位数字
        }
        if(isNegative) {
            result = -result; // 如果为负数,结果取反
        }
        return result;
    }
}
```
## Cpp
```Cpp
class Solution {
public:
    int reverse(int x) {
        int result = 0; // 结果初始化为0
        bool isNegative = x < 0; // 判断是否为负数
        if (isNegative) {
            if (x == INT_MIN) { // 如果是最小值,取反会溢出,直接返回0
                return 0;
            }
            x = -x; // 负数取反使之为正数
        }
        while (x != 0) {
            int pop = x % 10; // 取余取得末尾数字
            x /= 10; // 移除末尾数字
            if (result > INT_MAX/10 || (result == INT_MAX/10 && pop > INT_MAX%10)) {
                return 0; // 检查越界
            }
            if (result < INT_MIN/10 || (result == INT_MIN/10 && pop < INT_MIN%10)) {
                return 0;
            }
            result = result * 10 + pop; // 组装结果
        }
        if (isNegative) {
            result = -result; // 恢复负号
        }
        return result;
    }
};
```
### Go 版本
Go语言基础知识:
- var 定义变量,可以初始化值
- for 循环
- if 条件判断
- % 取余运算
- / 除法运算
- 右移运算符 >> ,可以用于快速计算2的指数
- 返回值通过 return 关键字返回
### Python 版本
Python基础知识:
- result = 0 定义变量并初始化
- if/else 条件判断
- while 循环
- % 取余
- // 整数除法
- ** 幂运算符,可以计算2的指数
- return 直接返回值
### Java版本
Java基础知识:
- int result = 0 定义变量并初始化
- if/else 条件判断
- while 循环
- % 取余
- / 除法
- Math.pow(2, n) 计算2的指数
- return 返回值
### C++版本
C++基础知识:
- int result = 0 定义变量并初始化
- bool 类型判断真假
- if/else 条件判断
- while 循环
- % 取余运算
- / 除法
- pow(2, n) 计算2的指数
- return 返回值

此外,Java和C++版本要注意反转最小值时的溢出问题,需要特判。