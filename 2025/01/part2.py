with open("input.txt") as f:
    lines = f.read().strip().split()
    rotations = [(l[0], int(l[1:])) for l in lines]

val = 50
ans = 0

for d, n in rotations:
    if d == "R":
        ans += (val + n) // 100
        val += n
    else:
        ans += (100 - val + n) // 100
        if val == 0:
            ans -= 1
        val -= n
    val = (val + 100) % 100

print(ans)
