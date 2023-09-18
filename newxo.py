# -*- coding: utf-8 -*-
import random
import Util
import computerstep


while True:
    choise=input("Выберите крестиками или ноликами вы будете играть:")
    if choise!="X" and choise!="O":
        print("Введите X или O")
    else:
        if choise=="X":
            computerchoise="O"
        else:
            computerchoise="X"
        break
while True:
    mapsize=int(input("Введите размер поля:"))
    if mapsize<3 or mapsize>10:
        print("Введите число от 3 до 10")
    else:
        break

commonMap=Util.fillmap(mapsize)

Util.printmap2(commonMap)


while True:
    while True:
        x=int(input("Ваш ход по x:"))
        y=int(input("Ваш ход по y:"))
        if 0<=x<=mapsize and 0<=y<=mapsize:
            if (not Util.checkinput(x, y, commonMap)):
                print("Это место уже занято")
            else:
                break
        else:
            print("Ведите числа от 0 до"+mapsize)
    commonMap[x][y]=choise

    Util.printmap2(commonMap)

    # проверка
    if computerstep.isfull(commonMap,mapsize) == False:
        print("Ничья")
        exit()

    ret=computerstep.getHumanWinPos(commonMap, mapsize, choise, computerchoise)
    if ret!=None:
        (setx,sety)=ret
        commonMap[setx][sety]=computerchoise
        if computerstep.checkwinoncommonmap(commonMap,mapsize)!=None:
            answer=computerstep.checkwinoncommonmap(commonMap,mapsize)
            Util.printmap2(commonMap)
            print("Победил",answer)
            exit()
    else:
        (setx,sety)=computerstep.optimalCompStep(commonMap,mapsize,choise,computerchoise)
        commonMap[setx][sety]=computerchoise
        if computerstep.checkwinoncommonmap(commonMap,mapsize)!=None:
            answer=computerstep.checkwinoncommonmap(commonMap,mapsize)
            Util.printmap2(commonMap)
            print("Победил",answer)
            exit()

    Util.printmap2(commonMap)
