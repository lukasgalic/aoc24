matrix = []


with open('test.txt', 'r', encoding='utf-8') as file:
    for line in file:
        row = [int(char) for char in line.strip()]
        matrix.append(row)

current = 0
sum_of_trailheads = 0
directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        if matrix[r][c] == 0:
            has_one_higher = True
            while has_one_higher:
                if current == 9:
                    sum_of_trailheads += 1
                    current = 0
                    break
                for direction in directions:
                    nr = r - 1
                    nr1 = r+1
                    nc = c-1
                    nc1 = c+1
                    if nr > 0 and matrix[r-1][c] == current+1:
                        r = r-1
                        current += 1
                    elif nr1 < len(matrix) and matrix[r+1][c] == current+1:
                        r = r+1
                        current += 1
                    elif nc > 0 and matrix[r][c-1] == current+1:
                        c = c-1
                        current += 1
                    elif nc1 < len(matrix[0]) and matrix[r][c+1] == current+1:
                        c = c+1
                        current += 1
                    else:
                        has_one_higher = False
                        current = 0
                        break


print(f"Sum of trailheads: {sum_of_trailheads}")
