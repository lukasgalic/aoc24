def can_reach_target(numbers, target, i, current_value):
    # If we've placed all operators and reached the end:
    if i == len(numbers):
        return current_value == target

    # Try adding the next number
    if can_reach_target(numbers, target, i + 1, current_value + numbers[i]):
        return True

    # Try multiplying the next number
    if can_reach_target(numbers, target, i + 1, current_value * numbers[i]):
        return True

    if can_reach_target(numbers, target, i + 1, int(str(current_value) + str(numbers[i]))):
        return True

    return False


def equals_test_value(arr, test_value):
    lst = list(map(int, arr.split()))
    test_val = int(test_value)

    c = int(str(lst[0]) + str(lst[1]))

    # If only two numbers, just check directly:
    if len(lst) == 2:
        return (lst[0] + lst[1] == test_val) or (lst[0] * lst[1] == test_val) or c == test_val

    # Recursively try all combinations starting with the first number as current_value
    return can_reach_target(lst, test_val, 1, lst[0])


total_sum = 0
with open('input.txt', 'r') as file:
    for line in file:
        test_value, arr = line.split(':')
        if equals_test_value(arr.strip(), test_value.strip()):
            total_sum += int(test_value)

print(total_sum)
