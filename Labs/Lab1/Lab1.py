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

# Initialize an empty dictionary 'num_map' to store numbers seen so far, with the number as key and its index as value.
# Iterate through the list 'nums' using enumerate() to get both the index and the number.
# Calculate the complement by subtracting the current number from the target.
# Check if the complement exists in 'num_map':
# If it does, return a list containing the index of the complement and the current index.
# If it doesn't, store the current number and its index in 'num_map'.
# If the loop completes without finding a solution, it means there are no two numbers that add up to the target, so return None or handle the case appropriately.
# In the main code, specify the list of numbers 'nums' and the target sum 'target'.
# Call the 'two_sum' function with the given inputs and print the result.
