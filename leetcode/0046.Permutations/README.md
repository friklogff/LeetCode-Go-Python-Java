# [46. Permutations](https://leetcode.com/problems/permutations/)


## 题目

Given a collection of **distinct** integers, return all possible permutations.

**Example:**


    Input: [1,2,3]
    Output:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]


## 题目大意

给定一个没有重复数字的序列，返回其所有可能的全排列。


## 解题思路

- 求出一个数组的排列组合中的所有排列，用 DFS 深搜即可。

Go 版本解题思路：

1. **深度优先搜索 (DFS)：** 这个解法使用深度优先搜索算法来生成所有可能的排列。
   
2. **DFS 递归函数：** 在 `dfs` 函数中，我们维护了两个重要的参数：`path` 和 `visited`。`path` 存储当前正在生成的排列，`visited` 用于标记哪些数字已经被使用过。

3. **递归过程：** 在每次递归调用中，我们尝试将未被使用过的数字添加到 `path` 中，并标记为已使用。然后，递归调用 `dfs` 函数，继续生成下一个数字。递归的结束条件是 `path` 的长度等于输入数组 `nums` 的长度，表示已经生成了一个完整的排列。

4. **回溯：** 当递归返回时，我们需要回溯（backtrack）到上一层状态。这包括将最后一个添加到 `path` 的数字移除，并将其对应的 `visited` 标记设为未使用，以便在下一次迭代中尝试其他数字。

5. **结果收集：** 每当我们找到一个完整的排列时，将其复制到一个结果集中（`ans`），最终返回所有的排列。

Python 版本解题思路：

1. **深度优先搜索 (DFS)：** 这个解法同样使用深度优先搜索算法来生成所有可能的排列。

2. **DFS 递归函数：** 在 `trackback` 函数中，我们维护了三个重要参数：`curr` 存储当前正在生成的排列，`used` 存储已经使用的数字的索引，`nums` 是输入数组。

3. **递归过程：** 在每次递归调用中，我们循环遍历未被使用过的数字（通过检查 `used` 列表），将其添加到 `curr` 中，并将对应的索引添加到 `used` 中。然后，递归调用 `trackback` 函数，继续生成下一个数字。递归的结束条件是 `curr` 的长度等于输入数组 `nums` 的长度，表示已经生成了一个完整的排列。

4. **回溯：** 当递归返回时，我们需要回溯（backtrack）到上一层状态。这包括将最后一个添加到 `curr` 的数字移除，并将其对应的索引从 `used` 中移除，以便在下一次迭代中尝试其他数字。

5. **结果收集：** 每当我们找到一个完整的排列时，将其添加到结果集中，并最终返回所有的排列。

Java 版本解题思路：

1. **深度优先搜索 (DFS)：** 这个解法同样使用深度优先搜索算法来生成所有可能的排列。

2. **DFS 递归函数：** 在 `dfs` 函数中，我们维护了三个重要参数：`nums` 是输入数组，`path` 存储当前正在生成的排列，`visited` 是一个布尔数组，用于标记哪些数字已经被使用过。

3. **递归过程：** 在每次递归调用中，我们循环遍历未被使用过的数字，将其添加到 `path` 中，并标记为已使用。然后，递归调用 `dfs` 函数，继续生成下一个数字。递归的结束条件是 `path` 的长度等于输入数组 `nums` 的长度，表示已经生成了一个完整的排列。

4. **回溯：** 当递归返回时，我们需要回溯（backtrack）到上一层状态。这包括将最后一个添加到 `path` 的数字移除，并将其对应的索引的 `visited` 标记设为未使用，以便在下一次迭代中尝试其他数字。

5. **结果收集：** 每当我们找到一个完整的排列时，将其添加到结果集中（`ans`），最终返回所有的排列。

C++ 版本解题思路：

1. **深度优先搜索 (DFS)：** 这个解法同样使用深度优先搜索算法来生成所有可能的排列。

2. **DFS 递归函数：** 在 `dfs` 函数中，我们维护了四个重要参数：`nums` 是输入数组，`currentPermutation` 存储当前正在生成的排列，`visited` 是一个布尔数组，用于标记哪些数字已经被使用过，`ans` 是用于存储所有排列的结果。

3. **递归过程：** 在每次递归调用中，我们循环遍历未被使用过的数字，将其添加到 `currentPermutation` 中，并标记为已使用。然后，递归调用 `dfs` 函数，继续生成下一个数字。递归的结束条件是 `currentPermutation` 的长度等于输入数组 `nums` 的长度，表示已经生成了一个完整的排列。

4. **回溯：** 当递归返回时，我们需要回溯（backtrack）到上一层状态。这包括将最后一个添加到 `currentPermutation` 的数字移除，并将其对应的索引的 `visited` 标记设为未使用，以便在下一次迭代中尝试其他数字。

5. **结果收集：** 每当我们找到一个完整的排列时，将其添加到结果集 `ans` 中，最终返回所有的排列。

## 代码

## Go

```Go
func permute(nums []int) [][]int {
    var ans [][]int
    var dfs func(path []int, visited []bool)

    dfs = func(path []int, visited []bool) {
        if len(path) == len(nums) {
            temp := make([]int, len(path))
            copy(temp, path)
            ans = append(ans, temp)
            return
        }

        for i := 0; i < len(nums); i++ {
            if visited[i] {
                continue
            }
            path = append(path, nums[i])
            visited[i] = true
            dfs(path, visited)
            visited[i] = false
            path = path[:len(path)-1]
        }
    }

    visited := make([]bool, len(nums))
    dfs([]int{}, visited)
    return ans
}

```

## Python

```Python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.trackback([], [], nums, res)
        return res
        
    def trackback(self, curr, used, nums, res):
        if len(curr) == len(nums):
            res.append(curr)
            return
        else:
            for i in range(len(nums)):
                if i not in used:
                    self.trackback(curr+[nums[i]], used+[i], nums, res)
```

## Java

```Java
class Solution {
    List<List<Integer>> ans;  // 用于存储所有全排列的结果
    public List<List<Integer>> permute(int[] nums) {
        ans = new ArrayList<>();
        boolean[] visited = new boolean[nums.length];  // 用于标记数字是否已经被访问
        dfs(nums, new ArrayList<Integer>(), visited);  // 调用深度优先搜索函数
        return ans;  // 返回所有全排列的结果
    }

    public void dfs(int[] nums, List<Integer> path, boolean[] visited) {
        if (path.size() == nums.length) {  // 如果当前路径的长度等于数组长度，表示找到了一个全排列
            ans.add(new ArrayList<>(path));  // 将当前路径加入结果集
            return;  // 返回上一层继续搜索
        }

        for (int i = 0; i < nums.length; i++) {
            if (visited[i]) {
                continue;  // 如果数字已经被访问过，则跳过
            }
            path.add(nums[i]);  // 将数字加入当前路径
            visited[i] = true;  // 标记数字已经被访问
            dfs(nums, path, visited);  // 递归搜索下一层
            visited[i] = false;  // 恢复标记，以便尝试其他可能的数字
            path.remove(path.size() - 1);  // 移除最后一个数字，回溯到上一层状态
        }
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> currentPermutation;
        vector<bool> visited(nums.size(), false);

        dfs(nums, currentPermutation, visited, ans);

        return ans;
    }

    void dfs(vector<int>& nums, vector<int>& currentPermutation, vector<bool>& visited, vector<vector<int>>& ans) {
        if (currentPermutation.size() == nums.size()) {
            ans.push_back(currentPermutation);
            return;
        }

        for (int i = 0; i < nums.size(); i++) {
            if (!visited[i]) {
                currentPermutation.push_back(nums[i]);
                visited[i] = true;
                dfs(nums, currentPermutation, visited, ans);
                visited[i] = false;
                currentPermutation.pop_back();
            }
        }
    }
};

```
每个版本中需要掌握的基础知识：

Go 版本：

1. **基础知识**：
   - Go 语言的基本语法，包括变量、函数、循环、条件语句等。
   - 切片（Slice）：Go 中的可变长度数组，用于动态存储数据。
   - 递归：了解递归的概念和使用方法，因为这里使用了递归来生成全排列。

2. **DFS（深度优先搜索）**：
   - 理解深度优先搜索算法的工作原理，它是解决组合和排列问题的常见方法。
   - 在递归函数中如何维护状态，包括路径和访问标记。

Python 版本：

1. **基础知识**：
   - Python 的基本语法，包括列表、循环、条件语句等。
   - 列表（List）：Python 中的可变序列，用于存储多个元素。
   - 递归：了解递归的概念和使用方法，因为这里使用了递归来生成全排列。

2. **DFS（深度优先搜索）**：
   - 理解深度优先搜索算法的工作原理，它是解决组合和排列问题的常见方法。
   - 在递归函数中如何维护状态，包括当前排列、已使用元素列表等。

Java 版本：

1. **基础知识**：
   - Java 语言的基本语法，包括类、方法、数组、循环、条件语句等。
   - 列表（List）：Java 中的集合类，用于存储多个元素。
   - 递归：了解递归的概念和使用方法，因为这里使用了递归来生成全排列。

2. **DFS（深度优先搜索）**：
   - 理解深度优先搜索算法的工作原理，它是解决组合和排列问题的常见方法。
   - 在递归函数中如何维护状态，包括当前排列、已使用元素的标记数组等。

C++ 版本：

1. **基础知识**：
   - C++ 的基本语法，包括类、函数、数组、循环、条件语句等。
   - 向量（Vector）：C++ 中的可变长度数组，用于存储多个元素。
   - 递归：了解递归的概念和使用方法，因为这里使用了递归来生成全排列。

2. **DFS（深度优先搜索）**：
   - 理解深度优先搜索算法的工作原理，它是解决组合和排列问题的常见方法。
   - 在递归函数中如何维护状态，包括当前排列、已使用元素的标记数组等。

无论选择哪个版本，理解深度优先搜索和递归的概念是关键。这些代码示例都展示了如何使用深度优先搜索来解决排列问题，其中递归是核心的思维方式。同时，了解每种编程语言的语法和数据结构也是很重要的，因为它们在不同语言中可能会有不同的实现方式。