# Vincent Ren
# 2017-12-26

# ================== Solutions ==================
def part1(inputs):
    
    def rotate(arr):
        R = len(arr)
        C = len(arr[0])

        res = tuple([''.join([arr[r][c] for r in range(R)][::-1]) for c in range(C)])

        return res


    def flip(arr):
        R = len(arr)
        C = len(arr[0])

        res = tuple([''.join([arr[r][c] for c in range(C)][::-1]) for r in range(R)])

        return res

    print(inputs[0])

    d = {}

    state = (
        '.#.',
        '..#',
        '###'
        )

    # state = (
    #     '#..#',
    #     '....',
    #     '....',
    #     '#..#',
    # )


    # print(state)
    # print(rotate(state))
    # print(flip(state))

    # for x in (state):
    #     print(x)
    # for x in (rotate(state)):
    #     print(x)
    # for x in (flip(state)):
    #     print(x)

    for input in inputs:
        pre, post = [ x.split('/') for x in input.split(' => ')]
        # print(pre, post)
        d[tuple(pre)] = tuple(post)

        rotations = pre
        flips = flip(pre)
        d[tuple(flips)] = tuple(post)

        for i in range(3):
            rotations = rotate(rotations)
            flips = rotate(flips)

            d[tuple(rotations)] = tuple(post)
            d[tuple(flips)] = tuple(post)

            # print(rotations)
            # print(flips)



    # print(d)
    print()
    for k, v in d.items():
        print(k, v)

    print()
    for row in state:
        print(row)
    print()


    steps = 0

    while steps < 18:
        N = len(state)
        steps += 1
        nextstate = []

        if N % 2 == 0:
            for row in range(0,N,2):
                rowbuilder = [[],[],[]]

                for col in range(0,N,2):
                    preblock = []
                    for i in range(2):
                        preblock.append(state[row+i][col:col+2])
                    # print(preblock)

                    for i, postrow in enumerate(d[tuple(preblock)]):
                        # print(i, postrow)
                        rowbuilder[i].append(postrow)

                for r in rowbuilder:
                    nextstate.append(''.join(r))
                
            state = nextstate

        else: # % 3 == 0
            for row in range(0,N,3):
                rowbuilder = [[],[],[],[]]

                for col in range(0,N,3):
                    preblock = []
                    for i in range(3):
                        preblock.append(state[row+i][col:col+3])
                    # print(preblock)

                    for i, postrow in enumerate(d[tuple(preblock)]):
                        # print(i, postrow)
                        rowbuilder[i].append(postrow)

                for r in rowbuilder:
                    nextstate.append(''.join(r))
                
            state = nextstate

        # print()
        # for row in state:
        #     print(row)
        # print()



    return sum([row.count('#') for row in state])


# -----------------------------------------------

def part2(inputs):

    count = 0

    print(inputs[0])

    for input in inputs:
        # print(input)
        pass

    return count



# =================== Driver ====================

with open("in21.txt", "r") as f:

    # as single string
    # inputs = f.read()

    # as single int
    # inputs = int(f.read())

    # as lists of ints
    # inputs = [[int(x) for x in row.split()] for row in f.read().split('\n')]

    # as single array of ints
    # inputs = [ int(row) for row in f.read().split('\n')]

    # as generic list of strings
    inputs = [row for row in f.read().split('\n')]

    print("\n----------------- input stats -----------------")
    print("len(inputs):", len(inputs))
    # print("row sum", sum(inputs[0]))
    print("inputs[0]:", inputs[0])
    print("len(inputs[0]):", len(inputs[0]))

    print("\n----------------- solutions -----------------")
    print("part1:", part1(inputs))
    # print("part2:", part2(inputs))

    print("\n")