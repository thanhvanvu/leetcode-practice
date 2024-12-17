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
def getIntersectionNode(headA, headB):
    hashSet = set()

    node1 = headA

    while node1 is not None:
        hashSet.add(node1)
        node1 = node1.next

    node2 = headB

    while node2 is not None:
        if node2 in hashSet:
            return node2

        node2 = node2.next

    return None


# O(m+n), O(1)
def getIntersectionNode2(headA, headB):
    lengthA = 0
    lengthB = 0

    cur1 = headA
    cur2 = headB

    # find length of linked list
    while cur1:
        lengthA += 1
        cur1 = cur1.next

    while cur2:
        lengthB += 1
        cur2 = cur2.next

    # find different length of linked list
    diff = abs(lengthB - lengthA)

    # list A = 5
    # list B = 6
    # diff = 1
    # move list B 1 step to make 2 list equally
    nodeA = headA
    nodeB = headB
    if lengthB > lengthA:
        while diff > 0:
            nodeB = nodeB.next
            diff -= 1

    if lengthA > lengthB:
        while diff > 0:
            nodeA = nodeA.next
            diff -= 1

    # run through 2 list and compare 2 node
    # if we see 2 nodes equally, it means it is intersection
    while nodeA and nodeB:
        if nodeA == nodeB:
            return nodeA
        nodeA = nodeA.next
        nodeB = nodeB.next



# Example usage
values = [4, 1, 8, 4, 5]
values2 = [5, 6, 1, 8, 4, 5]
linked_list1 = create_linked_list(values)
linked_list2 = create_linked_list(values2)

print(print_linked_list(linked_list1))
print(print_linked_list(linked_list2))
print(print_linked_list(getIntersectionNode2(linked_list1, linked_list2)))
