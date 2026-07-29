# Time Complexity: O(n)
# Space Complexity: O(1)

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        newNode = ListNode(0)
        newNode.next = head
        current = head
        temp = newNode
        while(current):
            if(current.val == val):
                temp.next = current.next
            else:
                temp = current
            current = current.next
        return newNode.next

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(5)

obj = Solution()
new_head = obj.removeElements(head,3)

current = new_head

while current:
    print(current.val, end=" ")
    current = current.next
            