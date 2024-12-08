infile = open('input.txt', 'r')
lines = infile.readlines()
infile.close()

board = []
for line in lines:
    line = line.strip()
    l = []
    for ch in line:
        l.append(ch)
    board.append(l)

board_copy = board.copy()

from collections import deque


def in_bounds(i, j):
    return (i >= 0) and (i < len(board)) and (j >= 0) and (j < len(board[0]))


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
inf = 10 ** 9
lee = [[inf for _ in range(len(board[0]))] for _ in range(len(board))]


def find_path(istart, jstart, symbol, vs: set):
    viz = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    global lee
    lee = [[inf for _ in range(len(board[0]))] for _ in range(len(board))]
    q = deque()
    q.append((istart, jstart))
    viz[istart][jstart] = 1
    lee[istart][jstart] = 0
    while q:
        icurr, jcurr = q.popleft()
        if board[icurr][jcurr] == symbol and (icurr != istart or jcurr != jstart) and (icurr, jcurr) not in vs:
            return icurr, jcurr

        for k in range(4):
            inext, jnext = icurr + di[k], jcurr + dj[k]
            if in_bounds(inext, jnext) and not viz[inext][jnext] and lee[icurr][jcurr] + 1 < lee[inext][jnext]:
                viz[inext][jnext] = 1
                lee[inext][jnext] = lee[icurr][jcurr] + 1
                q.append((inext, jnext))
    return -1, -1


def reconstruct_path(ifin, jfin, lee) -> list:
    path_directions = []
    i, j = ifin, jfin
    while lee[i][j] != 0:
        for k in range(4):
            inext, jnext = i + di[k], j + dj[k]
            if in_bounds(inext, jnext) and lee[i][j] - 1 == lee[inext][jnext]:
                i, j = inext, jnext
                path_directions.append((di[k], dj[k]))
                break
    return path_directions


def print_lee(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == inf:
                print('X', end=' ')
            else:
                print(board[i][j], end=' ')
        print()


antenas = set()
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] not in '.#':
            for ii in range(len(board)):
                for jj in range(len(board[i])):
                    if board[ii][jj] == board[i][j] and (ii != i or jj != j):
                        antenas.add((ii, jj))
            visited_symbols = set()
            while True:
                ic, jc = i, j
                ifin, jfin = find_path(i, j, board[i][j], visited_symbols)
                if ifin == -1:
                    break
                visited_symbols.add((ifin, jfin))
                path = reconstruct_path(ifin, jfin, lee)
                while True:
                    for step in path:
                        ic += step[0]
                        jc += step[1]
                    if in_bounds(ic, jc) and (ic, jc) not in antenas:
                        antenas.add((ic, jc))
                    if not in_bounds(ic, jc):
                        break

print(len(antenas))