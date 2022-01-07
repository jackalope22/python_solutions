from icecream import ic

graph = {
    "A": ["C"],
    "B": ["C"],
    "C": ["D"],
    "D": ["F", "E"],
    "E": [],
    "F": ["G"],
    "G": []
}

def bfs_shortest_path(graph, start, goal):
    
    explored = []
    queue = [start]

    if start == goal:
        print("no steps needed")

    while queue:
        ic(queue)
        path = queue.pop(0)
        ic(path)
        node = path[-1]
        ic(node)
        if node not in explored:
            neighbors = graph[node]
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == goal:
                    return new_path

            explored.append(node)

    if new_path[-1] != goal:
        print("No connection")
    else:
        print(f"Path equals {new_path}")



def comparePaths():
    A = set(bfs_shortest_path(graph, "A", "G")) 
    print(A)
    B = set(bfs_shortest_path(graph, "B", "G"))
    print(B)

    distinct = A.union(B)
    print(distinct)

comparePaths()