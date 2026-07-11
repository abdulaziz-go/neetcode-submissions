class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        res = []
        for k , v in count.items():
            print(k , v)
            if k == 0:
                 for _ in range(v):
                    res.append(0)

        for k , v in count.items():
            if k == 1:
                for _ in range(v):
                    res.append(1)
        print(res)
        for k , v in count.items():
            if k == 2:
                for _ in range(v):
                    res.append(2)
        
        for i in range(len(nums)):
            nums[i]=res[i]
        return res