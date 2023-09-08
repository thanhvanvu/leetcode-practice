# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def reverseList(head):
    prev = None
    curr = head

    while curr is not None:
        next_node = curr.next  # save next
        curr.next = prev  # reverse
        prev = curr  # advance prev and curr
        curr = next_node  # advance prev and curr

    return prev
