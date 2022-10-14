from typing import Generator

double_nums = (x * 2 for x in range(10))

# print(double_nums)

for num in double_nums:
    print(num)

