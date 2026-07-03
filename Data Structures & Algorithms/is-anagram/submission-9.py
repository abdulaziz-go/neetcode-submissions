class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = [0] * 26
        
        for letter in s:
            counter[ord(letter) - ord('a')]+=1 
        
        for letter in t:
            counter[ord(letter) - ord('a')]-=1
        
        for n in counter:
            if n != 0:
                return False
            
        return True