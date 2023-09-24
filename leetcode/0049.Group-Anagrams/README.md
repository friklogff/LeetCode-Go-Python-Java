# [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)

## 题目

Given an array of strings, group anagrams together.

Example:

```c
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```

Note:

- All inputs will be in lowercase.
- The order of your output does not matter.

## 题目大意

给出一个字符串数组，要求对字符串数组里面有 Anagrams 关系的字符串进行分组。Anagrams 关系是指两个字符串的字符完全相同，顺序不同，两者是由排列组合组成。

## 解题思路

这道题可以将每个字符串都排序，排序完成以后，相同 Anagrams 的字符串必然排序结果一样。把排序以后的字符串当做 key 存入到 map
中。遍历数组以后，就能得到一个 map，key 是排序以后的字符串，value 对应的是这个排序字符串以后的 Anagrams 字符串集合。最后再将这些
value 对应的字符串数组输出即可。
当然，以下是每个版本的解题思路：

Go 版本解题思路

1. 创建一个空的映射 (map)，用于将具有相同字母组成的字符串分组。
2. 创建一个空的结果切片 (slice)。
3. 定义一个匿名函数 `sign`，该函数接受一个字符串作为输入，并返回一个表示字符串字母组成的标识符。
4. 遍历输入的字符串数组：
    - 对每个字符串计算其字母组成的标识符，通过匿名函数 `sign` 实现。
    - 将当前字符串添加到对应标识符的分组中，使用映射进行组织。
5. 遍历映射中的每个分组，将分组转换为切片，并将切片添加到结果切片中。
6. 返回最终的结果切片，其中包含了按字母组成分组的字符串。

Python 版本解题思路

1. 创建一个空的字典 (dictionary)，用于将具有相同字母组成的字符串分组。
2. 遍历输入的字符串列表：
    - 将每个字符串排序，形成一个元组，该元组将被用作字典的键。
    - 如果该键不存在于字典中，则创建一个空列表作为值，并将原始字符串添加到该列表中。
    - 如果该键已经存在于字典中，则将原始字符串添加到对应键的列表中。
3. 将字典的值（分组）转换为列表，并返回结果。

Java 版本解题思路

1. 创建一个映射 (Map)，用于将具有相同字母组成的字符串分组。在 Java 中，通常使用 `HashMap`。
2. 遍历输入的字符串数组：
    - 将每个字符串转换为字符数组，并对字符数组进行排序，形成排序后的字符串。
    - 使用排序后的字符串作为映射的键，原始字符串作为值存入映射中。
3. 将映射中的分组转换为列表，并返回结果。

C++ 版本解题思路

1. 创建一个映射 (unordered_map)，用于将具有相同字母组成的字符串分组。
2. 遍历输入的字符串向量：
    - 将每个字符串排序，形成排序后的字符串。
    - 使用排序后的字符串作为映射的键，原始字符串作为值存入映射中。
3. 将映射的值（分组）转换为向量，并返回结果。

无论使用哪种版本的解决方案，基本思路都是利用数据结构（如映射或字典）来组织和存储具有相同字母组成的字符串，然后将它们分组起来。排序字符串是为了确保相同
Anagrams 的字符串具有相同的标识符，以便正确地分组它们。

## 代码

## Go

```Go
func groupAnagrams(strs []string) [][]string {
    // 创建一个空的映射（map），用于将具有相同字母组成的字符串分组
    hashMap := map[string][]string{}
    // 创建一个空的结果切片（slice）
    res := [][]string{}

    // 定义一个匿名函数 sign，该函数接受一个字符串 s，并返回一个表示 s 字母组成的标识符
    sign := func(s string) string {
        // 创建一个长度为 26 的字节数组，用于统计每个字母出现的次数
        strB := [26]byte{}
        // 遍历字符串 s 中的每个字符
        for _, v := range s {
            // 将字符 v 转换为小写字母，并将对应字母的计数加一
            strB[v-'a']++
        }
        // 将字节数组转换为字符串并返回
        return string(strB[:])
    }

    // 遍历输入的字符串切片 strs
    for _, v := range strs {
        // 对当前字符串 v 计算其字母组成的标识符
        signV := sign(v)
        // 将当前字符串添加到对应标识符的分组中
        hashMap[signV] = append(hashMap[signV], v)
    }

    // 遍历映射中的每个分组，并将其添加到结果切片 res 中
    for _, v := range hashMap {
        res = append(res, v)
    }
    // 返回最终的结果切片，其中包含了按字母组成分组的字符串
    return res
}

```

## Python

```Python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 创建一个字典，用于将具有相同字母组成的字符串分组
        hashMap = {}

        # 遍历输入的字符串列表
        for str in strs:
            # 将字符串转换为排序后的元组，作为字典的键
            sorted_str = tuple(sorted(str))
            # 将原始字符串添加到对应键的列表中
            hashMap.setdefault(sorted_str, []).append(str)

        # 将字典的值（分组）转换为列表，并返回结果
        result = list(hashMap.values())
        return result

```

## Java

```Java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // 创建一个映射，用于将具有相同字母组成的字符串分组
        Map<String, List<String>> hashMap = new HashMap<>();

        // 遍历输入的字符串数组
        for (String str : strs) {
            // 将字符串转换为字符数组，并排序
            char[] charArray = str.toCharArray();
            Arrays.sort(charArray);
            // 排序后的字符数组作为键，原始字符串作为值存入映射中
            String sortedStr = new String(charArray);
            if (!hashMap.containsKey(sortedStr)) {
                hashMap.put(sortedStr, new ArrayList<>());
            }
            hashMap.get(sortedStr).add(str);
        }

        // 将映射中的分组转换为列表
        List<List<String>> result = new ArrayList<>(hashMap.values());
        return result;
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // 创建一个映射，用于将具有相同字母组成的字符串分组
        unordered_map<string, vector<string>> hashMap;
        
        // 遍历输入的字符串向量
        for (string str : strs) {
            // 将字符串排序，作为映射的键
            string sortedStr = str;
            sort(sortedStr.begin(), sortedStr.end());
            // 将原始字符串添加到对应键的向量中
            hashMap[sortedStr].push_back(str);
        }
        
        // 将映射的值（分组）转换为向量，并返回结果
        vector<vector<string>> result;
        for (auto& pair : hashMap) {
            result.push_back(pair.second);
        }
        return result;
    }
};

```

每个版本的所需基础知识：

Go 版本

- **Go 语言基础**: 了解 Go 语言的基本语法，包括变量声明、函数定义、条件语句、循环等。
- **切片 (Slices) 和映射 (Maps)**: 了解如何使用切片和映射来处理集合数据。在这个解决方案中，使用了切片和映射来组织和存储分组的
  Anagrams。
- **匿名函数 (Anonymous Functions)**: 了解如何定义匿名函数，如解决方案中的 `sign` 函数。
- **字符操作**: 了解如何处理字符串，包括字符的遍历和比较。

Python 版本

- **Python 基础**: 熟悉 Python 的基本语法，包括变量、列表、循环、条件语句等。
- **字典 (Dictionaries) 和列表 (Lists)**: 了解如何使用字典和列表来处理集合数据。在这个解决方案中，使用字典来组织和存储分组的
  Anagrams。
- **字符串操作**: 熟悉 Python 字符串的基本操作，包括字符串排序。
- **元组 (Tuples)**: 了解如何使用元组，如解决方案中的排序后的字符串元组。

Java 版本

- **Java 基础**: 理解 Java 的基本语法，包括类和方法的定义、循环、条件语句等。
- **集合框架 (Collections Framework)**: 了解 Java 集合框架，包括 `HashMap` 和 `ArrayList`
  的使用。在这个解决方案中，使用 `HashMap` 来组织和存储分组的 Anagrams。
- **字符操作和排序**: 熟悉 Java 中的字符操作，包括将字符串转换为字符数组并进行排序。

C++ 版本

- **C++ 基础**: 了解 C++ 的基本语法，包括变量声明、函数定义、循环、条件语句等。
- **STL (Standard Template Library)**: 熟悉 C++ STL，包括 `unordered_map` 和 `vector`
  的使用。在这个解决方案中，使用 `unordered_map` 来组织和存储分组的 Anagrams。
- **字符操作和排序**: 了解如何在 C++ 中处理字符串，包括将字符串排序。

无论你选择哪种语言的版本，都需要基本的编程知识，包括掌握基本的语法和数据结构操作，以便理解和修改这些解决方案。此外，了解算法的基本思想对理解这些代码也会有帮助。