# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

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


def pairSum(head):
    # find middle linked list
    slow = head
    fast = head
    max_sum = float("-inf")
    while fast and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    prev = None
    cur = slow

    while cur is not None:
        next_node = cur.next
        cur.next = prev
        prev = cur

        cur = next_node

    first = head
    second = prev

    while second:
        total = first.val + second.val
        max_sum = max(max_sum, total)

        first = first.next
        second = second.next

    return max_sum



# Example usage
values = [1,100000]
linked_list = create_linked_list(values)

print(print_linked_list(linked_list))
print(pairSum(linked_list))
