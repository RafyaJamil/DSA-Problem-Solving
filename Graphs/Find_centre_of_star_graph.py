# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
       if edges[0][0] in edges[1]:
        return edges[0][0]
       return edges[0][1]
s = Solution()
print(s.findCenter([[1,2],[2,3],[2,4]]))