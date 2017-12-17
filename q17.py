# Vincent Ren
# 2017-12-17

# ================== Solutions ==================
def part1(inputs):
    
    count = 0

    print(inputs)

    spinlock = [0]
    currPos = 0
    # step = 3
    step = inputs

    for i in range(1, 2018):
        insertPos = (currPos + step) % len(spinlock) + 1
        spinlock.insert(insertPos, i)
        currPos = insertPos

    print(spinlock)



    return count


# -----------------------------------------------

def part2(inputs):

    count = 0

    print(inputs)

    # spinlock = [0]
    currPos = 0
    # step = 3
    step = inputs

    size = 1

    # print(spinlock)

    for i in range(1, 50000000):
        insertPos = (currPos + step) % size + 1
        # spinlock.insert(insertPos, i)
        currPos = insertPos

        size += 1

        # print(spinlock)
        if insertPos == 1:
            print(i)



    return count



# =================== Driver ====================

with open("in17.txt", "r") as f:

    # as single string
    # inputs = f.read()

    # as single int
    inputs = int(f.read())

    # as lists of ints
    # inputs = [[int(x) for x in row.split()] for row in f.read().split('\n')]

    # as single array of ints
    # inputs = [ int(row) for row in f.read().split('\n')]

    # as generic list of strings
    # inputs = [[x for x in row.split()] for row in f.read().split('\n')]

    print("\n----------------- input stats -----------------")
    # print("len(inputs):", len(inputs))
    # print("row sum", sum(inputs[0]))
    # print("inputs[0]:", inputs[0])
    # print("len(inputs[0]):", len(inputs[0]))

    print("\n----------------- solutions -----------------")
    # print("part1:", part1(inputs))
    print("part2:", part2(inputs))

    print("\n")