# [1. Two Sum](https://leetcode.com/problems/two-sum/)

## 题目

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```



## 题目大意

在数组中找到 2 个数之和等于给定值的数字，结果返回 2 个数字在数组中的下标。

## 解题思路

这道题最优的做法时间复杂度是 O(n)。

顺序扫描数组，对每一个元素，在 map 中找能组合给定值的另一半数字，如果找到了，直接返回 2 个数字的下标即可。如果找不到，就把这个数字存入 map 中，等待扫到“另一半”数字的时候，再取出来返回结果。

1. 使用map[int]int来保存元素值和索引的映射
2. 遍历数组nums,计算目标值与当前元素的差值another
3. 在map中查找another是否存在,如果找到则返回两个索引
4. 如果map中不存在another,则将当前元素和索引存入map
5. 遍历结束后若没有结果则返回nil

Python:
1. 使用字典num_map保存元素和索引的映射
2. 遍历nums列表,利用enumerate同时获取索引和值
3. 计算目标值与当前元素的差值another,判断another是否在num_map中
4. 如果在,返回两个元素的索引;如果不在,将当前元素和索引存入num_map
5. 遍历结束若无结果则返回空列表[]

Java:
1. 使用HashMap保存元素值和索引的映射
2. 遍历数组nums,计算目标值与当前元素差值another
3. 判断another是否在Map中,如果存在直接返回两个索引
4. 如果another不在Map中,将当前元素和索引存入Map
5. 遍历结束若无结果则返回空数组new int[0]
## Go
```Go
func twoSum(nums []int, target int) []int {
  // 定义map用于存储元素和索引
  m := make(map[int]int)
  
  // 遍历数组
  for i := 0; i < len(nums); i++ {
    // 计算另一个需要的数
    another := target - nums[i]
    
    // 在map中查找another是否存在
    if _, ok := m[another]; ok { 
      // 如果存在,返回两个数的索引
      return []int{m[another], i}
    }
    
    // 不存在,将当前元素和索引存入map
    m[nums[i]] = i
  }
  
  // 遍历完成未找到,返回nil
  return nil 
}
```
## Python
```Python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      
        # 定义字典保存元素和索引映射
        num_map = {}
        
        # 遍历nums列表,enumerate可以同时获得迭代对象的索引和值
        for i, num in enumerate(nums):
          
            # 计算需要的另一个数
            another = target - num  
            
            # 判断another是否在num_map中
            if another in num_map:
              
                # 如果在,返回两个数的索引
                return [num_map[another], i]
            
            # 如果不在,将当前num和索引添加到num_map
            num_map[num] = i
            
        # 遍历结束没有找到,返回空列表
        return []

```
## Java
```Java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        // 定义HashMap保存数值和索引
        Map<Integer, Integer> numMap = new HashMap<>();
        
        // 遍历数组
        for (int i = 0; i < nums.length; i++) {
            
            // 计算需要的另一个数
            int another = target - nums[i];
            
            // 判断map中是否存在该数
            if (numMap.containsKey(another)) {
                
                // 如果存在直接返回两个数的索引
                return new int[] {numMap.get(another), i};
                
            }
            
            // 不存在则将当前数和索引放入map
            numMap.put(nums[i], i);
        }
        
        // 遍历结束没有结果则返回空数组
        return new int[0];
    }
}

```
三个版本两数之和解法所需的基础知识:

Go 版本:
1. map:Go中内置的字典类型,用于存储键值对。查找时间复杂度 O(1)。
2. 索引访问:Go中的数组可以通过索引快速访问元素。
3. _, ok:= map[key] 操作:在map中查找key,ok为bool类型,表示是否找到。
4. 语法:条件判断、循环、函数定义、变量声明等语法基础。

Python 版本:
1. 字典(dict):Python内置的数据结构,用于存储键值对映射关系。查找速度快,时间复杂度为 O(1)。
2. enumerate():Python 的内置函数,可以同时遍历序列的元素和索引。
3. list:Python 的列表数据类型,可变序列,支持快速插入和删除。
4. in操作符:用于判断字典中是否存在指定的键。
5. 语法:条件表达式、循环、函数定义、索引访问等基础语法。

Java 版本:
1. HashMap:Java中的哈希表实现,用于存储键值对。查找速度快,时间复杂度为 O(1)。
2. 数组和索引:数组int[]存储数据,索引访问元素。
3. containsKey():Map中的方法,判断是否包含指定的键。
4. 语法:条件判断、循环、方法定义、数组索引等基础语法。

