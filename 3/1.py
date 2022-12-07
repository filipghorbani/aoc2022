input = open("3/input.txt", "r")

sum = 0
for line in input.readlines():
    x = line[:len(line)//2]
    y = line[len(line)//2:]

    item = [item for item in x if item in y][0]
    sum += (ord(item)-38) if item.isupper() else (ord(item)-96)

print(sum)
