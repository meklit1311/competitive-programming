# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cont =[]
        if  not head:
            return head
        while head:
            cont.append(head.val)
            head=head.next
        n=len(cont)
        cont.reverse()
        head = ListNode(cont[0])
        pointer =  head
        for i in range(1,n):
            pointer.next = ListNode(cont[i])
            pointer=pointer.next

        return head
