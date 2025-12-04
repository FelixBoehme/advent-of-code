with open("input.txt") as f:
    lines = f.read().strip().split(",")
    pairs = [l.strip().split("-") for l in lines]

sum = 0

for s, e in pairs:
    matched = set()
    for i in range(2, len(e) + 1):
        num = s[: len(s) // i]
        if len(s) % i > 0:
            num = "1" + "0" * (len(s) // i)
        while int(num * i) <= int(e):
            if int(num * i) >= int(s) and (num * i) not in matched:
                matched.add(num * i)
                sum += int(num * i)
            num = str(int(num) + 1)

print(sum)
