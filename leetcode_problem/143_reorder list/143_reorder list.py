# https://leetcode.com/problems/reorder-list/description/
# https://www.youtube.com/watch?v=S5bfdUTrKLM&ab_channel=NeetCode

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


def reorderList(head):
    slow = head
    fast = head

    # use fast and slow technique to find the middle of linked list
    while fast and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    # slow will have [4,5,6,7]
    # we only want to get [5,6,7]
    # then reverse the second half
    prev = None
    second = slow.next
    slow.next = None  # Disconnect the first half from the second half

    while second is not None:
        next_node = second.next  # save next node before reverse link
        second.next = prev  # reverse the link from right to left
        prev = second  # update pointer cur to current node

        second = next_node  # update current node to next node

    # reorder list
    # loop though 2 list head and prev
    first = head
    second = prev

    dummy = ListNode()
    cur = dummy

    while first and second:
        cur.next = first
        cur = cur.next
        first = first.next

        cur.next = second
        cur = cur.next
        second = second.next

    if first:
        cur.next = first

    if second:
        cur.next = second

    return dummy.next


# Example usage
values = [1, 2, 3, 4, 5, 6, 7]
linked_list = create_linked_list(values)

print(print_linked_list(linked_list))
print(print_linked_list(reorderList(linked_list)))
