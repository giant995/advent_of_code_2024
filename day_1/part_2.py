from collections import Counter


list_a = []
list_b = []

with open("input.txt") as file:
    for line in file:
        num_1, num_2 = line.rstrip().split("   ")
        list_a.append(int(num_1))
        list_b.append(int(num_2))

occurences = Counter(list_b)

similarity_score = 0

for n in list_a:
    similarity_score += n * occurences[n]

print(similarity_score)
