# [48. Rotate Image](https://leetcode.com/problems/rotate-image/)

## 题目

You are given an *n* x *n* 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

**Note:**

You have to rotate the image **[in-place](https://en.wikipedia.org/wiki/In-place_algorithm)**, which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.

**Example 1**:

![](https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg)

    Given input matrix = 
    [
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ],
    
    rotate the input matrix in-place such that it becomes:
    [
      [7,4,1],
      [8,5,2],
      [9,6,3]
    ]


**Example 2**:

![](https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg)

    Given input matrix =
    [
      [ 5, 1, 9,11],
      [ 2, 4, 8,10],
      [13, 3, 6, 7],
      [15,14,12,16]
    ], 
    
    rotate the input matrix in-place such that it becomes:
    [
      [15,13, 2, 5],
      [14, 3, 4, 1],
      [12, 6, 8, 9],
      [16, 7,10,11]
    ]


## 题目大意

给定一个 n × n 的二维矩阵表示一个图像。将图像顺时针旋转 90 度。说明：你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。


## 解题思路

- 给出一个二维数组，要求顺时针旋转 90 度。
- 这一题比较简单，按照题意做就可以。这里给出 2 种旋转方法的实现，顺时针旋转和逆时针旋转。
当解决问题 "Rotate Image" 时，每个版本的解题思路基本相同，只是具体语言的语法和操作略有不同。以下是每个版本的解题思路：

Go 版本解题思路

1. **对角线变换**：首先，我们进行对角线变换，将矩阵中的元素按照主对角线（从左上角到右下角）进行交换。这一步实际上是将矩阵顺时针旋转了 90 度的一半。

2. **竖直轴对称翻转**：接下来，我们对每一行进行竖直轴对称翻转。这一步将完成矩阵的剩余旋转，使其顺时针旋转 90 度。

Python 版本解题思路

Python 版本的解题思路与 Go 版本基本相同，包括对角线变换和竖直轴对称翻转两个步骤。

Java 版本解题思路

Java 版本的解题思路也与 Go 版本类似：

1. **对角线变换**：首先，我们进行对角线变换，将矩阵中的元素按照主对角线进行交换。

2. **竖直轴对称翻转**：接下来，对每一行进行竖直轴对称翻转，完成矩阵的剩余旋转。

C++ 版本解题思路

C++ 版本的解题思路与 Java 版本非常相似：

1. **对角线变换**：首先，我们进行对角线变换，将矩阵中的元素按照主对角线进行交换。

2. **竖直轴对称翻转**：然后，对每一行进行竖直轴对称翻转，完成矩阵的剩余旋转。

总之，每个版本的解题思路都遵循了对角线变换和竖直轴对称翻转这两个步骤，以实现矩阵的顺时针旋转 90 度。如果您有任何特定版本的问题或需要更详细的解释，请告诉我。
## 代码

## Go

```Go
// 解法一
func rotate(matrix [][]int) {
	length := len(matrix) // 获取矩阵的长度

	// rotate by diagonal 对角线变换
	for i := 0; i < length; i++ { // 遍历行
		for j := i + 1; j < length; j++ { // 遍历列，从当前行的下一个元素开始
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] // 交换矩阵[i][j]和矩阵[j][i]的值，实现对角线翻转
		}
	}

	// rotate by vertical centerline 竖直轴对称翻转
	for i := 0; i < length; i++ { // 遍历每一行
		for j := 0; j < length/2; j++ { // 遍历每一行的前一半列
			matrix[i][j], matrix[i][length-j-1] = matrix[i][length-j-1], matrix[i][j] // 交换矩阵[i][j]和矩阵[i][length-j-1]的值，实现竖直轴对称翻转
		}
	}
}

```

## Python

```Python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        length = len(matrix)

        # rotate by diagonal 对角线变换
        for i in range(length):
            for j in range(i + 1, length):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # rotate by vertical centerline 竖直轴对称翻转
        for i in range(length):
            for j in range(length // 2):
                matrix[i][j], matrix[i][length - j - 1] = matrix[i][length - j - 1], matrix[i][j]

```

## Java

```Java
class Solution {
    public void rotate(int[][] matrix) {
        int length = matrix.length;

        // rotate by diagonal 对角线变换
        for (int i = 0; i < length; i++) {
            for (int j = i + 1; j < length; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }

        // rotate by vertical centerline 竖直轴对称翻转
        for (int i = 0; i < length; i++) {
            for (int j = 0; j < length / 2; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][length - j - 1];
                matrix[i][length - j - 1] = temp;
            }
        }
    }
}

```

## Cpp

```Cpp
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        length = len(matrix)

        # rotate by diagonal 对角线变换
        for i in range(length):
            for j in range(i + 1, length):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # rotate by vertical centerline 竖直轴对称翻转
        for i in range(length):
            for j in range(length // 2):
                matrix[i][j], matrix[i][length - j - 1] = matrix[i][length - j - 1], matrix[i][j]

```

 Go 版本

1. **Slice（切片）**：在 Go 中，切片是一种灵活的数据结构，用于处理动态数组。在这个问题中，我们使用切片来表示二维矩阵。

2. **循环和迭代**：Go 使用 `for` 循环来遍历数组和切片。在这里，我们使用嵌套的 `for` 循环来遍历矩阵的行和列。

3. **交换变量值**：在 Go 中，可以通过多重赋值来交换两个变量的值。这是实现矩阵元素交换的关键。

Python 版本

1. **列表**：在 Python 中，我们使用列表来表示数组或矩阵。这里的矩阵就是一个二维列表。

2. **循环和迭代**：Python 使用 `for` 循环来遍历列表。在这个问题中，我们使用嵌套的 `for` 循环来遍历矩阵的行和列。

3. **多重赋值**：Python 允许使用多重赋值来交换两个变量的值，这对于交换矩阵元素很有用。

Java 版本

1. **二维数组**：Java 使用二维数组来表示矩阵。在这个问题中，我们将矩阵表示为 `int[][]` 类型。

2. **嵌套循环**：Java 使用嵌套 `for` 循环来遍历二维数组。第一个循环用于遍历行，第二个循环用于遍历列。

3. **临时变量**：我们使用一个临时变量来在交换两个矩阵元素的值时进行存储。

C++ 版本

1. **二维数组**：C++ 也使用二维数组来表示矩阵。矩阵的类型是 `vector<vector<int>>`。

2. **循环和迭代**：C++ 使用 `for` 循环来遍历向量（vector）。嵌套的 `for` 循环用于遍历二维向量。

3. **临时变量**：和 Java 一样，我们使用一个临时变量来交换两个矩阵元素的值。

这些是解决这个问题所需的基础知识，包括数据结构和编程概念，如循环、迭代和变量操作。如果您有任何关于这些版本的特定问题或需要更详细的解释，请随时提出。