# [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

## 题目

Given a string containing digits from`2-9`inclusive, return all possible letter combinations that the number could
represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any
letters.

![](http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)

**Example:**

```c
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```

**Note:**

Although the above answer is in lexicographical order, your answer could be in any order you want.

## 题目大意

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

## 解题思路

当使用不同的编程语言来实现 "Letter Combinations of a Phone Number" 这个问题时，虽然解法的思路是相同的，但由于语言的差异，实现细节会有所不同。下面将分别介绍每个版本的解题思路：

## 解题思路（Go 版本）：

### 解法一：DFS（深度优先搜索）

1. 创建一个 `letterMap` 数组，其中每个索引对应一个数字，存储了该数字对应的可能字母集合。
2. 创建一个结果切片 `res`，用于存储最终的字母组合结果。
3. 定义一个递归函数 `findCombination`，该函数会根据当前数字的索引递归地生成字母组合。
4. 在 `letterCombinations` 函数中，如果输入的数字串为空，直接返回空切片。
5. 调用 `findCombination` 函数，将初始状态的数字串、索引和空字符串传入。递归过程中，每次都会将当前数字对应的字母加入当前组合 `s` 中，直到处理完所有数字。
6. 当递归深度达到数字串的长度时，将当前组合 `s` 加入结果切片 `res` 中。
7. 返回最终的结果切片 `res`。

### 解法二：非递归

1. 创建一个 `letterMap` 数组，其中每个索引对应一个数字，存储了该数字对应的可能字母集合。
2. 创建一个结果切片 `res`，用于存储最终的字母组合结果。
3. 遍历输入的数字串，依次处理每个数字。
4. 对于第一个数字，获取其对应的字母集合，初始化一个初始结果切片 `res`，将其中的每个字母作为起始元素。
5. 对于后续的数字，获取其对应的字母集合，将当前结果切片 `res` 中的每个元素与字母集合中的每个字母组合，生成新的结果切片 `tmp`。
6. 更新结果切片 `res` 为新生成的结果切片 `tmp`。
7. 返回最终的结果切片 `res`。

### 解法三：回溯

1. 创建一个 `letterMap` 数组，其中每个索引对应一个数字，存储了该数字对应的可能字母集合。
2. 创建一个结果切片 `res`，用于存储最终的字母组合结果。
3. 创建一个 `dict` 字典，将每个数字映射到其对应的可能字母集合。
4. 定义一个回溯函数 `letterFunc`，该函数会递归地生成字母组合。
5. 在 `letterCombinations` 函数中，如果输入的数字串为空，直接返回空切片。
6. 调用 `letterFunc` 函数，将初始状态的空组合 `""` 和数字串传入。递归过程中，每次将当前数字对应的每个字母加入组合 `res` 中，继续处理下一个数字。
7. 当递归深度达到数字串的长度时，将当前组合加入结果切片 `res` 中。
8. 返回最终的结果切片 `res`。

## 解题思路（Python 版本）：

与 Go 版本的解法思路相同，只是在 Python 中使用了不同的语法来实现相同的逻辑。

## 解题思路（Java 版本）：

与 Go 版本的解法思路相同，只是在 Java 中使用了不同的语法来实现相同的逻辑。在 Java 版本中，数组和集合的操作稍微有所不同，需要使用 ArrayList 或其他集合类来存储最终结果。

## 解题思路（C++ 版本）：

与 Go 版本的解法思路相同，只是在 C++ 中使用了不同的语法来实现相同的逻辑。在 C++ 版本中，需要使用 vector 来存储最终结果。

总的来说，不同版本的解法思路都是基于递归、深度优先搜索和回溯的思想，通过在每个数字上选择其中一个字母，然后递归地处理剩余数字，直到生成完整的字母组合。差异主要体现在语言的语法、数据结构和函数调用上。
## 代码

## Go

```Go
// 解法一 DFS
var (
    letterMap = []string{
        " ",    //0
        "",     //1
        "abc",  //2
        "def",  //3
        "ghi",  //4
        "jkl",  //5
        "mno",  //6
        "pqrs", //7
        "tuv",  //8
        "wxyz", //9
    }
    res   = []string{} // 存储最终结果的切片
    final = 0          // 标记当前处理的组合数
)

func letterCombinations(digits string) []string {
    if digits == "" {
        return []string{} // 若输入为空，则返回空切片
    }
    res = []string{} // 重置结果切片
    findCombination(&digits, 0, "") // 调用递归函数生成字母组合
    return res
}

func findCombination(digits *string, index int, s string) {
    if index == len(*digits) {
        res = append(res, s) // 所有数字已经处理完，将当前组合加入结果切片
        return
    }
    num := (*digits)[index]
    letter := letterMap[num-'0'] // 获取当前数字对应的字母集合
    for i := 0; i < len(letter); i++ {
        findCombination(digits, index+1, s+string(letter[i])) // 递归生成下一个数字对应的字母组合
    }
    return
}

// 解法二 非递归
var (
    letterMap = []string{
        " ",    //0
        "",     //1
        "abc",  //2
        "def",  //3
        "ghi",  //4
        "jkl",  //5
        "mno",  //6
        "pqrs", //7
        "tuv",  //8
        "wxyz", //9
    }
    res   = []string{} // 存储最终结果的切片
    final = 0          // 标记当前处理的组合数
)

func letterCombinations(digits string) []string {
    if digits == "" {
        return []string{} // 若输入为空，则返回空切片
    }
    index := digits[0] - '0' // 获取第一个数字对应的索引
    letter := letterMap[index] // 获取对应的字母集合
    tmp := []string{} // 临时存储新生成的字母组合
    for i := 0; i < len(letter); i++ {
        if len(res) == 0 {
            res = append(res, "")
        }
        for j := 0; j < len(res); j++ {
            tmp = append(tmp, res[j]+string(letter[i])) // 将当前字母与已有组合进行拼接
        }
    }
    res = tmp // 更新结果切片
    final++
    letterCombinations(digits[1:]) // 继续处理剩余的数字
    final--
    if final == 0 {
        tmp = res
        res = []string{} // 重置结果切片
    }
    return tmp
}

// 解法三 回溯（参考回溯模板，类似DFS）
var (
    letterMap = []string{
        " ",    //0
        "",     //1
        "abc",  //2
        "def",  //3
        "ghi",  //4
        "jkl",  //5
        "mno",  //6
        "pqrs", //7
        "tuv",  //8
        "wxyz", //9
    }
    res   = []string{} // 存储最终结果的切片
    final = 0          // 标记当前处理的组合数
)
var result []string // 用于存储结果的全局切片
var dict = map[string][]string{ // 数字到字母的映射
    "2": []string{"a", "b", "c"},
    "3": []string{"d", "e", "f"},
    "4": []string{"g", "h", "i"},
    "5": []string{"j", "k", "l"},
    "6": []string{"m", "n", "o"},
    "7": []string{"p", "q", "r", "s"},
    "8": []string{"t", "u", "v"},
    "9": []string{"w", "x", "y", "z"},
}

func letterCombinations(digits string) []string {
    result = []string{} // 重置结果切片
    if digits == "" {
        return result
    }
    letterFunc("", digits) // 调用回溯函数生成字母组合
    return result
}

func letterFunc(res string, digits string) {
    if digits == "" {
        result = append(result, res) // 所有数字已经处理完，将当前组合加入结果切片
        return
    }

    k := digits[0:1]
    digits = digits[1:]
    for i := 0; i < len(dict[k]); i++ {
        res += dict[k][i] // 添加当前字母到组合
        letterFunc(res, digits) // 继续处理下一个数字
        res = res[0:len(res)-1] // 回溯，移除最后一个字母
    }
}

```

## Python

```Python
class Solution:
    def __init__(self):
        # 字母映射表，与之前的Java代码中的letterMap相同
        self.letterMap = [
            " ",    #0
            "",     #1
            "abc",  #2
            "def",  #3
            "ghi",  #4
            "jkl",  #5
            "mno",  #6
            "pqrs", #7
            "tuv",  #8
            "wxyz"  #9
        ]

    # 解法一 DFS
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if not digits:
            return result
        self.findCombination(result, digits, 0, "")
        return result

    def findCombination(self, result: List[str], digits: str, index: int, s: str):
        if index == len(digits):
            result.append(s)
            return
        num = int(digits[index])
        letter = self.letterMap[num]
        for char in letter:
            self.findCombination(result, digits, index + 1, s + char)

    # 解法二 非递归
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if not digits:
            return result

        letter = self.letterMap[int(digits[0])]
        res = [char for char in letter]

        for digit in digits[1:]:
            letter = self.letterMap[int(digit)]
            tmp = []
            for prefix in res:
                for char in letter:
                    tmp.append(prefix + char)
            res = tmp
        return res

    # 解法三 回溯
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if not digits:
            return result

        dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        self.letterFunc(result, "", digits, dict)
        return result

    def letterFunc(self, result: List[str], res: str, digits: str, dict: Dict[str, List[str]]):
        if not digits:
            result.append(res)
            return

        k = digits[0]
        digits = digits[1:]
        for letter in dict[k]:
            self.letterFunc(result, res + letter, digits, dict)

```

## Java

```Java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    // 字母映射表，与之前的Go代码中的letterMap相同
    private static final String[] letterMap = {
        " ",    //0
        "",     //1
        "abc",  //2
        "def",  //3
        "ghi",  //4
        "jkl",  //5
        "mno",  //6
        "pqrs", //7
        "tuv",  //8
        "wxyz"  //9
    };

    // 解法一 DFS
    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        if (digits.isEmpty()) {
            return result;
        }
        findCombination(result, digits, 0, "");
        return result;
    }

    private void findCombination(List<String> result, String digits, int index, String s) {
        if (index == digits.length()) {
            result.add(s);
            return;
        }
        int num = digits.charAt(index) - '0';
        String letter = letterMap[num];
        for (int i = 0; i < letter.length(); i++) {
            findCombination(result, digits, index + 1, s + letter.charAt(i));
        }
    }

    // 解法二 非递归
    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        if (digits.isEmpty()) {
            return result;
        }

        char[] digitsArray = digits.toCharArray();
        String letter = letterMap[digitsArray[0] - '0'];

        List<String> res = new ArrayList<>();
        for (int i = 0; i < letter.length(); i++) {
            res.add("" + letter.charAt(i));
        }

        for (int i = 1; i < digitsArray.length; i++) {
            letter = letterMap[digitsArray[i] - '0'];
            List<String> tmp = new ArrayList<>();
            for (String prefix : res) {
                for (int j = 0; j < letter.length(); j++) {
                    tmp.add(prefix + letter.charAt(j));
                }
            }
            res = tmp;
        }
        return res;
    }

    // 解法三 回溯
    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        if (digits.isEmpty()) {
            return result;
        }
        Map<String, String[]> dict = new HashMap<>();
        dict.put("2", new String[]{"a", "b", "c"});
        dict.put("3", new String[]{"d", "e", "f"});
        dict.put("4", new String[]{"g", "h", "i"});
        dict.put("5", new String[]{"j", "k", "l"});
        dict.put("6", new String[]{"m", "n", "o"});
        dict.put("7", new String[]{"p", "q", "r", "s"});
        dict.put("8", new String[]{"t", "u", "v"});
        dict.put("9", new String[]{"w", "x", "y", "z"});

        letterFunc(result, "", digits, dict);
        return result;
    }

    private void letterFunc(List<String> result, String res, String digits, Map<String, String[]> dict) {
        if (digits.isEmpty()) {
            result.add(res);
            return;
        }

        String k = digits.substring(0, 1);
        digits = digits.substring(1);
        for (String letter : dict.get(k)) {
            letterFunc(result, res + letter, digits, dict);
        }
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    // 字母映射表，与之前的Java代码中的letterMap相同
    vector<string> letterMap = {
        " ",    //0
        "",     //1
        "abc",  //2
        "def",  //3
        "ghi",  //4
        "jkl",  //5
        "mno",  //6
        "pqrs", //7
        "tuv",  //8
        "wxyz"  //9
    };

    // 解法一 DFS
    vector<string> letterCombinations(string digits) {
        vector<string> result;
        if (digits.empty()) {
            return result;
        }
        string combination;
        findCombination(result, digits, 0, combination);
        return result;
    }

    void findCombination(vector<string>& result, const string& digits, int index, string& s) {
        if (index == digits.length()) {
            result.push_back(s);
            return;
        }
        int num = digits[index] - '0';
        string letter = letterMap[num];
        for (int i = 0; i < letter.length(); i++) {
            s.push_back(letter[i]);
            findCombination(result, digits, index + 1, s);
            s.pop_back(); // 回溯，移除最后一个字母
        }
    }

    // 解法二 非递归
    vector<string> letterCombinations(string digits) {
        vector<string> result;
        if (digits.empty()) {
            return result;
        }

        string letter = letterMap[digits[0] - '0'];
        vector<string> res;
        for (int i = 0; i < letter.length(); i++) {
            res.push_back(string(1, letter[i]));
        }

        for (int i = 1; i < digits.length(); i++) {
            letter = letterMap[digits[i] - '0'];
            vector<string> tmp;
            for (const string& prefix : res) {
                for (char c : letter) {
                    tmp.push_back(prefix + c);
                }
            }
            res = tmp;
        }
        return res;
    }

    // 解法三 回溯
    vector<string> letterCombinations(string digits) {
        vector<string> result;
        if (digits.empty()) {
            return result;
        }
        unordered_map<string, vector<string>> dict = {
            {"2", {"a", "b", "c"}},
            {"3", {"d", "e", "f"}},
            {"4", {"g", "h", "i"}},
            {"5", {"j", "k", "l"}},
            {"6", {"m", "n", "o"}},
            {"7", {"p", "q", "r", "s"}},
            {"8", {"t", "u", "v"}},
            {"9", {"w", "x", "y", "z"}}
        };

        letterFunc(result, "", digits, dict);
        return result;
    }

    void letterFunc(vector<string>& result, string res, string digits, unordered_map<string, vector<string>>& dict) {
        if (digits.empty()) {
            result.push_back(res);
            return;
        }

        string k = digits.substr(0, 1);
        digits = digits.substr(1);
        for (const string& letter : dict[k]) {
            letterFunc(result, res + letter, digits, dict);
        }
    }
};

```
当使用不同的编程语言来实现同一个问题时，虽然解法的思路是相同的，但由于语言的差异，有些基础知识是需要掌握的。下面将逐个介绍每个版本所需要的基础知识：

## Go 版本基础知识：

1. **变量和数据类型：** 需要了解如何声明变量、赋值以及基本的数据类型，如字符串、整数等。
2. **切片：** 切片是 Go 中动态数组的数据结构，用于存储字符串结果集，需要了解切片的创建、操作和使用。
3. **递归：** 了解递归的概念和使用方法，因为第一种解法使用了深度优先搜索（DFS）的递归思路。
4. **函数和方法：** 了解如何定义函数和方法，以及函数的参数和返回值。
5. **字符串操作：** 掌握字符串的拼接、分割等基本操作。

## Python 版本基础知识：

1. **变量和数据类型：** 需要了解如何声明变量、赋值以及基本的数据类型，如字符串、整数等。
2. **列表（List）：** 列表是 Python 中的动态数组，用于存储字符串结果集，需要了解列表的创建、操作和使用。
3. **递归：** 了解递归的概念和使用方法，因为第一种解法使用了深度优先搜索（DFS）的递归思路。
4. **函数定义和调用：** 掌握如何定义函数和调用函数，以及函数的参数和返回值。
5. **字符串操作：** 掌握字符串的拼接、分割等基本操作。

## Java 版本基础知识：

1. **变量和数据类型：** 需要了解如何声明变量、赋值以及基本的数据类型，如字符串、整数等。
2. **数组和集合：** Java 中的数组和集合（如 ArrayList）用于存储字符串结果集，需要了解数组和集合的创建、操作和使用。
3. **递归：** 了解递归的概念和使用方法，因为第一种解法使用了深度优先搜索（DFS）的递归思路。
4. **方法定义和调用：** 掌握如何定义方法和调用方法，以及方法的参数和返回值。
5. **字符串操作：** 掌握字符串的拼接、分割等基本操作。

## C++ 版本基础知识：

1. **变量和数据类型：** 需要了解如何声明变量、赋值以及基本的数据类型，如字符串、整数等。
2. **向量（Vector）：** C++ 中的向量（vector）用于存储字符串结果集，需要了解向量的创建、操作和使用。
3. **递归：** 了解递归的概念和使用方法，因为第一种解法使用了深度优先搜索（DFS）的递归思路。
4. **函数定义和调用：** 掌握如何定义函数和调用函数，以及函数的参数和返回值。
5. **字符串操作：** 掌握字符串的拼接、分割等基本操作。

