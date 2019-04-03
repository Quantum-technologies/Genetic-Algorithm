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
    #func = Gen**2
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
    for i in range(n):
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
    Old = sorted(Parents)
    Young = sorted(NewDecisionMut)
    for i in range(n):
        if fitness(Young[i]) < fitness(Old[i]):
            NewDesig.append(Young[i])
        else:
            NewDesig.append(Old[i])
    return(NewDesig)

def forPlot(goodnes):
    x = goodnes  # Массив значений аргумента
    plt.plot(x, fitness(x))  # Построение графика
    plt.xlabel(r'$x$')  # Метка по оси x в формате TeX
    plt.ylabel(r'$f(x)$')  # Метка по оси y в формате TeX
    plt.title(r'$y=x^2$')  # Заголовок в формате TeX
    plt.grid(True)  # Сетка
    plt.show() # Показать график


t0 = int(input('Введите число поколений: ')) #число поколений
n = int(input('Введите размер популяции: '))  #размер популяции
#m = int(input())  #размер популяции


t = 0 #начальное поколение
NewDecisions = [] #массив новых особей
NewDecisionMut = [] #одна новая особь
ArrPopulation = [] #готовая популяция

NewDecisions = FirstPopulation()
tik = 0

while t != t0:
    Parents = NewDecisions
    NewDecisions = []
    NewDecisions = OKFunc(Parents)
    NewDecisionsMut = Mutation(NewDecisions)
    goodDesig = Selection(Parents, NewDecisionsMut)
    #print('Родители - ', sorted(Parents))
    #print('Дети - ', sorted(NewDecisions))
    #print('Мутанты - ', sorted(NewDecisionsMut))
    print('Поколение №', t, goodDesig, sum(goodDesig))
    if sum(goodDesig) == sum(Parents): tik += 1
    else: tik = 0
    #goodnes = np.asarray(goodDesig, dtype=np.int)
    #forPlot(goodnes)
    NewDecisions = goodDesig
    NewDecisionsMut = []

    if tik == 10000:
        print('Нет изменений в поколениях \n Решение найдено за ', t - tik,' поколений')
        print('Экстренум функции лежит в точке(', goodDesig[0],',', fitness(goodDesig[0]), ')')
        break
    goodDesig = []
    t += 1

