list_a = []
list_b = []

with open("input.txt") as file:
    for line in file:
        num_1, num_2 = line.rstrip().split("   ")
        list_a.append(int(num_1))
        list_b.append(int(num_2))

list_a.sort()
list_b.sort()

distance = 0

for i in range(len(list_a)):
    distance += abs(list_a[i] - list_b[i])

print(distance)
