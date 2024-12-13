before = {}

file = open('input.txt', 'r')
lines = file.read().splitlines()
blank_line_index = lines.index('')

first_input = lines[:blank_line_index]
last_input = lines[blank_line_index+1:]

total_sum = 0

for elem in first_input:
    x, y = elem.strip().split('|')
    if x not in before:
        before[x] = set()
    before[x].add(y)

def valid_line(line):
    for i in range(len(line)):
        if i == len(line) -1:
            return True
        if line[i] in before:
            values0 = before[line[i]]
        if line[i+1] in before:
            values1 = before[line[i+1]]
        else:
            continue
        if line[i+1] in values0:
            continue
        else:
            return False
    return True
    
    
for elem in last_input:
    line = elem.split(',');
    if valid_line(line):
        total_sum += int(line[len(line)//2])
        
print(f"totalsum = {total_sum}")