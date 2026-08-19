# Time Complexity: O(n * k log k)
# Space Complexity: O(n * k)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        return list(groups.values())

s = Solution()
print(s.groupAnagrams(["aabb","abab","tap","pat","cab"]))