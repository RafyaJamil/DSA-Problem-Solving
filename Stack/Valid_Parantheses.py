# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        NewList = []
        for c in s:
            if(c == '(' or c == '{' or c == '['):
                NewList.append(c)
            else:
                if(not NewList):
                    return False
                if(c == ')' and NewList[-1] == '('):
                    NewList.pop()
                elif(c == '}' and NewList[-1] == '{'):
                    NewList.pop()
                elif(c == ']' and NewList[-1] == '['):
                    NewList.pop()
                else:
                    return False
        if(not NewList):
            return True
        return False

s = Solution()
print(s.isValid("[(})]"))