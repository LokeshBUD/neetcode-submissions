class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hm = defaultdict(int)
        for c in s:
            hm[c] += 1
        for c in t: 
            hm[c] -= 1
            if hm[c] < 0:
                return False
        
        return True
        