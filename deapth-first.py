graph = {
    "A": ["B","C"],
    "B": ["D","E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

visited = set() # set to keep track of visited nodes

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

dfs(visited, graph, "A")
