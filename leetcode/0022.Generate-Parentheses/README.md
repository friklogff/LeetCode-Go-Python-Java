# [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)


## 题目

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:


    [
      "((()))",
      "(()())",
      "(())()",
      "()(())",
      "()()()"
    ]


## 题目大意

给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。


## 解题思路

- 这道题乍一看需要判断括号是否匹配的问题，如果真的判断了，那时间复杂度就到 O(n * 2^n)了，虽然也可以 AC，但是时间复杂度巨高。
- 这道题实际上不需要判断括号是否匹配的问题。因为在 DFS 回溯的过程中，会让 `(` 和 `)` 成对的匹配上的。
当然，请继续阅读，我会为你分别介绍每个版本的解题思路。

Go 版本解题思路：

这个解题思路使用了深度优先搜索（DFS）的方法来生成有效的括号组合。主要的步骤如下：

1. 定义 `generateParenthesis` 函数，接收括号对数目 `n` 作为参数，返回有效的括号组合列表。

2. 如果 `n` 为 0，直接返回一个空的字符串列表，因为没有括号需要生成。

3. 初始化一个空的结果列表 `res`，用于存储有效的括号组合。

4. 调用辅助函数 `findGenerateParenthesis` 来递归生成括号组合。传入当前剩余左右括号数目、当前生成的字符串和结果列表的指针。

5. 在 `findGenerateParenthesis` 函数中，当左右括号剩余数目都为 0 时，将当前生成的字符串添加到结果列表中。

6. 如果剩余的左括号数目大于 0，可以在当前字符串后添加一个左括号，然后递归生成。

7. 如果剩余的右括号数目大于 0，并且剩余的右括号数目严格大于剩余的左括号数目（以保证有效性），可以在当前字符串后添加一个右括号，然后递归生成。

8. 返回最终的有效括号组合列表 `res`。

Python 版本解题思路：

这个解题思路同样使用了深度优先搜索（DFS）的方法来生成有效的括号组合。主要的步骤如下：

1. 定义一个 `Solution` 类，其中有一个 `generateParenthesis` 方法，接收括号对数目 `n` 作为参数，返回有效的括号组合列表。

2. 初始化一个空的结果列表 `res`，用于存储有效的括号组合。

3. 调用递归函数 `generate` 来生成括号组合。传入当前剩余左右括号数目、当前生成的字符串和结果列表。

4. 在 `generate` 函数中，有两个基准情况：

   - 如果剩余的左右括号数目都为 0，将当前生成的字符串添加到结果列表中。
   - 如果剩余的左括号数目大于 0，可以在当前字符串后添加一个左括号，然后递归生成。

5. 如果剩余的右括号数目大于 0，并且剩余的右括号数目严格大于剩余的左括号数目（以保证有效性），可以在当前字符串后添加一个右括号，然后递归生成。

6. 最后，`generateParenthesis` 方法返回最终的有效括号组合列表 `res`。

Java 版本解题思路：

这个解题思路与前两个版本类似，同样使用深度优先搜索（DFS）的方法来生成有效的括号组合。主要的步骤如下：

1. 定义一个 `Solution` 类，其中有一个 `generateParenthesis` 方法，接收括号对数目 `n` 作为参数，返回有效的括号组合列表。

2. 初始化一个空的结果列表 `res`，用于存储有效的括号组合。

3. 调用递归函数 `generate` 来生成括号组合。传入当前剩余左右括号数目、当前生成的字符串和结果列表。

4. 在 `generate` 函数中，同样有两个基准情况：

   - 如果剩余的左右括号数目都为 0，将当前生成的字符串添加到结果列表中。
   - 如果剩余的左括号数目大于 0，可以在当前字符串后添加一个左括号，然后递归生成。

5. 如果剩余的右括号数目大于 0，并且剩余的右括号数目严格大于剩余的左括号数目（以保证有效性），可以在当前字符串后添加一个右括号，然后递归生成。

6. 最后，`generateParenthesis` 方法返回最终的有效括号组合列表 `res`。

C++ 版本解题思路：

这个解题思路与其他版本相似，同样使用深度优先搜索（DFS）的方法来生成有效的括号组合。主要的步骤如下：

1. 定义一个 `Solution` 类，其中有一个 `generateParenthesis` 方法，接收括号对数目 `n` 作为参数，返回有效的括号组合列表。

2. 初始化一个空的结果列表 `res`，用于存储有效的括号组合。

3. 调用递归函数 `generate` 来生成括号组合。传入当前剩余左右括号数目、当前生成的字符串和结果列表。

4. 在 `generate` 函数中，同样有两个基准情况：

   - 如果剩余的左右括号数目都为 0，将当前生成的字符串添加到结果列表中。
   - 如果剩余的左括号数目大于 0，可以在当前字符串后添加一个左括号，然后递归生成。

5. 如果剩余的右括号数目大于 0，并且剩余的右括号数目严格大于剩余的左括号数目（以保证有效性），可以在当前字符串后添加一个右括号，然后递归生成。

6. 最后，`generateParenthesis` 方法返回最终的有效括号组合列表 `res`。


## 代码
## Go
```Go
// 定义一个函数 generateParenthesis，输入参数 n 表示括号对数目，返回有效的括号组合列表。
func generateParenthesis(n int) []string {
    // 如果括号对数目为 0，直接返回一个空的字符串列表。
    if n == 0 {
        return []string{}
    }
    // 初始化一个结果列表用于存储有效的括号组合。
    res := []string{}
    // 调用辅助函数 findGenerateParenthesis 生成括号组合，传入当前左右括号剩余数目、当前生成的字符串和结果列表的指针。
    findGenerateParenthesis(n, n, "", &res)
    // 返回最终的有效括号组合列表。
    return res
}

// 定义辅助函数 findGenerateParenthesis，用于递归生成有效的括号组合。
func findGenerateParenthesis(lindex, rindex int, str string, res *[]string) {
    // 当左右括号剩余数目都为 0 时，说明已经生成了一个有效的括号组合，将其添加到结果列表中。
    if lindex == 0 && rindex == 0 {
        *res = append(*res, str)
        return
    }
    // 如果左括号剩余数目大于 0，可以在当前字符串后添加一个左括号，继续递归生成。
    if lindex > 0 {
        findGenerateParenthesis(lindex-1, rindex, str+"(", res)
    }
    // 如果右括号剩余数目大于 0，并且剩余的右括号数目严格大于剩余的左括号数目，
    // 则可以在当前字符串后添加一个右括号，继续递归生成。
    if rindex > 0 && lindex < rindex {
        findGenerateParenthesis(lindex, rindex-1, str+")", res)
    }
}

```
## Python
```Python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [] # 存储最终的有效括号组合列表
        self.generate(n, n, "", res) # 调用递归函数生成括号组合
        return res
    
    # 递归生成括号组合的辅助函数
    def generate(self, left: int, right: int, current: str, res: List[str]):
        # 当左右括号剩余数目都为 0 时，说明已经生成了一个有效的括号组合，将其添加到结果列表中。
        if left == 0 and right == 0:
            res.append(current)
            return
        
        # 如果左括号剩余数目大于 0，可以在当前字符串后添加一个左括号，继续递归生成。
        if left > 0:
            self.generate(left - 1, right, current + "(", res)
        
        # 如果右括号剩余数目大于 0，并且剩余的右括号数目严格大于剩余的左括号数目，
        # 则可以在当前字符串后添加一个右括号，继续递归生成。
        if right > 0 and left < right:
            self.generate(left, right - 1, current + ")", res)

```
## Java
```Java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>(); // 存储最终的有效括号组合列表
        generate(n, n, "", res); // 调用递归函数生成括号组合
        return res;
    }
    
    // 递归生成括号组合的辅助函数
    private void generate(int left, int right, String current, List<String> res) {
        // 当左右括号剩余数目都为 0 时，说明已经生成了一个有效的括号组合，将其添加到结果列表中。
        if (left == 0 && right == 0) {
            res.add(current);
            return;
        }
        
        // 如果左括号剩余数目大于 0，可以在当前字符串后添加一个左括号，继续递归生成。
        if (left > 0) {
            generate(left - 1, right, current + "(", res);
        }
        
        // 如果右括号剩余数目大于 0，并且剩余的右括号数目严格大于剩余的左括号数目，
        // 则可以在当前字符串后添加一个右括号，继续递归生成。
        if (right > 0 && left < right) {
            generate(left, right - 1, current + ")", res);
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int n = 3; // 设置括号对数目
        List<String> result = solution.generateParenthesis(n); // 调用生成函数
        for (String str : result) {
            System.out.println(str); // 输出生成的括号组合
        }
    }
}

```
## Cpp
```Cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res; // 存储最终的有效括号组合列表
        generate(n, n, "", res); // 调用递归函数生成括号组合
        return res;
    }
    
    // 递归生成括号组合的辅助函数
    void generate(int left, int right, string current, vector<string>& res) {
        // 当左右括号剩余数目都为 0 时，说明已经生成了一个有效的括号组合，将其添加到结果列表中。
        if (left == 0 && right == 0) {
            res.push_back(current);
            return;
        }
        
        // 如果左括号剩余数目大于 0，可以在当前字符串后添加一个左括号，继续递归生成。
        if (left > 0) {
            generate(left - 1, right, current + "(", res);
        }
        
        // 如果右括号剩余数目大于 0，并且剩余的右括号数目严格大于剩余的左括号数目，
        // 则可以在当前字符串后添加一个右括号，继续递归生成。
        if (right > 0 && left < right) {
            generate(left, right - 1, current + ")", res);
        }
    }
};


```
每个版本代码所需要的基础知识。

Go 版本基础知识：

1. **函数声明与调用：** 了解如何声明和调用函数，Go 使用 `func` 关键字来定义函数。

2. **条件语句：** 了解 `if` 条件语句的用法，以及如何使用条件判断。

3. **切片（Slices）：** 切片是 Go 中灵活的数据结构，类似于动态数组。了解如何声明、初始化和操作切片。

4. **递归：** 了解递归的概念，以及如何在函数中调用自身。

5. **指针与引用：** 了解 Go 中的指针和引用，因为函数中需要通过引用传递结果列表。

Python 版本基础知识：

1. **函数定义与调用：** 理解如何定义和调用函数，Python 使用 `def` 关键字来声明函数。

2. **条件语句：** 理解 `if` 条件语句的语法，以及如何使用条件判断。

3. **列表（Lists）：** 列表是 Python 中常用的数据结构，类似于动态数组。了解如何创建、修改和操作列表。

4. **递归：** 理解递归的概念，以及如何在函数中调用自身。

Java 版本基础知识：

1. **函数声明与调用：** 了解如何声明和调用函数，Java 使用方法（methods）来定义函数。

2. **条件语句：** 了解 `if` 条件语句的语法，以及如何进行条件判断。

3. **列表（Lists）：** 在 Java 中，可以使用 `ArrayList` 类作为动态数组。了解如何创建、修改和操作 ArrayList。

4. **递归：** 了解递归的概念，以及如何在方法中调用自身。

5. **类与对象：** Java 是面向对象的编程语言，理解类和对象的概念，以及如何定义和使用它们。

C++ 版本基础知识：

1. **函数声明与调用：** 了解如何声明和调用函数，C++ 使用函数（functions）来定义函数。

2. **条件语句：** 理解 `if` 条件语句的语法，以及如何进行条件判断。

3. **向量（Vectors）：** 在 C++ 中，可以使用 `vector` 类作为动态数组。了解如何创建、修改和操作向量。

4. **递归：** 理解递归的概念，以及如何在函数中调用自身。

5. **类与对象：** C++ 也是面向对象的编程语言，理解类和对象的概念，以及如何定义和使用它们。

