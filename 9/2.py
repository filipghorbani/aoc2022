def move(head, dir):
    if dir == 'U':
        head = (head[0], head[1]+1)
    elif dir == 'L':
        head = (head[0]-1, head[1])
    elif dir == 'D':
        head = (head[0], head[1]-1)
    elif dir == 'R':
        head = (head[0]+1, head[1])
    return head


def follow(head, tail):
    if head[0] - tail[0] > 1:
        tail = (tail[0]+1, tail[1])
        if(head[1] - tail[1] > 0):
            tail = (tail[0], tail[1]+1)
        elif(head[1] - tail[1] < 0):
            tail = (tail[0], tail[1]-1)
    elif head[0] - tail[0] < -1:
        tail = (tail[0]-1, tail[1])
        if(head[1] - tail[1] > 0):
            tail = (tail[0], tail[1]+1)
        elif(head[1] - tail[1] < 0):
            tail = (tail[0], tail[1]-1)
    elif head[1] - tail[1] > 1:
        tail = (tail[0], tail[1]+1)
        if(head[0] - tail[0] > 0):
            tail = (tail[0]+1, tail[1])
        elif(head[0] - tail[0] < 0):
            tail = (tail[0]-1, tail[1])
    elif head[1] - tail[1] < -1:
        tail = (tail[0], tail[1]-1)
        if(head[0] - tail[0] > 0):
            tail = (tail[0]+1, tail[1])
        elif(head[0] - tail[0] < 0):
            tail = (tail[0]-1, tail[1])
    return tail


input = open("9/input.txt", "r")
visited = set()
visited.add((0, 0))
head = (0, 0)
tails = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
         (0, 0), (0, 0), (0, 0), (0, 0)]


for line in input.readlines():
    line = line[:-1].split(' ')
    for i in range(int(line[1])):
        head = move(head, line[0])
        tails[0] = follow(head, tails[0])
        for i in range(1, 9):
            tails[i] = follow(tails[i-1], tails[i])
            visited.add(tails[8])

print(len(visited))
