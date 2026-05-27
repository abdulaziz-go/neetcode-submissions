from collections import defaultdict
from typing import List



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for str in strs:
            count = [0] * 26

            for e in str:
                count[ord(e) - ord("a")]+=1

            result[tuple(count)].append(str)

        return [value for value in result.values()]