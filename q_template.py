# Vincent Ren
# 2017-12-05

# ================== Solutions ==================
def part1(inputs):
    
    _sum = 0
    for input in inputs:

        N = len(input)
        for i in range(N):
            
            _sum += input[i]

    return _sum


# -----------------------------------------------

def part2(inputs):

    _sum = 0
    for input in inputs:

        N = len(input)
        for i in range(N):
            
            _sum += input[i]

    return _sum



# =================== Driver ====================

with open("in2.txt", "r") as f:

    # as single string
    # inputs = f.read()

    # as single int
    # inputs = int(f.read())

    # as lists of ints
    # inputs = [[int(x) for x in row.split()] for row in f.read().split('\n')]

    # as single array of ints
    inputs = [ int(row) for row in f.read().split('\n')]

    # as something else
    # inputs = [[x for x in row.split()] for row in f.read().split('\n')]

    print("\n----------------- input stats -----------------")
    print("len(inputs):", len(inputs))
    # print("row sum", sum(inputs[0]))
    print("inputs[0]:", inputs[0])
    print("len(inputs[0]):", len(inputs[0]))

    print("\n----------------- solutions -----------------")
    print("part1:", part1(inputs))
    # print("part2:", part2(inputs))

    print("\n")