line = open("6/input.txt", "r").readline()

for i in range(len(line)):
    l = line[i:i+4]
    if len(set(l)) == len(l):
        print(i+4)
        break