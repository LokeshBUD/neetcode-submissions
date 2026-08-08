class Solution:
    def isPalindrome(self, s: str) -> bool:
        # this is string reverse approach
        res = ''
        for c in s:
            if c.isalnum():
                res += c.lower()
        return res == res[::-1]