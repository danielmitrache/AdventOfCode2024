infile = open("input.txt", "r")
line = infile.readline()
infile.close()

line = list(map(int, line.strip().split()))
def count_digits(n: int) -> int:
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

def blink(l: list) -> list:
    tmp = []
    for i in range(len(l)):
        if l[i] == 0:
            tmp.append(1)
        elif count_digits(l[i]) % 2 == 0:
            p = count_digits(l[i]) // 2
            num1, num2 = l[i] // 10 ** p, l[i] % 10 ** p
            tmp.append(num1)
            tmp.append(num2)
        else:
            tmp.append(l[i] * 2024)
    return tmp

for i in range(75):
    line = blink(line)

print(len(line))