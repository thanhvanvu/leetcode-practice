# https://leetcode.com/problems/palindrome-linked-list/description/
# https://www.youtube.com/watch?v=yOzXms1J6Nk

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


# O(n)
# space: O(1)
def isPalindrome(head):
    slow = head
    fast = head

    # find middle of original link list
    while fast and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    # reverse half list
    prev = None
    cur = slow

    while cur is not None:
        next_node = cur.next
        cur.next = prev
        prev = cur

        cur = next_node  # this is actually updating pointer step

    # before reverse: [3, 2, 1]
    # after reverse: [1, 2, 3]
    # now loop through all reversed linked list
    # check if val = original linked list?
    # if yes => palindrome

    reversed_list = prev
    cur = reversed_list
    cur_original = head
    while cur is not None:
        if cur.val != cur_original.val:
            return False
        else:
            cur = cur.next
            cur_original = cur_original.next

    # if while loop is done
    # => palindrome

    return True


# O(n)
# space: O(n)
def isPalindrome_2pointer(head):
    cur = head
    lst = []
    while cur is not None:
        lst.append(cur.val)
        cur = cur.next

    L = 0
    R = len(lst) - 1

    while L < R:
        if lst[L] != lst[R]:
            return False
        L += 1
        R -= 1
    return True



# Example usage
values = [1, 2, 3, 3, 2, 1]
linked_list = create_linked_list(values)

print(print_linked_list(linked_list))

print(isPalindrome_2pointer(linked_list))
print(isPalindrome(linked_list))

