# Vincent Ren
# 2017-12-27

# ================== Solutions ==================
def part1(inputs):
    
    from collections import defaultdict

    d = defaultdict(int)

    count = 0

    # print(inputs[0])

    i = 0

    while i < len(inputs):
        print(inputs[i])
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

        elif op == 'sub':
            try:
                d[reg] -= int(val)
            except ValueError:
                d[reg] -= d[val]

        elif op == 'mul':
            try:
                d[reg] *= int(val)
            except ValueError:
                d[reg] *= d[val]
            count += 1
        elif op == 'jnz':
            try:
                if int(reg) != 0:
                    i -= 1
                    try:
                        i += int(val)
                    except ValueError:
                        i += d[val]

            except ValueError:

                if d[reg] != 0:
                    i -= 1
                    try:
                        i += int(val)
                    except ValueError:
                        i += d[val]
        
        i += 1

    return count


# -----------------------------------------------

def part2(inputs):

    def isprime(n):
        for i in range(2, int(n**0.5)):
            if n % i == 0:
                return False
        return True



    h = 0

    b = 84 * 100 + 100000
    c = b + 17000

    for g in range(b, c + 1, 17):
        if not isprime(g):
            h += 1

    return h








    # from collections import defaultdict

    # d = defaultdict(int)
    # d['a'] = 1
    
    # i = 0
    # steps = 0

    # # while i < len(inputs) and steps < 100000:
    # while i < len(inputs):
    #     steps += 1
        
    #     print(inputs[i])
    #     print(inputs[i], 'b d', (d['b'],d['d']) )
    #     # print(inputs[i], 'e g', (d['e'],d['g']) )
    #     # for k,v in d.items():
    #     #     print(k,v)
    #     # print()
    #     # if inputs[i] == ['jnz', 'g', '-8']:
    #     #     print()
        
        
    #     op = inputs[i][0]
    #     reg = inputs[i][1]

    #     if len(inputs[i]) > 2:
    #         val = inputs[i][2]

    #     if op == 'set':
    #         try:
    #             d[reg] = int(val)
    #         except ValueError:
    #             d[reg] = d[val]

    #     elif op == 'sub':
    #         try:
    #             d[reg] -= int(val)
    #         except ValueError:
    #             d[reg] -= d[val]

    #     elif op == 'mul':
    #         try:
    #             d[reg] *= int(val)
    #         except ValueError:
    #             d[reg] *= d[val]

    #     elif op == 'jnz':
    #         try:
    #             if int(reg) != 0:
    #                 i -= 1
    #                 try:
    #                     i += int(val)
    #                 except ValueError:
    #                     i += d[val]

    #         except ValueError:

    #             if d[reg] != 0:
    #                 i -= 1
    #                 try:
    #                     i += int(val)
    #                 except ValueError:
    #                     i += d[val]
        
    #     i += 1



    # return d['h']




# =================== Driver ====================

with open("in23.txt", "r") as f:

    # as single string
    # inputs = f.read()

    # as single int
    # inputs = int(f.read())

    # as lists of ints
    # inputs = [[int(x) for x in row.split()] for row in f.read().split('\n')]

    # as single array of ints
    # inputs = [ int(row) for row in f.read().split('\n')]
    
    # I tried modifying the original instruction, but it's not that trival
    modifiedinput = '''set b 84
    set c b
    jnz a 2
    jnz 1 5
    mul b 100
    sub b -100000
    set c b
    sub c -17000
    set f 1
    set d 2
    set e 2
    set e b
    set f 0
    sub d -1
    set g d
    sub g b
    jnz g -6
    jnz f 2
    sub h -1
    set g b
    sub g c
    jnz g 2
    jnz 1 3
    sub b -17
    jnz 1 -16'''


    # as generic list of strings
    # inputs = [[x for x in row.split()] for row in f.read().split('\n')]
    inputs = [[x for x in row.split()] for row in modifiedinput.split('\n')]
    print(inputs)


    print("\n----------------- input stats -----------------")
    print("len(inputs):", len(inputs))
    # print("row sum", sum(inputs[0]))
    print("inputs[0]:", inputs[0])
    print("len(inputs[0]):", len(inputs[0]))

    print("\n----------------- solutions -----------------")
    # print("part1:", part1(inputs))
    print("part2:", part2(inputs))

    print("\n")