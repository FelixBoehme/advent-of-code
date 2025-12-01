with open("input.txt") as f:
    lines = f.read().splitlines()

ans = 0

width = len(lines[0])
height = len(lines)

for lineIndex, line in enumerate(lines):
    for cIndex, c in enumerate(line):
        if c == "A":
            if (
                (lineIndex < height - 1)
                and (lineIndex > 0)
                and (cIndex < width - 1)
                and (cIndex > 0)
            ):
                if (
                    (
                        (lines[lineIndex - 1][cIndex - 1] == "S")
                        and (lines[lineIndex + 1][cIndex + 1] == "M")
                    )
                    or (
                        (lines[lineIndex - 1][cIndex - 1] == "M")
                        and (lines[lineIndex + 1][cIndex + 1] == "S")
                    )
                ) and (
                    (
                        (lines[lineIndex - 1][cIndex + 1] == "S")
                        and (lines[lineIndex + 1][cIndex - 1] == "M")
                    )
                    or (
                        (lines[lineIndex - 1][cIndex + 1] == "M")
                        and (lines[lineIndex + 1][cIndex - 1] == "S")
                    )
                ):
                    ans += 1

print(ans)
