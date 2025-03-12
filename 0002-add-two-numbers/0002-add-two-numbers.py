# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0
        itr1 = l1
        itr2 = l2
        mul = 1
        while itr1 != None:
            num1 += itr1.val * mul
            mul = mul*10
            itr1 = itr1.next
        mul = 1
        while itr2 != None:
            num2 += itr2.val * mul
            mul = mul*10
            itr2 = itr2.next
        
        final = num1 + num2
        final = list(map(int, str(final)))

        head = None
        for digit in final:
            curr = ListNode(digit)
            curr.next = head
            head = curr

        return head

