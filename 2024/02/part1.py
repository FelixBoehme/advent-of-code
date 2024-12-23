with open("input.txt") as f:
    lines = f.read().splitlines()

safe_reports = 0

for line in lines:
    numbers = [int(n) for n in line.split()]
    report_length = len(numbers)
    direction = numbers[0] - numbers[report_length - 1]

    failed = False

    if abs(direction) < report_length:
        continue

    for n in range(0, report_length - 1):
        diff = numbers[n] - numbers[n + 1]

        if abs(diff) < 1 or abs(diff) > 3:
            failed = True
            break
        elif direction > 0 and diff < 0:
            failed = True
            break
        elif direction < 0 and diff > 0:
            failed = True
            break

    if not failed:
        safe_reports += 1

print(safe_reports)
