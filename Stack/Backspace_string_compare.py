# Time Complexity: O(n + m)
# Space Complexity: O(n + m)

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        for i in range(len(s)):
            if(s[i] == "#"):
                stack1.pop()
            else:
                stack1.append(s[i])
        stack2 = []
        for j in range(len(t)):
            if(t[j] == "#"):
                stack2.pop()
            else:
                stack2.append(t[j])
        if(stack1 == stack2):
            return True
        return False
s = Solution()
print(s.backspaceCompare("ab#","abc##"))