import re

first_do_dont_pattern = r"do\(\)|don't\(\)" # Find first occurance of do() or don't()
remaining_pattern = r"do\(\)(.*?)(?=don't\(\))" # Find do() until don't()

regex_pattern = r"mul\((\d{1,3}),(\d{1,3})\)" # Find mul(x,y)

with open('input.txt', 'r') as file:
    content = file.read()

# Collect all matches for mul(x, y)
all_matches = []

splitted_list = re.split(first_do_dont_pattern, content, maxsplit=1)
first_part = re.findall(regex_pattern, splitted_list[0])

all_matches.extend(first_part)

# Find all sections starting with do() and ending with don't(), allowing multiline matches
sections = re.findall(remaining_pattern, splitted_list[1], flags=re.DOTALL)

for section in sections:
    matches = re.findall(regex_pattern, section)
    all_matches.extend(matches)

total_sum = 0
for elem in all_matches:
    total_sum += int(elem[0]) * int(elem[1])

print(total_sum) 
    