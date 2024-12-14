def in_bounds(i, j):
    return 0 <= i < n and 0 <= j < m

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
def fill(i, j):
    # Pentru a numara cate laturi sunt, numaram colturile
    global nrl, aria

    aria += 1

    nrv = 0
    auxi, auxj = 0, 0
    for k in range(4):
        nexti, nextj = i + di[k], j + dj[k]
        if not in_bounds(nexti, nextj) or (in_bounds(nexti, nextj) and mat[nexti][nextj] != mat[i][j]):
            nrv += 1
            auxi += di[k]
            auxj += dj[k]

    if nrv == 3:
        nrl += 2 # Daca avem 3 vecini diferiti, avem 2 colturi => 2 laturi
    elif nrv == 2 and auxi != 0 and auxj != 0:
        nrl += 1 # Daca avem 2 vecini diferiti, avem 1 colt => 1 latura
    elif nrv == 4:
        nrl += 4

    if in_bounds(i, j + 1) and in_bounds(i + 1, j) and in_bounds(i + 1, j + 1):
        if mat[i][j + 1] == mat[i][j] and mat[i + 1][j] == mat[i][j] and mat[i + 1][j + 1] != mat[i][j]:
            nrl += 1
    if in_bounds(i, j - 1) and in_bounds(i + 1, j) and in_bounds(i + 1, j - 1):
        if mat[i][j - 1] == mat[i][j] and mat[i + 1][j] == mat[i][j] and mat[i + 1][j - 1] != mat[i][j]:
            nrl += 1
    if in_bounds(i, j + 1) and in_bounds(i - 1, j) and in_bounds(i - 1, j + 1):
        if mat[i][j + 1] == mat[i][j] and mat[i - 1][j] == mat[i][j] and mat[i - 1][j + 1] != mat[i][j]:
            nrl += 1
    if in_bounds(i, j - 1) and in_bounds(i - 1, j) and in_bounds(i - 1, j - 1):
        if mat[i][j - 1] == mat[i][j] and mat[i - 1][j] == mat[i][j] and mat[i - 1][j - 1] != mat[i][j]:
            nrl += 1

    viz[i][j] = 1
    for k in range(4):
        nexti, nextj = i + di[k], j + dj[k]
        if in_bounds(nexti, nextj) and not viz[nexti][nextj] and mat[nexti][nextj] == mat[i][j]:
            fill(nexti, nextj)


infile = open("input.txt", "r")
lines = infile.readlines()
infile.close()

mat = []
for line in lines:
    line = line.strip()
    l = []
    for ch in line:
        l.append(ch)
    mat.append(l)

n, m = len(mat), len(mat[0])
viz = [[0 for _ in range(m)] for _ in range(n)]
sol = 0
for i in range(n):
    for j in range(m):
        if not viz[i][j]:
            nrl = 0
            aria = 0
            fill(i, j)
            sol += aria * nrl

print(sol)