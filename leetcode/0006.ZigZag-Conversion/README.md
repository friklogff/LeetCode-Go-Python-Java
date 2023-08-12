# [6. ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/)

## 题目

The string`"PAYPALISHIRING"`is written in a zigzag pattern on a given number of rows like this: (you may want to display
this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line:`"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows:

```
string convert(string s, int numRows);
```

**Example 1:**

```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

**Example 2:**

```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
```

**Example 3:**

```
Input: s = "A", numRows = 1
Output: "A"
```

**Constraints:**

- `1 <= s.length <= 1000`
- `s`consists of English letters (lower-case and upper-case),`','`and`'.'`.
- `1 <= numRows <= 1000`

## 题目大意

将一个给定字符串 `s` 根据给定的行数 `numRows` ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 `"PAYPALISHIRING"`行数为 3 时，排列如下：

```go
P   A   H   N
A P L S I I G
Y   I   R
```

之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如：`"PAHNAPLSIIGYIR"`。

请你实现这个将字符串进行指定行数变换的函数：

```go
string convert(string s, int numRows);
```

## 解题思路

- 这一题没有什么算法思想，考察的是对程序控制的能力。用 2 个变量保存方向，当垂直输出的行数达到了规定的目标行数以后，需要从下往上转折到第一行，循环中控制好方向ji

**Go版本:**
1. 初始化二维字节数组matrix来存储Z字形排列的字符串
2. 使用down和up索引控制遍历添加字符的方向
3. 当down达到numRows时改变方向,up达到0时也改变方向
4. 遍历字符串,根据索引添加到matrix对应的行
5. 遍历matrix拼接所有行得到结果

**Python版本:**
1. 初始化字符串列表rows来存储Z字形排列字符串
2. 使用going_down标志控制索引变化方向
3. 当cur_row到达首尾行时,改变going_down的值
4. 遍历字符串,将字符添加到对应的rows行
5. 使用join()拼接rows得到结果

**Java版本:**
1. 初始化二维字符数组matrix来存储排列后的字符串
2. 使用dir标志控制索引变化方向
3. 当curRow到达首尾行时,改变dir方向
4. 遍历字符串到matrix对应行
5. 遍历matrix拼接每行得到结果

**C++版本:**
1. 初始化字符串向量rows来存储排列后的字符串
2. goingDown标志控制索引变化方向
3. 当当前行为首尾行时改变goingDown
4. 遍历字符串到rows对应的行
5. 遍历rows拼接得到结果
## 代码

```go
package leetcode


func convert(s string, numRows int) string { // 定义函数convert,接受字符串s和整数numRows作为参数,返回字符串
    matrix, down, up := make([][]byte, numRows, numRows), 0, numRows-2 // 初始化三个变量:二维字节数组matrix,下标变量down和up
    
    for i := 0; i != len(s); { // 使用for循环遍历字符串s
       if down != numRows { // 如果down不等于numRows
          matrix[down] = append(matrix[down], byte(s[i])) // 将s的第i个字节加入matrix的第down行
          down++ // down自增1
          i++ // i自增1
       } else if up > 0 { // 否则如果up大于0
          matrix[up] = append(matrix[up], byte(s[i])) // 将s的第i个字节加入matrix的第up行  
          up-- // up自减1
          i++ // i自增1
       } else { // 否则
          up = numRows - 2  // 将up赋值为numRows-2
          down = 0 // 将down赋值为0
       }
    }
    
    solution := make([]byte, 0, len(s)) // 初始化字节数组solution
    for _, row := range matrix { // 遍历matrix的每一行
       for _, item := range row { // 遍历每一行的每个元素
          solution = append(solution, item) // 将该元素加入solution
       }
    }
    return string(solution) // 将solution转换成字符串并返回
}
```

## Python
```Python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
     
        if numRows == 1: # 如果只有1行,不需转换
            return s
        
        rows = ["" for _ in range(numRows)] # 初始化长度为numRows的空字符串列表rows表示矩阵
        
        cur_row = 0 # 当前行编号
        going_down = False # 索引变化方向标志
        
        for c in s: # 遍历字符串s的每个字符
            rows[cur_row] += c # 在对应行末尾添加字符
            
            if cur_row == 0 or cur_row == numRows - 1: # 如果在第一行或最后一行
                going_down = not going_down # 改变索引变化方向
            
            if going_down: # 如果向下遍历
                cur_row += 1 # 当前行号+1
            else: # 如果向上遍历
                cur_row -= 1 # 当前行号-1
                
        return "".join(rows) # 拼接rows得到结果并返回

```
## Java
```Java
class Solution {
  public String convert(String s, int numRows) {

    if (numRows == 1) return s; // 如果只有1行,不需转换

    char[][] matrix = new char[numRows][s.length()]; // 初始化二维字符数组matrix,行数为numRows,每行长度为s的长度

    int curRow = 0; // 当前行号
    int dir = -1; // 索引变化方向,-1代表向上

    for (int i = 0; i < s.length(); i++) {  
      matrix[curRow] = addChar(matrix[curRow], s.charAt(i)); // 将当前字符加入 matrix 的当前行
      
      if (curRow == 0 || curRow == numRows - 1) { // 如果在第一行或最后一行
        dir = -dir; // 改变索引变化方向
      }

      curRow += dir; // 当前行号移动
    }

    StringBuilder result = new StringBuilder();
    for (char[] row : matrix) { // 遍历每一行
      for (char c : row) { 
        if (c != 0) result.append(c); // 添加非空字符到结果字符串
      }
    }

    return result.toString(); // 转成字符串并返回
  }

  private char[] addChar(char[] array, char c) { // 在数组末尾添加一个字符
    if (array == null) { 
      return new char[] {c}; 
    }
    int n = array.length;
    char[] newArray = Arrays.copyOf(array, n + 1); 
    newArray[n] = c;
    return newArray;
  }
}

```
## Cpp
```Cpp
class Solution {
public:
    string convert(string s, int numRows) {
        
        if(numRows == 1) return s; // 只有1行,不需转换
        
        vector<string> rows(numRows); // 初始化长度为numRows的字符串向量rows表示矩阵
        
        int curRow = 0; // 当前行索引
        bool goingDown = false; // 索引变化方向标志

        for(char c : s) { // 遍历字符串s的每个字符
            rows[curRow] += c; // 将字符添加到对应行
            
            if(curRow == 0 || curRow == numRows-1) { // 当前行为第一行或最后一行
                goingDown = !goingDown; // 改变索引变化方向
            }
            
            if(goingDown) { // 如果向下遍历
                curRow++; // 当前行索引+1
            } else { // 如果向上遍历 
                curRow--; // 当前行索引-1
            }
        }

        string ans; 
        for(string row : rows) { // 遍历每一行
            ans += row; // 将行内容拼接到结果字符串
        }
        return ans; // 返回转换结果
    }
};

```
**Go版本:**
- make初始化一个切片或映射,可以指定容量
- 二维字节数组matrix存储字符,append向切片追加元素
- range遍历切片或映射
- string()将字节切片转换成字符串

**Python版本:**
- []创建列表并可以指定长度,+=向列表追加元素 
- join()可以拼接列表中的字符串元素
- 不需要预先指定列表长度,根据需求动态增长

**Java版本:**
- 二维字符数组matrix存储字符,需指定行数和列数
- Arrays.copyOf扩容数组,返回新数组
- StringBuilder用于字符串拼接,toString()转换为String
- charAt()获取字符串指定位置的字符

**C++版本:**
- vector初始化时可以指定大小
- +=向向量追加元素
- 遍历使用范围for语句,自动获取元素
- string类支持加法拼接