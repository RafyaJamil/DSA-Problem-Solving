# Time Complexity: O(log n)
# Space Complexity: O(1)

picked_number = 6

def guess(num):
    if num == picked_number:
        return 0
    elif num > picked_number:
        return -1
    else:
        return 1

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while(left <= right):
            mid = (left + right) // 2
            if(guess(mid) == 0):
                return mid
            elif(guess(mid) == -1):
                right = mid - 1
            else:
                left = mid + 1

s = Solution()
print(s.guessNumber(10))