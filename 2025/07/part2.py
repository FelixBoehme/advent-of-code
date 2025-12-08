with open("input.txt") as f:
    lines = f.read().strip().split()

checked = dict()


def getSplits(diagram, index, offset):
    height = len(diagram)
    line = 0
    while diagram[line][index] != "^" and line < height - 1:
        line += 1
    if (line + offset, index) in checked:
        return checked[(line + offset, index)]
    if line == height - 1:
        return 0
    else:
        result = (
            getSplits(diagram[line + 1 :], index - 1, line + offset + 1)
            + getSplits(diagram[line + 1 :], index + 1, line + offset + 1)
            + (2 if offset == 0 else 1)
        )
        checked[(line + offset, index)] = result
        return result


print(getSplits(lines, lines[0].find("S"), 0))
