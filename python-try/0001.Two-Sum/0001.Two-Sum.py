"""

NAME : 0001.Two-Sum

USER : admin

DATE : 20/10/2023

PROJECT_NAME : README.md

CSDN : friklogff
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

            # 定义字典保存元素和索引映射
            num_map = {}

            # 遍历nums列表,enumerate可以同时获得迭代对象的索引和值
            for i, num in enumerate(nums):
                print("i,num:",i,num)
                print('num_map',num_map)
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


if __name__ == '__main__':
    S = Solution()
    res = S.twoSum([1, 1, 3, 4, 5], 6)
    print(res)
