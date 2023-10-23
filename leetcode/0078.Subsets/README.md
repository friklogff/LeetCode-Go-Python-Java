# [78. Subsets](https://leetcode.com/problems/subsets/)


## 题目

Given a set of **distinct** integers, *nums*, return all possible subsets (the power set).

**Note:** The solution set must not contain duplicate subsets.

**Example:**

    Input: nums = [1,2,3]
    Output:
    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]


## 题目大意

给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。说明：解集不能包含重复的子集。


## 解题思路

- 找出一个集合中的所有子集，空集也算是子集。且数组中的数字不会出现重复。用 DFS 暴力枚举即可。
- 这一题和第 90 题，第 491 题类似，可以一起解答和复习。
让我们分别介绍每个版本的解题思路：

**Go 版本**：

1. `subsets` 函数初始化一个空切片 `c` 用于存储当前生成的子集，以及一个空切片 `res` 用于存储最终的结果。

2. 使用一个循环来遍历不同大小的子集，从空集合开始到包含所有元素的集合。

3. 在每个循环中，调用 `generateSubsets` 函数来生成当前大小 `k` 的子集，并将其添加到 `res` 中。

4. `generateSubsets` 函数是一个递归函数，用于生成指定大小 `k` 的子集。它从 `start` 索引开始，依次将元素添加到 `c` 中，然后递归生成子集。

5. 当 `c` 中的元素数量达到 `k` 时，表示一个子集生成完成，将其添加到 `res` 中。

6. 在 `generateSubsets` 函数中，使用回溯操作来移除最后一个元素，以便尝试下一个元素。

**Python 版本**：

1. 与 Go 版本类似，Python 版本使用递归和循环来生成子集。

2. `subsets` 函数初始化一个空列表 `res` 用于存储最终的结果。

3. 使用一个循环来遍历不同大小的子集，从空集合开始到包含所有元素的集合。

4. 在每个循环中，调用 `generateSubsets` 函数来生成当前大小 `k` 的子集，并将其添加到 `res` 中。

5. `generateSubsets` 函数是一个递归函数，用于生成指定大小 `k` 的子集。它从 `start` 索引开始，依次将元素添加到 `c` 中，然后递归生成子集。

6. 当 `c` 中的元素数量达到 `k` 时，表示一个子集生成完成，将其添加到 `res` 中。

7. 在 `generateSubsets` 函数中，使用回溯操作来移除最后一个元素，以便尝试下一个元素。

**Java 版本**：

1. Java 版本同样使用递归和回溯来生成子集。

2. `subsets` 函数初始化一个空的 `ArrayList` 对象 `res` 用于存储最终的结果。

3. 在 `subsets` 函数中，调用辅助函数 `generateSubsets` 来生成子集。

4. `generateSubsets` 函数是一个递归函数，用于生成子集。它将当前子集 `subset` 加入到 `res` 中，然后从 `start` 索引开始逐个添加元素，递归生成子集。

5. 当 `subset` 达到目标大小时，将其加入到 `res` 中，然后进行回溯操作，移除最后一个元素，以便尝试下一个元素。

**C++ 版本**：

1. C++ 版本与其他版本类似，使用递归和回溯来生成子集。

2. `subsets` 函数初始化一个空的向量 `res` 用于存储最终的结果。

3. 在 `subsets` 函数中，调用辅助函数 `generateSubsets` 来生成子集。

4. `generateSubsets` 函数是一个递归函数，用于生成子集。它将当前子集 `subset` 加入到 `res` 中，然后从 `start` 索引开始逐个添加元素，递归生成子集。

5. 当 `subset` 达到目标大小时，将其加入到 `res` 中，然后进行回溯操作，移除最后一个元素，以便尝试下一个元素。

总的来说，不论使用哪种编程语言，解题思路都是使用递归和回溯技术来生成不同大小的子集，然后将这些子集添加到结果集中。递归的基本思想是生成一个子集，然后递归生成下一个子集，直到达到目标大小。回溯操作用于维护和移除生成子集的元素，以便尝试其他可能性。这种方法能够生成所有可能的子集，包括空集。
## 代码

## Go

```Go
// 定义一个函数 subsets，它接受一个整数数组 nums，返回这个数组的所有子集。
func subsets(nums []int) [][]int {
    // c 用于暂时存储正在生成的子集，res 用于存储所有生成的子集。
    c, res := []int{}, [][]int{}
    
    // 通过循环生成不同大小的子集，从空集合到包含全部元素的集合。
    for k := 0; k <= len(nums); k++ {
        // 调用 generateSubsets 函数来生成当前大小 k 的子集，并将其加入 res 中。
        generateSubsets(nums, k, 0, c, &res)
    }
    
    // 返回所有生成的子集。
    return res
}

// 定义一个辅助函数 generateSubsets，用于生成指定大小的子集。
func generateSubsets(nums []int, k, start int, c []int, res *[][]int) {
    // 如果 c 中的元素数量达到了 k，表示一个子集生成完成。
    if len(c) == k {
        // 创建一个新的切片 b，将 c 的内容复制到 b 中，然后将 b 加入到结果集 res 中。
        b := make([]int, len(c))
        copy(b, c)
        *res = append(*res, b)
        return
    }
    
    // 在数组 nums 中，从索引 start 开始，依次将元素加入 c 中，然后递归生成子集。
    // i 最多会到达 len(nums) - (k - len(c)) + 1
    for i := start; i < len(nums) - (k - len(c)) + 1; i++ {
        c = append(c, nums[i]) // 将 nums[i] 加入 c 中
        generateSubsets(nums, k, i+1, c, res) // 递归生成子集，下一轮的起始索引为 i+1
        c = c[:len(c)-1] // 回溯操作，将最后一个元素从 c 中移除，以便尝试下一个元素。
    }
    return
}

```

## Python

```Python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def generate_subsets(nums, k, start, c, res):
            if len(c) == k:
                res.append(c[:])
                return
            for i in range(start, len(nums) - (k - len(c)) + 1):
                c.append(nums[i])
                generate_subsets(nums, k, i + 1, c, res)
                c.pop()
        
        res = []
        for k in range(len(nums) + 1):
            generate_subsets(nums, k, 0, [], res)
        return res

```

## Java

```Java
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        
        // 辅助函数用于递归生成子集
        generateSubsets(nums, 0, new ArrayList<Integer>(), res);
        
        return res;
    }
    
    private void generateSubsets(int[] nums, int start, List<Integer> subset, List<List<Integer>> res) {
        res.add(new ArrayList<>(subset)); // 将当前子集加入结果集
        
        for (int i = start; i < nums.length; i++) {
            subset.add(nums[i]);
            generateSubsets(nums, i + 1, subset, res); // 递归生成子集，下一轮的起始索引为 i+1
            subset.remove(subset.size() - 1); // 回溯操作，将最后一个元素移除
        }
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> subset;
        
        // 辅助函数用于递归生成子集
        generateSubsets(nums, 0, subset, res);
        
        return res;
    }
    
    void generateSubsets(vector<int>& nums, int start, vector<int>& subset, vector<vector<int>>& res) {
        res.push_back(subset); // 将当前子集加入结果集
        
        for (int i = start; i < nums.size(); i++) {
            subset.push_back(nums[i]);
            generateSubsets(nums, i + 1, subset, res); // 递归生成子集，下一轮的起始索引为 i+1
            subset.pop_back(); // 回溯操作，将最后一个元素移除
        }
    }
};

```
理解并解释每个版本的代码需要掌握的基础知识：

1. **Go 版本**：

   - **切片（Slices）**：Go 中的切片是动态数组，用于存储元素的有序集合。在该版本的代码中，切片用于存储当前生成的子集 `c` 和最终的结果集 `res`。
   
   - **递归（Recursion）**：这个解决方案使用递归来生成子集。理解递归的工作原理和如何处理递归堆栈很重要。

   - **循环（Loops）**：在 `subsets` 函数中使用了循环，以便生成不同大小的子集。

2. **Python 版本**：

   - **递归（Recursion）**：与 Go 版本一样，Python 版本也使用递归生成子集。

   - **列表（Lists）**：Python 中的列表用于存储元素的有序集合，类似于 Go 中的切片。在该版本的代码中，列表用于存储当前生成的子集 `c` 和最终的结果集 `res`。

3. **Java 版本**：

   - **递归（Recursion）**：Java 版本使用递归来生成子集。

   - **列表（Lists）**：Java 中使用 `List` 接口和 `ArrayList` 类来表示集合。在该版本的代码中，列表用于存储当前生成的子集 `subset` 和最终的结果集 `res`。

   - **回溯（Backtracking）**：这个解决方案使用回溯技术来处理生成子集的过程。了解如何回溯和维护状态是关键。

4. **C++ 版本**：

   - **递归（Recursion）**：与其他版本一样，C++ 版本也使用递归生成子集。

   - **向量（Vectors）**：C++ 中的向量（`vector`）类似于动态数组，用于存储元素的有序集合。在该版本的代码中，向量用于存储当前生成的子集 `subset` 和最终的结果集 `res`。

   - **回溯（Backtracking）**：与 Java 版本一样，这个解决方案使用回溯技术来处理生成子集的过程。

总的来说，要理解这些版本的代码，需要熟悉所用编程语言的基本语法和数据结构，特别是与列表或切片相关的概念。此外，理解递归和回溯的概念对于理解这些解决方案非常重要，因为它们是用于生成子集的关键技术。
