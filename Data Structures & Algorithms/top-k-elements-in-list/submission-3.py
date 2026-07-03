class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        result = []
        for _ in range(k):
            freqCount = 0
            num = None

            for k , v in hashmap.items():
                if v > freqCount:
                    freqCount=v
                    num = k
            result.append(num)
            del hashmap[num]

        return result




