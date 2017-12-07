# Vincent Ren
# 2017-12-07

# ================== Solutions ==================

class Node(object):
    def __init__(self, val):
        self.val = val
        self.parent = None

def part1(inputs):
    
    d = {}

    res = 0
    # print(inputs[:5])
    for input in inputs:
        # print(input)
        # print(len(input))
        if len(input) > 2:
            parent = input[0]
            children = input[3:]

            # print(parent)
            # print(children)

            if parent not in d:
                d[parent] = Node(parent)

            for child in children:
                # print("child")
                # print(children)
                # print(child)
                if child not in d:
                    d[child] = Node(child)
                d[child].parent = d[parent]

    node = d[parent]
    while node.parent:
        node = node.parent


    return node.val


# -----------------------------------------------
class Node(object):
    def __init__(self, val, weight=0):
        self.val = val
        self.parent = None
        self.children = []
        self.weight = weight
        self.cumulative = 0


def part2(inputs):
    
    d = {}

    res = 0
    # print(inputs[:5])
    for input in inputs:
        # print(input)
        # print(len(input))




        if len(input) > 2:
            parent = input[0]
            weight = int(input[1])
            children = input[3:]
            
            

            # print(parent)
            # print(children)

            if parent not in d:
                d[parent] = Node(parent, weight)
            else:
                d[parent].weight = weight

            for child in children:

                if child not in d:
                    d[child] = Node(child)

                d[child].parent = d[parent]
                d[parent].children.append(d[child])

        # simple input with no children
        else:
            node = input[0]
            weight = int(input[1])
            if node not in d:
                d[node] = Node(node, weight)
            else:
                d[node].weight = weight

    root = d['hmvwl']
    # root = d['tknk']

    def cumulativeSum(node):
        if not node.children:
            node.cumulative = node.weight
            return node.cumulative

        _sum = 0
        for child in node.children:
            _sum += cumulativeSum(child)
        
        node.cumulative = _sum + node.weight
        return node.cumulative
    

    print(cumulativeSum(root))

    from collections import deque
    q = deque()

    q.append(root)

    depth_dict = {0:1}
    depth = 0
    res = []
    level = []

    while q:
        node = q.popleft()
        level.append(node.cumulative)
        
        for child in node.children:
            q.append(child)
            depth_dict[depth+1] = depth_dict.get(depth+1, 0) + 1
            
        depth_dict[depth] -= 1
        if depth_dict[depth] == 0:
            depth += 1
            res.append(level)
            level = []

    for row in res:
        print(row)
        print("")

    return root.children


# =================== Driver ====================

with open("in7.txt", "r") as f:

    # as single string
    # inputs = f.read()

    # as single int
    # inputs = int(f.read())

    # as lists of ints
    # inputs = [[int(x) for x in row.split('\t')] for row in f.read().split('\n')]

    # as single array of ints
    # inputs = [ int(row) for row in f.read().split('\n')]

    # as something else
    # inputs = [[x for x in row.split()] for row in f.read().split('\n')]
    inputs = [[x.strip('(,)') for x in row.split()] for row in f.read().split('\n')]

    print("\n----------------- input stats -----------------")
    print("len(inputs):", len(inputs))
    # print("row sum", sum(inputs[0]))
    print("inputs[0]:", inputs[0])
    print("len(inputs[0]):", len(inputs[0]))

    print("\n----------------- solutions -----------------")
    # print("part1:", part1(inputs))
    print("part2:", part2(inputs))

    print("\n")