# Vincent Ren
# 2017-12-12

# ================== Solutions ==================
def part1(inputs):
    
    d = {}
    visited = set()

    _sum = 0
    for input in inputs:
        node = input[0]
        connected = input[1].replace(" ", "").split(',')
        # print(node, connected)
        
        d[node] = connected

    # print(d)

    stack = []
    stack.append('0')

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            # print("visiting", node)
            _sum += 1
            for adjnode in d[node]:
                if adjnode not in visited:
                    stack.append(adjnode)


    return _sum


# -----------------------------------------------

def part2(inputs):

    d = {}
    visited = set()
    graphs = 0

    _sum = 0
    for input in inputs:
        node = input[0]
        connected = input[1].replace(" ", "").split(',')
        # print(node, connected)
        
        d[node] = connected

    # print(len(d))

    for node in d:
        

        if not node in visited:
            
            _sum += 1
            stack = []
            stack.append(node)

            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    # print("visiting", node)
                    
                    for adjnode in d[node]:
                        if adjnode not in visited:
                            stack.append(adjnode)

            

    return _sum


# =================== Driver ====================

with open("in12.txt", "r") as f:

    # as single string
    # inputs = f.read()

    # as single int
    # inputs = int(f.read())

    # as lists of ints
    # inputs = [[int(x) for x in row.split()] for row in f.read().split('\n')]

    # as single array of ints
    # inputs = [ int(row) for row in f.read().split('\n')]

    # as something else
    inputs = [[x for x in row.split(' <-> ')] for row in f.read().split('\n')]

    print("\n----------------- input stats -----------------")
    print("len(inputs):", len(inputs))
    # print("row sum", sum(inputs[0]))
    print("inputs[0]:", inputs[0])
    print("len(inputs[0]):", len(inputs[0]))

    print("\n----------------- solutions -----------------")
    # print("part1:", part1(inputs))
    print("part2:", part2(inputs))

    print("\n")