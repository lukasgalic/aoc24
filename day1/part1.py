list1 = []
list2 = []
total = 0

with open('input1.txt', 'r') as file:
    for line in file:
        id1, id2 = line.split()
        list1.append(id1)
        list2.append(id2)
        
list1.sort()
list2.sort()

for i in range (len(list1)):
    total += abs(int(list1[i]) - int(list2[i]))

print(total)
    