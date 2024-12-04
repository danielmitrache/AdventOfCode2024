infile = open('input.txt')
lines = infile.readlines()
infile.close()

n = len(lines)
m = -1
a = []
for line in lines:
    line = line.strip()
    l = []
    for letter in line:
        l.append(letter)
    l.extend([0] * 5)
    if m == -1:
        m = len(l)
    a.append(l)

l = [0] * (m + 5)
a.append(5 * l)

sol = 0
for i in range(n):
    for j in range(m):
        if a[i][j] != 'X':
            continue

        if a[i][j + 1] == 'M' and a[i][j + 2] == 'A' and a[i][j + 3] == 'S':
            sol += 1
        if a[i][j - 1] == 'M' and a[i][j - 2] == 'A' and a[i][j - 3] == 'S':
            sol += 1
        if a[i - 1][j] == 'M' and a[i - 2][j] == 'A' and a[i - 3][j] == 'S':
            sol += 1
        if a[i + 1][j] == 'M' and a[i + 2][j] == 'A' and a[i + 3][j] == 'S':
            sol += 1
        if a[i + 1][j + 1] == 'M' and a[i + 2][j + 2] == 'A' and a[i + 3][j + 3] == 'S':
            sol += 1
        if a[i + 1][j - 1] == 'M' and a[i + 2][j - 2] == 'A' and a[i + 3][j - 3] == 'S':
            sol += 1
        if a[i - 1][j - 1] == 'M' and a[i - 2][j - 2] == 'A' and a[i - 3][j - 3] == 'S':
            sol += 1
        if a[i - 1][j + 1] == 'M' and a[i - 2][j + 2] == 'A' and a[i - 3][j + 3] == 'S':
            sol += 1


print(sol)
