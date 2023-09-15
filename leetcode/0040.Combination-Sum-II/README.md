# [40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)

## 题目

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations
in`candidates`where the candidate numbers sums to`target`.

Each number in`candidates`may only be used**once**in the combination.

**Note:**

- All numbers (including`target`) will be positive integers.
- The solution set must not contain duplicate combinations.

**Example 1:**

    Input: candidates = [10,1,2,7,6,1,5], target = 8,
    A solution set is:
    [
      [1, 7],
      [1, 2, 5],
      [2, 6],
      [1, 1, 6]
    ]

**Example 2:**

    Input: candidates = [2,5,2,1,2], target = 5,
    A solution set is:
    [
      [1,2,2],
      [5]
    ]

## 题目大意

给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

## 解题思路


### Go 版本解题思路

1. **排序候选数组**: 首先，对给定的 `candidates` 数组进行排序。这是为了方便后续去重操作，相同的元素会相邻排列。

2. **使用递归进行搜索**: 使用递归函数 `findcombinationSum2` 来搜索符合条件的组合。函数的参数包括当前的 `candidates` 数组，目标值 `target`，当前搜索的起始位置 `index`，当前正在构建的组合 `c`，以及结果列表 `res`。

3. **递归搜索**: 在递归搜索中，首先检查是否已经达到目标值 `target`，如果是，则将当前组合 `c` 添加到结果列表 `res` 中。

4. **遍历候选数**: 遍历 `candidates` 数组中的元素，从当前的 `index` 开始。在遍历的过程中，注意进行去重操作，如果当前元素和前一个元素相同，就跳过，以避免重复组合。

5. **构建组合**: 对于每个合法的候选数，将它添加到当前组合 `c` 中，并更新目标值 `target`。然后，递归调用 `findcombinationSum2` 函数，继续搜索。

6. **回溯操作**: 在递归调用返回后，需要进行回溯操作，将最后添加的候选数移出当前组合 `c`，以便继续搜索其他可能的组合。

7. **返回结果**: 最终，返回结果列表 `res`，其中包含了所有符合条件的唯一组合。

### Python 版本解题思路

Python 版本的解题思路与 Go 版本类似，但使用了 Python 特定的语法和函数。以下是解题思路：

1. **排序候选数组**: 首先，对给定的 `candidates` 列表进行排序。这是为了方便后续去重操作，相同的元素会相邻排列。

2. **使用递归进行搜索**: 使用递归函数 `dfs` 来搜索符合条件的组合。函数的参数包括当前的 `candidates` 列表，目标值 `target`，当前搜索的起始位置 `start`，当前正在构建的组合 `sub`，以及结果列表 `res`。

3. **递归搜索**: 在递归搜索中，首先检查是否已经达到目标值 `target`，如果是，则将当前组合 `sub` 添加到结果列表 `res` 中。

4. **遍历候选数**: 遍历 `candidates` 列表中的元素，从当前的 `start` 开始。在遍历的过程中，注意进行去重操作，如果当前元素和前一个元素相同，就跳过，以避免重复组合。

5. **构建组合**: 对于每个合法的候选数，将它添加到当前组合 `sub` 中，并更新目标值 `target`。然后，递归调用 `dfs` 函数，继续搜索。

6. **回溯操作**: 在递归调用返回后，需要进行回溯操作，将最后添加的候选数移出当前组合 `sub`，以便继续搜索其他可能的组合。

7. **返回结果**: 最终，返回结果列表 `res`，其中包含了所有符合条件的唯一组合。

### Java 版本解题思路

Java 版本的解题思路与 Python 版本类似，但使用了 Java 特定的语法和集合类。以下是解题思路：

1. **排序候选数组**: 首先，对给定的 `candidates` 数组进行排序。这是为了方便后续去重操作，相同的元素会相邻排列。

2. **使用匿名内部类进行搜索**: 使用匿名内部类来实现 `AbstractList` 接口，该类重写了 `get` 和 `size` 方法，以便实现结果列表的惰性生成。

3. **递归搜索**: 在递归搜索中，首先检查是否已经达到目标值 `target`，如果是，则将当前组合添加到结果列表中。

4. **遍历候选数**: 遍历 `candidates` 数组中的元素，从当前的起始位置开始。在遍历的过程中，注意进行去重操作，如果当前元素和前一个元素相同，就跳过，以避免重复组合。

5. **构建组合**: 对于每个合法的候选数，将它添加到当前组合中，并更新目标值。然后，递归调用搜索函数，继续搜索。

6. **回溯操作**: 在递归调用返回后，需要进行回溯操作，将最后添加的候选数移出当前组合，以便继续搜索其他可能的组合。

7. **返回结果**: 最终，返回结果列表，其中包含了所有符合条件的唯一组合。

### C++ 版本解题思路

C++ 版本的解题思路与 Python 版本类似，但使用了 C++ 特定的语法和标准库函数。以下是解题思路：

1. **排序候选数组**: 首先，对给定的 `candidates` 向量进行排序。这是为了方便后续去重操作，相同的元素会相邻排列。

2. **使用递归进行搜索 (continued)**: 在递归搜索中，首先检查是否已经达到目标值 `target`，如果是，则将当前组合 `currentCombination` 添加到结果向量 `result` 中。

3. **遍历候选数**: 遍历 `candidates` 向量中的元素，从当前的 `index` 开始。在遍历的过程中，注意进行去重操作，如果当前元素和前一个元素相同，就跳过，以避免重复组合。

4. **构建组合**: 对于每个合法的候选数，将它添加到当前组合 `currentCombination` 中，并更新目标值 `target`。然后，递归调用 `findCombinationSum2` 函数，继续搜索。

5. **回溯操作**: 在递归调用返回后，需要进行回溯操作，将最后添加的候选数移出当前组合 `currentCombination`，以便继续搜索其他可能的组合。

6. **返回结果**: 最终，返回结果向量 `result`，其中包含了所有符合条件的唯一组合。


## 代码

## Go

```Go
import (
    "sort"
)

func combinationSum2(candidates []int, target int) [][]int {
    if len(candidates) == 0 {
        return [][]int{}
    }
    c, res := []int{}, [][]int{}
    sort.Ints(candidates) // 这里是去重的关键逻辑
    findcombinationSum2(candidates, target, 0, c, &res)
    return res
}

func findcombinationSum2(nums []int, target, index int, c []int, res *[][]int) {
    if target == 0 {
        b := make([]int, len(c))
        copy(b, c)
        *res = append(*res, b)
        return
    }
    for i := index; i < len(nums); i++ {
        if i > index && nums[i] == nums[i-1] { // 这里是去重的关键逻辑,本次不取重复数字，下次循环可能会取重复数字
            continue
        }
        if target >= nums[i] {
            c = append(c, nums[i])
            findcombinationSum2(nums, target-nums[i], i+1, c, res)
            c = c[:len(c)-1]
        }
    }
}
```

## Python

```Python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # 对候选数组进行排序，以便去重
        res = []  # 用于存储最终结果的列表

        def dfs(candidates, start, sub, subTarget):
            if subTarget == 0:  # 当子目标值为0时，表示找到了一个组合
                res.append(sub)
                return
            if subTarget < 0:  # 当子目标值小于0时，不符合条件，直接返回
                return

            for i in range(start, len(candidates)):
                if candidates[i] > subTarget:
                    break  # 剪枝：如果当前候选数大于子目标值，跳出循环
                if i > start and candidates[i] == candidates[i - 1]:
                    continue  # 去重逻辑：跳过重复的候选数

                # 递归调用，尝试将当前候选数加入子组合，并更新子目标值和下一次搜索的起始位置
                dfs(candidates, i + 1, sub + [candidates[i]], subTarget - candidates[i])

        dfs(candidates, 0, [], target)  # 初始调用 DFS
        return res  # 返回最终结果

```

## Java

```Java
import java.util.AbstractList;

class Solution {
    public static List<List<Integer>> combinationSum2(int[] candidates, int target) {
        return new AbstractList<List<Integer>>() { // 创建一个继承自 AbstractList 的匿名内部类
            private final List<List<Integer>> list = new ArrayList<>(); // 存储最终结果的列表
            private final List<Integer> comb = new ArrayList<>(); // 存储当前组合的列表

            @Override
            public List<Integer> get(int index) {
                init(); // 初始化，确保结果列表已经生成
                return list.get(index); // 返回指定索引处的组合
            }

            @Override
            public int size() {
                init(); // 初始化，确保结果列表已经生成
                return list.size(); // 返回结果列表的大小
            }

            public void init() {
                if (list.isEmpty()) { // 如果结果列表为空，进行初始化操作
                    Arrays.sort(candidates); // 对候选数组进行排序，以便进行去重和优化
                    getComb(target, 0); // 调用递归函数生成组合
                }
            }

            public void getComb(int target, int beginIndex) {
                if (target == 0) { // 当目标值为0时，表示找到一个组合
                    list.add(new ArrayList<>(comb)); // 将当前组合添加到结果列表中
                    return;
                }
                for (int i = beginIndex; i < candidates.length; i++) {
                    if (candidates[i] > target) {
                        return; // 剪枝：如果当前候选数大于目标值，直接返回，不再继续搜索
                    }
                    comb.add(candidates[i]); // 将当前候选数加入组合
                    getComb(target - candidates[i], i + 1); // 递归调用，更新目标值和起始位置
                    comb.remove(comb.size() - 1); // 回溯，移除最后一个候选数
                    while (i + 1 < candidates.length && candidates[i + 1] == candidates[i]) {
                        i++; // 去重逻辑：跳过重复的候选数
                    }
                }
            }
        };
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> result; // 存储最终结果的二维向量
        vector<int> currentCombination; // 存储当前组合的一维向量

        if (candidates.empty()) {
            return result; // 如果候选数组为空，直接返回空结果
        }

        sort(candidates.begin(), candidates.end()); // 对候选数组进行排序，以便进行去重和优化
        findCombinationSum2(candidates, target, 0, currentCombination, result); // 调用递归函数生成组合

        return result;
    }

private:
    void findCombinationSum2(vector<int>& candidates, int target, int index, vector<int>& currentCombination, vector<vector<int>>& result) {
        if (target == 0) { // 当目标值为0时，表示找到一个组合
            result.push_back(currentCombination); // 将当前组合添加到结果中
            return;
        }

        for (int i = index; i < candidates.size(); i++) {
            if (i > index && candidates[i] == candidates[i - 1]) {
                continue; // 去重逻辑：跳过重复元素
            }

            if (target >= candidates[i]) {
                currentCombination.push_back(candidates[i]); // 添加当前候选数到组合中
                findCombinationSum2(candidates, target - candidates[i], i + 1, currentCombination, result); // 递归调用，更新目标值和起始位置
                currentCombination.pop_back(); // 回溯，移除当前候选数
            }
        }
    }
};

```
当我们分别介绍每个版本的代码时，我会详细解释每种编程语言的基础知识要求。以下是每个版本的说明：

### Go 版本

Go 是一种静态类型的编程语言，如果您要理解 Go 版本的代码，需要掌握以下基础知识：

1. **变量和数据类型**: 了解如何声明变量和使用不同的数据类型，例如整数、切片、数组和切片等。

2. **函数**: 了解如何定义和调用函数，以及函数的参数和返回值。

3. **切片和数组**: 了解 Go 中的切片和数组，它们在此代码中用于存储组合。

4. **递归**: 理解递归的概念和工作原理，因为代码使用递归来查找组合。

5. **排序**: 理解如何使用 `sort` 包对切片进行排序，以进行去重。

6. **循环和条件语句**: 理解如何使用循环和条件语句来控制程序的流程。

### Python 版本

Python 是一种简单而强大的编程语言，如果您要理解 Python 版本的代码，需要掌握以下基础知识：

1. **变量和数据类型**: 了解如何声明变量和使用不同的数据类型，例如整数、列表和元组等。

2. **函数**: 了解如何定义和调用函数，以及函数的参数和返回值。

3. **列表**: 了解 Python 中的列表，它们在此代码中用于存储组合。

4. **递归**: 理解递归的概念和工作原理，因为代码使用递归来查找组合。

5. **排序**: 了解如何使用 `sorted` 函数对列表进行排序，以进行去重。

6. **循环和条件语句**: 理解如何使用循环和条件语句来控制程序的流程。

### Java 版本


1. **类和对象**: 了解如何定义类和创建对象，因为 Java 是面向对象的语言。

2. **方法**: 了解如何定义和调用方法，以及方法的参数和返回值。

3. **列表和集合**: 了解 Java 中的列表和集合，它们在此代码中用于存储组合。

4. **递归**: 理解递归的概念和工作原理，因为代码使用递归来查找组合。

5. **排序**: 了解如何使用 `Collections.sort` 方法对列表进行排序，以进行去重。

6. **循环和条件语句**: 理解如何使用循环和条件语句来控制程序的流程。

### C++ 版本

C++ 是一种多范式编程语言，如果您要理解 C++ 版本的代码，需要掌握以下基础知识：

1. **变量和数据类型**: 了解如何声明变量和使用不同的数据类型，例如整数、向量和数组等。

2. **函数**: 了解如何定义和调用函数，以及函数的参数和返回值。

3. **向量和数组**: 了解 C++ 中的向量和数组，它们在此代码中用于存储组合。

4. **递归**: 理解递归的概念和工作原理，因为代码使用递归来查找组合。

5. **排序**: 了解如何使用标准库的 `sort` 函数对向量进行排序，以进行去重。

6. **循环和条件语句**: 理解如何使用循环和条件语句来控制程序的流程。

以上是每个版本代码所需的基础知识要求。您可以根据您的编程语言偏好选择其中一个版本，并深入学习相关的语言特性和库函数，以更好地理解和修改代码。