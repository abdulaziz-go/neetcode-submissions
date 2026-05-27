class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        checker = {} # key[List]
        for word in strs:
            key = "".join(sorted(word))
            if key in checker:
                checker[key].append(word)
            else: checker[key]=[word]


        return list(checker.values())