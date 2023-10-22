# [77. Combinations](https://leetcode.com/problems/combinations/)


## 题目

Given two integers *n* and *k*, return all possible combinations of *k* numbers out of 1 ... *n*.

**Example:**

    Input: n = 4, k = 2
    Output:
    [
      [2,4],
      [3,4],
      [2,3],
      [1,2],
      [1,3],
      [1,4],
    ]

## 题目大意

给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

## 解题思路

- 计算排列组合中的组合，用 DFS 深搜即可，注意剪枝
- 下面分别介绍每个版本的解题思路：

Go 版本解题思路：

1. **组合问题**：给定一个范围从 1 到 `n`，要求生成所有长度为 `k` 的组合。

2. **DFS 深度搜索**：使用深度优先搜索 (DFS) 来生成所有可能的组合。

3. **剪枝 (Pruning)**：在搜索过程中，采用剪枝策略来减少不必要的搜索。如果当前已选的元素个数超过 `k`，则停止向下搜索，这是剪枝的一种情况。

4. **遍历范围**：从 1 开始遍历到 `n - (k - len(path)) + 1`，其中 `len(path)` 是当前已选元素的个数。这个范围的选择是为了确保生成的组合不会超出 `k` 个元素。

5. **组合存储**：用一个切片 (`path`) 来存储当前正在生成的组合，当达到长度为 `k` 时，将其复制并添加到结果中。

Python 版本解题思路：

1. **组合问题**：给定一个范围从 1 到 `n`，要求生成所有长度为 `k` 的组合。

2. **DFS 深度搜索**：使用深度优先搜索 (DFS) 来生成所有可能的组合。

3. **Memoization**：采用 memoization 技巧，避免重复计算相同子问题，提高递归性能。

4. **递归函数**：定义递归函数 `dfsHelper(start, k)`，其中 `start` 表示当前数字的起始点，`k` 表示剩余需要选的数字个数。

5. **基本情况**：在递归函数中，处理基本情况。当 `k` 为 0 时，返回一个包含空列表的列表，表示找到一个组合。

6. **生成组合**：递归地生成组合，包括当前数字 (`start`) 和不包括当前数字两种情况。

7. **返回结果**：返回生成的组合结果。

Java 版本解题思路：

1. **组合问题**：给定一个范围从 1 到 `n`，要求生成所有长度为 `k` 的组合。

2. **深度优先搜索 (DFS)**：使用深度优先搜索 (DFS) 来生成所有可能的组合。

3. **抽象类和匿名子类**：在 Java 中，定义了一个抽象类来封装组合生成的逻辑，并创建一个匿名子类来提供更方便的接口。

4. **递归函数**：定义递归函数 `dfsHelper(parentDepth, n, k)`，其中 `parentDepth` 表示上一级递归的深度，`n` 表示总的数字范围，`k` 表示还需要选择的数字个数。

5. **基本情况**：在递归函数中，处理基本情况。当 `k` 为 0 时，将当前组合添加到结果中。

6. **生成组合**：递归地生成组合，包括当前数字和不包括当前数字两种情况。

7. **返回结果**：返回生成的组合结果。

C++ 版本解题思路：

1. **组合问题**：给定一个范围从 1 到 `n`，要求生成所有长度为 `k` 的组合。

2. **DFS 深度搜索**：使用深度优先搜索 (DFS) 来生成所有可能的组合。

3. **Lambda 表达式**：在 C++ 中，使用 lambda 表达式来定义递归函数。

4. **递归函数**：定义递归函数 `dfsHelper(parentDepth)`，其中 `parentDepth` 表示上一级递归的深度。

5. **基本情况**：在递归函数中，处理基本情况。当当前组合的长度等于 `k` 时，将其添加到结果中。

6. **生成组合**：递归地生成组合，包括当前数字和不包括当前数字两种情况。

7. **返回结果**：返回生成的组合结果。

这些是不同版本的解题思路的关键要点，它们共同使用深度优先搜索 (DFS) 和递归来生成所有可能的组合，同时在某些版本中还使用了剪枝或 memoization 来优化性能。
## 代码

## Go

```Go
func combine(n int, k int) [][]int {
    result := make([][]int, 0)
    path := make([]int, 0)

    var backtracking func(n,k,startIndex int)
    backtracking = func(n,k,startIndex int) {
        if len(path) == k {
            tmp := make([]int, k)
            copy(tmp, path)
            result = append(result, tmp)
        }
        
        for i:=startIndex; i <= n - (k - len(path)) + 1; i++ {
            if len(path) > k{  // 剪枝
                break
            }
            path = append(path, i)
            backtracking(n,k,i+1)
            path = path[:len(path)-1]
        }
    }

    backtracking(n,k,1)
    return result
}
```

## Python

```Python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        memo = {}
        def dfs(start, k):
            if (start, k) in memo:
                return memo[(start, k)]

            if k == 0:
                return [[]]
            if start > n:
                return []
            if start == n:
                return [[n]] if k == 1 else []
            
            res = []

            # Generate combinations that include the "start" element
            for rest in dfs(start + 1, k - 1):
                res.append([start] + rest)

            # Add combinations that don't include the "start" element
            res.extend(dfs(start + 1, k))
            
            memo[(start, k)] = res
            return res
        
        return dfs(1, k)
```

## Java

```Java
// 导入Java的AbstractList类
import java.util.AbstractList;

// 创建一个Solution类
class Solution {
    private List<List<Integer>> res;

    // 定义公共方法combine，用于生成组合
    public List<List<Integer>> combine(int n, int k) {
        // 返回一个AbstractList的匿名子类实例
        return new AbstractList<List<Integer>>() {
            @Override
            public int size() {
                // 初始化并返回结果的大小
                init();
                return res.size();
            }

            @Override
            public List<Integer> get(int index) {
                // 初始化并返回指定索引的组合
                init();
                return res.get(index);
            }

            // 初始化组合的计算
            protected void init() {
                if (res != null)
                    return;
                res = new ArrayList<List<Integer>>();
                dfsHelper(-1, n, k, res, new ArrayList<Integer>());
            }
        };
    }

    // 定义深度优先搜索的辅助方法
    private void dfsHelper(int parentDepth, int n, int k, List<List<Integer>> res, List<Integer> subset) {
        parentDepth += 1;
        if (parentDepth == n) {
            if (subset.size() == k) {
                // 如果subset的大小为k，将其添加到结果res中
                res.add(new ArrayList<Integer>(subset));
            }
        } else {
            /* <-.前序决策左、右子结点: */

            // 递归调用dfsHelper，不包含当前数字
            dfsHelper(parentDepth, n, k, res, subset);

            // 将当前数字加入subset
            subset.add(parentDepth + 1);
            // 递归调用dfsHelper，包含当前数字
            dfsHelper(parentDepth, n, k, res, subset);
            // 移除最后添加的数字，以便尝试下一个数字
            subset.remove(subset.size() - 1);
        }
    }
}
```

## Cpp

```Cpp
class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> res;
        vector<int> subset;

        function<void(int)> dfsHelper = [&](int parentDepth) {
            if (subset.size() == k) {
                res.push_back(subset);
                return;
            }
            for (int i = parentDepth + 1; i <= n; i++) {
                subset.push_back(i);
                dfsHelper(i);
                subset.pop_back();
            }
        };

        dfsHelper(0);
        return res;
    }
};

```

理解不同版本的代码需要一些基本的编程和算法知识。以下是每个版本所需的基础知识的详细介绍：

Go 版本：

1. **Go 编程语言**：理解 Go 语言的基础语法，数据结构，以及函数的定义和使用。

2. **递归和深度优先搜索 (DFS)**：了解递归的概念和如何使用递归来解决问题。此外，理解深度优先搜索 (DFS) 是如何应用在这个代码中的。

3. **切片 (Slices)**：Go 中的切片是动态数组，它的长度可以动态变化。在这个代码中，切片被用于存储部分组合结果。

4. **剪枝 (Pruning)**：剪枝是一种优化技巧，用于减少搜索空间。在这个代码中，剪枝用于提前终止搜索不可能生成有效组合的情况。

Python 版本：

1. **Python 编程语言**：理解 Python 语言的基础语法，包括列表、字典、函数等。

2. **递归和深度优先搜索 (DFS)**：了解递归的概念和如何使用递归来解决问题。在这个代码中，深度优先搜索 (DFS) 用于生成组合。

3. **Memoization**：Memoization 是一种优化技巧，用于存储已计算的结果以避免重复计算。在这个代码中，memoization 被用于提高递归函数的性能。

Java 版本：

1. **Java 编程语言**：理解 Java 语言的基础语法，包括类、方法、集合类等。

2. **递归和深度优先搜索 (DFS)**：了解递归的概念和如何使用递归来解决问题。在这个代码中，深度优先搜索 (DFS) 用于生成组合。

3. **抽象类 (Abstract Class)**：了解抽象类的概念，它在这个代码中用于创建一个抽象的数据结构。

4. **匿名子类 (Anonymous Inner Class)**：理解匿名子类的概念，它用于在代码中创建一个匿名的子类。

C++ 版本：

1. **C++ 编程语言**：理解 C++ 语言的基础语法，包括类、函数、lambda 表达式等。

2. **递归和深度优先搜索 (DFS)**：了解递归的概念和如何使用递归来解决问题。在这个代码中，深度优先搜索 (DFS) 用于生成组合。

3. **Lambda 表达式**：理解 C++ 中的 lambda 表达式，它在这个代码中用于定义递归函数。

这些基础知识是理解和分析这些代码的关键要点。如果您对其中的某个概念不熟悉，建议深入学习相关的编程和算法知识，以便更好地理解这些代码。