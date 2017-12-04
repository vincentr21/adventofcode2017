# Vincent Ren
# 2017-12-04

# ================== Solutions ==================
def part1(inputs):
    
    _sum = 0
    for input in inputs:

        d = set()
        valid = True
        for word in input:
            if word in d:
                valid = False
                break
            # print(word)
            d.add(word)
        if valid:
            _sum += 1


    return _sum


# -----------------------------------------------

def part2(inputs):

    _sum = 0
    for input in inputs:

        d = set()
        valid = True
        for word_ana in input:
            word = ''.join(sorted(word_ana))
            # print(word)
            if word in d:
                valid = False
                break
            # print(word)
            d.add(word)
        if valid:
            _sum += 1


    return _sum



# =================== Driver ====================

with open("in4.txt", "r") as f:

    # as single string
    # inputs = f.read()

    # as single int
    # inputs = int(f.read())

    # as lists of ints
    # inputs = [[int(x) for x in row.split('\t')] for row in f.read().split('\n')]

    # as something else
    inputs = [[x for x in row.split()] for row in f.read().split('\n')]

    # print(part1(inputs))
    print(part2(inputs))