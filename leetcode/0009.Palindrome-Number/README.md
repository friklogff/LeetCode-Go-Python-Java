# [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)

## 题目

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

**Example 1**:

```
Input: 121
Output: true
```

**Example 2**:

```
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

**Example 3**:

```
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

**Follow up**:

Coud you solve it without converting the integer to a string?

## 题目大意

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

## 解题思路

- 判断一个整数是不是回文数。
- 简单题。注意会有负数的情况，负数，个位数，10 都不是回文数。其他的整数再按照回文的规则判断。
Go语言版本:
1. 用if判断负数和末尾为0的情况,直接返回false
2. 用for循环不断对x取余,获取每个数字存入切片arr
3. 判断切片长度,从两端向中间遍历,判断是否相等
4. 如果不相等直接返回false,遍历结束返回true

Python语言版本:
1. 用if判断负数情况,直接返回false
2. 将整数转换为字符串s,方便后续遍历
3. 求字符串长度,从两端向中间遍历字符串
4. 判断字符是否相等,不等返回false,遍历结束返回true

Java语言版本:
1. 方法一:和Python类似,将整数转换为字符串s
2. 判断字符串长度,从两端向中间遍历,判断字符是否相等
3. 方法二:通过整除和取余直接操作整数
4. 用while循环逐位对比,判断是否回文

C++语言版本:
1. 用if判断负数情况,直接返回false
2. 用while循环对x取余,得到每位数字存入vector
3. 判断vector长度,从两端向中间遍历,判断是否相等
4. 也可以转换为字符串进行操作,思路同上
5. 如果不相等直接返回false,遍历结束返回true
## 代码

## Go
```Go
// 解法一
func isPalindrome(x int) bool {
    if x < 0 { // 如果x是负数,返回false
       return false
    }
    if x == 0 { // 如果x是0,返回true
       return true
    }
    if x%10 == 0 { // 如果x能被10整除,返回false
       return false
    }
    arr := make([]int, 0, 32) // 创建一个空切片arr
    for x > 0 { // 当x大于0时循环
       arr = append(arr, x%10) // 将x对10取余作为个位数存入arr
       x = x / 10 // x整除10
    }
    sz := len(arr) // 获得arr的长度
    for i, j := 0, sz-1; i <= j; i, j = i+1, j-1 { // 从头尾两边向中间遍历arr
       if arr[i] != arr[j] { // 如果两边的数字不相等
          return false // 返回false
       }
    }
    return true // 遍历完成,说明是回文,返回true
}
// 解法二 数字转字符串
func isPalindrome(x int) bool {
    if x < 0 { // 如果x是负数,返回false
       return false
    }
    if x < 10 { // 单位数都是回文,返回true
       return true
    }
    s := strconv.Itoa(x) // 将x转为字符串
    length := len(s) // 获得字符串长度
    for i := 0; i <= length/2; i++ { // 从两头向中间遍历字符串
       if s[i] != s[length-1-i] { // 如果两边的字符不相等
          return false // 返回false
       }
    }
    return true // 遍历完成,说明是回文,返回true
} 
```
## Python
```Python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 方法一
        if x < 0:
            return False
        if x == 0:
            return True
        if x % 10 == 0:
            return False
        arr = []
        while x > 0:
            arr.append(x % 10)
            x //= 10
        n = len(arr)
        for i in range(n // 2):
            if arr[i] != arr[n - 1 - i]:
                return False
        return True
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 方法二
        if x < 0:
            return False
        if x < 10:
            return True
        s = str(x)
        n = len(s)
        for i in range(n // 2):
            if s[i] != s[n - 1 - i]:
                return False
        return True 
```
## Java
```Java
class Solution {    
  // 解法一:整数转换为字符串
  public boolean isPalindrome(int x) {
    if (x < 0) {
      return false;
    }
    if (x < 10) {
      return true;
    }
    String s = String.valueOf(x);
    int length = s.length();
    for (int i = 0; i <= length / 2; i++) {
      if (s.charAt(i) != s.charAt(length - 1 - i)) {
        return false;
      }
    }
    return true;
  }

}

class Solution {
  // 解法二:直接对整数操作
  public boolean isPalindrome(int x) {
    if (x < 0) {
      return false;
    }
    if (x == 0) {
      return true;
    }
    int div = 1;
    while (x / div >= 10) {
      div *= 10;
    }
    while (x != 0) {
      int left = x / div;
      int right = x % 10;
      if (left != right) {
        return false;
      }
      x = (x % div) / 10;
      div /= 100;
    }
    return true;
  }
}
```
## Cpp
```Cpp
class Solution {
public:
    bool isPalindrome(int x) {
        // 方法一
        if(x < 0) return false;
        if(x == 0) return true;
        if(x % 10 == 0) return false;
        vector<int> arr;
        while(x > 0) {
            arr.push_back(x % 10);
            x /= 10;
        }
        int n = arr.size();
        for(int i = 0; i < n / 2; i++) {
            if(arr[i] != arr[n - 1 - i])
                return false;
        }
        return true;

    }
}; 
class Solution {
public:
    bool isPalindrome(int x) {
        // 方法二
        if(x < 0) return false;
        if(x < 10) return true;
        string s = to_string(x);
        int n = s.size();
        for(int i = 0; i < n / 2; i++) {
            if(s[i] != s[n - 1 - i])
                return false;
        }
        return true;

    }
}; 

```

每个语言版本所需要掌握的基础知识:

Go语言版本:
1. if条件判断,根据题目要求判断负数和0的情况
2. 切片slice的定义和append添加元素
3. for循环遍历切片
4. len()求切片长度
5. %取余运算符获取每位数字
6. /=运算符整除并赋值

Python语言版本:
1. if条件判断负数和0
2. 将整数转换为字符串str()
3. len()求字符串长度
4. 字符串遍历和索引访问s[i]
5. //运算符整除

Java语言版本:
1. if条件判断负数和0
2. String类及其方法charAt()
3. 字符串遍历和长度len
4. 整除运算符/和取余运算符%
5. while循环

C++语言版本:
1. if条件判断负数和0
2. vector容器添加push_back和遍历
3. size()求vector长度
4. 字符串转换to_string和遍历
5. %取余运算符获取每位数字
6. /=运算符整除并赋值
