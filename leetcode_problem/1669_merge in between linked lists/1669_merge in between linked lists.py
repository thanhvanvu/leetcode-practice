# https://leetcode.com/problems/merge-in-between-linked-lists/description/
# https://www.youtube.com/watch?v=pI775VutBxg&ab_channel=NeetCodeIO

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


def mergeInBetween(list1, list2, a, b):
    cur1 = list1
    i = 0

    # a = 2, i = 0
    # 0 1 2 3 4 5 6 7
    # to stop at 1
    # i < a - 1
    # i < 2
    while i < a - 1:
        cur1 = cur1.next
        i += 1

    head = cur1

    # continue to loop through list1zx  xzz
    while i <= b:
        cur1 = cur1.next
        i += 1

    # connect pointer cur1 to list2
    head.next = list2

    # run through list2 until None
    # if we do this way, the last node will point at None
    # while list2 is not None:
    #     list2 = list2.next

    # so we stop at list2.next
    # pointer will stop at last node
    while list2.next is not None:
        list2 = list2.next

    list2.next = cur1

    return list1


# Example usage
values = [0, 1, 2, 3, 4, 5, 6]
values2 = [1000000, 1000001, 1000002, 1000003, 1000004]
linked_list1 = create_linked_list(values)
linked_list2 = create_linked_list(values2)

print(print_linked_list(mergeInBetween(linked_list1, linked_list2, 2, 5)))
