infile = open('input.txt', 'r')
lines = infile.readlines()
infile.close()

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

a = []
istart, jstart = 0, 0
for i, line in enumerate(lines):
    line = line.strip()
    l = []
    for j, ch in enumerate(line):
        l.append(ch)
        if ch == '^':
            istart = i
            jstart = j
    l.append('0')
    a.append(l)
a.append(['0'] * len(a[0]))

def choose_k(directie):
    match directie:
        case 'up':
            return 2
        case 'right':
            return 1
        case 'down':
            return 0
        case 'left':
            return 3
        case _:
            return None

def turn_right(directie):
    match directie:
        case 'up':
            return 'right'
        case 'right':
            return 'down'
        case 'down':
            return 'left'
        case 'left':
            return 'up'
        case _:
            return None

def walk(i, j, directie):
    sol = 0
    d = directie
    while a[i][j] != '0':
        if a[i][j] in '.^':
            sol += 1
        a[i][j] = 'X'
        k = choose_k(d)
        if a[i + di[k]][j + dj[k]] == '#':
            d = turn_right(d)
            continue
        elif a[i + di[k]][j + dj[k]] in '.X0':
            i += di[k]
            j += dj[k]
    return sol

sol = walk(istart, jstart, 'up')
print(sol)