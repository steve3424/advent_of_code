import heapq

def GetExploreList(grid, row, col):
    max_row = len(grid) - 1
    max_col = len(grid[0]) - 1

    top = [row - 1, col]
    bot = [row + 1, col]
    lef = [row, col - 1]
    rig = [row, col + 1]

    res = []
    if 0 <= top[0]:
        res.append(top)
    if 0 <= lef[1]:
        res.append(lef)
    if bot[0] <= max_row:
        res.append(bot)
    if rig[1] <= max_col:
        res.append(rig)
    return res

with open("chiton_input.txt") as f:
    grid = []
    line = f.readline()
    while line:
        line = line.strip()
        row = []
        for c in line:
            row.append(int(c))
        grid.append(row)
        line = f.readline()

    grid_2 = []
    for i in range(5):
        for r in grid:
            row = []
            for j in range(5):
                for c in r:
                    n = int(c) + i + j
                    if n > 9:
                        n = (n % 10) + 1
                    row.append(int(n))
            grid_2.append(row)

    # Part 1 search
    visited = set()
    h = []
    heapq.heappush(h, tuple([0,0,0]))
    while len(h) > 0:
        # Change to comma sep
        cell = heapq.heappop(h)
        risk = cell[0]
        row = cell[1]
        col = cell[2]
        if tuple([row, col]) in visited:
            continue
        else:
            visited.add(tuple([row, col]))

        if row == (len(grid) - 1) and col == (len(grid[0]) - 1):
            print(f"Part 1: {risk}")
            break
        else:
            to_explore = GetExploreList(grid, row, col)
            for ex in to_explore:
                new_row = ex[0]
                new_col = ex[1]
                new_risk = risk + grid[new_row][new_col]
                if tuple([new_row, new_col]) not in visited:
                    heapq.heappush(h, tuple([new_risk, new_row, new_col]))
    # Part 2 search
    visited = set()
    h = []
    heapq.heappush(h, tuple([0,0,0]))
    while len(h) > 0:
        # Change to comma sep
        cell = heapq.heappop(h)
        risk = cell[0]
        row = cell[1]
        col = cell[2]
        if tuple([row, col]) in visited:
            continue
        else:
            visited.add(tuple([row, col]))

        if row == (len(grid_2) - 1) and col == (len(grid_2[0]) - 1):
            print(f"Part 2: {risk}")
            break
        else:
            to_explore = GetExploreList(grid_2, row, col)
            for ex in to_explore:
                new_row = ex[0]
                new_col = ex[1]
                new_risk = risk + grid_2[new_row][new_col]
                if tuple([new_row, new_col]) not in visited:
                    heapq.heappush(h, tuple([new_risk, new_row, new_col]))
