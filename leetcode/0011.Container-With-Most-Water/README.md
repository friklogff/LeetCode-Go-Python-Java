# [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

## 题目

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 1:

```c
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
```


## 题目大意

给出一个非负整数数组 a1，a2，a3，…… an，每个整数标识一个竖立在坐标轴 x 位置的一堵高度为 ai 的墙，选择两堵墙，和 x 轴构成的容器可以容纳最多的水。

## 解题思路


这一题也是对撞指针的思路。首尾分别 2 个指针，每次移动以后都分别判断长宽的乘积是否最大。
## Go版本
- 定义最大面积max,左右指针start和end
- 循环判断start<end
- 计算宽度width为end-start
- 初始化高度high为0
- 判断height[start]和height[end]大小
- 高度high取较小值
- 移动高度较小指针
- 计算面积temp为宽度*高度
- 比较temp和max,更新max
## Python版本
- 定义最大面积max,左右指针start和end指向列表两端
- 循环判断start<end
- 计算宽度width为end-start
- 初始化高度high为0
- 判断height[start]和height[end]大小
- 高度high取较小值
- 移动高度较小指针
- 计算面积area为宽度*高度
- 比较area和max,更新max
## Java版本
- 定义最大面积max,左右指针start和end指向数组两端
- 循环判断start<end
- 计算宽度width为end-start
- 初始化高度high为0 
- 判断height[start]和height[end]大小
- 高度high取较小值
- 移动高度较小指针
- 计算面积temp为宽度*高度
- 比较temp和max,更新max
## C++版本
- 定义最大面积max,左右指针start和end指向向量两端
- 循环判断start<end
- 计算宽度width为end-start
- 初始化高度high为0
- 判断height[start]和height[end]大小
- 高度high取较小值 
- 移动高度较小指针
- 计算面积temp为宽度*高度
- 比较temp和max,更新max

## 代码

## Go
```Go
func maxArea(height []int) int {
    // 初始化最大面积max为0,start为0,end为数组长度-1
    max, start, end := 0, 0, len(height)-1 
    // 当start小于end时循环
    for start < end {
       // 宽度为end-start
       width := end - start 
       // 高初始化为0 
       high := 0
       // 如果start位置的高度小于end位置 
       if height[start] < height[end] {
          // 高为start位置的高度
          high = height[start]
          // start加1
          start++
       } else {
          // 否则高为end位置的高度
          high = height[end]
          // end减1
          end--
       }
       // 临时面积为宽乘高
       temp := width * high
       // 如果临时面积大于最大面积
       if temp > max {
          // 更新最大面积
          max = temp
       }
    }
    // 返回最大面积
    return max
}
```
## Python
```Python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 初始化最大面积为0,左右指针start和end分别指向列表两端
        max_area = 0
        start = 0
        end = len(height) - 1
        while start < end:
            # 计算当前宽度
            width = end - start
            # 初始化高度为0
            high = 0
            if height[start] < height[end]:
                # 如果左指针对应的高度更小,则取左指针高度
                high = height[start]
                # 左指针右移
                start += 1
            else:
                # 否则取右指针高度
                high = height[end]
                # 右指针左移
                end -= 1
            # 计算当前面积   
            area = width * high
            # 如果当前面积大于最大面积,则更新最大面积
            if area > max_area:
                max_area = area
        return max_area
```
## Java
```Java
class Solution {
    public int maxArea(int[] height) {
        // 初始化最大面积为0,左右指针start和end分别指向数组两端
        int max = 0, start = 0, end = height.length - 1;
        while(start < end) {
            // 计算当前宽度
            int width = end - start;
            // 初始化高度为0
            int high = 0;
            if(height[start] < height[end]) {
                // 如果左指针对应的高度更小,则取左指针高度
                high = height[start];
                // 左指针右移
                start++;
            } else {
                // 否则取右指针高度
                high = height[end];
                // 右指针左移
                end--;
            }
            // 计算当前面积
            int temp = width * high;
            // 如果当前面积大于最大面积,则更新最大面积
            if(temp > max) {
                max = temp;
            }
        }
        return max;
    }
}
```
## Cpp
```Cpp
class Solution {
public:
    int maxArea(vector<int>& height) {
        // 初始化最大面积为0,左右指针start和end分别指向向量两端
        int max = 0, start = 0, end = height.size() - 1;
        while(start < end) {
            // 计算当前宽度
            int width = end - start;
            // 初始化高度为0
            int high = 0;
            if(height[start] < height[end]) {
                // 如果左指针对应的高度更小,则取左指针高度
                high = height[start];
                // 左指针右移
                start++;
            } else {
                // 否则取右指针高度
                high = height[end];
                // 右指针左移
                end--;
            }
            // 计算当前面积
            int temp = width * high;
            // 如果当前面积大于最大面积,则更新最大面积
            if(temp > max) {
                max = temp;
            }
        }
        return max;
    }
};
```
每个语言版本需要掌握的基础知识:
## Go 版本
Go语言版本需要掌握以下知识:
- 变量声明 - 使用`:=`声明并初始化变量
- 数组 - 使用`[]int`声明数组,len()获取数组长度
- for循环 - for 开始条件; 结束条件; 步进
- if条件判断 - if条件 {} else {}
- 相加减 - +,-
- 乘法 - *
- 大于小于 - >,<
- 返回值 - 使用`return`
## Python版本
Python版本需要掌握以下知识:
- 变量 - 无需声明类型,直接赋值使用
- 列表 - 使用`[]`声明列表,len()获取长度
- while循环 - while 条件:
- if条件判断 - if 条件: 、`else:`
- 相加减 - +,-
- 乘法 - *
- 大于小于 - >,<  
- 返回值 - return
## Java版本
Java版本需要掌握以下知识:
- 变量声明 - 声明变量类型,如`int`
- 数组 - 使用`int[]`声明数组,.length获取长度
- for循环或while循环
- if条件判断 - if() {} else {}
- 相加减 - +,-
- 乘法 - *
- 大于小于 - >,<
- 返回值 - return
## C++版本
C++版本需要掌握以下知识:
- 变量声明 - 声明变量类型,如`int`
- vector容器 - vector<int>声明,.size()获取长度
- while循环
- if条件判断 - if() {} else {}
- 相加减 - +,-
- 乘法 - *
- 大于小于 - >,<
- 返回值 - return