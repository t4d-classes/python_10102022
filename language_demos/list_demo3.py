from random import randint


# nums = []

# for _ in range(10):
#   nums.append(randint(0, 100))

nums = list(map(lambda _: randint(0, 100), range(10)))

# nums = [ randint(0, 100) for _ in range(10) ]

# print(nums)
# print(nums[0])
# print(nums[-1])
# # print(nums[len(nums) - 1])
# print(nums[:3])
# print(nums[1:5])
# print(nums[::2])

# nums.sort()
# print(nums)

sorted_nums = sorted(nums, reverse=True)
print(nums)
print(sorted_nums)
