# Vincent Ren
# 2017-12-16

# ================== Solutions ==================
def part1(inputs):
    
    count = 0
    N = 16
    prog = [chr(ord('a') + i) for i in range(N)]
    

    print(prog)
    print(inputs[0])

    for i in range(1000000000):

        for input in inputs:
            if input[0] == 's':
                spin = int(input[1:])

                prog = prog[N-spin:] + prog[:N-spin]

            elif input[0] == 'x':
                tokens = input.split('/')
                a = int(tokens[0][1:])
                b = int(tokens[1])

                prog[a], prog[b] = prog[b], prog[a]

            elif input[0] == 'p':
                a = input[1]
                b = input[3]

                ai = prog.index(a)
                bi = prog.index(b)

                prog[ai], prog[bi] = prog[bi], prog[ai]
            
        # print(prog)
        

    return ''.join(prog)


# -----------------------------------------------

def part2(inputs):


    # def dance(arr):

    #     res = ['x' for ch in arr]

    #     res[0] = arr[6]
    #     res[1] = arr[10]
    #     res[2] = arr[12]
    #     res[3] = arr[13]
    #     res[4] = arr[3]
    #     res[5] = arr[0]
    #     res[6] = arr[7]
    #     res[7] = arr[14]
    #     res[8] = arr[11]
    #     res[9] = arr[9]
    #     res[10] = arr[1]
    #     res[11] = arr[5]
    #     res[12] = arr[2]
    #     res[13] = arr[4]
    #     res[14] = arr[15]
    #     res[15] = arr[8]
        
    #     return res

    #     # abcdefghij klmnop
    #     # 0123456789 012345
    #     # gkmndaholj bfcepi

    
    # def cheapdance(arr):

    #     print(arr)

    #     res = [ch for ch in arr]

    #     res[3] = arr[13]
    #     res[4] = arr[3]
    #     res[13] = arr[4]

    #     # res[3] = arr[4]
    #     # res[4] = arr[13]
    #     # res[13] = arr[3]

    #     print(res)
    #     return res



    N = 16
    prog = [chr(ord('a') + i) for i in range(N)]
    

    print(prog)
    print(inputs[0])

    memo = {}

    # for i in range(1000000000):
    for i in range(40):
        if tuple(prog) in memo:
            print(i)
            break
            prog = memo[tuple(prog)]

        else:
            currProg = tuple(prog)

            for input in inputs:
                if input[0] == 's':
                    spin = int(input[1:])

                    prog = prog[N-spin:] + prog[:N-spin]

                elif input[0] == 'x':
                    tokens = input.split('/')
                    a = int(tokens[0][1:])
                    b = int(tokens[1])

                    prog[a], prog[b] = prog[b], prog[a]

                elif input[0] == 'p':
                    a = input[1]
                    b = input[3]

                    ai = prog.index(a)
                    bi = prog.index(b)

                    prog[ai], prog[bi] = prog[bi], prog[ai]
            
            memo[currProg] = prog[:]
        
    print(1000000000 % 60)

    return ''.join(prog)


# =================== Driver ====================

with open("in16.txt", "r") as f:

    # as single string
    inputs = f.read().split(',')

    # as single int
    # inputs = int(f.read())

    # as lists of ints
    # inputs = [[int(x) for x in row.split()] for row in f.read().split('\n')]

    # as single array of ints
    # inputs = [ int(row) for row in f.read().split('\n')]

    # as generic list of strings
    # inputs = [[x for x in row.split(',')] for row in f.read().split(',')]
    # inputs = [[x for x in row.split(',')] for row in f.read().split(',')]
    

    print("\n----------------- input stats -----------------")
    print("len(inputs):", len(inputs))
    # print("row sum", sum(inputs[0]))
    print("inputs[0]:", inputs[0])
    print("len(inputs[0]):", len(inputs[0]))

    print("\n----------------- solutions -----------------")
    # print("part1:", part1(inputs))
    print("part2:", part2(inputs))

    print("\n")