class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        hm_s=defaultdict(int)
        hm_t=defaultdict(int)
        
        for i in range(len(s)):
            hm_s[s[i]] += 1
            hm_t[t[i]] += 1
        
        if hm_s == hm_t:
            return True
        
        return False

        