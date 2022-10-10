

nums = [1,2,3,4,5]

# for (int x = 0; x<nums.length; x++) {
#   print(nums[x]);
# }

# for (x = 0; x<len(nums); x++):
#   print(nums[x])

# difference between imperative and declarative code

# more imperative way

# count = len(nums)
# counter = 0

# while counter < count:
#   print(nums[counter])
#   counter = counter + 1

# more declarative

for num in nums:
  print(num)


# for (int x = 0; x<5; x++) {
#   print(x + 1);
# }

for num in range(5):
  print(num + 1)

print(list(range(5)))