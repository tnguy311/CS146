def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()  # Sort the array 

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue     # Skip duplicate fixed numbers

            target = -nums[i]
            seen = set()  # Hash set to store unique pairs

            for j in range(i + 1, len(nums)):
                complement = target - nums[j]

                # If complement is in the set, add the triplet to the result
                if complement in seen:
                    result.append([nums[i], complement, nums[j]])

                    # Skip duplicate numbers
                    while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                        j += 1

                seen.add(nums[j])

        return result

# Test cases
solution = Solution()
print(solution.threeSum([0, 1, 1]));
print(solution.threeSum([-5, 0, 5, 10, -10, 0]))  # Output: [[-10, 0, 10], [-5, 0, 5]]
