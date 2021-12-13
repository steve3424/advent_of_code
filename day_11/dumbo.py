def FlashOcto(row,col,grid):
    grid[row][col] = 0

    temp_row = row - 1
    temp_col = col - 1
    for r in range(temp_row, temp_row + 3):
        for c in range(temp_col, temp_col + 3):
            # Bounds checking
            if 0 <= r and r < len(grid) and 0 <= c and c < len(grid[0]):
                # 0 indicates it already flashed and we want all of these
                # to be 0 
                if grid[r][c] != 0:
                    grid[r][c] += 1

def PrintGrid(g):
    print("**************************")
    for l in g:
        for o in l:
            if o == 0:
                print('-',end="")
            else:
                print(o,end="")
        print("")
    print("**************************")

with open("dumbo_input.txt") as f:
    # Get input as grid of ints
    lines = f.readlines()
    lines = [l.rstrip() for l in lines]
    octos = [[int(c) for c in l] for l in lines]

    total_flashes = 0
    for i in range(100):
        # First iterate to increase all by 1
        for line in octos:
            for col in range(0,len(line)):
                line[col] += 1

        # Iterate until all flashes are done
        # Uses bubble sort tactic of iterating the
        # while loop until it goes through once with
        # no flashes
        still_flashing = True
        while still_flashing:
            still_flashing = False
            for row,line in enumerate(octos):
                for col,o in enumerate(line):
                    if o > 9:
                        still_flashing = True
                        total_flashes += 1
                        FlashOcto(row,col,octos)
    print(f"Part 1: {total_flashes}")
