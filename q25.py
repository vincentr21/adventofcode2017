# Vincent Ren
# 2017-12-25

# ================== Solutions ==================
def part1(inputs):
    
    from collections import defaultdict

    states = {
        'A': [[1, 0] , [1, -1] ,['B', 'D']],
        'B': [[1, 0] , [1, 1] ,['C', 'F']],
        'C': [[1, 1] , [-1, -1] ,['C', 'A']],
        'D': [[0, 1] , [-1, 1] ,['E', 'A']],
        'E': [[1, 0] , [-1, 1] ,['A', 'B']],
        'F': [[0, 0] , [1, 1] ,['C', 'E']],
    }


    # states = {
    #     'A': [[1, 0] , [1, -1] ,['B', 'B']],
    #     'B': [[1, 1] , [-1, 1] ,['A', 'A']],
    # }


    tape = defaultdict(int)
    state = 'A'

    steps = 0
    i = 0

    while steps < 12317297:
    # while steps < 6:

        tape_new  = states[state][0][tape[i]]
        state_new = states[state][2][tape[i]]
        i_new = i + states[state][1][tape[i]]

        tape[i] = tape_new
        state = state_new
        i = i_new
        

        steps += 1
    
    # print(list(tape))
    # print([ tape[x] for x in tape])

    return sum([ tape[x] for x in tape])


# -----------------------------------------------

def part2(inputs):

    count = 0

    print(inputs[0])

    for input in inputs:
        # print(input)
        pass

    return count



# =================== Driver ====================

with open("in25.txt", "r") as f:

    # as single string
    # inputs = f.read()

    # as single int
    # inputs = int(f.read())

    # as lists of ints
    # inputs = [[int(x) for x in row.split()] for row in f.read().split('\n')]

    # as single array of ints
    # inputs = [ int(row) for row in f.read().split('\n')]

    # as generic list of strings
    inputs = [[x for x in row.split()] for row in f.read().split('\n')]

    print("\n----------------- input stats -----------------")
    print("len(inputs):", len(inputs))
    # print("row sum", sum(inputs[0]))
    print("inputs[0]:", inputs[0])
    print("len(inputs[0]):", len(inputs[0]))

    print("\n----------------- solutions -----------------")
    print("part1:", part1(inputs))
    # print("part2:", part2(inputs))

    print("\n")