line = open("6/input.txt", "r").readline()

for i in range(len(line)):
    l = line[i:i+14]
    if len(set(l)) == len(l):
        print(i+14)
        break