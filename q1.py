with open("in1.txt", "r") as f:

    _sum = 0
    input = f.read()

    # input = "123123"

    N = len(input)
    checksize = N//2
    print( checksize)

    for i in range(N):
        # for j in range(1, checksize+1):
        if input[i] == input[(i+checksize) % N]:
            _sum += int(input[i])
                # break

    print(_sum)

    # _sum = 0
    # input = f.read()
    # # input = "qwe"
    # for i, ch in enumerate(input[:-1]):
    #     if input[i] == input[i+1]:
    #         _sum += int(input[i])

    # if input[-1] == input[0]:
    #         _sum += int(input[-1])
    
    # print(_sum)
