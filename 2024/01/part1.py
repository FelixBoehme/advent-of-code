with open("input.txt") as f:
    numbers = f.read().split()
    numbers = [int(numb) for numb in numbers]

sum = 0
list1 = sorted([numbers[i] for i in range(0, len(numbers), 2)])
list2 = sorted([numbers[i] for i in range(1, len(numbers), 2)])


for num1, num2 in zip(list1, list2):
    sum += abs(num1 - num2)

print(sum)
