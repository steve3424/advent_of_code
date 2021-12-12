def IsLowPoint(height, row_num, col_num, height_map):
    '''
    Grab 4 adjacent heights, then compare.
    If adjacent height is out of bounds, then add 10
    so it always evaluates to be lower.
    '''

    top_height = height_map[row_num - 1][col_num] if row_num - 1 >= 0 else 10
    bot_height = height_map[row_num + 1][col_num] if row_num + 1 < len(height_map) else 10
    lef_height = height_map[row_num][col_num - 1] if col_num - 1 >= 0 else 10
    rig_height = height_map[row_num][col_num + 1] if col_num + 1 < len(height_map[0]) else 10
    return height < top_height and height < bot_height and height < lef_height and height < rig_height

def PrintMap(m):
    for r in m:
        for c in r:
            print(c, end="")
        print("\n", end="")

with open("smoke_input.txt") as f:
    height_map = []

    # Create height_map as 2d array of ints
    line = f.readline()
    while line.rstrip():
        line = line.rstrip()

        row = []
        for c in line:
            row.append(int(c))
        height_map.append(row)

        line = f.readline()

    # change to 0 and 1 for easier visualization
    for r in height_map:
        for i,h in enumerate(r):
            if h < 9:
                r[i] = 0
            else:
                r[i] = 1

    top_three = []
    for row_num,row in enumerate(height_map):
        for col_num,height in enumerate(row):
            if height == 0:
                basin_size = 0

                # start DFS
                stack = [tuple([row_num, col_num])]
                while len(stack) > 0:
                    current = stack.pop()
                    r = current[0]
                    c = current[1]
                    
                    top = tuple([r - 1, c])
                    bot = tuple([r + 1, c])
                    lef = tuple([r, c - 1])
                    rig = tuple([r, c + 1])
                    if top[0] >= 0 and height_map[top[0]][top[1]] == 0:
                        stack.append(top)
                        height_map[top[0]][top[1]] = 1
                        basin_size += 1
                    if bot[0] < len(height_map) and height_map[bot[0]][bot[1]] == 0:
                        stack.append(bot)
                        height_map[bot[0]][bot[1]] = 1
                        basin_size += 1
                    if lef[1] >= 0 and height_map[lef[0]][lef[1]] == 0:
                        stack.append(lef)
                        height_map[lef[0]][lef[1]] = 1
                        basin_size += 1
                    if rig[1] < len(height_map[0]) and height_map[rig[0]][rig[1]] == 0:
                        stack.append(rig)
                        height_map[rig[0]][rig[1]] = 1
                        basin_size += 1
                if len(top_three) < 3:
                    top_three.append(basin_size)
                elif basin_size > min(top_three):
                    top_three.remove(min(top_three))
                    top_three.append(basin_size)

    # Multiply top three and return
    product = 1
    for n in top_three:
        product *= n
    print(product)
                    
    
    #risk = 0
    #for row_num,row in enumerate(height_map):
    #    for col_num,height in enumerate(row):
    #        if IsLowPoint(height, row_num, col_num, height_map):
    #            risk += (height + 1)
    #print(risk)
