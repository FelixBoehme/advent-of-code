with open("input.txt") as f:
    lists = f.read().strip().split("\n\n")
    ranges = [tuple(map(int, l.split("-"))) for l in lists[0].split()]

ranges = sorted(ranges)
ans = 0
curr = 0
for s, e in ranges:
    start = max(curr+1, s)
    if e >= start:
        ans += e-start+1
        curr = e

print(ans)
