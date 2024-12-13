import re

regex_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

with open('input.txt', 'r') as file:
    content = file.read()
    listy = re.findall(regex_pattern, content)

sum = 0
for elem in listy:
    sum += int(elem[0]) * int(elem[1])
    
print(sum)
    
