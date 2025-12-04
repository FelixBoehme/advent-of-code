with open("input.txt") as f:
    lines = f.read().strip().split(",")
    pairs = [l.strip().split("-") for l in lines]

sum = 0

for s, e in pairs:
    num = s[: len(s) // 2]
    if len(s) % 2 == 1:
        num = '1' + '0' * (len(s) // 2)
    while int(num * 2) <= int(e):
        if int(num * 2) >= int(s):
            sum += int(num * 2)
        num = str(int(num) + 1)

print(sum)
