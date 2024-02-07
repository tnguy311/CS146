def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
target = 17
result = two_sum(nums, target)
print(result)
