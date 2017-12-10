# Vincent Ren
# 2017-12-09

# ================== Solutions ==================
def part1(s):
    
    print(s)

    openBrackets = 0
    garbageActive = False
    _sum = 0

    i = 0
    while i < len(s):
        if s[i] == '!':
            i += 1
        elif not garbageActive:
            if s[i] == '{':
                openBrackets += 1
            elif s[i] == '}':
                _sum += openBrackets
                openBrackets -= 1
            elif s[i] == '<':
                garbageActive = True
        elif garbageActive:
            if s[i] == '>':
                garbageActive = False
        i += 1
    return _sum


# -----------------------------------------------

def part2(s):


    openBrackets = 0
    garbageActive = False
    _sum = 0
    garbageSum = 0

    i = 0
    while i < len(s):
        if s[i] == '!':
            i += 1
        elif not garbageActive:
            if s[i] == '{':
                openBrackets += 1
            elif s[i] == '}':
                _sum += openBrackets
                openBrackets -= 1
            elif s[i] == '<':
                garbageActive = True
        elif garbageActive:
            if s[i] == '>':
                garbageActive = False
            else:
                garbageSum += 1

        i += 1
    return garbageSum



# =================== Driver ====================

with open("in9.txt", "r") as f:

    # as single string
    inputs = f.read()

    # as single int
    # inputs = int(f.read())

    # as lists of ints
    # inputs = [[int(x) for x in row.split()] for row in f.read().split('\n')]

    # as single array of ints
    # inputs = [ int(row) for row in f.read().split('\n')]

    # as something else
    # inputs = [[x for x in row.split()] for row in f.read().split('\n')]

    print("\n----------------- input stats -----------------")
    print("len(inputs):", len(inputs))
    # print("row sum", sum(inputs[0]))
    print("inputs[0]:", inputs[0])
    print("len(inputs[0]):", len(inputs[0]))

    print("\n----------------- solutions -----------------")
    # print("part1:", part1(inputs))
    print("part2:", part2(inputs))

    print("\n")