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