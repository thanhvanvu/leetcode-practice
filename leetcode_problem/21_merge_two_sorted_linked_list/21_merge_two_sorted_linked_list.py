# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        node = dummy

        # loop through list1 and list 2
        while list1 and list2:
            if list1.val < list2.val:  # check value 2 nodes
                node.next = list1  # make a link from current node to next node
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next

            # move to next node
            node = node.next

            # if list1 has more node than list2
            if list1:
                node.next = list1

            if list2:
                node.next = list2

            return dummy.next

    def mergeLists(self, list1, list2):
        # create a dummy node
        # this is a brand new linked list
        dummy = ListNode()
        node = dummy

        # loop through list1, list2 until they reach NONE node
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                node.next = list1  # assign this node to brand new linked list
                list1 = list1.next  # update new node, otherwise it will infinite loop (i += 1)
            else:
                node.next = list2
                list2 = list2.next

            # move to next node from the brand new linked list
            node = node.next

        # case if list1 or list2 have mode nodes
        if list1 is not None:
            node.next = list1

        if list2 is not None:
            node.next = list2

        return dummy.next


def mergeTwoLists_practice(list1, list2):
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            # update list1 pointer
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next

    if list1:
        tail.next = list1

    if list2:
        tail.next = list2

    return dummy.next

list1 = [1, 2, 4]
list2 = [1, 3, 4]

print(mergeTwoLists_practice(list1, list2))
