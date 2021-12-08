with open('day_1_sonar_input.txt') as f:
    # Get file input as list of ints
    lines = f.readlines()
    lines = [int(l) for l in lines]

    # Day 1 part 1
    #prev_num = lines[0]
    #count = 0
    #for num in lines:
    #    if num > prev_num:
    #        count += 1
    #    prev_num = num
    #print(count)

    # Day 1 part 2
    prev_sum = lines[0] + lines[1] + lines[2]
    count = 0
    i,j,k = 1,2,3
    while k < len(lines):
        sum = lines[i] + lines[j] + lines[k]
        if sum > prev_sum:
            count += 1
        prev_sum = sum
        i += 1
        j += 1
        k += 1
    print(count)
