# Vincent Ren
# 2017-12-24

# ================== Solutions ==================
def part1(inputs):
    
    count = 0

    print(inputs[0])
    print(inputs)

    # for input in sorted(inputs):
    #     print(input)
        # pass

    maxval = 0

    def dfs(comps, port, val):
        maxval = max(maxval,val)
        for i in range(comps):
            if comps[i][0] == port:
                dfs(comps[:i] + comps[i+1:], comps[i][1] , val+comps[i][0]+comps[i][1])
            elif comps[i][1] == port:
                dfs(comps[:i] + comps[i+1:], comps[i][0] , val+comps[i][0]+comps[i][1])
    
    dfs(inputs, 0 , 0)



    return maxval


# -----------------------------------------------

def part2(inputs):

    
    count = 0

    print(inputs[0])
    print(inputs)

    # for input in sorted(inputs):
    #     print(input)
        # pass

    maxval = [0, 0]

    def dfs(comps, port, val, size):

        if size > maxval[1]:
            maxval[1] = size
            maxval[0] = val
        elif size == maxval[1] and val > maxval[0]:
            maxval[0] = val


        for i in range(len(comps)):
            if comps[i][0] == port:
                dfs(comps[:i] + comps[i+1:], comps[i][1] , val+comps[i][0]+comps[i][1], size + 1)
            elif comps[i][1] == port:
                dfs(comps[:i] + comps[i+1:], comps[i][0] , val+comps[i][0]+comps[i][1], size + 1)
    
    dfs(inputs, 0 , 0, 0)



    return maxval[0]



# =================== Driver ====================

with open("in24.txt", "r") as f:

    # as single string
    # inputs = f.read()

    # as single int
    # inputs = int(f.read())

    # as lists of ints
    # inputs = [[int(x) for x in row.split()] for row in f.read().split('\n')]

    # as single array of ints
    # inputs = [ int(row) for row in f.read().split('\n')]

    # as generic list of strings
    inputs = [[int(x) for x in row.split('/')] for row in f.read().split('\n')]

    print("\n----------------- input stats -----------------")
    print("len(inputs):", len(inputs))
    # print("row sum", sum(inputs[0]))
    print("inputs[0]:", inputs[0])
    print("len(inputs[0]):", len(inputs[0]))

    print("\n----------------- solutions -----------------")
    print("part1:", part1(inputs))
    # print("part2:", part2(inputs))

    print("\n")