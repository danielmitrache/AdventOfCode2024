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

def checkCorectOrder(l: list) -> bool:
    for ii in range(len(l) - 1, 0, -1):
        for jj in range(ii - 1, -1, -1):
            if (l[jj], l[ii]) not in manual and (l[ii], l[jj]) in manual:
                return False
    return True

sol = 0
for pagelist in pages:
    if checkCorectOrder(pagelist):
        continue
    while not checkCorectOrder(pagelist):
        for i in range(len(pagelist) - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                if (pagelist[j], pagelist[i]) not in manual and (pagelist[i], pagelist[j]) in manual:
                    pagelist[j], pagelist[i] = pagelist[i], pagelist[j]
    sol += pagelist[len(pagelist) // 2]

print(sol)