class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat = []
        for m in matrix:
            flat.extend(m)
        
        low , high = 0 , len(flat) - 1

        while low <= high:
            mid = (low+high) // 2
            if flat[mid] == target:
                return True
            elif flat[mid] > target:
                high = mid - 1
            else:
                low = mid+1
        return False

