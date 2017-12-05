# Vincent Ren
# 2017-12-05

# ================== Solutions ==================
def part1(inputs):
    steps = 0
    prev = 0
    curr = 0

    while 0 <= curr < len(inputs):
        prev = curr
        curr += inputs[curr]
        inputs[prev] += 1

    return steps

    # for num in inputs[:5]:
    #     print(num)
    # _sum = 0
    # for input in inputs:

    #     N = len(input)
    #     for i in range(N):
            
    #         _sum += input[i]

    # return _sum


# -----------------------------------------------

def part2(inputs):

    # inputs = [0,3,0,1,-3,]
    steps = 0
    prev = 0
    curr = 0

    while 0 <= curr < len(inputs):
        # print(inputs)
        prev = curr
        offset = inputs[curr] 

        # print(curr, offset)
        

        curr += offset
        
        # if abs(offset) >= 3:
        if offset >= 3:
            inputs[prev] -= 1
        else:
            inputs[prev] += 1

        steps += 1

    return steps


# =================== Driver ====================

with open("in5.txt", "r") as f:

    # as single string
    # inputs = f.read()

    # as single int
    # inputs = int(f.read())

    # as lists of ints
    # inputs = [[int(x) for x in row.split()] for row in f.read().split('\n')]

    inputs = [ int(row) for row in f.read().split('\n')]

    # as something else
    # inputs = [[x for x in row.split()] for row in f.read().split('\n')]

    print("\n----------------- input stats -----------------")
    # print("len(inputs):", len(inputs))
    # # print("row sum", sum(inputs[0]))
    # print("inputs[0]:", inputs[0])
    # print("len(inputs[0]):", len(inputs[0]))

    print("\n----------------- solutions -----------------")
    print("part1:", part1(inputs))
    # print("part2:", part2(inputs))

    print("\n")