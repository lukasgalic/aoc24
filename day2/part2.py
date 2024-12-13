def process_sequence(arr):
    current = arr[0]
    ascending = True
    descending = True
    index = 1

    for i in range(1, len(arr)):
        if ascending and arr[i] > current and arr[i] < current + 4:
            descending = False
            current = arr[i]
            index += 1
        elif descending and arr[i] < current and arr[i] > current - 4:
            ascending = False
            current = arr[i]
            index += 1
        else:
            # Invalid sequence, reset the state
            return False

    return index == len(arr)


total = 0
with open('input.txt', 'r') as file:
    for line in file:
        numbers = list(map(int, line.split()))
        if process_sequence(numbers):
            total += 1
        else:
            new_lists = [numbers[:i] + numbers[i+1:]
                         for i in range(len(numbers))]
            for sub_array in new_lists:
                if process_sequence(sub_array):
                    total += 1
                    break

print(total)
