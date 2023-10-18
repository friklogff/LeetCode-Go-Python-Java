# [73. Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)


## 题目

Given an *`m* x *n*` matrix. If an element is **0**, set its entire row and column to **0**. Do it **[in-place](https://en.wikipedia.org/wiki/In-place_algorithm)**.

**Follow up:**

- A straight forward solution using O(*mn*) space is probably a bad idea.
- A simple improvement uses O(*m* + *n*) space, but still not the best solution.
- Could you devise a constant space solution?

**Example 1:**

![https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg](https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg)

```
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
```

**Example 2:**

![https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg](https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg)

```
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

**Constraints:**

- `m == matrix.length`
- `n == matrix[0].length`
- `1 <= m, n <= 200`
- `2^31 <= matrix[i][j] <= 2^31 - 1`

## 题目大意

给定一个 `m x n` 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

## 解题思路

- 此题考查对程序的控制能力，无算法思想。题目要求采用原地的算法，所有修改即在原二维数组上进行。在二维数组中有 2 个特殊位置，一个是第一行，一个是第一列。它们的特殊性在于，它们之间只要有一个 0，它们都会变为全 0 。先用 2 个变量记录这一行和这一列中是否有 0，防止之后的修改覆盖了这 2 个地方。然后除去这一行和这一列以外的部分判断是否有 0，如果有 0，将它们所在的行第一个元素标记为 0，所在列的第一个元素标记为 0 。最后通过标记，将对应的行列置 0 即可。
以下是每个版本的解题思路的详细说明：

**Go版本：**
1. 首先检查矩阵是否为空，如果为空则直接返回。
2. 初始化两个布尔变量 `isFirstRowExistZero` 和 `isFirstColExistZero`，用于标记第一行和第一列是否包含0。
3. 遍历矩阵，检查第一列是否包含0，如果包含0，将 `isFirstColExistZero` 设为 true。
4. 同样地，检查第一行是否包含0，如果包含0，将 `isFirstRowExistZero` 设为 true。
5. 接下来，遍历矩阵的其余部分（除了第一行和第一列），如果某个元素为0，将对应的第一行和第一列的元素设置为0。
6. 再次遍历矩阵的其余部分，根据第一行和第一列的标记，将对应的行和列设置为0。
7. 最后，如果 `isFirstRowExistZero` 为 true，将整个第一行设置为0；如果 `isFirstColExistZero` 为 true，将整个第一列设置为0。

**Python版本：**
1. 检查矩阵是否为空，如果为空则直接返回。
2. 初始化两个布尔变量 `first_row_has_zero` 和 `first_col_has_zero`，用于标记第一行和第一列是否包含0。
3. 遍历矩阵，检查第一列是否包含0，如果包含0，将 `first_col_has_zero` 设为 true。
4. 同样地，检查第一行是否包含0，如果包含0，将 `first_row_has_zero` 设为 true。
5. 遍历矩阵的其余部分（除了第一行和第一列），如果某个元素为0，将对应的第一行和第一列的元素设置为0。
6. 再次遍历矩阵的其余部分，根据第一行和第一列的标记，将对应的行和列设置为0。
7. 最后，如果 `first_row_has_zero` 为 true，将整个第一行设置为0；如果 `first_col_has_zero` 为 true，将整个第一列设置为0。

**Java版本：**
1. 获取矩阵的行数和列数。
2. 创建两个布尔数组 `rowboolean` 和 `colboolean`，分别用于标记行和列中是否存在0元素，并初始化为全false。
3. 遍历矩阵的每个元素，如果某个元素为0，将对应的行和列在 `rowboolean` 和 `colboolean` 中标记为true。
4. 再次遍历矩阵，根据 `rowboolean` 和 `colboolean` 的标记，将对应的行和列置零。

**C++版本：**
1. 获取矩阵的行数和列数。
2. 创建两个布尔变量 `firstRowZero` 和 `firstColZero`，用于标记第一行和第一列是否包含0。
3. 遍历矩阵，检查第一列是否包含0，如果包含0，将 `firstColZero` 设为 true。
4. 同样地，检查第一行是否包含0，如果包含0，将 `firstRowZero` 设为 true。
5. 使用第一行和第一列来标记需要置零的行和列。
6. 遍历矩阵的其余部分，如果某个元素为0，将对应的第一行和第一列的元素设置为0。
7. 再次遍历矩阵的其余部分，根据第一行和第一列的标记，将对应的行和列设置为0。
8. 最后，如果 `firstRowZero` 为 true，将整个第一行设置为0；如果 `firstColZero` 为 true，将整个第一列设置为0。

这些解题思路的共同点是使用额外的标记来记录哪些行和列需要设置为0，并然后按照这些标记来进行相应的操作，以满足题目要求。
## 代码

## Go

```Go
func setZeroes(matrix [][]int) {
	// 检查矩阵是否为空
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return
	}

	// 初始化两个标志变量，用于判断第一行和第一列是否需要被置零
	isFirstRowExistZero, isFirstColExistZero := false, false

	// 检查第一列是否存在零元素
	for i := 0; i < len(matrix); i++ {
		if matrix[i][0] == 0 {
			isFirstColExistZero = true
			break
		}
	}

	// 检查第一行是否存在零元素
	for j := 0; j < len(matrix[0]); j++ {
		if matrix[0][j] == 0 {
			isFirstRowExistZero = true
			break
		}
	}

	// 遍历矩阵，如果元素为零，则将对应的第一行和第一列的元素置零
	for i := 1; i < len(matrix); i++ {
		for j := 1; j < len(matrix[0]); j++ {
			if matrix[i][j] == 0 {
				matrix[i][0] = 0
				matrix[0][j] = 0
			}
		}
	}

	// 处理除第一行以及第一列以外的行，将包含零元素的行全部置零
	for i := 1; i < len(matrix); i++ {
		if matrix[i][0] == 0 {
			for j := 1; j < len(matrix[0]); j++ {
				matrix[i][j] = 0
			}
		}
	}

	// 处理除第一行以及第一列以外的列，将包含零元素的列全部置零
	for j := 1; j < len(matrix[0]); j++ {
		if matrix[0][j] == 0 {
			for i := 1; i < len(matrix); i++ {
				matrix[i][j] = 0
			}
		}
	}

	// 如果第一行存在零元素，则将整个第一行置零
	if isFirstRowExistZero {
		for j := 0; j < len(matrix[0]); j++ {
			matrix[0][j] = 0
		}
	}

	// 如果第一列存在零元素，则将整个第一列置零
	if isFirstColExistZero {
		for i := 0; i < len(matrix); i++ {
			matrix[i][0] = 0
		}
	}
}

```

## Python

```Python
class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return

        # 初始化标志变量
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(len(matrix[0])))
…        # 处理第一行和第一列
        if first_row_has_zero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if first_col_has_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
```

## Java

```Java
class Solution {
    public void setZeroes(int[][] matrix) {
        int row = matrix.length;//行数
		int col = matrix[0].length;//列数
		boolean[] rowboolean = new boolean[row];//行数组，初始false
		boolean[] colboolean = new boolean[col];//列数组，初始false
		for (int i = 0; i < row; i++) {
			for (int j = 0; j < col; j++) {
				if(matrix[i][j] == 0){
					rowboolean[i] = true;
…		}
    }
}
```

## Cpp

```Cpp
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        bool firstRowZero = false;
        bool firstColZero = false;

        // 检查第一行和第一列是否包含零
        for (int i = 0; i < m; i++) {
            if (matrix[i][0] == 0) {
                firstColZero = true;
                break;
            }
        }
        for (int j = 0; j < n; j++) {
            if (matrix[0][j] == 0) {
                firstRowZero = true;
                break;
            }
        }

        // 使用第一行和第一列来标记需要置零的行和列
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        // 根据标记，将对应的行和列置零
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }

        // 处理第一行和第一列
        if (firstColZero) {
            for (int i = 0; i < m; i++) {
                matrix[i][0] = 0;
            }
        }
        if (firstRowZero) {
            for (int j = 0; j < n; j++) {
                matrix[0][j] = 0;
            }
        }
    }
};

```
当使用不同编程语言编写代码时，为理解和修改代码，需要了解以下基础知识：

**Go版本：**
- Go是一种静态编程语言，它具有强类型系统。
- 在Go中，你需要了解如何声明和使用变量、数组和切片（slices）。
- 了解循环和条件语句，例如`for`和`if`。
- 理解二维切片（2D slices）和如何通过索引访问元素。
- 函数的定义和调用方式，以及如何处理函数参数和返回值。
- 在Go中，数组和切片的长度可以使用`len()`函数获得。
- 使用布尔（boolean）类型来标记特定条件的存在与否。

**Python版本：**
- Python是一种动态脚本语言，具有弱类型系统。
- 了解Python的基本数据结构，如列表（lists）和嵌套列表。
- 掌握条件语句（如`if`）和循环结构（如`for`）的用法。
- 理解如何定义和调用函数，以及如何处理函数参数和返回值。
- 在Python中，你可以使用列表和嵌套列表来表示矩阵。
- 使用布尔类型来标记特定条件的存在与否，如`if element == 0`。

**Java版本：**
- Java是一种强类型编程语言，具有静态类型检查。
- 了解Java的类和对象，以及如何创建和操作二维数组。
- 掌握条件语句（如`if`）和循环结构（如`for`）的语法。
- 熟悉如何定义和调用方法（函数）。
- Java中的数组是定长的，需要提前指定大小。
- 使用布尔数组来标记特定条件的存在与否。

**C++版本：**
- C++是一种强类型编程语言，具有静态类型检查。
- 了解C++的类和对象，以及如何创建和操作二维数组。
- 掌握条件语句（如`if`）和循环结构（如`for`）的语法。
- 理解如何定义和调用函数，以及如何处理函数参数和返回值。
- C++中的数组是定长的，需要提前指定大小。
- 使用布尔数组来标记特定条件的存在与否。

无论使用哪种编程语言，理解基本的控制结构、数组/列表、条件语句和循环结构都是解决问题的关键。此外，了解如何在特定编程语言中声明变量、定义函数以及操作数据结构也是重要的基础知识。