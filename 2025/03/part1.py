with open("input.txt") as f:
    lines = f.read().strip().split()
    jolts = [[int(n) for n in l] for l in lines]

sum = 0
length = len(jolts[0])

for b in jolts:
    num1 = 0
    num2 = 0
    for i, n in enumerate(b):
        if i < length -1 and n > num1:
            num1 = n
            num2 = b[i + 1]
        elif n > num2:
            num2 = n
    sum += int(str(num1) + str(num2))

print(sum)
