def safeRow(l: list) -> bool:
    if l[0] < l[1]:
        order = 'up'
    else:
        order = 'down'
    for i in range(1, len(l) - 1):
        if l[i] >= l[i + 1] and order == 'up':
            return False
        elif l[i] <= l[i + 1] and order == 'down':
            return False
        elif abs(l[i] - l[i + 1]) > 3:
            return False
    if abs(l[0] - l[1]) > 3 or l[0] == l[1]:
        return False
    return True

infile = open('input1.txt', 'r')
lines = infile.readlines()
infile.close()
sol = 0
for line in lines:
    line = line.strip()
    l = list(map(int, line.split()))
    for i in range(len(l)):
        newlist = l[:i] + l[i+1:]
        if safeRow(newlist):
            sol += 1
            break

print(sol)
