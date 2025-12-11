with open("input.txt") as f:
    lines = f.read().strip().split()

points = []
for l in lines:
    x, y, z = map(int, l.split(","))
    points.append((x, y, z))

distances = []
for i, (x, y, z) in enumerate(points):
    for j, (a, b, c) in enumerate(points):
        if j > i:
            distances.append(((x - a) ** 2 + (y - b) ** 2 + (z - c) ** 2, i, j))

distances = sorted(distances)
sets = {i: i for i in range(len(lines))}


def find(x):
    parent = sets[x]
    if parent == x:
        return x
    return find(parent)


def mix(x, y):
    sets[find(x)] = find(y)


junks = 1
for p, (_, i, j) in enumerate(distances):
    if find(i) != find(j):
        junks += 1
        if junks == 1000:
            print(points[i][0] * points[j][0])
            break
        mix(i, j)
