# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/
# https://www.youtube.com/watch?v=4LsrgMyQIjQ&t=289s&ab_channel=NeetCodeIO

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


def swapNodes(head, k):
    # find kth node from beginning
    cur = head

    while cur is not None and k - 1 > 0:
        cur = cur.next
        k -= 1

    # find kth node from the end
    # using two pointer

    # save kth node
    left = cur

    node = head

    # if we let pointer cur go none
    # node will be at the end node
    # so instead cur, we say cur.next is not None
    while cur.next is not None:
        cur = cur.next
        node = node.next

    # swap 2 nodes
    left.val, node.val = node.val, left.val

    return head

# Example usage
values = [1, 2, 3, 4, 5]
linked_list = create_linked_list(values)

print(print_linked_list(linked_list))
removed_list = swapNodes(linked_list, 2)
print(print_linked_list(removed_list))
