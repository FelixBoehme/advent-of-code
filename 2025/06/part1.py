with open("input.txt") as f:
    lines = f.read().strip().split()

nums = []
ops = []

for l in lines:
    if l == '*' or l == '+':
        ops.append(l)
    else:
        nums.append(int(l))

results = [1 if o == "*" else 0 for o in ops]
opsLength = len(ops)

for i in range(len(nums)):
    if ops[i % opsLength] == "*":
        results[i % opsLength] *= nums[i]
    else:
        results[i % opsLength] += nums[i]

print(sum(results))
