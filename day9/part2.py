# Read the input from the file
lst = []
with open('input.txt', 'r') as file:
    line = file.read().strip()

i = 0
j = 0
for char in line:
    digit = int(char)
    if i % 2 == 0:
        # Add 'digit' blocks of file j
        lst.extend([j] * digit)
        j += 1
    else:
        # Add 'digit' free blocks (-1)
        lst.extend([-1] * digit)
    i += 1


# Compacting logic: Move whole files to the leftmost free span that can fit the file,
# only if that free span is strictly to the left of the file's current position.
n = len(lst)

# Files are identified by 0,1,2..., so the maximum file ID is max(lst)
# Note: If the disk could be all free space, handle that scenario:
max_file_id = max([val for val in lst if val != -1], default=-1)

for file_id in range(max_file_id, -1, -1):
    if file_id == -1:
        continue

    # Find the current positions of the file
    file_positions = [pos for pos, v in enumerate(lst) if v == file_id]
    if not file_positions:
        continue

    file_size = len(file_positions)
    file_start = min(file_positions)

    # Attempt to find a free space span large enough and strictly to the left of 'file_start'
    moved = False
    for start in range(file_start):
        # Ensure we don't look past the file_start for the free block
        if start + file_size <= file_start:
            if lst[start:start + file_size] == [-1] * file_size:
                # Move the entire file to this position
                for pos in file_positions:
                    lst[pos] = -1  # Clear the old positions
                lst[start:start + file_size] = [file_id] * file_size
                moved = True
                break

    # If no suitable space is found, file_id remains where it is.


# Calculate the checksum
tot_sum = 0
for i, value in enumerate(lst):
    if value != -1:
        tot_sum += i * value

print(tot_sum)
