# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in solution:
                return [solution[complement], i]
            else:
                solution[nums[i]] = i

s = Solution()
print(s.twoSum([2,6,7,8],9))