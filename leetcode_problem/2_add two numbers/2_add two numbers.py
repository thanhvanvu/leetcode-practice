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


# put all node in headA in set
# loop through headB
# if we see headB in set, it means it is an intersection node
# O(m+n), space O(n)
def addTwoNumbers(l1, l2):
    dummy = ListNode()
    cur = dummy

    carry = 0

    # loop runs if
    # l1 is not None
    # l2 is not None
    # carry > 0
    while l1 or l2 or carry > 0:

        if l1 is not None:
            v1 = l1.val
        else:
            v1 = 0

        if l2 is not None:
            v2 = l2.val
        else:
            v2 = 0

        val = v1 + v2 + carry

        # 18, carry is 1
        # to get 1, use // 10
        carry = val // 10

        # to get 8, use % 10
        val = val % 10

        cur.next = ListNode(val)

        # update cur to next node
        cur = cur.next

        # l1 = [9, 9, 9, 9, 9, 9, 9]
        # l2 = [9, 9, 9, 9]
        # if l2.next == None, we want to set its val = None
        # so it will continue the while loop
        # otherwise the loop will break
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next


# Example usage
values = [9]
values2 = [8]
linked_list1 = create_linked_list(values)
linked_list2 = create_linked_list(values2)

print(print_linked_list(linked_list1))
print(print_linked_list(linked_list2))
print(print_linked_list(addTwoNumbers(linked_list1, linked_list2)))
