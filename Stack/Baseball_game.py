# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            if(operation ==  "C"):
                stack.pop()
            elif(operation == "D"):
                stack.append(2 * stack[-1])
            elif(operation == "+"):
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(operation))
        return sum(stack)

s = Solution()
print(s.calPoints(["2","D","3","C","4","+"]))