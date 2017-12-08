# Vincent Ren
# 2017-12-08

# ================== Solutions ==================
def part1(inputs):
    
    d = {}
    
    print(inputs[0])
    for input in inputs:
        reg1 = input[0]
        op1 = input[1]
        val1 = int(input[2])

        reg2 = input[4]
        op2 = input[5]
        val2 = int(input[6])


        isTrue = False
        if op2 == '>':
            isTrue = d.get(reg2, 0) > val2
        elif op2 == '<':
            isTrue = d.get(reg2, 0) < val2
        elif op2 == '>=':
            isTrue = d.get(reg2, 0) >= val2
        elif op2 == '<=':
            isTrue = d.get(reg2, 0) <= val2
        elif op2 == '==':
            isTrue = d.get(reg2, 0) == val2
        elif op2 == '!=':
            isTrue = d.get(reg2, 0) != val2

        if isTrue:
            if op1 == 'inc':
                d[reg1] = d.get(reg1, 0) + val1
            else:
                d[reg1] = d.get(reg1, 0) - val1

        # print(d)
        
            
    return max(d.values())


# -----------------------------------------------

def part2(inputs):

    d = {}
    highest = 0
    _sum = 0
    
    for input in inputs:
        reg1 = input[0]
        op1 = input[1]
        val1 = int(input[2])

        reg2 = input[4]
        op2 = input[5]
        val2 = int(input[6])


        isTrue = False
        if op2 == '>':
            isTrue = d.get(reg2, 0) > val2
        elif op2 == '<':
            isTrue = d.get(reg2, 0) < val2
        elif op2 == '>=':
            isTrue = d.get(reg2, 0) >= val2
        elif op2 == '<=':
            isTrue = d.get(reg2, 0) <= val2
        elif op2 == '==':
            isTrue = d.get(reg2, 0) == val2
        elif op2 == '!=':
            isTrue = d.get(reg2, 0) != val2

        if isTrue:
            if op1 == 'inc':
                d[reg1] = d.get(reg1, 0) + val1
            else:
                d[reg1] = d.get(reg1, 0) - val1
            highest = max(highest, d[reg1])
        
            
    return highest



# =================== Driver ====================

with open("in8.txt", "r") as f:

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
    print("part1:", part1(inputs))
    # print("part2:", part2(inputs))

    print("\n")