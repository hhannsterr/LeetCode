# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def get_length(cur):
            if cur is None:
                return 0
            length = 1
            while cur:
                length += 1
                cur = cur.next
            return length
        
        def get_start_node(cur, start):
            for i in range(start):
                cur = cur.next
            return cur

        def get_intersection(cur_A, cur_B):
            while cur_A and cur_B:
                if cur_A == cur_B:
                    return cur_A
                cur_A = cur_A.next
                cur_B = cur_B.next
            return None


        len_A = get_length(headA)
        len_B = get_length(headB)

        if len_A > len_B:
            start_A = len_A - len_B
            cur_A = get_start_node(headA, start_A)
            return get_intersection(cur_A, headB)
        else:
            start_B = len_B - len_A
            cur_B = get_start_node(headB, start_B)
            return get_intersection(headA, cur_B)

        # def get_array(cur):
        #     array = []
        #     while cur:
        #         array.append(cur)
        #         cur = cur.next
        #     return array[::-1]

        # arrA = get_array(headA)
        # arrB = get_array(headB)

        # prev = None
        # for a, b in zip(arrA, arrB):
        #     if a == b:
        #         prev = a
        #     else:
        #         return prev
        # return prev
        