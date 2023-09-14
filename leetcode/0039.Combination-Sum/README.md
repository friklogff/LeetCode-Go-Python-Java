# [39. Combination Sum](https://leetcode.com/problems/combination-sum/)


## 题目

Given a **set** of candidate numbers (`candidates`) **(without duplicates)** and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sums to `target`.

The **same** repeated number may be chosen from `candidates` unlimited number of times.

**Note:**

- All numbers (including `target`) will be positive integers.
- The solution set must not contain duplicate combinations.

**Example 1:**


    Input: candidates = [2,3,6,7], target = 7,
    A solution set is:
    [
      [7],
      [2,2,3]
    ]


**Example 2:**


    Input: candidates = [2,3,5], target = 8,
    A solution set is:
    [
      [2,2,2,2],
      [2,3,3],
      [3,5]
    ]


## 题目大意

给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。


## 解题思路

以下是每个版本的解题思路的详细介绍：

Go 版本解题思路：

1. **切片初始化**：创建两个切片，`ret` 用于存储最终结果，`vals` 用于存储当前组合的临时值。

2. **排序**：对候选数集合 `candidates` 进行升序排序，这样可以在后续搜索中更方便地控制元素的使用。

3. **递归搜索**：定义名为 `backtracking` 的递归函数，它有三个参数：`start` 表示从候选数集合的哪个位置开始搜索，`sum` 表示当前组合的元素和。

4. **递归搜索逻辑**：在 `backtracking` 函数内部，首先检查 `sum` 是否等于 0。如果等于 0，说明找到了一个满足条件的组合，将当前的组合 `vals` 复制到一个临时切片中，并将该切片添加到结果 `ret` 中。

5. 遍历候选数集合：使用循环遍历候选数集合，从 `start` 开始，逐个考虑每个候选数。
   - 如果当前候选数大于 `sum`，说明后续的候选数也肯定大于 `sum`，因此可以提前结束循环（剪枝）。
   - 否则，将当前候选数添加到当前组合 `vals` 中，然后递归调用 `backtracking` 函数，继续搜索。
   - 在递归返回后，需要回溯，即将最后添加的候选数从 `vals` 中移除，以便尝试其他组合。

6. **调用递归函数**：最后，在 `combinationSum` 函数中调用 `backtracking` 函数，开始搜索组合。

7. **返回结果**：返回找到的所有组合，即 `ret` 切片。

Python 版本解题思路：

Python 版本的解题思路与 Go 版本基本相同，使用了相似的递归回溯方法和排序，但代码语法和列表操作略有不同。主要思路包括：

1. **列表初始化**：创建两个列表，`result` 用于存储最终结果，`current` 用于存储当前组合的临时值。

2. **排序**：对候选数列表 `candidates` 进行排序，以便在后续搜索中更容易控制元素的使用。

3. **递归搜索**：定义名为 `backtrack` 的递归函数，它有五个参数：`result` 用于存储结果，`current` 用于存储当前组合，`candidates` 是排序后的候选数列表，`target` 是目标和，`start` 是当前搜索的起始位置。

4. **递归搜索逻辑**：在 `backtrack` 函数内部，首先检查 `target` 是否等于 0。如果等于 0，说明找到了一个满足条件的组合，将当前组合 `current` 添加到结果 `result` 中。

5. **遍历候选数列表**：使用循环遍历候选数列表，从 `start` 开始，逐个考虑每个候选数。
   - 如果当前候选数小于或等于 `target`，将当前候选数添加到当前组合 `current` 中，然后递归调用 `backtrack` 函数，继续搜索。
   - 在递归返回后，需要回溯，即将最后添加的候选数从 `current` 中移除，以便尝试其他组合。

6. **调用递归函数**：在 `combinationSum` 函数中调用 `backtrack` 函数，开始搜索组合。

7. **返回结果**：返回找到的所有组合，即 `result` 列表。

Java 版本解题思路：

Java 版本的解题思路与 Python 版本相似，但使用了 Java 的 `ArrayList` 来存储结果和当前组合，以及 Java 的方法命名约定。主要思路包括：

1. **ArrayList 初始化**：创建两个 `ArrayList`，`result` 用于存储最终结果，`current` 用于存储当前组合的临时值。

2. **排序**：对候选数数组 `candidates` 进行排序，以便在后续搜索中更容易控制元素的使用。

3. **递归搜索**：定义名为 `backtrack` 的递归函数，它有五个参数：`result` 用于存储结果，`current` 用于存储当前组合，`candidates` 是排序后的候选数数组，`target` 是目标和，`start` 是当前搜索的起始位置。

4. **递归搜索逻辑**：在 `backtrack` 函数内部，首先检查 `target` 是否等于 0。如果等于 0，说明找到了一个满足条件的组合，将当前组合 `current` 添加到结果 `result` 中。

5. **遍历候选数数组**：使用循环遍历候选数数组，从 `start` 开始，逐个考虑每个候选数。
   - 如果当前候选数小于或等于 `target`，将当前候选数添加到当前组合 `current` 中，然后递归调用 `backtrack` 函数，继续搜索。
   - 在递归返回后，需要回溯，即将最后添加的候选数从 `current` 中移除，以便尝试其他组合。

6. **调用递归函数**：在 `combinationSum` 函数中调用 `backtrack` 函数，开始搜索组合。

7. **返回结果**：返回找到的所有组合，即 `result` 的 `ArrayList

## 代码

## Go

```Go
func combinationSum(candidates []int, target int) [][]int {
    ret := [][]int{}            // 用于存储结果的二维切片
    vals := []int{}             // 用于存储当前组合的切片
    var backtraking func(candidates []int, start, sum int) // 递归函数的声明

    sort.Ints(candidates)        // 对候选数集合进行升序排序

    // 定义递归函数，该函数用于搜索组合
    backtraking = func(candidates []int, start, sum int) {
        if sum == 0 {
            tmp := make([]int, len(vals))  // 创建一个临时切片以存储当前组合
            copy(tmp, vals)                 // 将当前组合复制到临时切片中
            ret = append(ret, tmp)          // 将临时切片添加到结果中
            return
        }

        for i := start; i < len(candidates); i++ {
            if candidates[i] > sum {
                break
            }
            vals = append(vals, candidates[i])     // 将当前候选数添加到组合中
            backtraking(candidates, i, sum-candidates[i]) // 递归调用函数，继续搜索
            vals = vals[:len(vals)-1]               // 回溯，将最后一个元素从组合中移除
        }
    }

    backtraking(candidates, 0, target) // 调用递归函数来开始搜索组合

    return ret // 返回找到的所有组合
}

```

## Python

```Python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(result, current, candidates, target, start):
            if target == 0:
                result.append(list(current))
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] <= target:
                    current.append(candidates[i])
                    backtrack(result, current, candidates, target - candidates[i], i)
                    current.pop()
        
        result = []
        current = []
        
        # 对候选数列表进行排序
        candidates.sort()
        
        # 调用回溯函数
        backtrack(result, current, candidates, target, 0)
        
        return result

```

## Java

```Java
import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> current = new ArrayList<>();
        
        // 对候选数列表进行排序
        Arrays.sort(candidates);
        
        // 调用回溯函数
        backtrack(result, current, candidates, target, 0);
        
        return result;
    }
    
    private void backtrack(List<List<Integer>> result, List<Integer> current, int[] candidates, int target, int start) {
        if (target == 0) {
            result.add(new ArrayList<>(current));
            return;
        }
        
        for (int i = start; i < candidates.length && candidates[i] <= target; i++) {
            current.add(candidates[i]);
            backtrack(result, current, candidates, target - candidates[i], i);
            current.remove(current.size() - 1);
        }
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> current;
        
        // 对候选数列表进行排序
        sort(candidates.begin(), candidates.end());
        
        // 调用回溯函数
        backtrack(result, current, candidates, target, 0);
        
        return result;
    }
    
    void backtrack(vector<vector<int>>& result, vector<int>& current, vector<int>& candidates, int target, int start) {
        if (target == 0) {
            result.push_back(current);
            return;
        }
        
        for (int i = start; i < candidates.size() && candidates[i] <= target; i++) {
            current.push_back(candidates[i]);
            backtrack(result, current, candidates, target - candidates[i], i);
            current.pop_back();
        }
    }
};

```


当我们用中文进行介绍时，分别介绍每个版本（Go、Python、Java 和 C++）的代码，以及为理解这些代码所需的基础知识：

Go 版本：

1. **切片（Slices）**：Go 中的切片是动态数组，它们的长度可以根据需要增长。在这个代码中，`vals` 和 `ret` 都是切片，用于存储组合的临时数据和最终结果。

2. **递归（Recursion）**：代码使用递归的方式来搜索可能的组合。了解递归的工作原理和如何编写递归函数对理解这段代码非常重要。

3. **排序（Sorting）**：在开始组合搜索之前，代码对候选数组进行了排序。了解排序的算法和如何在 Go 中进行排序是必要的。

4. **切片操作**：代码使用切片的操作，如 `append` 和切片截取，来处理组合的元素。

Python 版本：

1. **列表（Lists）**：Python 中的列表用于存储多个值。在这个代码中，`result` 和 `current` 都是列表，用于存储组合的临时数据和最终结果。

2. **递归（Recursion）**：代码使用递归的方式来搜索可能的组合。了解递归的工作原理和如何编写递归函数对理解这段代码非常重要。

3. **排序（Sorting）**：在开始组合搜索之前，代码对候选数组进行了排序。了解排序的算法和如何在 Python 中进行排序是必要的。

4. **列表操作**：代码使用列表的操作，如 `append` 和 `pop`，来处理组合的元素。

Java 版本：

1. **列表（Lists）**：Java 中可以使用 `ArrayList` 或其他列表来存储多个值。在这个代码中，`result` 和 `current` 都是 `ArrayList`，用于存储组合的临时数据和最终结果。

2. **递归（Recursion）**：代码使用递归的方式来搜索可能的组合。了解递归的工作原理和如何编写递归函数对理解这段代码非常重要。

3. **排序（Sorting）**：在开始组合搜索之前，代码对候选数组进行了排序。了解排序的算法和如何在 Java 中进行排序是必要的。

4. **列表操作**：代码使用列表的操作，如 `add` 和 `remove`，来处理组合的元素。

C++ 版本：

1. **向量（Vectors）**：C++ 中的 `vector` 用于存储多个值。在这个代码中，`result` 和 `current` 都是 `vector`，用于存储组合的临时数据和最终结果。

2. **递归（Recursion）**：代码使用递归的方式来搜索可能的组合。了解递归的工作原理和如何编写递归函数对理解这段代码非常重要。

3. **排序（Sorting）**：在开始组合搜索之前，代码对候选数组进行了排序。了解排序的算法和如何在 C++ 中进行排序是必要的。

4. **向量操作**：代码使用向量的操作，如 `push_back` 和 `pop_back`，来处理组合的元素。

在理解这些代码的基础上，还需要了解递归、排序算法和数据结构（如列表或切片）的基础知识，以便更好地理解和修改这些代码。
