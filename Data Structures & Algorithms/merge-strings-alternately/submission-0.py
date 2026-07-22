class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        ptr  = 0
        minLen = min(len(word1) , len(word2))
        while ptr < minLen:
            result+=word1[ptr]+ word2[ptr]
            ptr+=1
        
        if len(word1) > minLen:
            result+= word1[ptr:]
        if len(word2) > minLen:
            result+= word2[ptr:]

        return result