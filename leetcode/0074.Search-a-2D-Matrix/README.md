# [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)


## 题目

Write an efficient algorithm that searches for a value in an *m* x *n* matrix. This matrix has the following properties:

- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

**Example 1:**

    Input:
    matrix = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
    target = 3
    Output: true

**Example 2:**

    Input:
    matrix = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
    target = 13
    Output: false


## 题目大意

编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

- 每行中的整数从左到右按升序排列。
- 每行的第一个整数大于前一行的最后一个整数。


## 解题思路


- 给出一个二维矩阵，矩阵的特点是随着矩阵的下标增大而增大。要求设计一个算法能在这个矩阵中高效的找到一个数，如果找到就输出 true，找不到就输出 false。
- 虽然是一个二维矩阵，但是由于它特殊的有序性，所以完全可以按照下标把它看成一个一维矩阵，只不过需要行列坐标转换。最后利用二分搜索直接搜索即可。
以下是每个版本的解题思路的详细介绍：

Go 版本解题思路

1. 首先，检查输入的矩阵是否为空（长度为0）。如果矩阵为空，直接返回 `false`，因为无法在空矩阵中查找目标值。

2. 获取矩阵的列数（`m`），并初始化两个指针 `low` 和 `high`。`low` 初始化为0，`high` 初始化为矩阵中元素总数减1，表示搜索范围的开始和结束。

3. 进入一个循环，条件是 `low` 小于等于 `high`。这个循环是二分查找的核心部分。

4. 在循环中，首先计算中间索引 `mid`，以将搜索范围分成两半。这是通过 `low + (high - low) >> 1` 来实现的，使用位运算右移来取代除以2，以提高效率。

5. 然后，使用整数除法和取模运算，将 `mid` 转换为矩阵中的行和列索引，即 `mid/m` 和 `mid%m`。

6. 比较矩阵中索引为 `mid/m` 行，`mid%m` 列的元素与目标值 `target`。如果它们相等，说明找到了目标值，返回 `true`。

7. 如果矩阵中的元素小于 `target`，则更新 `low` 为 `mid + 1`，以排除左半边搜索范围。

8. 如果矩阵中的元素大于 `target`，则更新 `high` 为 `mid - 1`，以排除右半边搜索范围。

9. 循环结束后，如果没有找到目标值，返回 `false`，指示目标值不在矩阵中。

这个算法利用二分查找的思想，以 O(log(m*n)) 的时间复杂度来高效地在二维矩阵中查找目标值。

Python 版本解题思路

1. 首先，检查输入的矩阵是否为空。如果矩阵为空，直接返回 `False`，因为无法在空矩阵中查找目标值。

2. 获取矩阵的行数（`rows`）和列数（`cols`），用于后续计算。

3. 初始化两个指针，`low` 和 `high`，分别表示搜索范围的起始和结束。`low` 初始化为0，`high` 初始化为矩阵中元素总数减1。

4. 进入一个循环，条件是 `low` 小于等于 `high`。这个循环是二分查找的核心。

5. 在循循环中，首先计算中间索引 `mid`，以将搜索范围分成两半。这是通过 `low + (high - low) // 2` 来实现的。

6. 然后，使用整除和取模运算，将 `mid` 转换为矩阵中的行和列索引，即 `divmod(mid, cols)`。

7. 比较矩阵中索引为 `row` 和 `col` 的元素与目标值 `target`。如果它们相等，说明找到了目标值，返回 `True`。

8. 如果矩阵中的元素小于 `target`，则更新 `low` 为 `mid + 1`，以排除左半边搜索范围。

9. 如果矩阵中的元素大于 `target`，则更新 `high` 为 `mid - 1`，以排除右半边搜索范围。

10. 循环结束后，如果没有找到目标值，返回 `False`，指示目标值不在矩阵中。

这个算法使用二分查找的思想，以 O(log(m*n)) 的时间复杂度来高效地在二维矩阵中查找目标值。

Java 版本解题思路

1. 首先，检查输入的矩阵是否为空。如果矩阵为空，直接返回 `false`，因为无法在空矩阵中查找目标值。

2. 获取矩阵的行数（`rows`）和列数（`cols`），用于后续计算。

3. 初始化两个指针，`low` 和 `high`，分别表示搜索范围的起始和结束。`low` 初始化为0，`high` 初始化为矩阵中元素总数减1。

4. 进入一个循环，条件是 `low` 小于等于 `high`。这个循环是二分查找的核心。

5. 在循环中，首先计算中间索引 `mid`，以将搜索范围分成两半。这是通过 `low + (high - low) / 2` 来实现的。

6. 然后，使用整数除法和取模运算，将 `mid` 转换为矩阵中的行和列索引，即 `mid / cols` 和 `mid % cols`。

7. 比较矩阵中索引为 `row` 和 `col` 的元素与目标值 `target`。如果它们相等，说明找到了目标值，返回 `true`。

8. 如果矩阵中的元素小于 `target`，则更新 `low` 为 `mid + 1`，以排除左半边搜索范围。

9. 如果矩阵中的元素大于 `target`，则更新 `high` 为 `mid - 1`，以排除右半边搜索范围。

10. 循环结束后，如果没有找到目标值，返回 `false`，指示目标
## 代码

## Go

```Go
func searchMatrix(matrix [][]int, target int) bool {
    // 函数名：searchMatrix，接收两个参数，一个是二维整数数组 matrix，另一个是目标值 target。
    
    if len(matrix) == 0 {
        // 如果二维数组 matrix 为空，也就是没有元素，返回 false。
        return false
    }
    
    m, low, high := len(matrix[0]), 0, len(matrix[0])*len(matrix)-1
    // 定义变量 m，表示矩阵的列数；low 和 high 用于二分查找，初始化 low 为 0，high 为 (矩阵行数 * 列数 - 1)。
    
    for low <= high {
        // 进入一个循环，直到 low 大于 high 为止。
        
        mid := low + (high-low)>>1
        // 计算中间位置的索引 mid，这里采用二分查找的方式。
        
        if matrix[mid/m][mid%m] == target {
            // 如果矩阵中索引为 mid/m 行，mid%m 列的元素等于目标值 target，返回 true。
            return true
        } else if matrix[mid/m][mid%m] > target {
            // 如果矩阵中索引为 mid/m 行，mid%m 列的元素大于目标值 target，将 high 更新为 mid - 1，缩小搜索范围。
            high = mid - 1
        } else {
            // 如果矩阵中索引为 mid/m 行，mid%m 列的元素小于目标值 target，将 low 更新为 mid + 1，缩小搜索范围。
            low = mid + 1
        }
    }
    
    // 若循环结束仍未找到目标值，返回 false。
    return false
}

```

## Python

```Python
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            row, col = divmod(mid, cols)
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False

```

## Java

```Java
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix == null || matrix.length == 0) {
            return false;
        }

        int rows = matrix.length;
        int cols = matrix[0].length;
        int low = 0;
        int high = rows * cols - 1;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            int row = mid / cols;
            int col = mid % cols;

            if (matrix[row][col] == target) {
                return true;
            } else if (matrix[row][col] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return false;
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) {
            return false;
        }

        int rows = matrix.size();
        int cols = matrix[0].size();
        int low = 0;
        int high = rows * cols - 1;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            int row = mid / cols;
            int col = mid % cols;

            if (matrix[row][col] == target) {
                return true;
            } else if (matrix[row][col] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return false;
    }
};
```
当阅读不同版本的解决方案时，理解每个版本所需的基础知识是很重要的。以下是每个版本的详细基础知识要求：

Go 版本

- **基础语法**: 熟悉 Go 编程语言的基本语法，包括变量声明、条件语句、循环、函数定义、数组和切片等。

- **数组和切片**: 了解 Go 中的数组和切片，以便理解如何处理二维矩阵。

- **二分查找**: 理解二分查找算法的原理和实现方式，包括如何计算中间索引并根据比较结果更新搜索范围。

Python 版本

- **基础语法**: 熟悉 Python 编程语言的基本语法，包括变量声明、条件语句、循环、函数定义、列表等。

- **列表和元组**: 了解 Python 中的列表和元组，因为它们可以用于表示二维矩阵。

- **整除和取模运算**: 理解如何使用整除和取模运算 (`//` 和 `%`) 来将一维索引转换为二维坐标。

Java 版本

- **基础语法**: 熟悉 Java 编程语言的基本语法，包括类、方法、条件语句、循环、数组等。

- **二维数组**: 了解 Java 中的二维数组，包括如何声明、初始化和访问元素。

- **整数运算**: 理解如何使用整数运算来计算中间索引以及整数除法和取模运算 (`/` 和 `%`) 以将一维索引转换为二维坐标。

C++ 版本

- **基础语法**: 熟悉 C++ 编程语言的基本语法，包括类、方法、条件语句、循环、数组等。

- **二维向量**: 了解 C++ 中的二维向量（vector of vectors），包括如何声明、初始化和访问元素。

- **整数运算**: 理解如何使用整数运算来计算中间索引以及整数除法和取模运算 (`/` 和 `%`) 以将一维索引转换为二维坐标。

无论选择哪个版本，理解基本的编程概念、数组和列表、循环和条件语句、二分查找等算法，以及索引计算的原理都是解决问题的关键要素。熟练运用这些知识将有助于理解和编写类似的算法。