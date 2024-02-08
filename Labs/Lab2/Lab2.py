class Solution:
    def isAnagram(self, a: str, b: str) -> bool:
        return sorted(a) == sorted(b)

solution = Solution()
a = "silent"
b = "listen"
result = solution.isAnagram(a, b)
print(result)

#sorting the characters in both strings and comparing if the sorted versions are equal.
#In Python implementations, we use the the sorted() function to sort the characters in the strings.
#We then compare the sorted strings using the equality operator == to check if they are anagrams.
#If the lengths of the strings are different, they cannot be anagrams, so we return False immediately in that case.
#Otherwise, we return the result of the comparison. If the sorted strings are equal, it means the strings are anagrams, so we return True; otherwise, False.
