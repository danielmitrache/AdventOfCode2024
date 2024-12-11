infile = open("input.txt", "r")
line = infile.readline()
infile.close()

line = list(map(int, line.strip().split()))
from collections import defaultdict
stones = defaultdict(int)
for stone in line:
    stones[stone] += 1

def count_digits(n: int) -> int:
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

def blink(d):
    tmp = defaultdict(int)
    for stone in d.keys():
        if stone == 0:
            tmp[1] += d[stone]
        elif count_digits(stone) % 2 == 0:
            p = count_digits(stone) // 2
            num1, num2 = stone // 10 ** p, stone % 10 ** p
            tmp[num1] += d[stone]
            tmp[num2] += d[stone]
        else:
            tmp[stone * 2024] += d[stone]
    return tmp

for i in range(75):
    stones = blink(stones)

print(sum(stones.values()))