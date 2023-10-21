"""

NAME : input_test

USER : admin

DATE : 20/10/2023

PROJECT_NAME : README.md

CSDN : friklogff
"""
# numbers = list(map(int, input().split()))
# numbers.sort()
# for num in numbers:
#     print(num, end=' ')

# while True:
#     try:
#         a, b = map(int, input().strip().split())
#         print(a + b)
#     except EOFError:
#         break

# a, b = map(int, input().strip().split())
# print(a + b)

# num_students = int(input().strip())
#
#
# def is_numeric(x):
#     if ord(x[0]) < 90:  # 判断是数字还是字母
#         return int(x)
#     return x
#
#
# data = [list(map(is_numeric, input().split())) for i in range(num_students)]
# print(data)
#
# print([x[2] for x in data])
# average = sum([x[2] for x in data]) / num_students
# print(int(average), end=' ')
# max_score_student = max(data, key=lambda x: sum(x[2:]))
# print(*max_score_student)


# 使用Lambda函数计算两个数的和
add = lambda x, y: x + y
result = add(2, 3)
print(result)  # 输出: 5

# 使用Lambda函数作为sorted()函数的key参数，对列表进行排序
data = [(1, 'apple'),
        (3, 'banana'),
        (2, 'cherry')]
print((data, lambda x: x[1]))
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # 输出: [(1, 'apple'), (3, 'banana'), (2, 'cherry')]
