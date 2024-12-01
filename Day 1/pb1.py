infile = open('input1.txt', 'r')

lines = infile.readlines()
list1, list2 = [], []
for line in lines:
    line = line.strip()
    a, b = map(int, line.split())
    list1.append(a)
    list2.append(b)

list1.sort()
list2.sort()

sol = 0
for i in range(len(list1)):
    sol += abs(list1[i] - list2[i])

print(sol)

infile.close()