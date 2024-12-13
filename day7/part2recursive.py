def can_reach_target(numbers, target, i, current_value):

    if i == len(numbers):
        return current_value == target

    if can_reach_target(numbers, target, i + 1, current_value + numbers[i]):
        return True

    if can_reach_target(numbers, target, i + 1, current_value * numbers[i]):
        return True

    if can_reach_target(numbers, target, i + 1, int(str(current_value) + str(numbers[i]))):
        return True

    return False


def equals_test_value(arr, test_value):
    lst = list(map(int, arr.split()))
    test_val = int(test_value)

    c = int(str(lst[0]) + str(lst[1]))

    if len(lst) == 2:
        return (lst[0] + lst[1] == test_val) or (lst[0] * lst[1] == test_val) or c == test_val

    return can_reach_target(lst, test_val, 1, lst[0])


total_sum = 0
with open('input.txt', 'r') as file:
    for line in file:
        test_value, arr = line.split(':')
        if equals_test_value(arr.strip(), test_value.strip()):
            total_sum += int(test_value)

print(total_sum)
