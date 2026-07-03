class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        iters = sorted(s)
        itert = sorted(t)
        for i in range(len(s)):
            if iters[i] != itert[i]:
                return False
        
        return True