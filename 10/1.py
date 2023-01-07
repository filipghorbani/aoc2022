input = open("10/input.txt", "r")
cycle = 1
sum = 0
reg = 1

cycles = [20,60,100,140,180,220]

def checkCycle(cycle, reg):
    if (cycle+20)%40 == 0:
        return cycle*reg
    else:
        return 0

for line in input.readlines():
    sum += checkCycle(cycle,reg)
    line = line[:-1].split(' ')
    if line[0] =="noop":
        cycle += 1
    elif line[0] == "addx":
        cycle += 1
        sum += checkCycle(cycle,reg)
        cycle += 1
        reg += int(line[1])
print(sum)
        