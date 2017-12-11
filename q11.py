# Vincent Ren
# 2017-12-11

# ================== Solutions ==================
def part1(inputs):
    d = {
        'n' : ( 0, 1, -1),
        'ne' : ( 1, 0,-1),
        'se' : ( 1, -1, 0),
        's' : ( 0, -1, 1),
        'sw' : ( -1,0, 1 ),
        'nw' : ( -1, 1,0)
    }
    # print(inputs[0])

    pos = [0, 0, 0]
    for input in inputs:
        pos[0] += d[input][0]
        pos[1] += d[input][1]
        pos[2] += d[input][2]
        
    print(pos)
    return (abs(pos[0]) + abs(pos[1]) + abs(pos[2])) // 2


# -----------------------------------------------

def part2(inputs):

    d = {
        'n' : ( 0, 1, -1),
        'ne' : ( 1, 0,-1),
        'se' : ( 1, -1, 0),
        's' : ( 0, -1, 1),
        'sw' : ( -1,0, 1 ),
        'nw' : ( -1, 1,0)
    }
    # print(inputs[0])

    pos = [0, 0, 0]
    maxdist = 0
    for input in inputs:
        pos[0] += d[input][0]
        pos[1] += d[input][1]
        pos[2] += d[input][2]
        maxdist = max(maxdist,(abs(pos[0]) + abs(pos[1]) + abs(pos[2])) // 2)
        
    print(pos)
    return maxdist



# =================== Driver ====================

with open("in11.txt", "r") as f:

    # as single string
    # inputs = f.read()

    # as single int
    # inputs = int(f.read())

    # as lists of ints
    # inputs = [[int(x) for x in row.split()] for row in f.read().split('\n')]

    # as single array of ints
    # inputs = [ int(row) for row in f.read().split('\n')]

    # as something else
    # inputs = [[x for x in row.split(',')] for row in f.read().split('\n')]
    inputs = [x for x in f.read().split(',')]

    print("\n----------------- input stats -----------------")
    print("len(inputs):", len(inputs))
    # print("row sum", sum(inputs[0]))
    # print("inputs[0]:", inputs[0])
    print("len(inputs[0]):", len(inputs[0]))

    print("\n----------------- solutions -----------------")
    print("part1:", part1(inputs))
    # print("part2:", part2(inputs))

    print("\n")