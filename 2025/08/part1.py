from collections import defaultdict

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


for p, (_, i, j) in enumerate(distances):
    if p == 1000:
        sizes = defaultdict(int)
        for i in range(len(lines)):
            sizes[find(i)] += 1
        sizes = sorted(sizes.values(), reverse=True)
        print(sizes[0] * sizes[1] * sizes[2])
        break
    if find(i) != find(j):
        mix(i, j)
