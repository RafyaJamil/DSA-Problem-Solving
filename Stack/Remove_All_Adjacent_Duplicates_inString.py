# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def removeDuplicates(self, s: str) -> str:
        struct = []
        for c in s:
            if(not struct):
                struct.append(c)
            elif(c == struct[-1]):
                struct.pop()
            else:
                struct.append(c)
        newString = ''.join(struct)
        return newString

s = Solution()
print(s.removeDuplicates('accadcd'))