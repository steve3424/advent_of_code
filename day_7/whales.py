def Fuel_Part1(diff):
    return diff

def Fuel_Part2(diff):
    return int((diff*diff + diff) / 2)

with open("whales_input.txt") as f:
    line = f.readline()
    line = line.split(',')
    crabs = [int(l.rstrip()) for l in line]

    fuel_func = Fuel_Part1

    part_2 = True
    if part_2:
        fuel_func = Fuel_Part2

    min_fuel = 1000000000
    max_crab = max(crabs)
    for target in range(max_crab + 1):
        fuel = 0
        for c in crabs:
            diff = abs(c - target)
            fuel += fuel_func(diff)
        if fuel < min_fuel:
            min_fuel = fuel
    print(min_fuel)
