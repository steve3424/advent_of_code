with open("syntax_input.txt") as f:
    lines = f.readlines()
    lines = [l.rstrip() for l in lines]

    # Chars have different point values if they
    # are an error vs if they are in complete string
    error_values = {
            ')' : 3, 
            ']' : 57, 
            '}' : 1197, 
            '>' : 25137
    }
    complete_values = {
            ')' : 1, 
            ']' : 2, 
            '}' : 3, 
            '>' : 4
    }

    # Bracket indices should match in each list
    brackets_open  = ['(', '[', '{', '<']
    brackets_close = [')', ']', '}', '>']

    error_score = 0
    correction_scores = []
    for i,line in enumerate(lines):
        stack = []
        error_in_line = False
        for c in line:
            if c in brackets_open:
                stack.append(c)
            elif c in brackets_close:
                i = brackets_close.index(c)
                if stack[-1] == brackets_open[i]:
                    stack.pop()
                else:
                    error_in_line = True
                    error_score += error_values[c]
                    break
        if error_in_line == False and len(stack) > 0:
            correction_score = 0
            for c in reversed(stack):
                correction_score *= 5
                i = brackets_open.index(c)
                correction_score += complete_values[brackets_close[i]]
            correction_scores.append(correction_score)

    correction_scores.sort()
    print(f"Part 1: {error_score}")
    print(f"Part 2: {correction_scores[int(len(correction_scores) / 2)]}")
