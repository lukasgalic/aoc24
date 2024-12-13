
lst = []
with open('input.txt', 'r') as file:
    line = file.read().strip()

i = 0
j = 0
for char in line:
    digit = int(char)
    if i % 2 == 0:

        lst.extend([j] * digit)
        j += 1
    else:

        lst.extend([-1] * digit)
    i += 1


n = len(lst)


max_file_id = max([val for val in lst if val != -1], default=-1)

for file_id in range(max_file_id, -1, -1):
    if file_id == -1:
        continue

    file_positions = [pos for pos, v in enumerate(lst) if v == file_id]
    if not file_positions:
        continue

    file_size = len(file_positions)
    file_start = min(file_positions)

    moved = False
    for start in range(file_start):

        if start + file_size <= file_start:
            if lst[start:start + file_size] == [-1] * file_size:

                for pos in file_positions:
                    lst[pos] = -1
                lst[start:start + file_size] = [file_id] * file_size
                moved = True
                break


# Calculate checksum
tot_sum = 0
for i, value in enumerate(lst):
    if value != -1:
        tot_sum += i * value

print(tot_sum)
