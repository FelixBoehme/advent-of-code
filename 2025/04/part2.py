with open("input.txt") as f:
    lines = f.read().strip().split()

width = len(lines[0])
height = len(lines)

ans = 0


def checkRolls(lines):
    ans = 0
    for i, l in enumerate(lines):
        for j, c in enumerate(l):
            rolls = 0
            if c == "@":
                if j > 0 and l[j - 1] == "@":
                    rolls += 1
                if j < width - 1 and l[j + 1] == "@":
                    rolls += 1
                if i > 0 and lines[i - 1][j] == "@":
                    rolls += 1
                if i < height - 1 and lines[i + 1][j] == "@":
                    rolls += 1
                if j > 0 and i > 0 and lines[i - 1][j - 1] == "@":
                    rolls += 1
                if j > 0 and i < height - 1 and lines[i + 1][j - 1] == "@":
                    rolls += 1
                if j < width - 1 and i > 0 and lines[i - 1][j + 1] == "@":
                    rolls += 1
                if j < width - 1 and i < height - 1 and lines[i + 1][j + 1] == "@":
                    rolls += 1
                if rolls < 4:
                    ans += 1
                    lines[i] = lines[i][:j] + "." + lines[i][j + 1 :]
    return ans


localAns = checkRolls(lines)
while localAns > 0:
    ans += localAns
    localAns = checkRolls(lines)

print(ans)
