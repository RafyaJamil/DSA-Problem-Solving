# Time Complexity: O(n + t)
# Space Complexity: O(n)

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [0] * (n + 1)
        outdegree = [0] * (n + 1)

        for a, b in trust:
            outdegree[a] += 1
            indegree[b] += 1

        for person in range(1, n + 1):
            if outdegree[person] == 0 and indegree[person] == n - 1:
                return person

        return -1

solution = Solution()

n = 3
trust = [[1, 3], [2, 3]]
result = solution.findJudge(n, trust)
print("Judge is:", result)