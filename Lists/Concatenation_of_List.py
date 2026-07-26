# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def getConcatenation(self, nums):
        ans = []
        for i in range(len(nums)):
            ans.append(nums[i])
        ans1 = ans.copy()
        ans = ans + ans1
        return ans

s = Solution()
print(s.getConcatenation([1,2,3,5]))