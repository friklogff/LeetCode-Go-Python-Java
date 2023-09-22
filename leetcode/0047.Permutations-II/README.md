# [47. Permutations II](https://leetcode.com/problems/permutations-ii/)


## 题目

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

**Example:**


    Input: [1,1,2]
    Output:
    [
      [1,1,2],
      [1,2,1],
      [2,1,1]
    ]


## 题目大意

给定一个可包含重复数字的序列，返回所有不重复的全排列。

## 解题思路

- 这一题是第 46 题的加强版，第 46 题中求数组的排列，数组中元素不重复，但是这一题中，数组元素会重复，所以需要最终排列出来的结果需要去重。
- 去重的方法是经典逻辑，将数组排序以后，判断重复元素再做逻辑判断。
- 其他思路和第 46 题完全一致，DFS 深搜即可。

Go 版本解题思路：

1. **排序数组：** 首先，对输入的整数数组 `nums` 进行排序，这一步很关键，因为它将重复的元素放在一起，为后续去重逻辑做准备。

2. **深度优先搜索（DFS）：** 使用深度优先搜索算法，递归地生成排列。从头到尾，逐个考虑数组中的元素是否加入当前排列。

3. **去重逻辑：** 在递归生成排列的过程中，需要判断当前元素是否可以加入排列，以避免重复。如果当前元素与前一个元素相同，且前一个元素未被使用，就跳过当前元素，以防止重复排列。

4. **结果收集：** 每当生成一个完整的排列，就将其添加到结果集中。最终，返回结果集。

Python 版本解题思路：

1. **排序数组：** 同样，首先对输入的整数数组 `nums` 进行排序，以便处理重复元素。

2. **深度优先搜索（DFS）：** 使用深度优先搜索算法递归生成排列。递归的过程中，不断将元素添加到当前排列中。

3. **去重逻辑：** 在递归生成排列的过程中，通过判断元素是否已被使用以及是否与前一个元素相同且前一个元素未被使用，来避免重复。

4. **结果收集：** 每当生成一个完整的排列，就将其添加到结果列表中。最终，返回结果列表。

Java 版本解题思路：

1. **排序数组：** 对输入的整数数组 `nums` 进行排序，这有助于处理重复元素。

2. **深度优先搜索（DFS）：** 使用深度优先搜索算法递归生成排列。递归的过程中，不断将元素添加到当前排列中。

3. **去重逻辑：** 在递归生成排列的过程中，通过判断元素是否已被使用以及是否与前一个元素相同且前一个元素未被使用，来避免重复。

4. **结果收集：** 每当生成一个完整的排列，就将其添加到结果列表中。最终，返回结果列表。

C++ 版本解题思路：

1. **排序数组：** 同样，对输入的整数数组 `nums` 进行排序，以便处理重复元素。

2. **深度优先搜索（DFS）：** 使用深度优先搜索算法递归生成排列。递归的过程中，不断将元素添加到当前排列中。

3. **去重逻辑：** 在递归生成排列的过程中，通过判断元素是否已被使用以及是否与前一个元素相同且前一个元素未被使用，来避免重复。

4. **结果收集：** 每当生成一个完整的排列，就将其添加到结果向量中。最终，返回结果向量。

总的来说，这四个版本的解题思路都基于深度优先搜索（DFS）和去重逻辑，通过不断地添加、移除元素来生成排列并避免重复。排序数组是关键的预处理步骤，确保相同的元素在一起，以便进行去重判断。这些思路是解决排列问题的通用方法，在处理包含重复元素的情况时，需要格外小心去重。
## 代码

## Go

```Go
import "sort"

func permuteUnique(nums []int) [][]int {
    if len(nums) == 0 {
        return [][]int{}
    }
    used, p, res := make([]bool, len(nums)), []int{}, [][]int{}
    sort.Ints(nums) // 对输入数组进行排序，关键的去重逻辑
    generatePermutation47(nums, 0, p, &res, &used)
    return res
}

func generatePermutation47(nums []int, index int, p []int, res *[][]int, used *[]bool) {
    if index == len(nums) {
        temp := make([]int, len(p))
        copy(temp, p)
        *res = append(*res, temp) // 将当前排列添加到结果集中
        return
    }
    for i := 0; i < len(nums); i++ {
        if !(*used)[i] {
            if i > 0 && nums[i] == nums[i-1] && !(*used)[i-1] {
                continue // 关键的去重逻辑，跳过重复的数字
            }
            (*used)[i] = true // 标记当前数字已被使用
            p = append(p, nums[i]) // 将当前数字添加到排列中
            generatePermutation47(nums, index+1, p, res, used) // 递归生成下一个位置的排列
            p = p[:len(p)-1] // 回溯，移除当前数字
            (*used)[i] = false // 取消标记当前数字未被使用
        }
    }
    return
}

```

## Python

```Python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def generatePermutation(nums, used, current, result):
            if len(current) == len(nums):
                result.append(current[:])
                return
            
            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                    continue
                
                used[i] = True
                current.append(nums[i])
                generatePermutation(nums, used, current, result)
                current.pop()
                used[i] = False
        
        nums.sort() # 对输入数组进行排序，关键的去重逻辑
        result = []
        used = [False] * len(nums)
        generatePermutation(nums, used, [], result)
        return result

```

## Java

```Java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        if (nums == null || nums.length == 0) {
            return result;
        }
        
        Arrays.sort(nums); // 对输入数组进行排序，关键的去重逻辑
        boolean[] used = new boolean[nums.length];
        List<Integer> current = new ArrayList<>();
        
        generatePermutation(nums, used, current, result);
        
        return result;
    }
    
    private void generatePermutation(int[] nums, boolean[] used, List<Integer> current, List<List<Integer>> result) {
        if (current.size() == nums.length) {
            result.add(new ArrayList<>(current));
            return;
        }
        
        for (int i = 0; i < nums.length; i++) {
            if (used[i] || (i > 0 && nums[i] == nums[i - 1] && !used[i - 1])) {
                continue;
            }
            
            used[i] = true;
            current.add(nums[i]);
            generatePermutation(nums, used, current, result);
            current.remove(current.size() - 1);
            used[i] = false;
        }
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> result;
        if (nums.empty()) {
            return result;
        }
        
        sort(nums.begin(), nums.end()); // 对输入数组进行排序，关键的去重逻辑
        vector<bool> used(nums.size(), false);
        vector<int> current;
        
        generatePermutation(nums, used, current, result);
        
        return result;
    }
    
private:
    void generatePermutation(vector<int>& nums, vector<bool>& used, vector<int>& current, vector<vector<int>>& result) {
        if (current.size() == nums.size()) {
            result.push_back(current);
            return;
        }
        
        for (int i = 0; i < nums.size(); i++) {
            if (used[i] || (i > 0 && nums[i] == nums[i - 1] && !used[i - 1])) {
                continue;
            }
            
            used[i] = true;
            current.push_back(nums[i]);
            generatePermutation(nums, used, current, result);
            current.pop_back();
            used[i] = false;
        }
    }
};

```

相关的基础知识要点。

Go 版本：

- 基础知识：
  - Go 语言基础：熟悉 Go 语法、数据结构、切片（slice）、循环、条件语句等基本概念。
  - 切片和数组：了解 Go 中的切片（slice）和数组的区别以及如何使用它们。
  - 递归：理解递归的概念和如何在 Go 中实现递归函数。

Python 版本：

- 基础知识：
  - Python 基础：掌握 Python 的语法、数据类型、列表（list）、循环、条件语句等基本知识。
  - 列表和集合：了解 Python 中的列表和集合数据结构，以及它们的操作和特性。
  - 递归：理解递归的概念和如何在 Python 中实现递归函数。

Java 版本：

- 基础知识：
  - Java 基础：熟悉 Java 的语法、数组、列表（List）、循环、条件语句等基本知识。
  - 列表和集合：了解 Java 中的列表（List）和集合（Set）数据结构，以及它们的使用方法。
  - 递归：理解递归的概念和如何在 Java 中实现递归方法。

C++ 版本：

- 基础知识：
  - C++ 基础：掌握 C++ 的语法、数组、向量（vector）、循环、条件语句等基本概念。
  - 向量（vector）：了解 C++ 中的向量（vector）数据结构，以及如何使用它来存储和处理数据。
  - 递归：理解递归的概念和如何在 C++ 中实现递归函数。

