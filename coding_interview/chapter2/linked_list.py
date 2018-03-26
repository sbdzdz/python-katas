class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def append(self, value):
        node = Node(value)
        current = self
        while current.next is not None:
            current = current.next
        current.next = node

def delete_node(head, value):
    if head.value == value:
        return head.next
    current = head
    while current.next is not None:
        if current.next.value == value:
            current.next = current.next.next
            return head
        current = current.next
    return head

def list2linked(l):
    if not l:
        return None
    head = Node(l[0])
    current = head
    for element in l[1:]:
        node = Node(element)
        current.next = node
        current = current.next 
    return head

def linked2list(head):
    if head is None:
        return []
    l = []
    while head is not None:
        l.append(head.value)
        head = head.next
    return l
