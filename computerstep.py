# -*- coding: utf-8 -*-

import Util
# проверяет победил ли кто то из игроков на входе размер поля 3 на 3
def checkwin(map):
    count=0
    for i in range(3):
        rightchoise=None
        for c in range(3):
            if rightchoise==None:
                if map[i][c]!=" ":
                    rightchoise=map[i][c]
            if map[i][c]!=rightchoise:
                break
            count += 1
        if count==3:
            return rightchoise
        count=0
    count=0
    for i in range(3):
        rightchoise = None
        for c in range(3):
            if rightchoise == None:
                if map[c][i] != " ":
                    rightchoise = map[c][i]
            if map[c][i] != rightchoise:
                break
            count += 1
        if count == 3:
            return rightchoise
        count = 0
    rightchoise=None

    count=0
    for i in range(3):
        if rightchoise==None:
            if map[i][i]!=" ":
                rightchoise=map[i][i]
        if map[i][i]==rightchoise:
            count+=1
    if count==3:
        return rightchoise

    rightchoise = None
    count = 0
    for i in range(3):
        if rightchoise == None:
            if map[i][2-i] != " ":
                rightchoise = map[i][2-i]
        if map[i][2-i] == rightchoise:
            count += 1
    if count == 3:
        return rightchoise
    return None

# проверяет заполнено ли поле полностью.Работает с любым размером поля
def isfull(map,mapsize):
    answer=False
    for x in range(mapsize):
        for y in range(mapsize):
            if map[x][y]==" ":
                answer=True
                break
    return answer
# возвращяет ход,который надо сделать компьютеру.Работает на полном размере поля.Последовательно проверяет выигрышную позицию для себя и для пользователя.
def getHumanWinPos(commonMap, mapsize, choise, computerchoise):
    for xb in range(mapsize-2):
        for yb in range(mapsize-2):
            smallMap=Util.fillmap(3)
            for x in range(3):
                for y in range(3):
                    smallMap[x][y]=commonMap[x + xb][y + yb]
            if findHumanWinPosition3x3(smallMap, choise, computerchoise) != None:
                (setx, sety) = findHumanWinPosition3x3(smallMap, choise, computerchoise)
                return (setx+xb,sety+yb)
    for xb in range(mapsize - 2):
        for yb in range(mapsize - 2):
            smallMap = Util.fillmap(3)
            for x in range(3):
                for y in range(3):
                    smallMap[x][y] = commonMap[x + xb][y + yb]
            if findHumanWinPosition3x3block(smallMap, choise, computerchoise) != None:
                (setx, sety) = findHumanWinPosition3x3block(smallMap, choise, computerchoise)
                return (setx + xb, sety + yb)
    return None


# ищет оптимальный ход для компьютера(высчитывает победный ход для компьютера).работает с полем 3 на 3.Эффетивно только на заполненном поле.
def findHumanWinPosition3x3(map, choise, computerchoise):
    for x in range(3):
        row=map[x]
        for y in range(3):
            if row[y]!=choise and row[y]!=computerchoise:
                row[y]=computerchoise
                if checkwin(map)==computerchoise:
                    row[y]=" "
                    return (x, y)
                else:
                    row[y]=" "
    return None
# ищет оптимальный ход для компьютера(блокирует победу человека).работает с полем 3 на 3.Эффетивно только на заполненном поле.

def findHumanWinPosition3x3block(map, choise, computerchoise):
    for x in range(3):
        row = map[x]
        for y in range(3):
            if row[y] == " ":
                row[y] = choise
                if checkwin(map) == choise:
                    row[y] = " "
                    return (x, y)

                else:
                    row[y] = " "

    return None
#ищет победил ли кто то. Работает со всем размером поля, возвращает X или О
def checkwinoncommonmap(commonMap,mapsize):
    for xb in range(mapsize-2):
        for yb in range(mapsize-2):
            smallMap=Util.fillmap(3)
            for x in range(3):
                for y in range(3):
                    smallMap[x][y]=commonMap[x + xb][y + yb]
            if checkwin(smallMap)!=None:
                return checkwin(smallMap)
    return None
# подсчитывает количество сделанных человеком ходов. Работает на полном поле
def amountOfXO(commonMap,mapsize,choise,computerchoise):
    countO=0
    countX=0
    for ix in range(mapsize):
        for iy in range(mapsize):
            if commonMap[ix][iy]==choise:
                countX+=1
            elif commonMap[ix][iy]==computerchoise:
                countO+=1
    return(countX,countO)
# высчитывает оптимальных ход для компьютер, если человека не надо блокировать или побеждать самому
def optimalCompStep(commonMap,mapsize,choise,computerchoise):
    (iCntChoise,iCntCompChoise)=amountOfXO(commonMap,mapsize,choise,computerchoise)
    if iCntChoise==1:
        center=mapsize//2
        if commonMap[center][center]!=" ":
            return (center-1,center)
        else:
            return(center,center)
    elif iCntChoise>=2:
        for x in range(mapsize):
            for y in range(mapsize):
                if commonMap[x][y]==computerchoise:
                    xpos=x
                    ypos=y
        for x in range(mapsize):
            for y in range(mapsize):
                if xpos-1<=x<=xpos+1 and ypos-1<=y<=ypos+1:
                    if commonMap[x][y]==" ":
                        return(x,y)





