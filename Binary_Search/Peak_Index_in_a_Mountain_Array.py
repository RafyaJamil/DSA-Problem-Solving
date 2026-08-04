# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while(left < right):
            mid = (left + right) // 2
            if(arr[mid] > arr[mid + 1]):
                right = mid
            else:
                left = mid + 1
        return left

s = Solution()
print(s.peakIndexInMountainArray([1,2,3,4,2,0]))