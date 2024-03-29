# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/description/


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


def add_two_numbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    carryover = 0
    first = ListNode()
    current = first
    while l1 is not None or l2 is not None or carryover:
        l1_val = l1.val if l1 is not None else 0
        l2_val = l2.val if l2 is not None else 0

        result = l1_val + l2_val + carryover
        carryover = result // 10
        result = result % 10
        current.next = ListNode(result)
        current = current.next

        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None
    return first.next


if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = add_two_numbers(l1, l2)
    print(result, result.next, result.next.next)
