input = open("1/input.txt", "r")

highestAmount = 0
currentamount = 0
for line in input.readlines():
    if line.strip():
        currentamount += int(line)
    else:
        highestAmount = max(highestAmount, currentamount)
        currentamount = 0
print(highestAmount)
