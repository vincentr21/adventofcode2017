# Vincent Ren
# 2017-12-25

# ================== Solutions ==================
def part1(inputs):

    print('size:', len(inputs), len(inputs[0]))
    
    res = []

    pos = [0, inputs[0].index('|')]
    prev = pos[:]

    direc = [1, 0]
    
    print(pos)
    # print(inputs[5][8])

    while True:
        pos = [p + d for p,d in zip(pos, direc)]
        print(pos)
        if pos[0] < 0 or pos[0] >= len(inputs):
            break
        elif pos[1] < 0 or pos[1] >= len(inputs[0]):
            break

        if inputs[pos[0]][pos[1]] == '+':
            for dr, dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                r, c = pos[0] + dr, pos[1] + dc
                if 0 <= r < len(inputs) and 0 <= c < len(inputs[0]) and r != prev[0] and c != prev[1]:
                    # print(r,c)
                    if inputs[r][c] != ' ':
                        direc = [dr,dc]
                        break
        elif inputs[pos[0]][pos[1]] == ' ':
            break
        elif inputs[pos[0]][pos[1]] not in '|-':
            res.append(inputs[pos[0]][pos[1]])
        

        prev = pos[:]

    return ''.join(res)


# -----------------------------------------------

def part2(inputs):

    print('size:', len(inputs), len(inputs[0]))
    
    res = []
    count = 0

    pos = [0, inputs[0].index('|')]
    prev = pos[:]

    direc = [1, 0]
    
    print(pos)
    # print(inputs[5][8])

    while True:
        pos = [p + d for p,d in zip(pos, direc)]
        print(pos)
        count += 1
        if pos[0] < 0 or pos[0] >= len(inputs):
            break
        elif pos[1] < 0 or pos[1] >= len(inputs[0]):
            break

        if inputs[pos[0]][pos[1]] == '+':
            for dr, dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                r, c = pos[0] + dr, pos[1] + dc
                if 0 <= r < len(inputs) and 0 <= c < len(inputs[0]) and r != prev[0] and c != prev[1]:
                    # print(r,c)
                    if inputs[r][c] != ' ':
                        direc = [dr,dc]
                        break
        elif inputs[pos[0]][pos[1]] == ' ':
            break
        elif inputs[pos[0]][pos[1]] not in '|-':
            res.append(inputs[pos[0]][pos[1]])
        

        prev = pos[:]

    return count


# =================== Driver ====================

with open("in19.txt", "r") as f:

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