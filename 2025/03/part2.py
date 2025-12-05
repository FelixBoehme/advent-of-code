with open("input.txt") as f:
    lines = f.read().strip().split()
    jolts = [[int(n) for n in l] for l in lines]


def findBiggest(nums, numsLength, pos):
    if pos == 0:
        return ""

    max = 0
    index = 0
    while numsLength - index >= pos:
        if nums[index] > nums[max]:
            max = index
        index += 1

    return int(
        str(nums[max])
        + str(findBiggest(nums[max + 1 :], numsLength - (max + 1), pos - 1))
    )


sum = 0
numsLength = len(jolts[0])

for b in jolts:
    sum += findBiggest(b, numsLength, 12)

print(sum)
