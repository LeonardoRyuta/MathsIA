valuesTable = [
    ['n', 't', 'd'],
    [0, 0, 2.2]
]
dvdt = -9.81
h = 0.00001
counter = 1

while True:
    if counter == 100001:
        break

    n = valuesTable[counter][0]
    t = valuesTable[counter][1]
    d = valuesTable[counter][2]

    newT = t + h
    newD = d + h * (dvdt * t)
    newN = n + 1

    valuesTable.append([newN, newT, newD])

    counter += 1

    if (newD < 0):
        break

f = open("valuesTable2.txt", "w")

for p in range(len(valuesTable)):
    f.write(str(valuesTable[p]) + '\n')
