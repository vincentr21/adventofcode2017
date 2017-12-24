# Vincent Ren
# 2017-12-23

# ================== Solutions ==================
def part1(inputs):
    
    from collections import defaultdict

    d = defaultdict(int)

    res = 0

    print(inputs[0])

    snd = 0
    rcv = 0
    i = 0

    while i < len(inputs):
        # print(inputs[i], d)
        op = inputs[i][0]
        reg = inputs[i][1]

        if len(inputs[i]) > 2:
            val = inputs[i][2]

        if op == 'set':
            try:
                d[reg] = int(val)
            except ValueError:
                d[reg] = d[val]
        elif op == 'add':
            try:
                d[reg] += int(val)
            except ValueError:
                d[reg] += d[val]

        elif op == 'mul':
            try:
                d[reg] *= int(val)
            except ValueError:
                d[reg] *= d[val]
        elif op == 'mod':
            try:
                d[reg] %= int(val)
            except ValueError:
                d[reg] %= d[val]
        elif op == 'snd':
            snd = d[reg]
        elif op == 'rcv':
            if d[reg] != 0:
                rcv = snd
                break
        elif op == 'jgz':
            if d[reg] > 0:
                i -= 1
                i += int(val)
        
        i += 1

    return rcv


# -----------------------------------------------

def part2(inputs):
    
    from collections import defaultdict, deque

    d = [defaultdict(int), defaultdict(int)]

    d[0]['p'] = 0
    d[1]['p'] = 1

    q = [deque(), deque()]

    res = 0

    print(inputs[0])

    # program index, for program 0 and program 1
    i = [0, 0]
    j = 0
    while True:
    # while j < 200:
        # j += 1
        for p in range(2):

            op = inputs[i[p]][0]
            reg = inputs[i[p]][1]

            if len(inputs[i[p]]) > 2:
                val = inputs[i[p]][2]

            if op == 'set':
                try:
                    d[p][reg] = int(val)
                except ValueError:
                    d[p][reg] = d[p][val]
            elif op == 'add':
                try:
                    d[p][reg] += int(val)
                except ValueError:
                    d[p][reg] += d[p][val]

            elif op == 'mul':
                try:
                    d[p][reg] *= int(val)
                except ValueError:
                    d[p][reg] *= d[p][val]
            elif op == 'mod':
                try:
                    d[p][reg] %= int(val)
                except ValueError:
                    d[p][reg] %= d[p][val]
            elif op == 'snd':
                q[1-p].append(d[p][reg])
                if p == 1:
                    res += 1
            elif op == 'rcv':
                if q[p]:
                    d[p][reg] = q[p].popleft()
                else:
                    i[p] -= 1
            elif op == 'jgz':
                try:
                    if int(reg) > 0:
                        i[p] -= 1
                        try:
                            i[p] += int(val)
                        except ValueError:
                            i[p] += d[p][val]

                except ValueError:

                    if d[p][reg] > 0:
                        i[p] -= 1
                        try:
                            i[p] += int(val)
                        except ValueError:
                            i[p] += d[p][val]
                    
            i[p] += 1

        

        # print(inputs[i[0]], d[0], q[0])
        # print(inputs[i[1]], d[1], q[1])
        # print()
        

        if (not q[0] and not q[1] ) and inputs[i[0]][0] == inputs[i[1]][0] == 'rcv':
            print('deadlock')

            print(inputs[i[0]], d[0], q[0])
            print(inputs[i[1]], d[1], q[1])
            print()

            break

        
    return res




# =================== Driver ====================

with open("in18.txt", "r") as f:

    # as single string
    # inputs = f.read()

    # as single int
    # inputs = int(f.read())

    # as lists of ints
    # inputs = [[int(x) for x in row.split()] for row in f.read().split('\n')]

    # as single array of ints
    # inputs = [ int(row) for row in f.read().split('\n')]

    # as generic list of strings
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