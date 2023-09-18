# -*- coding: utf-8 -*-
import colorama
# каждый раз заполняет поле ходом
def fillmap(mapsize):
    commonmap=[]
    for i in range(mapsize):
        commonmap.append([])
        for j in range(mapsize):
            commonmap[i].append(" ")
    return commonmap
# проверяет ввод
def checkinput(x,y,map):
    if map[x][y]=="X"or map[x][y]=="O":
        return False
    else:
        return True
# каждый раз вырисовывает поле
def printmap2(map):
    strheader=' '
    for e in range(len(map)):
        e=str(e)
        strheader=strheader+' '+e
    strheader = "\x1b[42m" + strheader + " "+"Y" + "\x1b[30m"
    print(strheader)
    for i in range(len(map)):
        str2=""
        row=map[i]

        for c in range(len(map)):
            if row[c]=="X":
                str2=str2+"\x1b[31m"+row[c]+"\x1b[30m"
            elif row[c]=="O":
                str2 = str2 + "\x1b[32m" + row[c] + "\x1b[30m"
            else:
                str2=str2+row[c]
            str2=str2+"\x1b[37m"+"|"+"\x1b[0m"
        str2="\x1b[42m"+"\x1b[37m"+str(i)+"\x1b[0m"+"\x1b[37m"+"|" +"\x1b[0m"+str2+"\x1b[42m"+' '+"\x1b[30m"
        print(str2)
    strfooter=''
    for c in range(len(map)*2):
        strfooter = strfooter + ' '
    strfooter = "\x1b[42m" + "\x1b[37m"+"X" + strfooter + "  " + "\x1b[30m"+"\x1b[0m"
    print(strfooter)


