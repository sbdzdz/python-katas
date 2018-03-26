from linked_list import *

def find_nth_to_last(head, n):
    if head is None:
        return None
    length = 0
    current = head
    while current.next is not None:
        length += 1
        current = current.next
    print(length)

    current = head
    for i in range(length-n):
        current = current.next
    return current.value
