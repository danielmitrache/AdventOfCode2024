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
ADD = 10000000000000
for machine in machines:
    prize = machines[machine]['prize']
    prizeX = prize[0] + ADD
    prizeY = prize[1] + ADD

    buttonA = machines[machine]['A']
    buttonAX = buttonA[0]
    buttonAY = buttonA[1]

    buttonB = machines[machine]['B']
    buttonBX = buttonB[0]
    buttonBY = buttonB[1]

    # Sistem de ecuatii 2x2 => calculam determinantul si daca e diferit de 0 aplicam Cramer
    det = buttonAX * buttonBY - buttonAY * buttonBX
    if det == 0:
        continue

    # Cramer
    deltaA = prizeX * buttonBY - prizeY * buttonBX
    deltaB = buttonAX * prizeY - buttonAY * prizeX
    a = deltaA / det
    b = deltaB / det
    if a < 0 or b < 0 or a - int(a) != 0 or b - int(b) != 0:
        continue

    sol += int(a) * 3 + int(b)

print(sol)