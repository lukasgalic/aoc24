lst = []

file = open('input.txt', 'r')
line = file.read().strip()

i = 0
j = 0
for char in line:
    digit = int(char)
    if i % 2 == 0:
        lst.extend([j]*digit)
        j += 1
    else:
        lst.extend([-1]*digit)
    i += 1


woo = []
# Iterate through the list backwards
k = 0
for i in range(len(lst) - 1, -1, -1):
    if k >= i-1:
        break
    try:
        first_minus_one_index = lst.index(-1)
        k = first_minus_one_index
        lst[first_minus_one_index] = lst[i]
        lst.pop()
    except ValueError:
        break

tot_sum = 0
for i in range(len(lst)):
    if lst[i] == -1:
        continue
    value = i * lst[i]
    tot_sum += value

print(tot_sum)
