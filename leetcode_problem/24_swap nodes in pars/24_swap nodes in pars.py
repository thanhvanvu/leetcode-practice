# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
# https://www.youtube.com/watch?v=D0X0BONOQhI&ab_channel=NeetCode

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


def swapPairs(head):
    dummy = ListNode(0, head)
    prev = dummy
    cur = head

    while cur and cur.next is not None:
        # save pointers
        next_node = cur.next.next
        second = cur.next

        # reverse this pair:
        second.next = cur
        cur.next = next_node
        prev.next = second

        # update pointer
        prev = cur
        cur = next_node

    return dummy.next


# Example usage
values = [1, 2, 3, 4]
linked_list1 = create_linked_list(values)

print(print_linked_list(swapPairs(linked_list1)))
