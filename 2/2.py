input = open("2/input.txt", "r")

score = 0
x = [2, 0, 1, 2, 0]
for line in input.readlines():

    roundscore = (ord(line[2]) - 88) * 3

    if roundscore == 3:
        roundscore += ord(line[0])-64
    elif(roundscore == 0):
        roundscore += x[(ord(line[0])-64)-1]+1
    elif(roundscore == 6):
        roundscore += x[(ord(line[0])-64)+1]+1
    score += roundscore


print(score)
