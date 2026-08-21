class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        mi , ma = max(weights) , sum(weights)
        ans = ma
        while mi <= ma:
            mid = (mi + ma) // 2
            total_d = 1
            total_w = 0
            for w in weights:
                if total_w + w > mid:
                    total_d+=1
                    total_w=0
                total_w+=w
            if total_d <= days:
                ans = mid
                ma = mid - 1
            else:
                mi = mid + 1

        return ans