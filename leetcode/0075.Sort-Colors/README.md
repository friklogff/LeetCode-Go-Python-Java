# [75. Sort Colors](https://leetcode.com/problems/sort-colors/)

## 题目

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example 1:  

```
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

Follow up:

- A rather straight forward solution is a two-pass algorithm using counting sort.  
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
- Could you come up with a one-pass algorithm using only constant space?


## 题目大意

抽象题意其实就是排序。这题可以用快排一次通过。

## 解题思路

题目末尾的 Follow up 提出了一个更高的要求，能否用一次循环解决问题？这题由于数字只会出现 0，1，2 这三个数字，所以用游标移动来控制顺序也是可以的。具体做法：0 是排在最前面的，所以只要添加一个 0，就需要放置 1 和 2。1 排在 2 前面，所以添加 1 的时候也需要放置 2 。至于最后的 2，只用移动游标即可。

这道题可以用计数排序，适合待排序数字很少的题目。用一个 3 个容量的数组分别计数，记录 0，1，2 出现的个数。然后再根据个数排列 0，1，2 即可。时间复杂度 O(n)，空间复杂度 O(K)。这一题 K = 3。

这道题也可以用一次三路快排。数组分为 3 部分，第一个部分都是 0，中间部分都是 1，最后部分都是 2 。
以下是每个版本的解题思路的详细介绍：

Python 版本：

- **解题思路：** 这个解决方案采用了一种双指针的方法，其中`zero`指针用于跟踪0的位置，`one`指针用于跟踪1的位置。初始时，两个指针都在数组的开头。
  
- **遍历数组：** 通过遍历数组中的每个元素，首先将当前元素的值设置为2，以表示最终排序的数组中的元素都是2。

- **处理0和1：** 如果当前元素的值小于等于1（即0或1），将其设置为1，并将`one`指针向后移动。

- **处理0：** 如果当前元素的值为0，将其设置为0，并将`zero`指针向后移动。这样，0将排在1的前面。

- **结束：** 完成遍历后，数组将按照所需的顺序排序：首先是0，然后是1，最后是2。

Java 版本：

- **解题思路：** Java版本的解决方案也采用了双指针的方法，其中`zero`指针用于跟踪0的位置，`one`指针用于跟踪1的位置，以及`two`指针用于跟踪2的位置。

- **遍历数组：** 通过遍历数组中的每个元素，首先将当前元素的值设置为2，以表示最终排序的数组中的元素都是2。

- **处理0：** 如果当前元素的值为0，使用`swap`交换`zero`指针和`one`指针处的元素，并将`zero`指针和`one`指针都向后移动。这将把0排在1的前面。

- **处理2：** 如果当前元素的值为2，使用`swap`交换`one`指针和`two`指针处的元素，并将`two`指针向前移动。这将把2排在1的后面。

- **结束：** 完成遍历后，数组将按照所需的顺序排序：首先是0，然后是1，最后是2。

C++ 版本：

- **解题思路：** C++版本的解决方案也采用了双指针的方法，其中`zero`指针用于跟踪0的位置，`one`指针用于跟踪1的位置，以及`two`指针用于跟踪2的位置。

- **遍历数组：** 通过遍历数组中的每个元素，首先将当前元素的值设置为2，以表示最终排序的数组中的元素都是2。

- **处理0：** 如果当前元素的值为0，使用`std::swap()`交换`zero`指针和`one`指针处的元素，并将`zero`指针和`one`指针都向后移动。这将把0排在1的前面。

- **处理2：** 如果当前元素的值为2，使用`std::swap()`交换`one`指针和`two`指针处的元素，并将`two`指针向前移动。这将把2排在1的后面。

- **结束：** 完成遪历后，数组将按照所需的顺序排序：首先是0，然后是1，最后是2。

Go 版本：

- **解题思路：** Go版本的解决方案同样使用了双指针的方法。其中，`zero`指针用于跟踪0的位置，`one`指针用于跟踪1的位置。

- **遍历数组：** 通过遍历数组中的每个元素，首先将当前元素的值设置为2，以表示最终排序的数组中的元素都是2。

- **处理0：** 如果当前元素的值小于等于1，将其设置为1，并将`one`指针向后移动。

- **处理0：** 如果当前元素的值为0，将其设置为0，并将`zero`指针向后移动。这将把0排在1的前面。

- **结束：** 完成遍历后，数组将按照所需的顺序排序：首先是0，然后是1，最后是2。

总的来说，所有版本的代码采用了双指针的方法，通过一次遍历数组并根据元素的值来重新排列数组中的元素，以实现题目所要求的排序。这种方法具有时间复杂度O(n)和常数空间复杂度，因此是高效的解决方案。
## 代码

## Go

```Go
func sortColors(nums []int) {
	zero, one := 0, 0 // 初始化两个指针，分别表示数字0和数字1的位置
	for i, n := range nums {
		nums[i] = 2 // 将数组中的数字都设置为2，这是初始状态
		if n <= 1 {
			nums[one] = 1 // 如果当前数字是0或1，将其置为1，并将one指针向后移动
			one++
		}
		if n == 0 {
			nums[zero] = 0 // 如果当前数字是0，将其置为0，并将zero指针向后移动
			zero++
		}
	}
}

```

## Python

```Python
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, one = 0, 0
        for i, n in enumerate(nums):
            nums[i] = 2
            if n <= 1:
                nums[one] = 1
                one += 1
            if n == 0:
                nums[zero] = 0
                zero += 1

```

## Java

```Java
class Solution {
    public void sortColors(int[] nums) {
        int zero = 0, one = 0, two = nums.length - 1;
        while (one <= two) {
            if (nums[one] == 0) {
                int temp = nums[zero];
                nums[zero] = nums[one];
                nums[one] = temp;
                zero++;
                one++;
            } else if (nums[one] == 2) {
                int temp = nums[one];
                nums[one] = nums[two];
                nums[two] = temp;
                two--;
            } else {
                one++;
            }
        }
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int zero = 0, one = 0, two = nums.size() - 1;
        while (one <= two) {
            if (nums[one] == 0) {
                swap(nums[zero], nums[one]);
                zero++;
                one++;
            } else if (nums[one] == 2) {
                swap(nums[one], nums[two]);
                two--;
            } else {
                one++;
            }
        }
    }
};
```

当介绍不同版本的代码时，我们将分别讨论每个版本的代码中所需的基础知识。

Python 版本：

1. **Python基础知识：** 需要熟悉Python的基本语法、数据类型、列表（List）的使用，循环（for循环）和条件语句（if语句）的使用。此外，需要了解Python的面向对象编程（OOP）概念，因为代码中使用了类和方法。

2. **LeetCode题目理解：** 需要理解LeetCode的题目，包括输入参数和要求的输出，以便能够编写相应的解决方案。

3. **数组操作：** 理解如何遍历和操作数组元素，以及如何使用enumerate()函数来同时获取元素和索引。

Java 版本：

1. **Java基础知识：** 需要对Java编程语言有基本的了解，包括类、方法、变量的声明和使用。理解循环和条件语句的使用也是必要的。

2. **LeetCode题目理解：** 同样需要理解LeetCode的题目要求，包括输入和输出的格式。

3. **数组操作：** 了解如何遍历和操作数组元素，以及如何使用数组的下标。

C++ 版本：

1. **C++基础知识：** 需要了解C++编程语言的基本语法，包括类、方法、变量的声明和使用。了解循环和条件语句的使用也是必要的。

2. **LeetCode题目理解：** 需要理解LeetCode的题目要求，包括输入和输出的格式。

3. **数组操作：** 了解如何遍历和操作数组元素，以及如何使用数组的下标。在C++中，可以使用`std::swap()`函数来交换数组元素。

4. **类和方法的使用：** 了解如何定义和使用类以及类的方法。在这个示例中，使用了一个类来包装排序方法。

Go 版本：

1. **Go基础知识：** 需要对Go编程语言有一些基本了解，包括函数、切片（slice）、for循环和if语句的使用。

2. **LeetCode题目理解：** 同样需要理解LeetCode的题目要求，包括输入和输出的格式。

3. **切片（slice）的使用：** 了解如何操作和修改切片，以及如何通过索引访问切片中的元素。

总的来说，不管是哪个编程语言版本，理解LeetCode题目、数组操作和基本编程语法都是解决问题的基础。不同语言的语法和特性可能略有不同，但解决问题的思路和算法通常是相似的。