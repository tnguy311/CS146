class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        length = 0
        odd_count = False
        
        for count in char_count.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                odd_count = True
        
        if odd_count:
            length += 1
        
        return length
