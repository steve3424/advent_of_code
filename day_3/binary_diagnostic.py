def FindOxygenRating(nums, char_index):
    if(len(nums) == 1):
        return nums[0]
    else:
        ones = []
        zeros = []
        for line in nums:
            if line[char_index] == '1':
                ones.append(line)
            else:
                zeros.append(line)
        most_common = ones if len(ones) >= len(zeros) else zeros
        return FindOxygenRating(most_common, char_index + 1)

def FindCO2Rating(nums, char_index):
    if(len(nums) == 1):
        return nums[0]
    else:
        ones = []
        zeros = []
        for line in nums:
            if line[char_index] == '1':
                ones.append(line)
            else:
                zeros.append(line)
        least_common = zeros if len(zeros) <= len(ones) else ones
        return FindCO2Rating(least_common, char_index + 1)


with open("binary_diagnostic_input.txt") as f:
    # Read lines and strip '\n' from end
    lines = f.readlines();
    lines = [l.rstrip() for l in lines]

    # Part 1
    ## create array to count number of ones in each position
    #ones = [0 for i in lines[0]]

    ## go through each line and count ones in each position
    #for line in lines:
    #    for i,char in enumerate(line):
    #        if char == '1':
    #            ones[i] += 1
    #
    ## figure out if 1 or 0 was most common
    #gamma_bit_string = ""
    #epsil_bit_string = ""
    #for one in ones:
    #    if one > (len(lines) / 2):
    #        gamma_bit_string += '1'
    #        epsil_bit_string += '0'
    #    elif one < (len(lines) / 2):
    #        gamma_bit_string += '0'
    #        epsil_bit_string += '1'
    #    else:
    #        print("WTF!!!")
    #        gamma_bit_string += '1'
    #        epsil_bit_string += '0'

    ## calculate power
    #power = int(gamma_bit_string, 2) * int(epsil_bit_string, 2)
    #print(power)

    # Part 2
    # Recursive solution
    oxy_bit_string = FindOxygenRating(lines, 0)
    co2_bit_string = FindCO2Rating(lines, 0)
    print(int(oxy_bit_string, 2) * int(co2_bit_string, 2))

    # Iterative solution
    #ones = []
    #zero = []
    #oxy = lines
    #co2 = lines
    #for i in range(0, len(lines[0])):
    #    # go through all oxygens left and
    #    # discard the least common
    #    if len(oxy) > 1:
    #        for line in oxy:
    #            if line[i] == '1':
    #                ones.append(line)
    #            else:
    #                zero.append(line)
    #        if len(ones) >= len(zero):
    #            oxy = ones
    #        else:
    #            oxy = zero

    #        # reset array
    #        ones = []
    #        zero = []

    #    # go through all co2s left and
    #    # discard the most common
    #    if len(co2) > 1:
    #        for line in co2:
    #            if line[i] == '1':
    #                ones.append(line)
    #            else:
    #                zero.append(line)
    #        if len(zero) <= len(ones):
    #            co2 = zero
    #        else:
    #            co2 = ones

    #        # reset array
    #        ones = []
    #        zero = []
    #oxy_bit_string = oxy[0]
    #co2_bit_string = co2[0]
    #print(int(oxy_bit_string, 2) * int(co2_bit_string, 2))
