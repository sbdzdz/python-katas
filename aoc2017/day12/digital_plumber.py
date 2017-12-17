from collections import defaultdict

graph = defaultdict(list)

with open('input') as f:
    for line in f:
        line = line.replace(',', '')
        source, _, *rest = line.split()
        graph[int(source)].extend([int(node) for node in rest])

def find_connected(graph, root):
    fringe = [graph[root]]
    connected = {root}
    while fringe:
        current = fringe.pop()
        for node in current:
            if node not in connected:
                connected.add(node)
                fringe.append(graph[node])
    return connected

groups = [find_connected(graph, 0)]
for node in graph:
    if not any(node in group for group in groups):
        groups.append(find_connected(graph, node))

print(len(groups[0]))
print(len(groups))

