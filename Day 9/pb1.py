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

end = len(memory) - 1
for i in range(len(memory)):
    if i >= totalspace:
        break
    if memory[i] == '.':
        memory[i], memory[end] = memory[end], memory[i]
        while memory[end] == '.':
            end -= 1

sol = 0
for i in range(totalspace):
    sol += i * memory[i]

print(sol)
