infile = open("input.txt", "r")
lines = infile.readlines()
infile.close()

board = []
moves = []
robot_i, robot_j = 0, 0
for i, line in enumerate(lines):
    line = line.strip()
    r = []
    for j, ch in enumerate(line):
        r.append(ch)
        if ch == '@':
            robot_i = i
            robot_j = j
    board.append(r)

    if line.strip() == '':
        l = ''.join(lines[i+1:])
        for mv in l:
            if mv in "<>^v":
                moves.append(mv)
        break

def print_board(board):
    for r in board:
        print(''.join(r))

n, m = len(board), len(board[0])

def can_move(ri, rj, mv):
    if mv == '^':
        for i in range(ri - 1, -1, -1):
            if board[i][rj] == '#':
                return False
            elif board[i][rj] == '.':
                return (i, ri)
    if mv == 'v':
        for i in range(ri + 1, n):
            if board[i][rj] == '#':
                return False
            elif board[i][rj] == '.':
                return (i, rj)
    if mv == '>':
        for j in range(rj + 1, m):
            if board[ri][j] == '#':
                return False
            elif board[ri][j] == '.':
                return (ri, j)
    if mv == '<':
        for j in range(rj - 1, -1, -1):
            if board[ri][j] == '#':
                return False
            elif board[ri][j] == '.':
                return (ri, j)

def move(ri, rj, mv):
    if not can_move(ri, rj, mv):
        return (ri, rj)
    empty_i, empty_j = can_move(ri, rj, mv)
    match mv:
        case '^':
            for i in range(empty_i, ri):
                board[i][rj] = board[i + 1][rj]
            board[ri][rj] = '.'
            return (ri - 1, rj)
        case '>':
            for j in range(empty_j, rj, -1):
                board[ri][j] = board[ri][j - 1]
            board[ri][rj] = '.'
            return (ri, rj + 1)
        case 'v':
            for i in range(empty_i, ri, -1):
                board[i][rj] = board[i - 1][rj]
            board[ri][rj] = '.'
            return (ri + 1, rj)
        case '<':
            for j in range(empty_j, rj):
                board[ri][j] = board[ri][j + 1]
            board[ri][rj] = '.'
            return (ri, rj - 1)

for mv in moves:
    robot_i, robot_j = move(robot_i, robot_j, mv)

print_board(board)
sol = 0
for i in range(len(board) - 1):
    for j in range(len(board[0])):
        if board[i][j] == 'O':
            sol += i * 100 + j
print(sol)