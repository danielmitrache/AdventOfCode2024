infile = open('input.txt', 'r')
lines = infile.readlines()
infile.close()

manual, pages = [], []
for line in lines:
    if '|' in line:
        a, b = map(int, line.strip().split('|'))
        manual.append((a, b))
    elif line.strip() == '':
        continue
    else:
        v = list(map(int, line.strip().split(',')))
        pages.append(v)

sol = 0
for pagelist in pages:
    corectord = True
    for i in range(len(pagelist) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if (pagelist[j], pagelist[i]) not in manual and (pagelist[i], pagelist[j]) in manual:
                corectord = False
                break
    if corectord:
        print(pagelist)
        sol += pagelist[len(pagelist) // 2]

print(sol)