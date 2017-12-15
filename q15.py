# Vincent Ren
# 2017-12-15

# ================== Solutions ==================
def part1(inputs):
    
    genA = int(inputs[0][-1])
    genB = int(inputs[1][-1])

    # genA = 65
    # genB = 8921

    factorA = 16807
    factorB = 48271

    

    dividend = 2147483647
    # dividend = 214

    _sum = 0

    for i in range(40000000):
        # genA = (genA * factorA)
        # genB = (genB * factorB)

        genA = (genA * factorA) % dividend
        genB = (genB * factorB) % dividend

        # print(genA, genB)
        # print(bin(genA), bin(genB))
        # print(bin(genA)[-16:], bin(genB)[-16:])

        if bin(genA)[-16:] == bin(genB)[-16:]:
            _sum +=1

    return _sum


# -----------------------------------------------

def part2(inputs):

   
    genA = int(inputs[0][-1])
    genB = int(inputs[1][-1])

    # genA = 65
    # genB = 8921


    factorA = 16807
    factorB = 48271

    dividend = 2147483647

    _sum = 0

    arrA = []
    arrB = []

    
    while len(arrB) < 5000000:
        genA = (genA * factorA) % dividend
        genB = (genB * factorB) % dividend

        if genA % 4 == 0:
            arrA.append(bin(genA)[-16:])

        if genB % 8 == 0:
            arrB.append(bin(genB)[-16:])

    for a,b in zip(arrA, arrB):
        if a == b:
            _sum += 1

    print(len(arrA), len(arrB))

    return _sum


# =================== Driver ====================

with open("in15.txt", "r") as f:

    # as single string
    # inputs = f.read()

    # as single int
    # inputs = int(f.read())

    # as lists of ints
    # inputs = [[int(x) for x in row.split()] for row in f.read().split('\n')]

    # as single array of ints
    # inputs = [ int(row) for row in f.read().split('\n')]

    # as something else
    inputs = [[x for x in row.split()] for row in f.read().split('\n')]

    print("\n----------------- input stats -----------------")
    print("len(inputs):", len(inputs))
    # print("row sum", sum(inputs[0]))
    print("inputs[0]:", inputs[0])
    print("len(inputs[0]):", len(inputs[0]))

    print("\n----------------- solutions -----------------")
    # print("part1:", part1(inputs))
    print("part2:", part2(inputs))

    print("\n")