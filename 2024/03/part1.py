with open("input.txt") as f:
    data = f.read()

num1 = 0
num2 = 0

nmbToSkip = 0
startFound = False

ans = 0

for i, c in enumerate(data):
    if nmbToSkip > 0:
        nmbToSkip -= 1
        continue

    if (
        (c == "m")
        and (data[i + 1] == "u")
        and (data[i + 2] == "l")
        and (data[i + 3] == "(")
    ):
        nmbToSkip += 3
        startFound = True
        continue

    if startFound:
        num = ""

        for offset in range(0, 8):
            char = data[i + offset]
            if char.isnumeric():
                num += char
            elif char == ",":
                num1 = int(num)
                num = ""
            elif char == ")":
                num2 = int(num)
                ans += num1 * num2
                num1, num2 = 0, 0
                nmbToSkip += offset
                break
            else:
                nmbToSkip += offset
                break

        startFound = False

print(ans)
