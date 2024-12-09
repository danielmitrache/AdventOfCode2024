infile = open("input.txt", "r")
line = infile.readline()
infile.close()

memory = []
d = 0
totalspace = 0
for i, ch in enumerate(line):
    if i % 2 == 0:
        memory.extend([d] * int(ch))
        totalspace += int(ch)
        d += 1
    else:
        memory.extend(['.'] * int(ch))

for i in range(d - 1, -1, -1):
    neededspace = memory.count(i)
    try:
        firstappearance = memory.index(i)
    except ValueError:
        firstappearance = -1
    for j in range(len(memory)):
        if j > firstappearance:
            break
        if memory[j] == '.':
            enoughspace = True
            for k in range(j, j + neededspace):
                if memory[k] != '.':
                    enoughspace = False
                    break
            if enoughspace:
                memory[memory.index(i):memory.index(i) + neededspace] = ['.'] * neededspace
                memory[j:j + neededspace] = [i] * neededspace
                break

sol = 0
for i in range(len(memory)):
    if memory[i] == '.':
        continue
    sol += i * memory[i]

print(sol)