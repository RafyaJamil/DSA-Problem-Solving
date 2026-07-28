# Time Complexity: O(n)
# Space Complexity: O(1)
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while(temp and temp.next):
            if(temp.val == temp.next.val):
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(5)

obj = Solution()
new_head = obj.deleteDuplicates(head)

current = new_head

while current:
    print(current.val, end=" ")
    current = current.next