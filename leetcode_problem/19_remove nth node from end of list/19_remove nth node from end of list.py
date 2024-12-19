# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# https://www.youtube.com/watch?v=XVuQxVej6y8&ab_channel=NeetCode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to create a linked list from a list of values
def create_linked_list(values):
    if not values:  # If the list is empty, return None
        return None

    # Create the head of the linked list
    head = ListNode(values[0])
    current = head

    # Iterate through the remaining values and create nodes
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def print_linked_list(head):
    cur = head
    list = []

    if cur is None:
        return []

    while cur is not None:
        list.append(cur.val)
        cur = cur.next
    return list


# reverse linked list
def removeNthFromEnd(head, n):
    prev = None
    cur = head

    while cur is not None:
        next_node = cur.next

        # reverse link
        cur.next = prev
        prev = cur

        cur = next_node

    dummy = ListNode()
    dummy.next = prev
    cur = dummy

    while n - 1 > 0:
        cur = cur.next
        n -= 1

    # 1, 2, 3, 4, 5
    # to remove 3, we want pointer at num 2
    # then link 2 to 4

    if cur.next is not None:
        cur.next = cur.next.next

        # Step 3: Reverse the list back to its original order
        prev = None
        cur = dummy.next
        while cur is not None:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

    return prev


# 2 pointer:
def removeNthFromEnd_2pointer(head, n):
    R = head
    while R is not None and n > 0:
        R = R.next
        n -= 1

    # 1, 2, 3, 4, 5
    # to remove 4
    # L pointer should be at 3
    # R pointer should be at None
    # need to find where we should put L pointer at beginning
    # L = 2, R = 5
    # L = 1, R = 4
    # L = 0, R = 3
    # to set L = 0, need to create dummy node
    dummy = ListNode(next=head)
    L = dummy

    while R is not None:
        R = R.next
        L = L.next

    # delete nth node
    L.next = L.next.next

    return dummy.next


# Example usage
values = [1, 2, 3, 4, 5]
linked_list = create_linked_list(values)

print(print_linked_list(linked_list))
print(print_linked_list(removeNthFromEnd_2pointer(linked_list, 2)))
