infile = open('input1.txt', 'r')

lines = infile.readlines()
list1, list2 = [], []
for line in lines:
    line = line.strip()
    a, b = map(int, line.split())
    list1.append(a)
    list2.append(b)

sol = 0
for locationID in list1:
    cnt = list2.count(locationID)
    sol += locationID * cnt

print(sol)