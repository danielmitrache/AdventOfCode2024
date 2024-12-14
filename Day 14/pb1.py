infile = open('input.txt', 'r')
lines = infile.readlines()
infile.close()
n, m = 103, 101
board = [[0 for _ in range(m)] for _ in range(n)]
c = [[0, 0], [0, 0]]
import re
for line in lines:
    line = line.strip().split()
    sp = re.findall(r'(-?\d+)', line[0])
    v = re.findall(r'(-?\d+)', line[1])
    sx, sy = int(sp[0]), int(sp[1])
    vx, vy = int(v[0]), int(v[1])

    finalx = (100 * vx + sx) % m
    finaly = (100 * vy + sy) % n
    if finalx < 0:
        finalx += m
    if finaly < 0:
        finaly += n
    if finalx != m//2 and finaly != n//2:
        c[finaly > n//2][finalx > m//2] += 1

sol = c[0][0] * c[1][1] * c[0][1] * c[1][0]
print(sol)