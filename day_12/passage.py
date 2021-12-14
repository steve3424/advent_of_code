# Recursive solution
def FindPaths(graph, current_cave, visited):
    # If we find a path, return 1 to be added to total
    if current_cave == "end":
        return 1

    # Only block caves if it is lower case
    if current_cave.islower():
        visited.add(current_cave)

    paths_found = 0
    for c in graph[current_cave]:
        if c not in visited:
            paths_found += FindPaths(graph, c, visited)

    # Remove current_cave if necessary so other paths
    # can go through this
    if current_cave in visited:
        visited.remove(current_cave)

    return paths_found

def FindPaths2(graph, current_cave, visited, can_add_small_duplicate):
    # If we find a path, return 1 to be added to total
    if current_cave == "end":
        return 1

    # Need a local bool to determine whether or not to remove during backtracking
    cave_added_twice = False
    if current_cave.islower():
        if current_cave not in visited:
            visited.add(current_cave)
        else:
            if can_add_small_duplicate:
                can_add_small_duplicate = False
                cave_added_twice = True
            else:
                return 0

    paths_found = 0
    for c in graph[current_cave]:
        paths_found += FindPaths2(graph, c, visited, can_add_small_duplicate)
        #if c not in visited or can_add_small_duplicate:

    # Remove current cave only if it was not added twice
    if current_cave in visited and cave_added_twice == False:
            visited.remove(current_cave)

    return paths_found

for i in range(4):
    file_name = f"passage_input_{i}.txt"
    print(f"Input {file_name}")
    res = 0
    res_1 = 0
    with open(file_name) as f:
        # Create graph structure
        graph = {}
        line = f.readline()
        while line:
            caves = line.split('-')
            caves = [c.rstrip() for c in caves]
            cave_1 = caves[0]
            cave_2 = caves[1]
            
            # We don't need an entry for "end", we don't go anywhere from end
            # We don't need an entry to contain "start", we don't go back to start
            if cave_1 != "end" and cave_2 != "start":
                if cave_1 not in graph:
                    graph[cave_1] = [cave_2]
                else:
                    graph[cave_1].append(cave_2)
            if cave_2 != "end" and cave_1 != "start":
                if cave_2 not in graph:
                    graph[cave_2] = [cave_1]
                else:
                    graph[cave_2].append(cave_1)
            line = f.readline()

        res = FindPaths(graph, "start", set())
        res_1 = FindPaths2(graph, "start", set(), True)
    print(f"Part 1: {res}")
    print(f"Part 2: {res_1}")
