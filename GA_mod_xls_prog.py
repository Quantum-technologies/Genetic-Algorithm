import xlrd
import numpy as np
import random
import math

def toBin(x):
    n = ""
    while x > 0:
        y = str(x % 2)
        n = y + n
        x = int(x / 2)
    return(n)

def firstGeneration(t):
    xmas = np.zeros(t)
    mas = xlrd.open_workbook('time_series.xls', formatting_info=True)
    sheet = mas.sheet_by_index(0)
    for rownum in range(sheet.nrows):
        row = sheet.row_values(rownum)
        for i in range(0, t, 1):
            xmas[i] = row[i]
    return(xmas)

def Crossover(timeSeries):
    newDesig = timeSeries
    c = t
    Childrens = np.zeros(c)
    Childrens = Childrens.astype(np.int, copy=False)
    while len(Childrens) != 1:
        c = c // 2
        Childrens = np.zeros(c)
        Childrens = Childrens.astype(np.int, copy = False)
        print(newDesig)
        for i in range(0, len(Childrens), 2):
            firstParent = toBin(newDesig[i])
            secondParent = toBin(newDesig[i+1])
            while len(secondParent) < 5:
                if len(firstParent) > len(secondParent): secondParent = '0' + secondParent
            while len(firstParent) < 5:
                if len(firstParent) < len(secondParent): firstParent = '0' + firstParent
            crossPoint = random.randrange(1, 4, 1)
            Child = firstParent[0: crossPoint - 1] + secondParent[crossPoint:]
            Childrens[i] = int(Child, 2)
        newDesig = Childrens
    return (newDesig)

t = 20 #размер выборки
iteration = 10 #количество итераций поиска
it = 0
timeSeries = firstGeneration(t)
timeSeries = timeSeries.astype(np.int, copy = False)
print(timeSeries)
desigions = np.zeros(10)

while t != iteration:
    desigions = Crossover(timeSeries)
    print(desigions)
    it += 1