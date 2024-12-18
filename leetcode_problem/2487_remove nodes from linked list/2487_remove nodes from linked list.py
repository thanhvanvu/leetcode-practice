# https://leetcode.com/problems/remove-nodes-from-linked-list/description/
# https://www.youtube.com/watch?v=y783sRTezDg&ab_channel=NeetCodeIO

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


# monotonic increasing stack
# if new value is bigger than stack[-1]
# pop() all those values
def removeNodes(head):
    stack = []
    cur = head

    while cur is not None:

        while stack and cur.val > stack[-1].val:
            stack.pop()

        stack.append(cur)

        cur = cur.next

    # technique to create linked list
    dummy = ListNode()
    current = dummy

    for node in stack:
        current.next = node
        current = current.next

    # return dummy -> [0, 1, 2]
    # want to return [1, 2] -> must return dummy.next
    return dummy.next


# Example usage
values = [5, 2, 13, 3, 8]
linked_list = create_linked_list(values)

print(print_linked_list(linked_list))
print(print_linked_list(removeNodes(linked_list)))
