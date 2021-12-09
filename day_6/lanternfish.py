with open("lanternfish_input.txt") as f:
    # turn line into list of ints representing the fish
    line = f.readline()
    line = line.split(',')
    temp_fish = [int(n.rstrip()) for n in line]
    
    # Fast solution
    # index represents timer
    # val represents number of fish at that index
    fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for f in temp_fish:
        fish[f] += 1
    
    for j in range(256):
        fish_to_add = fish[0]
        for i in range(1, len(fish)):
            fish[i - 1] = fish[i]
        fish[6] += fish_to_add
        fish[8] = fish_to_add
    print(sum(fish))

    # Slow solution
    # takes 2 years to finish
    #fish = temp_fish
    #for i in range(80):
    #    #print(f"day {i}")
    #    fish_to_add = 0

    #    # decrement all counters,
    #    # reset 0 to 6
    #    # calculate fish to add
    #    for i,f in enumerate(fish):
    #        if f == 0:
    #            fish_to_add += 1
    #            fish[i] = 6
    #        else:
    #            fish[i] = f - 1
    #    
    #    # add fish from previous day
    #    for i in range(fish_to_add):
    #        fish.append(8)
    #print(len(fish))
