# Vincent Ren
# 2017-12-03

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

with open("in3.txt", "r") as f:

    # as single string
    # inputs = f.read()

    # as single int
    # inputs = int(f.read())

    # as lists of ints
    inputs = [[int(x) for x in row.split('\t')] for row in f.read().split('\n')]

    # as something else
    # inputs = [[int(x) for x in row.split('\t')] for row in f.read().split('\n')]

    print(part1(inputs))
    # print(part2(inputs))