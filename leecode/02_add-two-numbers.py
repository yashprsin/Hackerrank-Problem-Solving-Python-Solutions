# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        New_l1 = l1[::-1]
        New_l2 = l2[::-1]

        ls = []
        for i in range(0,len(l1)):
            ls.append(New_l1[i]+ New_l2[i])

        ls = ls[::-1]
        return ls