# https://leetcode.com/problems/remove-linked-list-elements/description/
# https://www.youtube.com/watch?v=JI71sxtHTng&t=3s

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


def removeElements(head, val):
    # create dummy node in case the value need to be removed
    # is the first element
    dummy = ListNode(next=head)
    prev = dummy
    cur = head

    while cur is not None:
        # get next node
        nxt = cur.next

        if cur.val == val:
            prev.next = nxt  # just update the link from previous node to next node of cur
        else:
            prev = cur  # case do not remove, just update node pre to cur

        cur = cur.next  # always update current node to new node

    return dummy.next


# Example usage
values = [1, 2, 6, 3, 4, 5, 6]
linked_list = create_linked_list(values)

print(print_linked_list(linked_list))
removed_list = removeElements(linked_list, 5)
print(print_linked_list(removed_list))
