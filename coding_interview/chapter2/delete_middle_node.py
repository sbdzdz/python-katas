def delete_middle_node(node):
    node.value = node.next.value
    node.next = node.next.next
