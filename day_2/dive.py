with open('dive_input.txt') as f:
    lines = f.readlines()

    # Part 1
    #x = 0
    #y = 0
    #for l in lines:
    #    # Get command from each line
    #    command = l.split(' ')
    #    direction = command[0]
    #    value = int(command[1])

    #    if direction == "forward":
    #        x += value
    #    elif direction == "down":
    #        y += value
    #    elif direction == "up":
    #        y -= value
    #print(x*y)
    
    # Part 2
    x = 0
    y = 0
    aim = 0
    for l in lines:
        # Get command from each line
        command = l.split(' ')
        direction = command[0]
        value = int(command[1])

        if direction == "forward":
            x += value
            y += (value * aim)
        elif direction == "down":
            aim += value
        elif direction == "up":
            aim -= value
    print(x*y)
