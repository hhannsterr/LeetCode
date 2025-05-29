# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def add_value(addition, carry):
            addition += carry
            if addition >= 10:
                carry = 1
                addition = addition % 10
            else:
                carry = 0
            return addition, carry


        l1_cur, l2_cur = l1, l2
        carry = 0
        result = []
        while l1_cur is not None and l2_cur is not None:
            
            addition, carry = add_value(l1_cur.val + l2_cur.val, carry)            
            
            result.append(addition)
            l1_cur, l2_cur = l1_cur.next, l2_cur.next
        
        while l1_cur is not None:
            
            addition, carry = add_value(l1_cur.val, carry)

            result.append(addition)
            l1_cur = l1_cur.next
        
        while l2_cur is not None:
            
            addition, carry = add_value(l2_cur.val, carry)

            result.append(addition)
            l2_cur = l2_cur.next
        
        if carry == 1:
            result.append(1)

        head = ListNode(result[0])
        current = head
        for i in range(1, len(result)):
            current.next = ListNode(result[i])
            current = current.next
        
        return head
        