with open("input.txt") as f:
    lines = f.read().splitlines()

safe_reports = 0


def report_invalid(numbers):
    report_length = len(numbers)
    direction = numbers[0] - numbers[report_length - 1]

    if direction == 0:
        for n in range(report_length - 2, 1, -1):
            dir = numbers[0] - numbers[n]
            if dir != 0:
                direction = dir
                break

    for n in range(0, report_length - 1):
        diff = numbers[n] - numbers[n + 1]

        if (
            (abs(diff) < 1 or abs(diff) > 3)
            or (direction > 0 and diff < 0)
            or (direction < 0 and diff > 0)
        ):
            return n

    return -1


for line in lines:
    numbers = [int(n) for n in line.split()]
    invalid = report_invalid(numbers)
    if invalid == -1:
        safe_reports += 1
    else:
        first = [i for i in numbers]
        second = [i for i in numbers]
        first.pop(invalid)
        second.pop(invalid + 1)
        if report_invalid(first) == -1 or report_invalid(second) == -1:
            safe_reports += 1

print(safe_reports)
