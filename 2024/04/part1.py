with open("input.txt") as f:
    lines = f.read().splitlines()

ans = 0

width = len(lines[0])
height = len(lines)

for lineIndex, line in enumerate(lines):
    for cIndex, c in enumerate(line):
        if c == "X":
            # left to right
            if (
                (cIndex < width - 3)
                and (line[cIndex + 1] == "M")
                and (line[cIndex + 2] == "A")
                and (line[cIndex + 3] == "S")
            ):
                ans += 1

            # right to left
            if (
                (cIndex > 2)
                and (line[cIndex - 1] == "M")
                and (line[cIndex - 2] == "A")
                and (line[cIndex - 3] == "S")
            ):
                ans += 1

            # vertical forward
            if (
                (lineIndex < height - 3)
                and (lines[lineIndex + 1][cIndex] == "M")
                and (lines[lineIndex + 2][cIndex] == "A")
                and (lines[lineIndex + 3][cIndex] == "S")
            ):
                ans += 1

            # vertical backwards
            if (
                (lineIndex > 2)
                and (lines[lineIndex - 1][cIndex] == "M")
                and (lines[lineIndex - 2][cIndex] == "A")
                and (lines[lineIndex - 3][cIndex] == "S")
            ):
                ans += 1

            if (
                (lineIndex < height - 3)
                and (cIndex < width - 3)
                and (lines[lineIndex + 1][cIndex + 1] == "M")
                and (lines[lineIndex + 2][cIndex + 2] == "A")
                and (lines[lineIndex + 3][cIndex + 3] == "S")
            ):
                ans += 1

            if (
                (lineIndex < height - 3)
                and (cIndex > 2)
                and (lines[lineIndex + 1][cIndex - 1] == "M")
                and (lines[lineIndex + 2][cIndex - 2] == "A")
                and (lines[lineIndex + 3][cIndex - 3] == "S")
            ):
                ans += 1

            if (
                (lineIndex > 2)
                and (cIndex > 2)
                and (lines[lineIndex - 1][cIndex - 1] == "M")
                and (lines[lineIndex - 2][cIndex - 2] == "A")
                and (lines[lineIndex - 3][cIndex - 3] == "S")
            ):
                ans += 1

            if (
                (lineIndex > 2)
                and (cIndex < height - 3)
                and (lines[lineIndex - 1][cIndex + 1] == "M")
                and (lines[lineIndex - 2][cIndex + 2] == "A")
                and (lines[lineIndex - 3][cIndex + 3] == "S")
            ):
                ans += 1

print(ans)
