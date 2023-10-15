# [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/)


## 题目

Implement`int sqrt(int x)`.

Compute and return the square root of*x*, where*x*is guaranteed to be a non-negative integer.

Since the return typeis an integer, the decimal digits are truncated and only the integer part of the resultis returned.

**Example 1:**

    Input: 4
    Output: 2

**Example 2:**

    Input: 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since 
                 the decimal part is truncated, 2 is returned.


## 题目大意

实现int sqrt(int x)函数。计算并返回x的平方根，其中x 是非负整数。由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。



## 解题思路

- 题目要求求出根号 x
- 根据题意，根号 x 的取值范围一定在 `[0,x]` 之间，这个区间内的值是递增有序的，有边界的，可以用下标访问的，满足这三点正好也就满足了二分搜索的 3 大条件。所以解题思路一，二分搜索。
- 解题思路二，牛顿迭代法。求根号 x，即求满足 `x^2 - n = 0` 方程的所有解。

    ![](https://img-blog.csdn.net/20171019164040871?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvY2hlbnJlbnhpYW5n/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)
## 代码

## Go

```Go
// 定义一个函数 mySqrt，用于计算整数 x 的平方根
func mySqrt(x int) int {
    // 如果 x 为 0，直接返回 0
    if x == 0 {
        return 0
    }
    // 如果 x 小于 4，直接返回 1，因为 1 的平方是 1，2 的平方是 4，3 的平方是 9
    if x < 4 {
        return 1
    }

    // 调用 binarySearch2 函数进行二分查找，寻找 x 的平方根
    res := binarySearch2(2, x/2, x)
    // 如果找到的平方根的平方大于 x，则返回平方根减 1
    if res*res > x {
        return res - 1
    }
    // 否则直接返回找到的平方根
    return res
}

// 定义一个二分查找函数 binarySearch2，用于在区间 [l, r] 中寻找 target 的平方根
func binarySearch2(l, r, target int) int {
    // 使用循环进行二分查找
    for l < r {
        // 计算中间值 mid，避免溢出使用位运算
        mid := l + ((r - l) >> 1)

        // 计算中间值的平方
        tmp := mid * mid

        // 如果中间值的平方等于目标值，则直接返回中间值
        if tmp == target {
            return mid
        } else if tmp < target {
            // 如果中间值的平方小于目标值，则将搜索范围缩小到[mid+1, r]
            l = mid + 1
        } else {
            // 如果中间值的平方大于目标值，则将搜索范围缩小到[l, mid-1]
            r = mid - 1
        }
    }
    // 如果循环结束时 l >= r，返回 l 即可
    return l
}

```

## Python

```Python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x < 4:
            return 1

        res = self.binarySearch(2, x // 2, x)
        if res * res > x:
            return res - 1
        return res

    def binarySearch(self, l, r, target):
        while l < r:
            mid = l + ((r - l) >> 1)
            tmp = mid * mid
            if tmp == target:
                return mid
            elif tmp < target:
                l = mid + 1
            else:
                r = mid - 1
        return l

```

## Java

```Java
class Solution {
    public int mySqrt(int x) {
        if (x == 0) {
            return 0;
        }

        // 将 C 初始化为 x，x0 初始化为 x
        double C = x, x0 = x;

        // 使用牛顿迭代法逼近平方根
        while (true) {
            // 计算下一个迭代值 xi
            double xi = 0.5 * (x0 + C / x0);

            // 如果当前迭代值与上一次迭代值之差小于 1e-7，则认为已经逼近到足够精度，跳出循环
            if (Math.abs(x0 - xi) < 1e-7) {
                break;
            }

            // 更新迭代值 x0
            x0 = xi;
        }

        // 将最终的浮点数转换为整数并返回
        return (int) x0;
    }
}

```

## Cpp

```Cpp
class Solution {
public:
    int mySqrt(int x) {
        if (x == 0) {
            return 0;
        }

        double C = x, x0 = x;
        while (true) {
            double xi = 0.5 * (x0 + C / x0);
            if (fabs(x0 - xi) < 1e-7) {
                break;
            }
            x0 = xi;
        }
        return int(x0);
    }
};

```
