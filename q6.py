# Vincent Ren
# 2017-12-06

# ================== Solutions ==================
def part1(inputs):
    
    N = len(inputs)
    count = 0
    s = set()

    curr = inputs
    print(curr)
    while(tuple(curr) not in s):
        s.add(tuple(curr))
        # print(s)
        # print(curr)
        maxValue = max(curr)
        maxIndex = curr.index(maxValue)
        curr[maxIndex] = 0
        blocks = maxValue
        index = (maxIndex + 1) % N
        while blocks > 0:
            curr[index] += 1
            index = (index + 1) % N
            blocks -= 1

        
        count += 1
        # print(curr)
        # print(s)
    return count
    
    
    # for num in inputs:
    #     pass


    return count


# -----------------------------------------------

def part2(inputs):

    N = len(inputs)
    count = 0
    d = {}

    curr = inputs
    print(curr)
    while(tuple(curr) not in d):
        d[tuple(curr)] = count
        # print(s)
        # print(curr)
        maxValue = max(curr)
        maxIndex = curr.index(maxValue)
        curr[maxIndex] = 0
        blocks = maxValue
        index = (maxIndex + 1) % N
        while blocks > 0:
            curr[index] += 1
            index = (index + 1) % N
            blocks -= 1

        
        count += 1
        # print(curr)
        # print(s)
    
    return count - d[tuple(curr)]



# =================== Driver ====================

with open("in6.txt", "r") as f:

    # as single string
    # inputs = f.read()

    # as single int
    # inputs = int(f.read())

    # as lists of ints
    # inputs = [[int(x) for x in row.split()] for row in f.read().split('\n')]

    # as single array of ints
    # inputs = [ int(row) for row in f.read().split('\n')]
    inputs = [ int(row) for row in f.read().split('\t')]

    # as something else
    # inputs = [[x for x in row.split()] for row in f.read().split('\n')]

    print("\n----------------- input stats -----------------")
    print("len(inputs):", len(inputs))
    # print("row sum", sum(inputs[0]))
    print("inputs[0]:", inputs[0])
    # print("len(inputs[0]):", len(inputs[0]))

    print("\n----------------- solutions -----------------")
    # print("part1:", part1(inputs))
    print("part2:", part2(inputs))

    print("\n")