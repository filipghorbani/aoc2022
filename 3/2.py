input = open("3/input.txt", "r").readlines()

sum = 0
for index, line in enumerate(input):
    if index % 3 == 0:
        items = [item for item in input[index] if item in input[index+1]]
        item = [item for item in items if item in input[index+2]][0]
        sum += (ord(item)-38) if item.isupper() else (ord(item)-96)

print(sum)
