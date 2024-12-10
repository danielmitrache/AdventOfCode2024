infile = open('input.txt', 'r')
lines = infile.readlines()
infile.close()
map = [[int(c) for c in line.strip()] for line in lines]
n, m = len(map), len(map[0])
viz = [[False for j in range(m)] for i in range(n)]
startposs = []
for i in range(n):
    for j in range(m):
        if map[i][j] == 0:
            startposs.append((i, j))

sol = 0
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
def in_bounds(i, j):
    return (i >= 0) and (i < n) and (j >= 0) and (j < m)
def fill(i, j):
    if map[i][j] == 9:
        global sol
        sol += 1
        return
    for k in range(4):
        nexti, nextj = i + di[k], j + dj[k]
        if in_bounds(nexti, nextj) and map[nexti][nextj] == map[i][j] + 1 and not viz[nexti][nextj]:
            viz[nexti][nextj] = True
            fill(nexti, nextj)

for startpos in startposs:
    i, j = startpos
    viz = [[False for j in range(m)] for i in range(n)]
    fill(i, j)

print(sol)