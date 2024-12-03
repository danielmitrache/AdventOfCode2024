import re

infile = open('input.txt', 'r')
lines = infile.readlines()
infile.close()

canDoMul = True
sol = 0
for line in lines:
    operations = re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', line)
    for operation in operations:
        if operation == 'do()':
            canDoMul = True
        elif operation == "don't()":
            canDoMul = False
        elif canDoMul:
            nums = re.findall(r'\d{1,3}', operation)
            a, b = map(int, nums)
            sol += a * b

print(sol)