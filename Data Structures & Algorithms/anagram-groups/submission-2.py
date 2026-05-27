from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        checker = defaultdict(list)
        
        for word in strs:
            # Create a count array for 26 lowercase English letters
            count = [0] * 26 
            
            for char in word:
                # Map character to index 0-25 using ASCII values
                count[ord(char) - ord('a')] += 1
                
            # Convert list to tuple so it can be used as a dictionary key
            checker[tuple(count)].append(word)
            
        return list(checker.values())