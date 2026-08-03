# Time Complexity: O(log n)
# Space Complexity: O(1)

first_bad = 4
def isBadVersion(version):
    return version >= first_bad
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n 
        while(left <= right):
            mid = (left + right) // 2
            if(isBadVersion(mid)):
                right = mid - 1
            else:
                left = mid + 1
        return left

s = Solution()
print(s.firstBadVersion(5))