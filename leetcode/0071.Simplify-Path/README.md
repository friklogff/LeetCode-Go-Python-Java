# [71. Simplify Path](https://leetcode.com/problems/simplify-path/)

## 题目

Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level. For more information, see: Absolute path vs relative path in Linux/Unix

Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the canonical path must be the shortest string representing the absolute path.



Example 1:

```c
Input: "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
```

Example 2:

```c
Input: "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
```
Example 3:

```c
Input: "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
```

Example 4:

```c
Input: "/a/./b/../../c/"
Output: "/c"
```


Example 5:

```c
Input: "/a/../../b/../c//.//"
Output: "/c"
```

Example 6:

```c
Input: "/a//b////c/d//././/.."
Output: "/a/b/c"
```

## 题目大意

给出一个 Unix 的文件路径，要求简化这个路径。这道题也是考察栈的题目。

## 解题思路

这道题笔者提交了好多次才通过，并不是题目难，而是边界条件很多，没考虑全一种情况就会出错。有哪些边界情况就看笔者的 test 文件吧。
当处理这个问题时，我们需要使用一个栈数据结构来辅助，以下是各个版本的解题思路：

**C++ 版本**

在C++版本中，我们使用了STL库中的`stack`容器来实现栈。算法思路如下：

1. 首先，我们将输入的路径按照斜杠`/`分割成目录列表。
2. 创建一个空的栈，遍历目录列表中的每个目录名。
3. 如果遇到普通目录名（不为空且不为`.`），将其入栈。
4. 如果遇到`..`，表示返回上一级目录，出栈一个目录。
5. 遍历完所有目录后，栈中的元素即为简化后的路径。
6. 最后，将栈中的元素连接起来，形成简化后的路径。

**Java 版本**

在Java版本中，我们使用`Stack`类来实现栈。算法思路如下：

1. 首先，将输入的路径按照斜杠`/`分割成目录列表。
2. 创建一个空的栈，遍历目录列表中的每个目录名。
3. 如果遇到普通目录名（不为空且不为`.`），将其入栈。
4. 如果遇到`..`，表示返回上一级目录，出栈一个目录。
5. 遍历完所有目录后，栈中的元素即为简化后的路径。
6. 最后，将栈中的元素连接起来，形成简化后的路径。

**Python 版本**

在Python版本中，我们使用列表（list）模拟栈的操作。算法思路如下：

1. 首先，将输入的路径按照斜杠`/`分割成目录列表。
2. 创建一个空的列表，遍历目录列表中的每个目录名。
3. 如果遇到普通目录名（不为空且不为`.`），将其加入列表。
4. 如果遇到`..`，表示返回上一级目录，出栈一个目录。
5. 遍历完所有目录后，列表中的元素即为简化后的路径。
6. 最后，将列表中的元素连接起来，形成简化后的路径。

**Go 版本**

在Go版本中，我们使用了内置的`stack`库实现栈。算法思路如下：

1. 首先，将输入的路径按照斜杠`/`分割成目录列表。
2. 创建一个空的栈，遍历目录列表中的每个目录名。
3. 如果遇到普通目录名（不为空且不为`.`），将其入栈。
4. 如果遇到`..`，表示返回上一级目录，出栈一个目录。
5. 遍历完所有目录后，栈中的元素即为简化后的路径。
6. 最后，将栈中的元素连接起来，形成简化后的路径。

以上就是各个版本的解题思路，它们的核心思想都是使用栈来模拟文件系统的路径，并根据`.`和`..`的出现进行相应的入栈和出栈操作，最终得到简化后的路径。希望这些解题思路能够帮助你更好地理解问题的解决方法！
## 代码

## Go

```Go
class Solution {
public:
    string simplifyPath(string path) {
        // 创建一个空栈
        stack<string> st;
        
        // 使用 "/" 字符来分割输入的路径字符串
        stringstream ss(path);
        string token;
        
        while (getline(ss, token, '/')) {
            if (token == "..") {
                // 如果遇到 ".." 表示要返回上一级目录
                if (!st.empty()) {
                    st.pop();
                }
            } else if (!token.empty() && token != ".") {
                // 如果不是空字符串或者当前目录 ".", 则入栈（表示进入下一级目录）
                st.push(token);
            }
        }
        
        // 使用 "/" 连接栈内的元素，形成简化后的路径
        string result = "";
        while (!st.empty()) {
            result = "/" + st.top() + result;
            st.pop();
        }
        
        return result.empty() ? "/" : result;
    }
};


```

## Python

```Python
class Solution:
    def simplifyPath(self, path: str) -> str:
        # 将输入路径按照斜杠分割成目录列表
        path_list = path.split("/")
        
        # 初始化一个空栈，用于存储简化后的路径
        stack = []

        # 遍历路径中的每个目录
        for item in path_list:
            # 如果当前目录是 ".."，则从栈中返回上一级目录（出栈）
            if item == "..":
                if stack:
                    stack.pop()
            # 如果当前目录不为空且不是 "."，则将其压入栈中
            elif item and item != '.':
                stack.append(item)

        # 通过连接栈中的目录，构建简化后的路径
        return "/" + "/".join(stack)

```

## Java

```Java
public class Solution {
    public String simplifyPath(String path) {
        // 如果输入的路径为空，则直接返回根目录 "/"
        if (path.length() == 0) return "/";

        // 初始化一个字符数组，用于存储简化后的路径
        char[] arr = new char[path.length()];
        arr[0] = '/'; // 将第一个字符设为根目录
        int len = 1; // 初始化简化路径的长度

        // 将输入路径字符串转换为字符数组
        char[] chars = path.toCharArray();
        int s = 0; // 用于遍历输入路径字符的索引

        // 遍历输入路径的字符
        while (s < chars.length) {
            // 跳过单个点（"."）
            if (chars[s] == '.' && (s == chars.length - 1 || chars[s + 1] == '/')) {
                s++;
                continue;
            }
            // 处理双点（".."）
            if (chars[s] == '.' && s + 1 < chars.length && chars[s + 1] == '.'
                    && (s + 1 == chars.length - 1 || chars[s + 2] == '/')) {
                // 返回到上一级目录（向上移动）
                while (len > 0 && arr[len - 1] != '/') len--;
                if (len > 1 && arr[len - 1] == '/') len--;
            } else if (chars[s] != '/') {
                // 如果当前字符不是斜杠（"/"）
                // 如果最后一个字符不是斜杠，则在简化路径中添加一个斜杠
                if (arr[len - 1] != '/') {
                    arr[len++] = '/';
                }
                // 将字符复制到简化路径，直到下一个斜杠
                while (s < chars.length && chars[s] != '/') {
                    arr[len++] = chars[s++];
                }
            }
            s++; // 移动到输入路径的下一个字符
        }

        // 从简化路径字符数组中创建新字符串
        return new String(arr, 0, len);
    }
}

```

## Cpp

```Cpp
#include <iostream>
#include <vector>
#include <sstream>

class Solution {
public:
    std::string simplifyPath(std::string path) {
        // 如果输入的路径为空，则直接返回根目录 "/"
        if (path.empty()) {
            return "/";
        }

        // 将输入路径按斜杠分割成目录列表
        std::vector<std::string> dirs;
        std::istringstream iss(path);
        std::string dir;

        // 用于存储简化后的路径的栈
        std::vector<std::string> stack;

        // 将目录分割后存入目录列表
        while (getline(iss, dir, '/')) {
            dirs.push_back(dir);
        }

        // 遍历目录列表
        for (const auto& dir : dirs) {
            // 跳过空目录和单个点（"."）
            if (dir.empty() || dir == ".") {
                continue;
            }
            // 处理双点（".."）
            else if (dir == "..") {
                // 如果栈不为空，则返回上一级目录（出栈）
                if (!stack.empty()) {
                    stack.pop_back();
                }
            } else {
                // 其他目录名入栈
                stack.push_back(dir);
            }
        }

        // 构建简化后的路径
        std::string simplified_path = "/";
        for (const auto& dir : stack) {
            simplified_path += dir + "/";
        }

        // 如果简化后的路径为空，返回根目录 "/"
        return simplified_path == "/" ? simplified_path : simplified_path.substr(0, simplified_path.size() - 1);
    }
};

 
```
当解决LeetCode上的算法问题时，无论使用哪种编程语言，都需要掌握以下基础知识：

1. **字符串操作**

- **C++/Java/Python**: 熟练使用字符串的拼接、切片、分割等操作。

  ```cpp
  std::string result = "/";
  result += dir;
  ```

  ```java
  String result = "/";
  result += dir;
  ```

  ```python
  result = result + "/" + dir
  ```

2. **数组或列表操作**

- **C++**: 使用STL库中的`vector`容器。

  ```cpp
  std::vector<std::string> stack;
  stack.push_back(dir);
  ```

- **Java**: 使用ArrayList或数组。

  ```java
  ArrayList<String> stack = new ArrayList<>();
  stack.add(dir);
  ```

- **Python**: 使用列表（list）。

  ```python
  stack.append(dir)
  ```

3. **栈（Stack）数据结构**

- **C++**: 使用STL库中的`stack`容器。

  ```cpp
  std::stack<std::string> st;
  st.push(dir);
  ```

- **Java**: 使用`Stack`类或者`LinkedList`实现栈。

  ```java
  Stack<String> stack = new Stack<>();
  stack.push(dir);
  ```

- **Python**: 利用列表模拟栈的操作。

  ```python
  stack.append(dir)
  ```

4. **流处理（仅针对C++和Java）**

- **C++**: 使用`istringstream`来分割字符串。

  ```cpp
  std::istringstream iss(path);
  std::string dir;
  while (getline(iss, dir, '/')) {
      // 处理目录
  }
  ```

- **Java**: 使用`StringTokenizer`或者`split`方法来分割字符串。

  ```java
  StringTokenizer tokenizer = new StringTokenizer(path, "/");
  while (tokenizer.hasMoreTokens()) {
      String dir = tokenizer.nextToken();
      // 处理目录
  }
  ```

5. **条件判断和循环**

- **C++/Java/Python**: 掌握`if`、`else if`、`else`条件判断语句和`while`、`for`循环语句的使用。

6. **面向对象编程（仅针对Java）**

- **Java**: 如果使用Java，需要了解类、对象、方法等面向对象编程的基本概念，以及如何定义和使用类。

以上是解决LeetCode算法问题时需要掌握的基础知识。对于不同编程语言，语法细节和一些特有的数据结构可能有所不同，但以上提到的基础知识是通用的。希望这些信息对你有所帮助，如果有任何疑问，请随时向我提问！