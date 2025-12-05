with open("input.txt") as f:
    lists = f.read().strip().split("\n\n")
    fresh = [tuple(map(int, l.split("-"))) for l in lists[0].split()]
    items = [int(l) for l in lists[1].split()]

ans = 0

for i in items:
    for s, e in fresh:
        if i >= s and i <= e:
            ans += 1
            break

print(ans)
