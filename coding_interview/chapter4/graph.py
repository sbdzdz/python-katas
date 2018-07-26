class Node(object):
    def __init__(self, id):
        self.id = id
        self.adjacent = set()

    def add_adjacent(self, node):
        self.adjacent.add(Node(id))

class Graph(object):
    def __init__(self, nodes):
        self.nodes = {}
        for node in nodes:
            self.nodes[node.id] = node

    def add_edge(node_from, id_to):
        self.nodes[id_from].add_adjacent(id_to)
