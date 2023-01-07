input = open("10/input.txt", "r")
cycle = 1
reg = 1

def draw(cycle, reg):
    if abs(cycle - reg-1) < 2:
        print('#', end='')
    else:
        print('.', end='')
    if(cycle == 40):
        print('')
        return 0
    else:
        return cycle

for line in input.readlines():
    cycle = draw(cycle,reg)
    line = line[:-1].split(' ')
    if line[0] =="noop":
        cycle += 1
    elif line[0] == "addx":
        cycle += 1
        cycle = draw(cycle,reg)
        cycle += 1
        reg += int(line[1])
        