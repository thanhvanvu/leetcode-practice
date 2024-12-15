# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://www.youtube.com/watch?v=O0By4Zq0OFc&t=372s
# https://leetcode.com/problems/reverse-linked-list/


def reverseList(head):
    prev = None
    curr = head

    # pointer will loop until it reaches none
    while curr is not None:
        next_node = curr.next  # save next node before breaking the link
        curr.next = prev  # reverse
        prev = curr  # move pointer prev to next node
        curr = next_node  # move pointer curr to next node

    return prev
