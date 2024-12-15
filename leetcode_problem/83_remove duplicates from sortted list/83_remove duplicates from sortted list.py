# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
# https://www.youtube.com/watch?v=Nvf9Yt1EElg

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


def deleteDuplicates(head):
    cur = head

    # check if cur is not none
    # also the next node not none
    while cur is not None and cur.next is not None:
        next_node = cur.next
        if next_node.val == cur.val:
            cur.next = cur.next.next  # update the link to the next of the next node
        else:
            cur = cur.next  # if do not see duplicate, just move to next node and check again

    return head


# Example usage
values = [1, 1, 2, 3, 3]
linked_list = create_linked_list(values)

print(print_linked_list(linked_list))

removed_list = deleteDuplicates(linked_list)
print(print_linked_list(removed_list))
