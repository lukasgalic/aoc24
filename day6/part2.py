def traverse_matrix(matrix, start_point, direction):
    """
    Traverses the matrix starting from the given point and following the direction rules.
    Returns a tuple (visited, completed, loop_detected), where:
        - 'visited' is the set of visited coordinates
        - 'completed' is a boolean indicating whether traversal completed successfully
        - 'loop_detected' is True if a loop is detected
    """
    num_rows = len(matrix)
    num_columns = len(matrix[0])
    r, c = start_point
    visited = set()
    path_history = set()  # Tracks (row, col, direction) history
    completed = True  # Assume completed unless an invalid move is encountered

    while 0 <= r < num_rows and 0 <= c < num_columns:
        current_state = (r, c, direction)

        # Check for a loop
        if current_state in path_history:
            return visited, False, True  # Loop detected

        # Record this position and direction
        path_history.add(current_state)
        visited.add((r, c))

        if is_valid_move(matrix, r, c, direction, num_rows, num_columns):
            if direction == 'up':
                r -= 1
                if r > 0 and matrix[r - 1][c] == '#':
                    direction = 'right'
            elif direction == 'right':
                c += 1
                if c + 1 < num_columns and matrix[r][c + 1] == '#':
                    direction = 'down'
            elif direction == 'down':
                r += 1
                if r + 1 < num_rows and matrix[r + 1][c] == '#':
                    direction = 'left'
            elif direction == 'left':
                c -= 1
                if c > 0 and matrix[r][c - 1] == '#':
                    direction = 'up'
        else:
            completed = False  # Invalid move
            break

    return visited, completed, False  # No loop detected


def is_valid_move(matrix, r, c, direction, num_rows, num_columns):
    """
    Checks if the current move is valid based on the direction and position.
    Returns True if valid, False otherwise.
    """
    if direction == 'up':
        return r > 0 and matrix[r - 1][c] != '#'
    elif direction == 'right':
        return c + 1 < num_columns and matrix[r][c + 1] != '#'
    elif direction == 'down':
        return r + 1 < num_rows and matrix[r + 1][c] != '#'
    elif direction == 'left':
        return c > 0 and matrix[r][c - 1] != '#'
    return False


# Main program
matrix = []

# Read input matrix
with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        row = [char for char in line.strip()]
        matrix.append(row)

value_to_find = '^'

# Find the starting point
coordinates_of_start_point = None
for row_index, row in enumerate(matrix):
    for col_index, element in enumerate(row):
        if element == value_to_find:
            coordinates_of_start_point = (row_index, col_index)

if not coordinates_of_start_point:
    print("Start point not found.")
    exit()

# Set initial direction
initial_direction = 'up'

# Use the function to traverse the matrix
visited_cells, completed, loop_detected = traverse_matrix(
    matrix, coordinates_of_start_point, initial_direction
)

print(f"Initial Traversal:")
print(f"- Number of visited cells: {len(visited_cells)}")
print(f"- Traversal completed: {completed}")
print(f"- Loop detected in initial traversal: {loop_detected}")

# Check for loops after modifying the matrix
loop_count = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        original_value = matrix[i][j]
        matrix[i][j] = '#'  # Temporarily block this cell

        visited_cells, completed, loop_detected = traverse_matrix(
            matrix, coordinates_of_start_point, initial_direction
        )

        if loop_detected:
            loop_count += 1

        matrix[i][j] = original_value  # Restore the cell

print(f"\nModified Traversal Results:")
print(f"- Loop count: {loop_count}")
