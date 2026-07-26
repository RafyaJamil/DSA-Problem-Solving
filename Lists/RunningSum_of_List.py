# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def runningSum(self, nums):
        runningSum = []
        add = 0
        for i in range(len(nums)):
            add = add + nums[i]
            runningSum.append(add)
        return runningSum

s = Solution()
print(s.runningSum([1,3,5,6]))