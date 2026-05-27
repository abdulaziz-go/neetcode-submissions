class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
       
        counterS , counterD = {}, {}
        for e in s:
            if not e in counterS:
                counterS[e]=1
            else: counterS[e]+=1

        for d in t:
            if not d in counterD:
                counterD[d]=1
            else: counterD[d]+=1
        for key , value in counterS.items():
            if key in counterD and key in counterS:
                if counterD[key] != counterS[key]:
                    return False
            else: return False
        return True