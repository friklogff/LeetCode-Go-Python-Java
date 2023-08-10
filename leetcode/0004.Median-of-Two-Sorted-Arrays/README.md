# [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

## 题目

There are two sorted arrays**nums1**and**nums2**of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume**nums1**and**nums2**cannot be both empty.

**Example 1:**

    nums1 = [1, 3]
    nums2 = [2]
    
    The median is 2.0

**Example 2:**

    nums1 = [1, 2]
    nums2 = [3, 4]
    
    The median is (2 + 3)/2 = 2.5

## 题目大意

给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

## 解题思路

- 给出两个有序数组，要求找出这两个数组合并以后的有序数组中的中位数。要求时间复杂度为 O(log (m+n))。
- 这一题最容易想到的办法是把两个数组合并，然后取出中位数。但是合并有序数组的操作是 `O(m+n)`
  的，不符合题意。看到题目给的 `log` 的时间复杂度，很容易联想到二分搜索。
- 由于要找到最终合并以后数组的中位数，两个数组的总大小也知道，所以中间这个位置也是知道的。只需要二分搜索一个数组中切分的位置，另一个数组中切分的位置也能得到。为了使得时间复杂度最小，所以二分搜索两个数组中长度较小的那个数组。
- 关键的问题是如何切分数组 1 和数组 2 。其实就是如何切分数组 1 。先随便二分产生一个 `midA`
  ，切分的线何时算满足了中位数的条件呢？即，线左边的数都小于右边的数，即，`nums1[midA-1] ≤ nums2[midB] && nums2[midB-1] ≤ nums1[midA]`
  。如果这些条件都不满足，切分线就需要调整。如果 `nums1[midA] < nums2[midB-1]`，说明 `midA`
  这条线划分出来左边的数小了，切分线应该右移；如果 `nums1[midA-1] > nums2[midB]`，说明 midA
  这条线划分出来左边的数大了，切分线应该左移。经过多次调整以后，切分线总能找到满足条件的解。
- 假设现在找到了切分的两条线了，`数组 1` 在切分线两边的下标分别是 `midA - 1` 和 `midA`。`数组 2`
  在切分线两边的下标分别是 `midB - 1` 和 `midB`
  。最终合并成最终数组，如果数组长度是奇数，那么中位数就是 `max(nums1[midA-1], nums2[midB-1])`
  。如果数组长度是偶数，那么中间位置的两个数依次是：`max(nums1[midA-1], nums2[midB-1])` 和 `min(nums1[midA], nums2[midB])`
  ，那么中位数就是 `(max(nums1[midA-1], nums2[midB-1]) + min(nums1[midA], nums2[midB])) / 2`。图示见下图：

  ![](https://img.halfrost.com/Leetcode/leetcode_4.png)

各语言版本的解题思路:

Go版本:
1. 定义一个float64切片nums来存放输入的数字
2. 循环遍历nums,计算每个数的32位二进制表示
3. 统计每个位上0和1的数量,如果0比1多,则该位全部清0,否则该位全部置1
4. 得到修改后的32位二进制数,转为10进制浮点数并存入结果res切片

Python版本: 
1. 定义一个nums列表存放输入数字
2. 遍历nums中的每个数
3. 对每个数,获取它的32位二进制形式,统计每个位上0和1的数量
4. 如果0的个数多,该位赋值为0,否则赋值为1
5. 将修改后的32位二进制数转换为10进制浮点数,添加到结果列表res中

Java版本:
1. 定义一个数组nums来存放输入的数字
2. 遍历nums,对每个数字求它的32位二进制表示
3. 统计每个位上0和1的个数,如果0较多则该位赋0,否则赋1
4. 根据修改后的二进制数组生成十进制浮点数
5. 将浮点数添加到结果数组res中并返回

C++版本: 
1. 定义vector<double> nums来存输入数字
2. 遍历nums,对每个数字转二进制并统计每位上的0、1数量
3. 如果0的数量多,该位赋0,否则赋1
4. 将修改后的二进制数转十进制浮点数
5. 将浮点数添加到结果vector res中

## Go

```Go
func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
    // 假设 nums1 的长度小
    if len(nums1) > len(nums2) {
        return findMedianSortedArrays(nums2, nums1) // 如果nums1更长,交换参数位置,递归调用
    }
    low, high, k, nums1Mid, nums2Mid := 0, len(nums1), (len(nums1)+len(nums2)+1)>>1, 0, 0 // low和high表示二分查找的下界和上界,k表示两数组总长度的中位数索引,nums1Mid和nums2Mid表示nums1和nums2的中位数索引
    for low <= high {
        // nums1:  .................. nums1[nums1Mid-1] | nums1[nums1Mid] ........................
        // nums2:  .................. nums2[nums2Mid-1] | nums2[nums2Mid] ........................
        nums1Mid = low + (high-low)>>1 // 分界限右侧是mid,分界线左侧是mid - 1,二分查找更新nums1的中位数索引
        nums2Mid = k - nums1Mid // 根据nums1的中位数索引推算出nums2的中位数索引
        if nums1Mid > 0 && nums1[nums1Mid-1] > nums2[nums2Mid] {
            // nums1中的中位数划分偏右,需要左移
            high = nums1Mid - 1
        } else if nums1Mid != len(nums1) && nums1[nums1Mid] < nums2[nums2Mid-1] {
            // nums1中的中位数划分偏左,需要右移
            low = nums1Mid + 1
        } else {
            // 找到合适的划分,可以输出结果了
            break
        }
    }
    midLeft, midRight := 0, 0
    if nums1Mid == 0 {
        // nums1划分到左边界,取nums2中位数左边那个数
        midLeft = nums2[nums2Mid-1]
    } else if nums2Mid == 0 {
        // nums2划分到左边界,取nums1中位数左边那个数
        midLeft = nums1[nums1Mid-1]
    } else {
        // 否则取两个中位数左边的最大值
        midLeft = max(nums1[nums1Mid-1], nums2[nums2Mid-1])
    }
    if (len(nums1)+len(nums2))&1 == 1 {
        // 如果奇数长度,中位数就是midLeft
        return float64(midLeft)
    }
    if nums1Mid == len(nums1) {
        // nums1划分到右边界,取nums2中位数右边那个数
        midRight = nums2[nums2Mid]
    } else if nums2Mid == len(nums2) {
        // nums2划分到右边界,取nums1中位数右边那个数
        midRight = nums1[nums1Mid]
    } else {
        // 否则取两个中位数右边的最小值
        midRight = min(nums1[nums1Mid], nums2[nums2Mid])
    }
    return float64(midLeft+midRight) / 2 // 如果偶数长度,中位数是midLeft和midRight的平均值
}
func max(a int, b int) int {
    if a > b {
       return a
    }
    return b
}
func min(a int, b int) int {
    if a < b {
       return a
    }
    return b
}

```

## Python

```Python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 确保nums1更短
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        # 初始化变量
        low, high = 0, len(nums1)
        k = (len(nums1) + len(nums2) + 1) // 2
        while low <= high:
            # 计算nums1中的中间位置
            nums1_mid = low + (high - low) // 2
            # 计算nums2中的中间位置
            nums2_mid = k - nums1_mid
            # 判断是否找到正确的划分
            if nums1_mid > 0 and nums1[nums1_mid - 1] > nums2[nums2_mid]:
                # nums1中位数划分过大,向左移动
                high = nums1_mid - 1
            elif nums1_mid < len(nums1) and nums1[nums1_mid] < nums2[nums2_mid - 1]:
                # nums1中位数划分过小,向右移动
                low = nums1_mid + 1
            else:
                # 找到正确的划分,计算中位数
                break
        # 计算中位数       
        mid_left = 0
        if nums1_mid == 0:
            mid_left = nums2[nums2_mid - 1]
        elif nums2_mid == 0:
            mid_left = nums1[nums1_mid - 1]
        else:
            mid_left = max(nums1[nums1_mid - 1], nums2[nums2_mid - 1])
        if (len(nums1) + len(nums2)) % 2 == 1:
            return mid_left
        mid_right = 0
        if nums1_mid == len(nums1):
            mid_right = nums2[nums2_mid]
        elif nums2_mid == len(nums2):
            mid_right = nums1[nums1_mid]
        else:
            mid_right = min(nums1[nums1_mid], nums2[nums2_mid])
        return (mid_left + mid_right) / 2
```

## Java

```Java
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // 假设 nums1 长度小于等于 nums2
        if (nums1.length > nums2.length) {
            return findMedianSortedArrays(nums2, nums1);
        }
        int low = 0;
        int high = nums1.length;
        int k = (nums1.length + nums2.length + 1) / 2;
        int nums1Mid = 0;
        int nums2Mid = 0;
        while (low <= high) {
            // nums1: 左子数组.......... nums1[nums1Mid-1] | nums1[nums1Mid]..........右子数组
            // nums2: 左子数组.......... nums2[nums2Mid-1] | nums2[nums2Mid]..........右子数组
            nums1Mid = (low + high) / 2;
            nums2Mid = k - nums1Mid;
            if (nums1Mid > 0 && nums1[nums1Mid - 1] > nums2[nums2Mid]) {
                // nums1 中的分界线划多了,要向左边移动
                high = nums1Mid - 1;
            } else if (nums1Mid != nums1.length && nums1[nums1Mid] < nums2[nums2Mid - 1]) {
                // nums1 中的分界线划少了,要向右边移动
                low = nums1Mid + 1;
            } else {
                // 找到合适的划分,可以输出结果
                break;
            }
        }
        // 计算中位数
        int midLeft = 0, midRight = 0;
        if (nums1Mid == 0) {
            midLeft = nums2[nums2Mid - 1];
        } else if (nums2Mid == 0) {
            midLeft = nums1[nums1Mid - 1];
        } else {
            midLeft = Math.max(nums1[nums1Mid - 1], nums2[nums2Mid - 1]);
        }
        if ((nums1.length + nums2.length) % 2 == 1) {
            // 奇数的情况下中位数就是 midLeft
            return midLeft;
        }
        // 偶数的情况下需要计算 midRight
        if (nums1Mid == nums1.length) {
            midRight = nums2[nums2Mid];
        } else if (nums2Mid == nums2.length) {
            midRight = nums1[nums1Mid];
        } else {
            midRight = Math.min(nums1[nums1Mid], nums2[nums2Mid]);
        }
        return (midLeft + midRight) / 2.0;
    }
}
```

## Cpp

```Cpp
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // 假设nums1数组更短
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1); // 如果nums1更长,交换两个数组作为参数,递归调用
        }
        int low = 0; // 二分查找左边界
        int high = nums1.size(); // 二分查找右边界
        int k = (nums1.size() + nums2.size() + 1) / 2; // 两个数组总长度的中位数索引
        int nums1Mid, nums2Mid; // nums1和nums2数组的中位数索引
        while(low <= high) {
            nums1Mid = low + (high - low) / 2; // 计算nums1数组的中位数索引
            nums2Mid = k - nums1Mid; // 根据nums1的中位数索引计算出nums2中的中位数索引
            if (nums1Mid > 0 && nums1[nums1Mid-1] > nums2[nums2Mid]) {
                // nums1中的中位数划分偏右,需要左移边界
                high = nums1Mid - 1; 
            } else if (nums1Mid != nums1.size() && nums1[nums1Mid] < nums2[nums2Mid-1]) {
                // nums1中的中位数划分偏左,需要右移边界 
                low = nums1Mid + 1;
            } else {
                // 找到合适的划分,退出二分查找循环
                break; 
            }
        }
        int midLeft, midRight; // 两个中位数的值
        if (nums1Mid == 0) {
            // nums1数组划分到最左,取nums2数组中位数左边的值
            midLeft = nums2[nums2Mid-1];
        } else if (nums2Mid == 0) {
            // nums2数组划分到最左,取nums1数组中位数左边的值
            midLeft = nums1[nums1Mid-1];
        } else {
            // 否则取两个数组中位数左边的最大值
            midLeft = max(nums1[nums1Mid-1], nums2[nums2Mid-1]); 
        }
        if ((nums1.size() + nums2.size()) % 2 == 1) {
            // 如果总长度是奇数,中位数就是midLeft
            return midLeft;
        }
        if (nums1Mid == nums1.size()) {
            // nums1数组划分到最右,取nums2数组中位数右边的值 
            midRight = nums2[nums2Mid];
        } else if (nums2Mid == nums2.size()) {
            // nums2数组划分到最右,取nums1数组中位数右边的值
            midRight = nums1[nums1Mid];
        } else {
            // 否则取两个数组中位数右边的最小值
            midRight = min(nums1[nums1Mid], nums2[nums2Mid]);
        }
        return (midLeft + midRight) / 2.0; // 如果总长度是偶数,返回平均值
    }
}; 
```
四个版本解法所需的基础知识:

Go版本:
- 切片的定义、初始化,使用len获取长度,通过下标访问元素
- 移位运算符像<<、>>,与运算符&用于获取特定bit
- math包下的Abs、Pow、Sqrt等数学函数
- 浮点数的基本运算 + - * /
- float64()将整数转为浮点数

Python版本:
- list的定义、初始化,使用len获取长度,通过下标访问元素 
- 整数除法//和求余运算%
- 内置函数max、min求最大最小值
- 浮点数的基本运算 + - * /
- float()将整数转浮点数

Java版本:
- 数组的定义、初始化,使用length获取长度,通过下标访问元素
- Math类的静态方法max、min求最大最小值
- 静态方法Math.abs获取绝对值
- 强制类型转换(double)将整数转为双精度浮点数
- 浮点数的基本运算 + - * /

C++版本:
- vector的定义、初始化,size() 获取元素数量,通过下标访问元素
- 整数相除的运算符/和求余运算%
- algorithm头文件下的max、min模板函数求最大最小值
- cmath头文件下的abs等数学函数
- 浮点数的基本运算 + - * /
- 静态强制类型转换static_cast<double>将整数转为双精度浮点数
