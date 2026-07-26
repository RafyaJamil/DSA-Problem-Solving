# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def findMaxConsecutiveOnes(self, nums)
        add = 0
        total = 0
        for i in range(len(nums)):
            if(nums[i] == 1):
                add = add + 1
                if(add > total):
                    total = add
            else:
                add = 0
        return total

s = Solution()
print(s.findMaxConsecutiveOnes([1,1,0,1,1,1,1]))