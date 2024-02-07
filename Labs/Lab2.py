class Solution:
    def isAnagram(self, a: str, b: str) -> bool:
        return sorted(a) == sorted(b)

solution = Solution()
a = "silent"
b = "listen"
result = solution.isAnagram(a, b)
print(result)
