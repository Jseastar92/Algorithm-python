def score(dice):
    tri=[1000, 200, 300, 400, 500, 600]
    one=[100, 0, 0, 0, 50, 0]
    diceNum=[0,0,0,0,0,0]
    scr=int()

    for i in dice:
        diceNum[i-1] += 1

    for i in range(6):
        if diceNum[i] >= 3:
            scr += int(diceNum[i]/3) * tri[i]
            scr += diceNum[i]%3 * one[i]
        else :
            scr += diceNum[i] * one[i]
    return scr

score([2, 4, 4, 5, 4])

# # best
# def score(dice):
#   sum = 0
#   counter = [0,0,0,0,0,0]
#   points = [1000, 200, 300, 400, 500, 600]
#   extra = [100,0,0,0,50,0]
#   for die in dice:
#     counter[die-1] += 1
#
#   for (i, count) in enumerate(counter):
#     sum += (points[i] if count >= 3 else 0) + extra[i] * (count%3)
#
#   return sum
# 
# def score(dice):
#     return dice.count(1)//3 * 1000 + dice.count(1)%3 * 100 \
#            + dice.count(2)//3 * 200 \
#            + dice.count(3)//3 * 300 \
#            + dice.count(4)//3 * 400 \
#            + dice.count(5)//3 * 500 + dice.count(5)%3 * 50 \
#            + dice.count(6)//3 * 600 \
