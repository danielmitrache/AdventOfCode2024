def in_bounds(i, j):
    return 0 <= i < n and 0 <= j < m

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
def fill(i, j):
    # Numaram cati din cei 4 vecini sunt diferiti pentru a putea calcula perimetrul
    global perimetru, aria
    aria += 1
    for k in range(4):
        nexti, nextj = i + di[k], j + dj[k]
        if not in_bounds(nexti, nextj) or (in_bounds(nexti, nextj) and mat[nexti][nextj] != mat[i][j]):
            perimetru += 1

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
            perimetru = 0
            aria = 0
            fill(i, j)
            sol += aria * perimetru

print(sol)

