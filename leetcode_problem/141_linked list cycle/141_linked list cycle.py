# https://leetcode.com/problems/linked-list-cycle/description/
# https://www.youtube.com/watch?v=gBTe7lFR3vc&ab_channel=NeetCode

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


# use hashSet
def hasCycle(head):
    hashSet = set()
    cur = head
    while cur is not None:
        if cur in hashSet:
            return True

        hashSet.add(cur)

        cur = cur.next
    return False


# fast and slow
def hasCycle_fl(head):
    fast = head
    slow = head

    while fast and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# Example usage
values = [1, 2, 3, 4, 5]
linked_list = create_linked_list(values)

print(print_linked_list(linked_list))
print(hasCycle(linked_list))
