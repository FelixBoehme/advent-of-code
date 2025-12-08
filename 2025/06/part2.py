with open("input.txt") as f:
    lines = f.read().replace("\n\n", "\n").split("\n")

lines.pop()
lengths = []
ops = []
length = 0
for c in lines.pop():
    if c == "+" or c == "*":
        ops.append(c)
        if length == 0:
            length += 1
        else:
            lengths.append(length - 1)
            length = 1
    if length > 0 and c == " ":
        length += 1
lengths.append(length)

nums = [["" for i in range(lengths[j])] for j in range(len(ops))]

for l in lines:
    index = 0
    offset = 0
    for i, c in enumerate(l):
        if i - offset == lengths[index]:
            offset = i + 1
            index += 1
        nums[index][i - offset] += c

ans = 0
for i, o in enumerate(ops):
    if o == "+":
        ans += sum(map(lambda s: int(s.replace(" ", "")), nums[i]))
    else:
        product = 1
        for n in nums[i]:
            product *= int(n.replace(" ", ""))
        ans += product

print(ans)
