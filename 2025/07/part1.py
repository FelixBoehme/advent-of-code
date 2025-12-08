with open("input.txt") as f:
    lines = f.read().strip().split()

checked = set()


def getSplits(diagram, index, offset):
    height = len(diagram)
    line = 0
    while diagram[line][index] != "^" and line < height - 1:
        line += 1
    if line == height - 1 or (line + offset, index) in checked:
        return 0
    else:
        checked.add((line + offset, index))
        return (
            1
            + getSplits(diagram[line + 1 :], index - 1, line + offset + 1)
            + getSplits(diagram[line + 1 :], index + 1, line + offset + 1)
        )


print(getSplits(lines, lines[0].find("S"), 0))
