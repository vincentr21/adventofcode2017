# Vincent Ren
# 2017-12-14

# ================== Solutions ==================
def part1(inputs):
    

    # print(q10_part2(""))

    knotHashes = []

    print(inputs)

    for i in range(128):
        knotHash = q10_part2(inputs+'-'+str(i))
        knotHashes.append(knotHash)

    # print(knotHashes)

    binaryGrid = ["{0:0128b}".format(int(x, 16)) for x in knotHashes]

    print(binaryGrid[0])

    _sum = sum( [x.count('1') for x in binaryGrid])


    return _sum


# -----------------------------------------------

def part2(inputs):

    knotHashes = []

    for i in range(128):
        knotHash = q10_part2(inputs+'-'+str(i))
        knotHashes.append(knotHash)

    binaryGrid = ["{0:0128b}".format(int(x, 16)) for x in knotHashes]

    # binaryGrid = [  '101',
    #                 '010',
    #                 '110']

    # print(binaryGrid)
    
    def unique_regions(grid):

        R = len(grid)
        C = len(grid[0])
        count = 0

        marked = set()


        def dfs(grid, row, col):
            stack = []
            stack.append((row,col))

            while stack:
                r,c = stack.pop()
                marked.add((r,c))
                # print("marking", r, c)

                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    tr = r+dr
                    tc = c+dc
                    if 0 <= tr < R and 0 <= tc < C and grid[tr][tc] == '1' and (tr,tc) not in marked:
                        stack.append((tr,tc))

        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1' and (r,c) not in marked:
                    count += 1
                    dfs(grid, r, c)

        

        return count

    return unique_regions(binaryGrid)


def q10_part2(inputs):

    nums = [ord(bytearray(ch, 'utf-8')) for ch in inputs] + [17, 31, 73, 47, 23]
    # print(nums)

    def circularReverse(array, start, length):
        N = len(array)
        end = start+length

        for i in range(0, length//2):
            # print(i)
            startmod = (start+i) % N
            endmod = (end-i-1) % N
            # print(array[startmod], array[endmod])
            array[startmod], array[endmod] = array[endmod] ,array[startmod]



    N = 256
    arr = list(range(N))
    curr = 0
    skip = 0

    # circularReverse(arr,curr,4)
    # print(arr)

    for i in range(64):
        for num in nums:
            circularReverse(arr,curr,num)
            curr = (curr + num + skip) % N
            skip += 1

    # print(arr)

    res = []

    for i in range(16):
        start, end = i*16, i*16 + 16
        # print(start,end)
        xor = arr[start]
        for j in range(start+1, end):
            xor = xor ^ arr[j] 
        res.append(xor)

    # print(res)
    a = "".join([("%0.2x" % x) for x in res])
    # print(a)
    return a


# =================== Driver ====================

with open("in14.txt", "r") as f:

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