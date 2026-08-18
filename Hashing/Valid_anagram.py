# Time Complexity: O(n + m)
# Space Complexity: O(k)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ana = {}
        for i in range(len(s)):
            if s[i] not in ana:
                ana[s[i]] = 0
            ana[s[i]] += 1
        for j in range(len(t)):
            if t[j] not in ana:
                ana[t[j]] = 0
            ana[t[j]] -= 1
        for value in ana.values():
            if value != 0:
                return False
        return True

s = Solution()
print(s.isAnagram("aabb","abab"))