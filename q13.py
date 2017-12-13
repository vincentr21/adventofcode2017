# Vincent Ren
# 2017-12-13

# ================== Solutions ==================
def part1(inputs):
    
    maxDepth = inputs[-1][0]
    print(maxDepth)
    

    _sum = 0
    layers = {x[0] : x[1] for x in inputs}

    for i in range(maxDepth+1):
        if i in layers and i % ( (layers[i]-1)*2 ) == 0:
            # print(i, 'active',  (layers[i]-1)*2)
            _sum += i*layers[i]

    return _sum


# -----------------------------------------------

def part2(inputs):

    maxDepth = inputs[-1][0]
    print(maxDepth)
    

    
    layers = {x[0] : x[1] for x in inputs}

    delayOffset = 0
    safe = False



    # print('in delay', delayOffset)
    # safe = True
    # for i in range(maxDepth+1):
    #     if i in layers and (i+ delayOffset) % ( ( (layers[i]-1)*2 )  ) == 0:
    #         print(i, 'active',  (layers[i]-1)*2 + delayOffset)
    #         safe = False
            


    while not safe:
        print('in delay', delayOffset)
        safe = True
        for i in range(maxDepth+1):
            if i in layers and (i+ delayOffset) % ( ( (layers[i]-1)*2)  ) == 0:
                # print(i, 'active',  (layers[i]-1)*2 + delayOffset)
                safe = False
                break

        delayOffset += 1


    return delayOffset - 1



# =================== Driver ====================

with open("in13.txt", "r") as f:

    # as single string
    # inputs = f.read()

    # as single int
    # inputs = int(f.read())

    # as lists of ints
    # inputs = [[int(x) for x in row.split()] for row in f.read().split('\n')]

    # as single array of ints
    # inputs = [ int(row) for row in f.read().split('\n')]

    # as something else
    inputs = [[int(x) for x in row.split(': ')] for row in f.read().split('\n')]

    print("\n----------------- input stats -----------------")
    print("len(inputs):", len(inputs))
    # print("row sum", sum(inputs[0]))
    print("inputs[0]:", inputs[0])
    print("len(inputs[0]):", len(inputs[0]))

    print("\n----------------- solutions -----------------")
    # print("part1:", part1(inputs))
    print("part2:", part2(inputs))

    print("\n")