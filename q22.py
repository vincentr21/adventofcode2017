# Vincent Ren
# 2017-12-27

# ================== Solutions ==================
def part1(inputs):
    
    from collections import defaultdict

    d = defaultdict(lambda: '.')


    turnleft = {
        (0,-1) : (1,0),
        (1,0) : (0,1),
        (0,1) : (-1,0),
        (-1,0) : (0,-1),
    }

    turnright = {
        (0,-1) : (-1,0),
        (1,0) : (0,-1),
        (0,1) : (1,0),
        (-1,0) : (0,1),
    }



    count = 0

    print(inputs[0])

    for r in range(len(inputs)):
        for c in range(len(inputs[0])):
            d[(r,c)] = inputs[r][c]

    print(d)

    pos = [len(inputs)//2, len(inputs[0])//2]
    print(pos)

    direc = (-1, 0)

    steps = 0
    while steps < 10000:
        steps += 1
        if d[tuple(pos)] == '#':
            d[tuple(pos)] = '.'
            direc = turnright[direc]
        else:
            d[tuple(pos)] = '#'
            direc = turnleft[direc]
            count += 1
        
        pos[0] += direc[0]
        pos[1] += direc[1]

    return count


# -----------------------------------------------

def part2(inputs):

    
    from collections import defaultdict

    d = defaultdict(lambda: '.')


    turnleft = {
        (0,-1) : (1,0),
        (1,0) : (0,1),
        (0,1) : (-1,0),
        (-1,0) : (0,-1),
    }

    turnright = {
        (0,-1) : (-1,0),
        (1,0) : (0,-1),
        (0,1) : (1,0),
        (-1,0) : (0,1),
    }



    count = 0

    print(inputs[0])

    for r in range(len(inputs)):
        for c in range(len(inputs[0])):
            d[(r,c)] = inputs[r][c]

    print(d)

    pos = [len(inputs)//2, len(inputs[0])//2]
    print(pos)

    direc = (-1, 0)

    steps = 0
    while steps < 10000000:
        steps += 1
        if d[tuple(pos)] == '#':
            d[tuple(pos)] = 'F'
            direc = turnright[direc]

        elif d[tuple(pos)] == '.':
            d[tuple(pos)] = 'W'
            direc = turnleft[direc]
            

        elif d[tuple(pos)] == 'W':
            d[tuple(pos)] = '#'
            count += 1

        elif d[tuple(pos)] == 'F':
            d[tuple(pos)] = '.'
            direc = turnleft[direc]
            direc = turnleft[direc]
        
        pos[0] += direc[0]
        pos[1] += direc[1]

    return count


# =================== Driver ====================

with open("in22.txt", "r") as f:

    # as single string
    # inputs = f.read()

    # as single int
    # inputs = int(f.read())

    # as lists of ints
    # inputs = [[int(x) for x in row.split()] for row in f.read().split('\n')]

    # as single array of ints
    # inputs = [ int(row) for row in f.read().split('\n')]

    # as generic list of strings
    inputs = [list(row) for row in f.read().split('\n')]

    print("\n----------------- input stats -----------------")
    print("len(inputs):", len(inputs))
    # print("row sum", sum(inputs[0]))
    print("inputs[0]:", inputs[0])
    print("len(inputs[0]):", len(inputs[0]))

    print("\n----------------- solutions -----------------")
    # print("part1:", part1(inputs))
    print("part2:", part2(inputs))

    print("\n")