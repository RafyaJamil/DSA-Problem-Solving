# Time Complexity: O(n)
# Space Complexity: O(1)

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head 
        current = head
        while(temp and temp.next): 
            current = current.next
            temp = temp.next.next
        return current

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

obj = Solution()
new_head = obj.middleNode(head)

current = new_head

while current:
    print(current.val, end=" ")
    current = current.next
