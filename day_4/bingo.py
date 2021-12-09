def CheckBoard(board):
    # check rows
    for row in board:
        vals = 0
        for val in row:
            if val[1] == True:
                vals += 1
        if vals == 5:
            # sum all unmarked nums
            total = 0
            for row in board:
                for val in row:
                    if val[1] == False:
                        total += val[0]
            return total

    # check cols
    for col in range(5):
        vals = 0
        for row in board:
            if row[col][1] == True:
                vals += 1
        if vals == 5:
            # sum all unmarked nums
            total = 0
            for row in board:
                for val in row:
                    if val[1] == False:
                        total += val[0]
            return total
    return -1

def Bingo():
    with open("bingo_input.txt") as f:
        # get called nums as ints
        nums = f.readline()
        called_nums = nums.rstrip().split(',')
        called_nums = [int(i) for i in called_nums]

        # read empty line
        f.readline()

        # create bingo boards
        # each board will be a 2d array
        # each entry will be a 2 member array with the board val
        # and a bool to see if it has been called
        all_boards = []
        l = f.readline()
        while(l):
            board = []
            for i in range(5):
                row = l.rstrip().split()
                row = [[int(i), False] for i in row]
                board.append(row)
                l = f.readline()
            all_boards.append(board)
            l = f.readline()

        # Part 1
        # call numbers one by one
        # mark off on all boards
        # stop when winner is found
        #for num in called_nums:
        #    # mark num in all boards
        #    for board in all_boards:
        #        for row in board:
        #            for val in row:
        #                if val[0] == num:
        #                    val[1] = True

        #    # check for winner
        #    for board in all_boards:
        #        winning_total = CheckBoard(board)
        #        if winning_total > 0:
        #            print("winner: ")
        #            print(winning_total * num)
        #            return 0

        # Part 2
        # call numbers one by one
        # mark off on all boards
        # add winners to array and choose last
        winner_totals = []
        for num in called_nums:
            # mark num in all boards
            for board in all_boards:
                for row in board:
                    for val in row:
                        if val[0] == num:
                            val[1] = True

            # check for winner
            for board in all_boards:
                winning_total = CheckBoard(board)
                if winning_total > 0:
                    winner_totals.append([winning_total, num])
                    all_boards.remove(board)
        last_winner = winner_totals.pop()
        print(last_winner[0] * last_winner[1])

Bingo()
