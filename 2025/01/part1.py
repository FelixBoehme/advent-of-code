with open("input.txt") as f:
    lines = f.read().strip().split()
    rotations = [(l[0], int(l[1:])) for l in lines]

val = 50
ans = 0

for d, n in rotations:
    if d == "R":
        val += n
    else:
        val -= n
    val = (val + 100) % 100

    if val == 0:
        ans += 1

print(ans)
