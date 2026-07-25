class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            if nums[i] > 0:
                return res
            if i != 0 and nums[i-1] == nums[i]:
                continue
            
            while left < right:
                s =  nums[left] + nums[right] + nums[i]
                if s == 0:
                    res.append([nums[i] , nums[left] , nums[right]])
                    left+=1
                    right-=1
                    while left < right and nums[left - 1] == nums[left]:
                        left+=1
                    while left < right and nums[right + 1] == nums[right]:
                        right-=1
                elif s > 0:
                    right -=1
                else:
                    left +=1
            
        return res
       
# [-2,0,0,1,2]
