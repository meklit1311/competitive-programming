# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        set1 = set()
        if not head:
            return head

        while head:
            set1.add(head.val)
            head=head.next

        ls = sorted(list(set1))
        
        n = len(ls)
        head = ListNode(ls[0])
        pointer=head

        for i in range(1,n):
            pointer.next=ListNode(ls[i])
            pointer=pointer.next

        return head
