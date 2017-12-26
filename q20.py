# Vincent Ren
# 2017-12-25

# ================== Solutions ==================
def part1(inputs):
    import re

    print(inputs[0])

    minval = 9999
    minindex = 0

    for i, input in enumerate(inputs):
        inputre = re.findall(r'-?\d+,-?\d+,-?\d+', input)
        # print(inputre)

        p = [int(x) for x in inputre[0].split(',')]
        v = [int(x) for x in inputre[1].split(',')]
        a = [int(x) for x in inputre[2].split(',')]
        
        print(p,v,a,)

        a_norm = sum([abs(x) for x in a])

        if a_norm < minval:
            minval = a_norm
            minindex = i

    print(minval, minindex)
    return minindex


# -----------------------------------------------

def part2(inputs):
    import re

    print(inputs[0])

    particles = []

    for i, input in enumerate(inputs):
        inputre = re.findall(r'-?\d+,-?\d+,-?\d+', input)
        # print(inputre)

        p = [int(x) for x in inputre[0].split(',')]
        v = [int(x) for x in inputre[1].split(',')]
        a = [int(x) for x in inputre[2].split(',')]
        
        particles.append([p,v,a])

    # print(particles)

    delete = set()

    steps = 0
    while steps < 1000:
        steps += 1

        for index, p in enumerate(particles):
            if index not in delete:
                for i in range(3):
                    p[1][i] += p[2][i]
                    p[0][i] += p[1][i]

        
        for curr in range(len(particles)):
            if curr not in delete:
                for other in range(curr+1, len(particles)):
                    if other not in delete:
                        if particles[curr][0] == particles[other][0]:
                            delete.add(curr)
                            delete.add(other)
        

        # print(delete)

        # particles = [particles[i] for i in not list(delete)]
        # print(particles)

    print(delete)

    return len(inputs) - len(delete)



# =================== Driver ====================

with open("in20.txt", "r") as f:

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
    # print("part1:", part1(inputs))
    print("part2:", part2(inputs))

    print("\n")