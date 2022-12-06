input = open("2/1.txt", "r")

score = 0
for line in input.readlines():
    roundscore = ord(line[2]) - 87
    if (ord(line[0])-64) - (ord(line[2]) - 87) == 0:
        roundscore += 3
    if(ord(line[0])-64) - (ord(line[2]) - 87) in (-1, 2):
        roundscore += 6
    score += roundscore

print(score)
