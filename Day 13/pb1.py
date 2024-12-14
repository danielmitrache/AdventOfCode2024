infile = open("input.txt", "r")
lines = infile.readlines()
infile.close()

lines = ''.join(lines)

import re

buttonA = re.findall(r'Button A: X\+(\d+), Y\+(\d+)', lines)
buttonB = re.findall(r'Button B: X\+(\d+), Y\+(\d+)', lines)
prize = re.findall(r'Prize: X=(\d+), Y=(\d+)', lines)

machines = {}
for i in range(len(buttonA)):
    machines[i] = {
        'A': (int(buttonA[i][0]), int(buttonA[i][1])),
        'B': (int(buttonB[i][0]), int(buttonB[i][1])),
        'prize': (int(prize[i][0]), int(prize[i][1]))
    }

sol = 0
max_pushes = 100
for machine in machines:
    prize = machines[machine]['prize']
    prizeX = prize[0]
    prizeY = prize[1]

    buttonA = machines[machine]['A']
    buttonAX = buttonA[0]
    buttonAY = buttonA[1]

    buttonB = machines[machine]['B']
    buttonBX = buttonB[0]
    buttonBY = buttonB[1]

    best = 100000
    for i in range(101):
        for j in range(101):
            AA = i * buttonAX + j * buttonBX
            BB = i * buttonAY + j * buttonBY
            if AA == prizeX and BB == prizeY:
                if 3 * i + j < best:
                    best = 3 * i + j
    if best < 100000:
        sol += best

print(sol)