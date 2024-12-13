list1 = []
list2 = []
seen_values = dict()

with open('input1.txt', 'r') as file:
    for line in file:
        id1, id2 = line.split()
        list1.append(id1)
        list2.append(id2)

for elem in list2:
    if elem in seen_values:
        seen_values[elem] += 1
    else:
        seen_values[elem] = 1

total = 0
for elem in list1:
    if elem in seen_values:
        total += seen_values[elem] * int(elem)

print(total)



        

        