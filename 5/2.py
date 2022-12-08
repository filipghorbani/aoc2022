input = open("5/input.txt", "r")

moves = False
matrix = []
for line in input.readlines():
    if not moves:
        if line == "\n":
            moves = True
            matrix = [list(column) for column in zip(*matrix[:-1])]
            matrix = [[element for element in row if not element.isspace()] for row in matrix]
        else:
            matrix.append(list(line[1::4]))
    else:
        values = [int(s) for s in line.split() if s.isdigit()]
        for i in reversed(range(values[0])):
            matrix[values[2]-1].insert(0,matrix[values[1]-1].pop(i))
            
for row in matrix:
    print(row[0], end='')