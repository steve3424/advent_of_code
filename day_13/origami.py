with open("origami_input_1.txt") as f:
    dense_grid = {'rows': {}, 'cols': {}}
    folds = []

    # Create dense grid data structure and
    # Get folding commands
    # from file
    line = f.readline()
    while line:
        line = line.rstrip()

        if len(line) > 0:
            if line[0] == 'f':
                direction,value = line.split("=")
                direction = direction[-1]
                value = int(value)
                folds.append([direction, value])
            else:
                col,row = line.split(',')
                col = int(col)
                row = int(row)
                if row in dense_grid['rows']:
                    dense_grid['rows'][row].add(col)
                else:
                    dense_grid['rows'][row] = set([col])
                if col in dense_grid['cols']:
                    dense_grid['cols'][col].add(row)
                else:
                    dense_grid['cols'][col] = set([row])
        line = f.readline()

    for i in range(len(folds)):
        fold = folds[i]
        other_dict = None
        current_dict = None
        direction = fold[0]
        value = fold[1]
        if direction == 'x':
            current_dict = dense_grid['cols']
            other_dict = dense_grid['rows']
        else:
            current_dict = dense_grid['rows']
            other_dict = dense_grid['cols']

        for i in range(1, value + 1):
            keep_key    = value - i
            combine_key = value + i
            keep_dict    = current_dict[keep_key]    if keep_key    in current_dict else None
            combine_dict = current_dict[combine_key] if combine_key in current_dict else None
            if keep_dict != None and combine_dict != None:
                keep_dict = keep_dict.union(combine_dict)
                current_dict[keep_key] = keep_dict
                current_dict.pop(combine_key)

                # Now need to modify other_dict
                for k in combine_dict:
                    other_dict[k].remove(combine_key)
                    other_dict[k].add(keep_key)
            elif combine_dict != None:
                current_dict[keep_key] = combine_dict
                current_dict.pop(combine_key)

                # Now need to modify other_dict
                for k in combine_dict:
                    other_dict[k].remove(combine_key)
                    other_dict[k].add(keep_key)
        if i == 1:
            # Count remaining dots
            num_dots = 0
            for k,v in dense_grid["rows"].items():
                num_dots += len(v)
            print(f"Part 1 {num_dots}")

    print(dense_grid)

    ##
    width = max(dense_grid["cols"].keys()) + 1
    rows = sorted(dense_grid["rows"].keys())
    empty_row = 0
    for row in rows:
        while empty_row < row:
            print('.' * width)
            empty_row += 1
        cols = sorted(dense_grid["rows"][row])
        empty_cell = 0
        for col in cols:
            while empty_cell < col:
                print('.', end="")
                empty_cell += 1
            print('#', end="")
            empty_cell += 1
        print('\n', end="")
        empty_row += 1
