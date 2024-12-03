import re

infile = open('input.txt', 'r')
lines = infile.readlines()
infile.close()

sol = 0
for line in lines:
    muls = re.findall(r'mul\(\d{1,3},\d{1,3}\)', line)
    for mul in muls:
        nums = re.findall(r'\d{1,3}', mul)
        a, b = map(int, nums)
        sol += a * b

print(sol)
