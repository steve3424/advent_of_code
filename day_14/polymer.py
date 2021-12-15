def GetCount(counts):
    kv = [v for k,v in counts.items()]
    kv.sort()
    # Add one here because the way we maintain
    # the count, we always miss the last letter
    return kv[-1] - kv[0] + 1

with open("polymer_input_1.txt") as f:
    # Get start polymer from file
    first_line = f.readline().rstrip()

    # This is the primary structure.
    # It is a dictionary where:
    # key: pair e.g. 'NN', 'CB'
    # val: num of times that pair occurs in polymer string
    # This works because as the number of pairs gets exponentially long,
    # the number of unique pairs remains very small and the dictionary
    # is only holding one entry for each unique pair
    pairs = {}
    i = 0
    j = 1
    while j < len(first_line):
        p = f"{first_line[i]}{first_line[j]}"
        if p in pairs:
            pairs[p] += 1
        else:
            pairs[p] = 1
        i += 1
        j += 1

    # Read blank line
    f.readline()

    # Create rules from file
    rules = {}
    line = f.readline()
    while line:
        line = line.rstrip()
        line = line.split("->")
        line = [l.strip() for l in line]

        if line[0] in rules:
            print(f"2 rules for key {line[0]}")
        else:
            rules[line[0]] = line[1]
        line = f.readline()
    
    part_1_count = 0
    current_pairs = pairs
    counts = {}
    for i in range(40):
        new_pairs = {}
        new_counts = {}
        for k,v in current_pairs.items():
            if k not in rules:
                new_pairs[k] = v
                if k[0] in new_counts:
                    new_counts[k[0]] += v
                else:
                    new_counts[k[0]] = v

                if k[1] in new_counts:
                    new_counts[k[1]] += v
                else:
                    new_counts[k[1]] = v
            else:
                # Create new pairs
                new_pair_1 = f"{k[0]}{rules[k]}"
                new_pair_2 = f"{rules[k]}{k[1]}"

                if new_pair_1[0] in new_counts:
                    new_counts[new_pair_1[0]] += v
                else:
                    new_counts[new_pair_1[0]] = v
                if new_pair_1[1] in new_counts:
                    new_counts[new_pair_1[1]] += v
                else:
                    new_counts[new_pair_1[1]] = v
                #if new_pair_2[1] in new_counts:
                #    new_counts[new_pair_2[1]] += v
                #else:
                #    new_counts[new_pair_2[1]] = v
                
                if new_pair_1 in new_pairs:
                    new_pairs[new_pair_1] += v
                else:
                    new_pairs[new_pair_1] = v

                if new_pair_2 in new_pairs:
                    new_pairs[new_pair_2] += v
                else:
                    new_pairs[new_pair_2] = v
        current_pairs = new_pairs
        counts = new_counts
        if i == 9:
            part_1_count = GetCount(counts)
    print(f"Part 1: {part_1_count}")
    print(f"Part 2: {GetCount(counts)}")
