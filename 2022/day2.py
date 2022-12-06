from read_input import read_input

lines = read_input("input2.txt")

loseOther: dict = { "A": "Z", "B": "X", "C": "Y" }
drawOther: dict = { "A": "X", "B": "Y", "C": "Z" }
winOther: dict = { "A": "Y", "B": "Z", "C": "X" }
moveDict: dict = { "X": loseOther, "Y": drawOther, "Z": winOther}
movePoints: dict = {"X": 1, "Y": 2, "Z": 3}
winLoseOrDrawPoints: dict = {"X": 0, "Y": 3, "Z": 6}

total_score = 0

for l in lines:
    other = l[0]
    winLoseOrDraw = l[2]
    mymove = moveDict[winLoseOrDraw][other]
    total_score += movePoints[mymove]
    total_score += winLoseOrDrawPoints[winLoseOrDraw]


print("My total score is " + str(total_score))
    