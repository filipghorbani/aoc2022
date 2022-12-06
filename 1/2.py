input = open("1/1.txt", "r")

amounts = []
currentamount = 0
for line in input.readlines():
    if line.strip():
        currentamount += int(line)
    else:
        amounts.append(currentamount)
        currentamount = 0

amounts.sort(reverse=True)
print(sum(amounts[0:3]))
