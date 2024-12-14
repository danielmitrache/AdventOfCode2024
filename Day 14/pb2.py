infile = open('input.txt', 'r')
lines = infile.readlines()
infile.close()
n, m = 103, 101
import re
startposs = []
velocities = []
for line in lines:
    line = line.strip().split()
    sp = re.findall(r'(-?\d+)', line[0])
    v = re.findall(r'(-?\d+)', line[1])
    sx, sy = int(sp[0]), int(sp[1])
    vx, vy = int(v[0]), int(v[1])

    startposs.append((sx, sy))
    velocities.append((vx, vy))

outfile = open('output.txt', 'w')
def printboard(board, i):
    outfile.write(f'Step: {i}\n')
    for row in board:
        outfile.write(''.join(['#' if x else ' ' for x in row]))
        outfile.write('\n')

for i in range(10000):
    board = [[0 for _ in range(m)] for _ in range(n)]
    u = len(startposs)
    for j in range(len(startposs)):
        sx, sy = startposs[j]
        vx, vy = velocities[j]

        finalx = (i * vx + sx) % m
        finaly = (i * vy + sy) % n
        if finalx < 0:
            finalx += m
        if finaly < 0:
            finaly += n

        board[finaly][finalx] += 1
        if board[finaly][finalx] == 2:
            u -= 1

    if u > len(startposs) - 3:
        printboard(board, i)



outfile.close()
