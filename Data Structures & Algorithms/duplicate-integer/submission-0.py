class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counterMap = Counter(nums)
        for _ , value in counterMap.items():
            if value > 1:
                return True

        return False