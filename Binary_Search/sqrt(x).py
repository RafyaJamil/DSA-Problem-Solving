# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        ans = 0
        while(left <= right):
            mid = (left + right) // 2
            if(mid * mid == x):
                return mid
            elif(mid * mid > x):
                right = mid - 1
            else:
                left = mid + 1
                ans = mid
        return ans

s = Solution()
print(s.mySqrt(36))