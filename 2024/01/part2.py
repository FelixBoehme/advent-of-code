with open("input.txt") as f:
    numbers = f.read().split()
    numbers = [int(numb) for numb in numbers]

sum = 0

left_side = set()
for i in range(0, len(numbers), 2):
    left_side.add(numbers[i])

for i in range(1, len(numbers), 2):
    if numbers[i] in left_side:
        sum += numbers[i]

print(sum)
