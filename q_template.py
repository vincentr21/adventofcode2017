# Vincent Ren
# 2017-12-16

# ================== Solutions ==================
def part1(inputs):
    
    count = 0

    print(inputs[0])

    for input in inputs:
        # print(input)
        pass

    return count


# -----------------------------------------------

def part2(inputs):

    count = 0

    print(inputs[0])

    for input in inputs:
        # print(input)
        pass

    return count



# =================== Driver ====================

with open("in16.txt", "r") as f:

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