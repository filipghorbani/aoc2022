input = open("4/input.txt", "r")

pairs = 0
for line in input.readlines():
    x = line.split('\n')[0]
    x = [i.split('-') for i in x.split(',')]

    a = range(int(x[0][0]), int(x[0][1])+1)
    b = range(int(x[1][0]), int(x[1][1])+1)
    if [o for o in a if o in b]:
        pairs += 1

print(pairs)
