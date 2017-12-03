# Vincent Ren
# 2017-12-03

# ================== Solutions ==================
def part1(inputs):
    
    print(inputs)
    a = 526**2
    b = 527**2

    print(inputs-a) 
    print(inputs-b) 
    # _sum = 0
    # for input in inputs:

    #     N = len(input)
    #     for i in range(N):
            
    #         _sum += input[i]

    # return _sum


# -----------------------------------------------

def part2(inputs):
    import operator
    
    d = {}
    d[(0,0)] = 1
    
    def changeDirection(delta):
        if delta == (1,0):
            return (0,1)
        if delta == (0,1):
            return (-1,0)
        if delta == (-1,0):
            return (0,-1)
        if delta == (0,-1):
            return (1,0)


    currDelta = (1,0)
    currPos = (0,0)
    currVal = 1
    dirCounter = 0
    dirLength = 1
    curr = 0

    while currVal <= inputs:
        if dirCounter >= 2:
            dirCounter = 0
            dirLength += 1
        
        if curr >= dirLength:
            currDelta = changeDirection(currDelta)
            dirCounter += 1
            curr = 0
        
        currPos = tuple(map(operator.add, currPos, currDelta))
        # currPos = currPos + currDelta

        _sum = 0
        neighbours = [
            tuple(map(operator.add, currPos, (-1,1))),
            tuple(map(operator.add, currPos, (0,1))),
            tuple(map(operator.add, currPos, (1,1))),
            tuple(map(operator.add, currPos, (-1,0))),
            tuple(map(operator.add, currPos, (1,0))),
            tuple(map(operator.add, currPos, (-1,-1))),
            tuple(map(operator.add, currPos, (0,-1))),
            tuple(map(operator.add, currPos, (1,-1))),
        ]
        
        for n in neighbours:
            _sum += d.get(n,0)
        print(_sum)
        d[currPos] = _sum
        currVal = _sum

        curr += 1



    



# =================== Driver ====================

with open("in3.txt", "r") as f:

    # as single string
    # inputs = f.read()

    # as lists of ints
    # inputs = [[int(x) for x in row.split('\t')] for row in f.read().split('\n')]


    inputs = int(f.read())
    # as something else
    # inputs = [[int(x) for x in row.split('\t')] for row in f.read().split('\n')]

    # print(part1(inputs))
    print(part2(inputs))