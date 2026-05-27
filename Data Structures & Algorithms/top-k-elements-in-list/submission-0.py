import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        min_heap = []
        for n , freq in count.items():
            heapq.heappush(min_heap , (freq , n))

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [num for freq , num in min_heap]