input = open("4/input.txt", "r")

pairs = 0
for line in input.readlines():
    x = line.split('\n')[0]
    x = [i.split('-') for i in x.split(',')]

    if (int(x[0][0]) <= int(x[1][0]) and int(x[0][1]) >= int(x[1][1])) or (int(x[1][0]) <= int(x[0][0]) and int(x[1][1]) >= int(x[0][1])):
        pairs += 1

print(pairs)
