# [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

## 题目

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

![](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!


**Example**:

```go
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

## 题目大意

从 x 轴开始，给出一个数组，数组里面的数字代表从 (0,0) 点开始，宽度为 1 个单位，高度为数组元素的值。如果下雨了，问这样一个容器能装多少单位的水？

## 解题思路

- 每个数组里面的元素值可以想象成一个左右都有壁的圆柱筒。例如下图中左边的第二个元素 1，当前左边最大的元素是 2 ，所以 2 高度的水会装到 1 的上面(因为想象成了左右都有筒壁)。这道题的思路就是左指针从 0 开始往右扫，右指针从最右边开始往左扫。额外还需要 2 个变量分别记住左边最大的高度和右边最大高度。遍历扫数组元素的过程中，如果左指针的高度比右指针的高度小，就不断的移动左指针，否则移动右指针。循环的终止条件就是左右指针碰上以后就结束。只要数组中元素的高度比保存的局部最大高度小，就累加 res 的值，否则更新局部最大高度。最终解就是 res 的值。
    ![](https://image.ibb.co/d6A2ZU/IMG-0139.jpg)  
- 抽象一下，本题是想求针对每个 i，找到它左边最大值 leftMax，右边的最大值 rightMax，然后 min(leftMax，rightMax) 为能够接到水的高度。left 和 right 指针是两边往中间移动的游标指针。最傻的解题思路是针对每个下标 i，往左循环找到第一个最大值，往右循环找到第一个最大值，然后把这两个最大值取出最小者，即为当前雨水的高度。这样做时间复杂度高，浪费了很多循环。i 在从左往右的过程中，是可以动态维护最大值的。右边的最大值用右边的游标指针来维护。从左往右扫一遍下标，和，从两边往中间遍历一遍下标，是相同的结果，每个下标都遍历了一次。    
    ![](https://img.halfrost.com/Leetcode/leetcode_42_1.png)  
- 每个 i 的宽度固定为 1，所以每个“坑”只需要求出高度，即当前这个“坑”能积攒的雨水。最后依次将每个“坑”中的雨水相加即是能接到的雨水数。    
    ![](https://img.halfrost.com/Leetcode/leetcode_42_0.png)  

以下是每个版本的解题思路：

Go 版本解题思路：

1. **初始化**：首先，我们初始化变量 `res` 为 0，`left` 为 0，`right` 为数组 `height` 的最后一个索引，`maxLeft` 和 `maxRight` 都为 0。

2. **双指针遍历**：使用一个循环来遍历 `height` 数组，`left` 和 `right` 分别指示当前操作的两个柱子的索引。

3. **左右夹逼**：在循环中，我们比较 `height[left]` 和 `height[right]` 的高度，如果 `height[left]` 小于等于 `height[right]`，则表示左边的柱子较低。在这种情况下，我们检查 `height[left]` 是否大于 `maxLeft`。如果是，则更新 `maxLeft` 为当前左边柱子的高度，否则将 `maxLeft - height[left]` 加到 `res` 中表示可以接到的雨水高度，并将 `left` 指针右移一位。

4. **右边柱子较低**：如果 `height[right]` 小于 `height[left]`，则表示右边的柱子较低。在这种情况下，我们检查 `height[right]` 是否大于等于 `maxRight`。如果是，则更新 `maxRight` 为当前右边柱子的高度，否则将 `maxRight - height[right]` 加到 `res` 中表示可以接到的雨水高度，并将 `right` 指针左移一位。

5. **循环结束**：重复执行上述步骤，直到 `left` 不再小于等于 `right`，这表示两个指针相遇，整个数组都被遍历完。

6. **返回结果**：最终，返回 `res`，表示可以接到的雨水总量。

Python 版本解题思路：

Python 版本的解题思路与 Go 版本基本相同，只是语法和变量声明略有不同。具体步骤如下：

1. **初始化**：初始化变量 `res` 为 0，`left` 为 0，`right` 为数组 `height` 的最后一个索引，`maxLeft` 和 `maxRight` 都为 0。

2. **双指针遍历**：使用一个循环来遍历 `height` 数组，`left` 和 `right` 分别指示当前操作的两个柱子的索引。

3. **左右夹逼**：在循环中，我们比较 `height[left]` 和 `height[right]` 的高度，如果 `height[left]` 小于等于 `height[right]`，则表示左边的柱子较低。在这种情况下，我们检查 `height[left]` 是否大于 `maxLeft`。如果是，则更新 `maxLeft` 为当前左边柱子的高度，否则将 `maxLeft - height[left]` 加到 `res` 中表示可以接到的雨水高度，并将 `left` 指针右移一位。

4. **右边柱子较低**：如果 `height[right]` 小于 `height[left]`，则表示右边的柱子较低。在这种情况下，我们检查 `height[right]` 是否大于等于 `maxRight`。如果是，则更新 `maxRight` 为当前右边柱子的高度，否则将 `maxRight - height[right]` 加到 `res` 中表示可以接到的雨水高度，并将 `right` 指针左移一位。

5. **循环结束**：重复执行上述步骤，直到 `left` 不再小于等于 `right`，这表示两个指针相遇，整个数组都被遍历完。

6. **返回结果**：最终，返回 `res`，表示可以接到的雨水总量。

Java 版本解题思路：

Java 版本的解题思路与 Go 和 Python 版本基本相同，只是语法和方法定义略有不同。具体步骤如下：

1. **初始化**：初始化变量 `res` 为 0，`left` 为 0，`right` 为数组 `height` 的最后一个索引，`maxLeft` 和 `maxRight` 都为 0。

2. **双指针遍历**：使用一个循环来遍历 `height` 数组，`left` 和 `right` 分别指示当前操作的两个柱子的索引。

3. **左右夹逼**：在循环中，我们比较 `height[left]` 和 `height[right]` 的高度，如果 `height[left]` 小于等于 `height[right]`，则表示左边的柱子较低。在这种情况下，我们检查 `height[left]` 是否大于 `maxLeft`。如果是，则更新 `maxLeft` 为当前左边柱子的高度，否则将 `maxLeft - height[left]` 加到 `res` 中表示可以接到的雨水高度，并将 `left` 指针右移一位。

4. **右边柱子较低**：如果 `height[right]` 小于 `height[left]`，则表示右边的柱子较低。在这种情况下，我们检查 `height[right]` 是否大于等于 `maxRight`。如果是，则更新 `maxRight` 为当前右边柱子的高度，否则将 `maxRight - height[right]` 加到 `res` 中表示可以接到的雨水高度，并将 `right` 指针左移一位。

5. **循环结束**：重复执行上述步骤，直到 `left` 不再小于等于 `right`，这表示两个指针相遇，整个数组都被遍历完。

6.**返回结果**：最终，返回 `res`，表示可以接到的雨水总量。

C++ 版本解题思路：

C++ 版本的解题思路与 Go、Python 和 Java 版本基本相同，只是语法和方法定义略有不同。具体步骤如下：

1. **初始化**：初始化变量 `res` 为 0，`left` 为 0，`right` 为数组 `height` 的最后一个索引，`maxLeft` 和 `maxRight` 都为 0。

2. **双指针遍历**：使用一个循环来遍历 `height` 数组，`left` 和 `right` 分别指示当前操作的两个柱子的索引。

3. **左右夹逼**：在循环中，我们比较 `height[left]` 和 `height[right]` 的高度，如果 `height[left]` 小于等于 `height[right]`，则表示左边的柱子较低。在这种情况下，我们检查 `height[left]` 是否大于 `maxLeft`。如果是，则更新 `maxLeft` 为当前左边柱子的高度，否则将 `maxLeft - height[left]` 加到 `res` 中表示可以接到的雨水高度，并将 `left` 指针右移一位。

4. **右边柱子较低**：如果 `height[right]` 小于 `height[left]`，则表示右边的柱子较低。在这种情况下，我们检查 `height[right]` 是否大于等于 `maxRight`。如果是，则更新 `maxRight` 为当前右边柱子的高度，否则将 `maxRight - height[right]` 加到 `res` 中表示可以接到的雨水高度，并将 `right` 指针左移一位。

5. **循环结束**：重复执行上述步骤，直到 `left` 不再小于等于 `right`，这表示两个指针相遇，整个数组都被遍历完。

6. **返回结果**：最终，返回 `res`，表示可以接到的雨水总量。

总的来说，无论使用哪种编程语言，这个问题的解决思路都是使用双指针夹逼法，动态地维护左边最大高度和右边最大高度，以便计算每个位置可以接到的雨水高度，并将其累加到结果中。最终，返回结果表示可以接到的雨水总量。不同编程语言的语法和细节略有不同，但基本思路保持一致。
## 代码

## Go

```Go
func trap(height []int) int {
    res, left, right, maxLeft, maxRight := 0, 0, len(height)-1, 0, 0
    // 初始化结果res为0，left为0，right为height数组的最后一个索引，maxLeft和maxRight都为0

    for left <= right {
        // 使用一个循环来遍历height数组，left和right指示当前操作的两个柱子的索引
        if height[left] <= height[right] {
            // 如果左边的柱子高度小于等于右边的柱子
            if height[left] > maxLeft {
                // 如果当前左边柱子的高度大于maxLeft
                maxLeft = height[left]
                // 更新maxLeft为当前左边柱子的高度
            } else {
                res += maxLeft - height[left]
                // 否则，将maxLeft与当前左边柱子的高度之差累加到结果res中
            }
            left++
            // 左边柱子向右移动一位
        } else {
            // 如果右边的柱子高度小于左边的柱子
            if height[right] >= maxRight {
                // 如果当前右边柱子的高度大于等于maxRight
                maxRight = height[right]
                // 更新maxRight为当前右边柱子的高度
            } else {
                res += maxRight - height[right]
                // 否则，将maxRight与当前右边柱子的高度之差累加到结果res中
            }
            right--
            // 右边柱子向左移动一位
        }
    }
    return res
    // 循环结束后，返回结果res，表示可以接到的雨水总量
}

```

## Python

```Python
class Solution:
    def trap(self, height: List[int]) -> int:
        res, left, right, maxLeft, maxRight = 0, 0, len(height) - 1, 0, 0
        
        while left <= right:
            if height[left] <= height[right]:
                if height[left] > maxLeft:
                    maxLeft = height[left]
                else:
                    res += maxLeft - height[left]
                left += 1
            else:
                if height[right] >= maxRight:
                    maxRight = height[right]
                else:
                    res += maxRight - height[right]
                right -= 1
        
        return res

```

## Java

```Java
class Solution {
    public int trap(int[] height) {
        int res = 0, left = 0, right = height.length - 1, maxLeft = 0, maxRight = 0;
        
        while (left <= right) {
            if (height[left] <= height[right]) {
                if (height[left] > maxLeft) {
                    maxLeft = height[left];
                } else {
                    res += maxLeft - height[left];
                }
                left++;
            } else {
                if (height[right] >= maxRight) {
                    maxRight = height[right];
                } else {
                    res += maxRight - height[right];
                }
                right--;
            }
        }
        
        return res;
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    int trap(vector<int>& height) {
        int res = 0, left = 0, right = height.size() - 1, maxLeft = 0, maxRight = 0;
        
        while (left <= right) {
            if (height[left] <= height[right]) {
                if (height[left] > maxLeft) {
                    maxLeft = height[left];
                } else {
                    res += maxLeft - height[left];
                }
                left++;
            } else {
                if (height[right] >= maxRight) {
                    maxRight = height[right];
                } else {
                    res += maxRight - height[right];
                }
                right--;
            }
        }
        
        return res;
    }
};

```

每个版本相关的基础知识和语法要点。我们将按照 Go、Python、Java 和 C++ 这四种编程语言来介绍各自的代码版本。

Go 版本：

1. **函数定义和返回值**：在 Go 中，函数的定义使用关键字 `func`，函数的返回值类型放在参数列表之后。例如，`func trap(height []int) int` 定义了一个名为 `trap` 的函数，它接受一个整数切片 `height` 作为参数，并返回一个整数作为结果。

2. **切片和数组**：Go 中的切片（slice）类似于动态数组，但它是引用类型。在代码中，`height` 是一个整数切片，表示高度数组。

3. **循环和条件语句**：Go 使用 `for` 循环和 `if` 条件语句来进行控制流程。在 `trap` 函数中，`for` 循环用于遍历数组，`if` 语句用于条件判断。

4. **变量声明和赋值**：Go 中的变量可以使用 `var` 关键字声明，也可以使用短变量声明 `:=` 进行赋值。在代码中，有多个变量的声明和赋值操作，如 `res`, `left`, `right`, `maxLeft`, 和 `maxRight`。

5. **数组/切片的索引访问**：通过使用方括号 `[]` 来访问数组或切片的元素。例如，`height[left]` 表示访问 `height` 切片的 `left` 索引处的元素。

Python 版本：

1. **类和方法**：Python 是一种面向对象的编程语言，类似于 Go，函数是通过 `def` 关键字定义的。在 Python 中，类方法的第一个参数通常是 `self`，表示对实例自身的引用。

2. **列表和循环**：Python 中的列表（List）是一种动态数组，类似于 Go 中的切片。循环通过 `for` 循环来实现。

3. **条件语句**：与 Go 一样，Python 使用 `if` 语句来进行条件判断。

4. **变量赋值**：Python 使用 `=` 运算符来进行变量赋值，如 `res`, `left`, `right`, `maxLeft`, 和 `maxRight`。

Java 版本：

1. **类和方法**：Java 是一种面向对象的编程语言，函数是通过 `public int trap(int[] height)` 这样的方法定义的。方法参数和返回值都需要指定类型。

2. **数组**：Java 中的数组是固定大小的，而不是像 Go 和 Python 中的切片一样动态增长。

3. **循环和条件语句**：Java 使用 `for` 循环和 `if` 语句来进行控制流程。

4. **变量声明和赋值**：Java 中的变量需要显式声明类型，并使用 `=` 运算符进行赋值。在代码中，有多个变量的声明和赋值操作，如 `res`, `left`, `right`, `maxLeft`, 和 `maxRight`。

C++ 版本：

1. **类和方法**：C++ 是一种多范式编程语言，函数是通过 `int trap(vector<int>& height)` 这样的方法定义的。方法参数和返回值都需要指定类型。

2. **容器和循环**：C++ 使用 `vector` 容器来表示动态数组，类似于 Go 和 Python 中的切片和列表。循环可以使用 `for` 或 `while` 实现。

3. **条件语句**：与 Go、Python 和 Java 一样，C++ 使用 `if` 语句来进行条件判断。

4. **变量声明和赋值**：C++ 中的变量声明通常在函数或代码块的开始处，然后可以使用 `=` 运算符进行赋值。在代码中，有多个变量的声明和赋值操作，如 `res`, `left`, `right`, `maxLeft`, 和 `maxRight`。

