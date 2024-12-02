infile = open('input1.txt', 'r')

lines = infile.readlines()
sol = 0

for line in lines:
    line = line.strip()
    l = list(map(int, line.split()))
    if l[0] < l[1]:
        order = 'up'
    else:
        order = 'down'

    safe = True
    for i in range(1, len(l) - 1):
        if l[i] >= l[i + 1] and order == 'up':
            safe = False
            break
        elif l[i] <= l[i + 1] and order == 'down':
            safe = False
            break
        elif abs(l[i] - l[i + 1]) > 3:
            safe = False
            break

    if abs(l[0] - l[1]) > 3 or l[0] == l[1]:
        safe = False

    if safe:
        sol += 1

print(sol)

infile.close()