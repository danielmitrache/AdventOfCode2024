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
        if ch != "#":
            l.append(ch)
        else:
            l.append('0')
        if ch == '^':
            istart = i
            jstart = j
    l.append('%')
    a.append(l)
a.append(['%'] * len(a[0]))

def print_map():
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()

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

def reset_map():
    for i in range(len(a) - 1):
        for j in range(len(a[i]) - 1):
            if a[i][j].isdigit():
                a[i][j] = '0'

def detect_infinite_cycle(i, j, directie):
    reset_map()
    d = directie
    while a[i][j] != '%':
        k = choose_k(d)
        newi, newj = i + di[k], j + dj[k]
        if a[newi][newj].isdigit():
            a[newi][newj] = str(int(a[newi][newj]) + 1)
            if a[newi][newj] == '5': #ciclu infinit gasit
                return True
            d = turn_right(d)
            continue
        else:
            i, j = newi, newj
    return False

sol = 0
for i in range(len(a) - 1):
    for j in range(len(a[i]) - 1):
        if i == istart and j == jstart or a[i][j].isdigit():
            continue

        a[i][j] = '0'
        if detect_infinite_cycle(istart, jstart, 'up'):
            sol += 1
        a[i][j] = '.'

print(sol)
