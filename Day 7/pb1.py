infile = open("input.txt", "r")
lines = infile.readlines()
infile.close()

def gen_combinations(n):
    if n == 0:
        return [[]]
    if n == 1:
        return [[0], [1]]
    return [[0] + x for x in gen_combinations(n-1)] + [[1] + x for x in gen_combinations(n-1)]

def myeval(operanzi: list, operatori: list) -> int:
    rezultat = operanzi[0]
    for i in range(1, len(operanzi)):
        if operatori[i - 1] == 0:
            rezultat += operanzi[i]
        else:
            rezultat *= operanzi[i]
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