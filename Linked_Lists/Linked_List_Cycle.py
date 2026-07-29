# Time Complexity: O(n)
# Space Complexity: O(1)

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        current = head
        while(temp and temp.next):
            current = current.next
            temp = temp.next.next
            if(temp == current):
                return True
        return False

head = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(4)

head.next = second
second.next = third
third.next = fourth
fourth.next = second     

obj = Solution()
if obj.hasCycle(head):
    print("Cycle Detected")
else:
    print("No Cycle")