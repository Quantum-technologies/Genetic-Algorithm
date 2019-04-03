import random
import math
import numpy as np
import matplotlib.pyplot as plt

def toBin(x):
    n = ""
    while x > 0:
        y = str(x % 2)
        n = y + n
        x = int(x / 2)

    return(n)

def fitness(Gen):
    func =math.floor(10 +(math.sqrt(Gen) - 10*math.cos(2*math.pi*Gen)))  #Функция Растригина min(0, 0)
    #func = math.sqrt(Gen)
    return (func)

def FirstPopulation():
    print('Для генерации случайной популяции \n введите диапазон значений.')
    ValueFirst = int(input('от: '))
    ValueLast = int(input('до: '))
    for i in range(n):
        ArrPopulation.append(random.randint(ValueFirst, ValueLast))
    return (ArrPopulation)

def OKFunc(buf):
    newDesig = []
    for i in range(10):
        NumberOne = random.randrange(0,n,1)
        NumberTwo = random.randrange(0,n,1)
        firstGen = toBin(buf[NumberOne])
        secondGen = toBin(buf[NumberTwo])
        while len(firstGen) != len(secondGen):
            if len(firstGen) > len(secondGen):
                secondGen = '0'+ secondGen
            else:
                firstGen = '0' + firstGen
        Point = random.randrange(0, 2, 1)
        newGen=''
        for i in range(len(firstGen)):
            if i != Point:
                newGen += firstGen[i]
            else: newGen += secondGen[i]
        while len(newGen) < 4:
            newGen = '0' + newGen
        newDesig.append(int(newGen, 2))
    return (newDesig)


def Mutation(newDesig):
    forMut = newDesig
    for i in range(len(forMut)):
        gen = toBin(forMut[i])
        mutagen = ''
        while len(gen) != 4:
            gen = '0' + gen
        PointMut = random.randrange(0, len(gen), 1)
        if gen[PointMut] == '1':
            for i in range(len(gen)):
                if i != PointMut: mutagen += gen[i]
                else: mutagen += '0'
        else:
            for i in range(len(gen)):
                if i != PointMut: mutagen += gen[i]
                else: mutagen += '1'
        forMut[i] = int(mutagen, 2)
    return (forMut)

def Selection(Parents, NewDecisionMut): #селекция плохая
    NewDesig = []
    a = 0
    Old = Parents
    Young = sorted(NewDecisionMut)
    for i in range(n, 2*n):
        Young.append(Old[a])
        a += 1
    sorted(Young)
    for i in range(n):
        NewDesig.append(Young[i])
    return(NewDesig)


t0 = int(input('Введите число поколений: ')) #число поколений
n = int(input('Введите размер популяции: '))  #размер популяции
#m = int(input())  #размер популяции


t = 0 #начальное поколение
NewDecisions = [] #массив новых особей
NewDecisionMut = [] #одна новая особь
ArrPopulation = [] #готовая популяция

NewDecisions = FirstPopulation()


while t != t0:
    Parents = NewDecisions
    NewDecisions = []
    NewDecisions = OKFunc(Parents)
    NewDecisionsMut = Mutation(NewDecisions)
    goodDesig = Selection(Parents, NewDecisionsMut)
    print(goodDesig)
    goodnes = np.asarray(goodDesig, dtype=np.int)
    NewDecisions = NewDecisionsMut
    NewDecisionsMut = []
    goodDesig = []
    t += 1