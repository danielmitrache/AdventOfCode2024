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
    if m == -1:
        m = len(l)
    l.append('X')
    a.append(l)

a.append(['X'] * (m + 1))

sol = 0
for i in range(n):
    for j in range(m):
        if a[i][j] != 'A':
            continue

        if (ord(a[i - 1][j - 1]) + ord(a[i + 1][j + 1])) == (ord(a[i - 1][j + 1]) + ord(a[i + 1][j - 1])) == 160:
            sol += 1

print(sol)