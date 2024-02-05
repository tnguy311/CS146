def two_sum(nums, target):
    # Create a special box called a dictionary to remember things
    complement_dict = {}

    # Go through each number in the list
    for i, num in enumerate(nums):
        # Calculate a special number that, when added to the current number, gives the target
        complement = target - num
        
        # Check if the special number is already in our special box
        if complement in complement_dict:
            # If it's there, we found our two numbers! Return their positions
            return [complement_dict[complement], i]
        
        # If the special number is not in our box, put the current number in the box
        complement_dict[num] = i

    # If we don't find the numbers, return an empty answer
    return []
