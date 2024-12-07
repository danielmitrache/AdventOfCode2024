infile = open("input.txt", "r")
lines = infile.readlines()
infile.close()

def gen_combinations(n):
    if n == 0:
        return [[]]
    smaller_lists = gen_combinations(n - 1)
    return [[0] + lst for lst in smaller_lists] + [[1] + lst for lst in smaller_lists] + [[2] + lst for lst in smaller_lists]

def myeval(operanzi: list, operatori: list) -> int:
    rezultat = operanzi[0]
    for i in range(1, len(operanzi)):
        if operatori[i - 1] == 0:
            rezultat += operanzi[i]
        elif operatori[i - 1] == 1:
            rezultat *= operanzi[i]
        else:
            rezultat = int(str(rezultat) + str(operanzi[i]))
    return rezultat

sol = 0
for line in lines:
    line = line.strip()
    line = line.split(":")
    rezultat = int(line[0].strip())
    operanzi = list(map(int, line[1].strip().split()))
    n = len(operanzi)
    for operatori in gen_combinations(n - 1):
        if myeval(operanzi, operatori) == rezultat:
            sol += rezultat
            break

print(sol)