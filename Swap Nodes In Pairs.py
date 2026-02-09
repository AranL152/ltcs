# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        curr = head
        oend = None
        if (curr == None):
            return head

        while (curr and curr.next):
            temp = curr.next 
            curr.next = temp.next
            temp.next = curr
            if (curr == head):
                head = temp
            elif (oend):
                oend.next = temp
            oend = curr
            curr = curr.next
            
            
        return head