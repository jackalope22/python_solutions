graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}


visited = [] #an empty list to track the visited nodes
queue = [] #store the next nodes to check

def bfs(visited, graph, node):
    counter = 0
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s)
        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

bfs(visited, graph, "A")
