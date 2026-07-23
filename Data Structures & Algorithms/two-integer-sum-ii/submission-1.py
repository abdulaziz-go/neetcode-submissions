class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        fp , sp = 0 , len(numbers) - 1
        while fp < sp:
            current_sum = numbers[fp] + numbers[sp]
            if current_sum > target:
                sp-=1
            elif current_sum < target:
                fp+=1
            else:
                return [fp+1 , sp+1]
        return []
