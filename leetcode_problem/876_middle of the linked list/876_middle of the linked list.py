# https://leetcode.com/problems/middle-of-the-linked-list/description/
# https://www.youtube.com/watch?v=A2_ldqM4QcY&t=261s

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

# slow and fast pointer technique
# fast will traversal 2 nodes ahead
# slow will traversal 1 node ahead
# when fast pointer reaches the end node
# slow pointer will automatically be at the middle
def middleNode(head):
    slow = head
    fast = head

    # keep looping until fast reach none:
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    return slow


# Example usage
values = [1, 2, 3, 4, 5]
linked_list = create_linked_list(values)

print(print_linked_list(linked_list))
print(print_linked_list(middleNode(linked_list)))
