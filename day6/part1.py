matrix = []


with open('test.txt', 'r', encoding='utf-8') as file:
    for line in file:
        row = [char for char in line]
        matrix.append(row)


value_to_find = '^'

for row_index, row in enumerate(matrix):
    for col_index, element in enumerate(row):
        if element == value_to_find:
            coordinates_of_start_point = [row_index, col_index]

num_rows = len(matrix)
num_columns = len(matrix[0])
direction = 'up'
r = coordinates_of_start_point[0]
c = coordinates_of_start_point[1]
visited = set()

while 0 <= r < num_rows and 0 <= c < num_columns:
    visited.add((r, c))
    if direction == 'up' and r > 0 and matrix[r-1][c] != '#':
        r -= 1
        if r > 0 and matrix[r-1][c] == '#':
            direction = 'right'
    elif direction == 'right' and c + 1 < num_columns and matrix[r][c+1] != '#':
        c += 1
        if c + 1 < num_columns and matrix[r][c+1] == '#':
            direction = 'down'
    elif direction == 'down' and r + 1 < num_rows and matrix[r+1][c] != '#':
        r += 1
        if r + 1 < num_rows and matrix[r+1][c] == '#':
            direction = 'left'
    elif direction == 'left' and c > 0 and matrix[r][c-1] != '#':
        c -= 1
        if c > 0 and matrix[r][c-1] == '#':
            direction = 'up'
    else:
        break  # No valid move

print(len(visited))
