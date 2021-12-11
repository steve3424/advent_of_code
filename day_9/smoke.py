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

    risk = 0
    for row_num,row in enumerate(height_map):
        for col_num,height in enumerate(row):
            if IsLowPoint(height, row_num, col_num, height_map):
                risk += (height + 1)
    print(risk)
