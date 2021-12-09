def IsHorizontal(point_1, point_2):
    return point_1[1] == point_2[1]

def IsVertical(point_1, point_2):
    return point_1[0] == point_2[0]

with open("hydrothermal_input.txt") as f:
    line = f.readline()

    # dictionary where
    # key = covered point
    # val = num times it is covered
    two_or_more = 0
    covered_points = {}
    while line:
        # convert each point to a tuple of x,y ints
        points = line.split("->")
        point_1 = points[0].split(',')
        point_2 = points[1].split(',')
        point_1 = tuple([int(p.rstrip()) for p in point_1])
        point_2 = tuple([int(p.rstrip()) for p in point_2])

        # calculate dx,dy
        dx = point_2[0] - point_1[0]
        dy = point_2[1] - point_1[1]

        # if both dx and dy are non-zero
        # then abs(dx) == abs(dy) in this
        # data set so we can grab either
        # else we grab the non-zero to calculate
        # how many loops we need to do
        diff = abs(dx) if dx != 0 else abs(dy)

        # dx,dy both either stay 0 or get
        # normalized to -1 or 1
        if dx > 0:
            dx = 1
        elif dx < 0:
            dx = -1
        if dy > 0:
            dy = 1
        elif dy < 0:
            dy = -1

        part_2 = False
        if part_2 or (dx == 0 or dy == 0):
            # start at point_1 and add dx,dy
            # until we get to point_2
            x = point_1[0]
            y = point_1[1]
            for i in range(diff + 1):
                t = tuple([x,y])
                if t in covered_points:
                    covered_points[t] += 1
                else:
                    covered_points[t] = 1
                x += dx
                y += dy

        # Old Solution
        #if IsHorizontal(point_1, point_2):
        #    # walk through x vals and add to covered points
        #    x_start = 0
        #    x_end   = 0
        #    if point_1[0] < point_2[0]:
        #        x_start = point_1[0]
        #        x_end   = point_2[0]
        #    else:
        #        x_start = point_2[0]
        #        x_end   = point_1[0]
        #    y = point_1[1]
        #    while x_start <= x_end:
        #        t = tuple([x_start,y])
        #        if t in covered_points:
        #            covered_points[t] += 1
        #        else:
        #            covered_points[t] = 1
        #        x_start += 1
        #elif IsVertical(point_1, point_2):
        #    # walk through y vals and add to covered points
        #    y_start = 0
        #    y_end   = 0
        #    if point_1[1] < point_2[1]:
        #        y_start = point_1[1]
        #        y_end   = point_2[1]
        #    else:
        #        y_start = point_2[1]
        #        y_end   = point_1[1]
        #    x = point_1[0]
        #    while y_start <= y_end:
        #        #print(y_start)
        #        #print(y_end)
        #        t = tuple([x,y_start])
        #        if t in covered_points:
        #            covered_points[t] += 1
        #        else:
        #            covered_points[t] = 1
        #        y_start += 1
        #else:
        #    dy = point_2[1] - point_1[1]
        #    dx = point_2[0] - point_1[0]
        #    dy = 1 if dy > 0 else -1
        #    dx = 1 if dx > 0 else -1
        #    x_start = point_1[0]
        #    y_start = point_1[1]
        #    x_end = point_2[0]
        #    y_end = point_2[1]
        #    for i in range(abs(point_2[0] - point_1[0]) + 1):
        #        t = tuple([x_start,y_start])
        #        if t in covered_points:
        #            covered_points[t] += 1
        #        else:
        #            covered_points[t] = 1
        #        x_start += dx
        #        y_start += dy
        line = f.readline()

    # check dictionary for all points with coverage >= 2
    count = 0
    for k,v in covered_points.items():
        if v >= 2:
            count += 1
    print(count)
