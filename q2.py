def part1(input):
    N = len(input)

    _sum = 0
    for row in input:
        nums = row.split()
        nums = [ int(x) for x in nums ]
        _sum += max(nums) - min(nums)
    return _sum



def part2(input):
    N = len(input)

    _sum = 0
    for i in range(N):
        nums = input[i].split()
        nums = [ int(x) for x in nums ]
        M = len(nums)

        for a in range(M):
            for b in range(a+1,M):
                if nums[a] >= nums[b] and nums[a] % nums[b] == 0:
                    _sum += nums[a] // nums[b]
                    break
                elif nums[a] < nums[b] and nums[b] % nums[a] == 0:
                    _sum += nums[b] // nums[a]
                    break



    return _sum


# -------------- Driver -------------------

with open("in2.txt", "r") as f:

    input = f.read().split('\n')
    # input = f.read().split()

    # print(part1(input))
    print(part2(input))