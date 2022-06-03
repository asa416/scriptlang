from calendar import c
from re import I
from dice import *

class Configuration:

    configs = [
        "Categoty", "Ones", "Twos", "threes", "Fours", "Fives", "Sixes",
        "Upper Scores", "Upper Bonus(35)",
        "3 of a kind", "4 of a kind", "Full House(25)",
        "Small Straight(30)", "Large Straight(40)", "Yahtzee(50)", "Chance",
        "Lower Scores", "Total"
    ]

    @staticmethod
    def getConfigs():       # 정적 메소드 (객체 없이 사용 가능)
        return Configuration.configs

    # row에 따라 주사위 점수를 계산하여 반환. 
    # 예를 들어, row가 0이면 "Ones"가, 2이면 "Threes"가 채점되어야 함을 의미. 
    # row가 득점위치가 아닌 곳(즉, UpperScore, UpperBonus, LowerScore, Total 등)을 나타내는 경우 -1을 반환.
    @staticmethod
    def score(row, dices):       # 정적 메소드 (객체 없이 사용 가능)
        if row == 6 or row == 7 or row == 15 or row == 16:
            return -1

        score = 0

        if row == 0 or row == 1 or row == 2 or row == 3 or row == 4 or row == 5:
            for dice in dices:
                if dice.getRoll() == row+1:
                    score += row+1
            return score

        if row == 8:
            checkingList = [0] * 6
            checking = False
            for dice in dices:
                checkingList[dice.getRoll() - 1] += 1
                score += dice.getRoll()
            for i in checkingList:
                if i == 3:
                    checking = True
                    break
            if checking:
                return score
            else:
                return 0

        if row == 9:
            checkingList = [0] * 6
            checking = False
            for dice in dices:
                checkingList[dice.getRoll() - 1] += 1
                score += dice.getRoll()
            for i in checkingList:
                if i == 4:
                    checking = True
                    break
            if checking:
                return score
            else:
                return 0

        if row == 10:
            checkingSet = set()
            checkingList = []
            for dice in dices:
                checkingSet.add(dice.getRoll())
                checkingList.append(dice.getRoll())
            if len(checkingSet) != 2:
                return score
            if checkingList[1] == checkingList[3]:
                return 25
                
        if row == 11:
            checking = set()
            for dice in dices:
                checking.add(dice.getRoll())
            if checking & {1, 2, 3, 4} == {1, 2, 3, 4} or checking & {2, 3, 4, 5} == {2, 3, 4, 5} or checking & {3, 4, 5, 6} == {3, 4, 5, 6}:
                score = 30
            return score

        if row == 12:
            checking = []
            for dice in dices:
                checking.append(dice.getRoll())
                checking.sort()
            if checking == [1, 2, 3, 4, 5] or checking == [2, 3, 4, 5, 6]:
                score = 40
            return score
        
        if row == 13:
            checkdice = dices[0].getRoll()
            for i, dice in enumerate(dices):
                if i == 0:
                    continue
                if checkdice != dice.getRoll():
                    break
            else:
                score = 50
            return score
        
        if row == 14:
            for dice in dices:
                score += dice.getRoll()
            return score

