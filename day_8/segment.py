with open("segment_input.txt") as f:
    # get output values as 2d array
    main_lines = f.readlines()
    lines = [l.split('|')[1] for l in main_lines]
    lines = [[i.rstrip() for i in l.split()] for l in lines]

    # Part 1
    #count = 0
    #for l in lines:
    #    for i in l:
    #        if len(i) == 2 or len(i) == 3 or len(i) == 4 or len(i) == 7:
    #            count += 1
    #print(count)

    # Part 2
    # Each line gets turned into a 2d array where line[0] contains everything before '|'
    # and line[1] contains the 4 outputs after the '|'.
    # Each set of letters in each of the 2 arrays is a frozen set. This allows the set
    # operations to deduce which output num each set of letters corresponds to and it 
    # allows us to creat a dictionary for the final output which will be a dictionary
    # mapping a set of letters to a decimal number output.
    lines = [l.split('|') for l in main_lines]
    lines = [[l[0].split(), l[1].split()] for l in lines]
    lines = [[[frozenset(x.rstrip()) for x in i] for i in l] for l in lines]


    total_sum = 0
    for line in lines:
        # Represents the final mapping:
        # key: frozenset of letters
        # val: numerical output of display
        final_map = {}
        ref = line[0]

        one = None
        four = None
        seven = None
        eight = None
        five_chars = []
        six_chars = []
        for r in ref:
            # Nums 1,4,7,8 can be figured out by the len
            # we can add them to final map and grab references
            # for later.
            # For len 5 and 6, we group them in array for now
            if len(r) == 2:
                final_map[r] = 1
                one = r
            elif len(r) == 4:
                final_map[r] = 4
                four = r
            elif len(r) == 3:
                final_map[r] = 7
                seven = r
            elif len(r) == 7:
                final_map[r] = 8
                eight = r
            elif len(r) == 5:
                five_chars.append(r)
            elif len(r) == 6:
                six_chars.append(r)

        # Start deducing five_chars and six_chars
        # Deduce all 6 char strings
        six = None
        for r in six_chars:
            if not one.issubset(r):
                final_map[r] = 6
                six = r
            elif four.issubset(r):
                final_map[r] = 9
            else:
                final_map[r] = 0
        # Find 3
        for r in five_chars:
            if one.issubset(r):
                final_map[r] = 3
            elif r.issubset(six):
                final_map[r] = 5
            else:
                final_map[r] = 2

        out = line[1]
        line_sum = 0
        line_sum += final_map[out[0]] * 1000
        line_sum += final_map[out[1]] * 100
        line_sum += final_map[out[2]] * 10
        line_sum += final_map[out[3]]
        total_sum += line_sum
    print(total_sum)
