class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s1 = {}
        l1 = {}
        for i in range(len(s)):
            s1[s[i]] = 0
            l1[t[i]] = 0
        for i in range(len(s)):
            s1[s[i]] += 1
            l1[t[i]] += 1

        
        if s1 == l1:
            return True
        return False