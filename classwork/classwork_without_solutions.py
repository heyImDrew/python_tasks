"""1
Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию 
distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1) и (x2,y2).
Считайте четыре действительных числа и выведите результат работы этой функции.
Если вы не знаете, как решить эту задачу, то вы, возможно, не изучали в школе 
теорему Пифагора. Попробуйте прочитать о ней на Википедии. 
"""

def distance(x1, y1, x2, y2):
    return (abs(x1-x2)**2+abs(y1-y2)**2)**(1/2)


"""2
Дан список списков, где внутренний список состоит из двух элементов, 
координат x и y одной точки. Предположим, что каждая последующая точка соединена
с предыдущей. Написать функцию, которая будет вычислять общий путь из первой 
точки в последнюю
"""

def Way(dotList):
    sum = 0
    for dot in dotList:
        if dotList.index(dot)!=len(dotList)-1:
            sum+=distance( dot[0] ,dot[1], dotList[dotList.index(dot)+1][0], dotList[dotList.index(dot)+1][1])
        else: break
    return sum


"""3
модифицировать предыдущую функцию, чтобы она принимала необязательный аргумент 
is_closed=False. Если при вызове функции установить его в True - функция 
добавит к пути расстояние от последней точки до 1-й
"""

def modifiedWay(dotList, is_closed=False):
    sum = 0
    for dot in dotList:
        if dotList.index(dot)!=len(dotList)-1:
            sum+=distance( dot[0] ,dot[1], dotList[dotList.index(dot)+1][0], dotList[dotList.index(dot)+1][1])
        else: break
    sum+=distance(dotList[0][0],dotList[0][1],dotList[len(dotList)-1][0],dotList[len(dotList)-1][1])
    return sum


"""4
Написать функцию process_text(text, strip=True, capitalize=False, swap=False)
которая при установке соответствующего ключа - выполняет соответствующие операции
над переданной строкой и возвращает что получилось. ключи capitalize, swap, upper
и lower взаимоисключающие если больше одного из них True - возбудить исключение
"""


class MyException(Exception):
    def __init__(self,text):
        self.txt = text
def process_text(text, strip=True, capitalize=False, swap=False):
    if [strip, capitalize, swap].count(True)>=2:
        raise MyException("More than one argument is 'True'.")
    else:
        if strip==True:        text = text.strip()
        if capitalize==True:   text = text.capitalize()
        if swap==True:         text = text.swapcase()
    return text
    

"""5
Создайте программу, которая будет выводить все возможные комбинации при броске 2
игральных костей и сумму их значений. Пример вывода:
2: [(1, 1)]
3: [(1, 2), (2, 1)]
...
"""


from itertools import combinations as c
def dice():
    combinations = list(c([1,2,3,4,5,6],2))
    combinations.append((1,1))
    combinations.append((6,6))
    for sum in range(2,13):
        out = []
        for combination in combinations:
            if combination[0]+combination[1]==sum:
                out.append(combination)
                out.append(tuple(list(combination)[::-1]))
        print(f"{sum}: \t{out}")


"""6
Изменить функцию process_text так, чтобы ключи передавались в kwargs и 
выполнялись те операции, которые пришли в kwargs добавить upper и lower.
Ключи capitalize, swap, upper и lower взаимоисключающие если больше одного
из них True - возбудить исключение
"""


def modified_process_text(text, **kwargs):
    values = []
    for key, value in kwargs.items():
        if key in ('lower','upper', 'strip', 'capitalize', 'swap'):
            values.append(value)
    if values.count(True)>=2:
        raise MyException("More than one argument is 'True'.")
    else:
        for key in kwargs.keys():
            if str(key)=='strip' and kwargs.get(key)==True:         text = text.strip()
            if str(key)=='capitalize' and kwargs.get(key)==True:    text = text.capitalize()
            if str(key)=='swap' and kwargs.get(key)==True:          text = text.swapcase()
            if str(key)=='upper' and kwargs.get(key)==True:         text = text.upper()
            if str(key)=='lower' and kwargs.get(key)==True:         text = text.lower()
    return text


"""7
Разработать приложение, которое записывает в файл все строки, введенные 
пользователем. Признак конца ввода — пустая строка. Пример:

Введите имя файла: data.txt
Начните вводить строки
> one
> two
> three
>

Файл записан.
"""

def writeToFile():
    print("Write some strings:")
    lines = []
    text = ' '
    while text!='':
        text = input()
        lines.append(text)
    with open('text.txt','w') as file:
        for line in lines:
            file.write(line + '\n')
    print("File updated.")


"""8
Модифицировать предыдущую программу, так чтобы она нумеровала строки:
1 one
2 two
3 three
"""

def modified_writeToFile():
    print("Write some strings:")
    lines = []
    text = ' '
    while text!='':
        text = input()
        lines.append(text)
    with open('text.txt','w') as file:
        for line in lines:
            if line!='':
                file.write(f"{lines.index(line)+1}: {line}\n")
    print("File updated.")


"""9
Создать класс для часов. Должна быть возможность установить время при создании 
объекта. Также необходимо реализовать методы, с помощью которых можно добавлять 
по одной минуте/секунде или по одному часу к текущему времени. Помнить, что 
значения минут и секунд не могут превышать 59, а часов 23.
"""


class Clocks():
    def __init__(self,hours=0,minutes=0,seconds=0):
        self.h = hours
        self.m = minutes
        self.s = seconds
        if self.s>59:
            self.m+=self.s//60
            self.s=self.s%60
        if self.m>59:
            self.h+=self.m//60
            self.m=self.m%60
        if self.h>23:
            self.h=self.h%24
        self.HOURS = ''
        self.MINUTES = ''
        self.SECONDS = ''
    def toString(self):
        if self.h<10:   self.HOURS = '0'+str(self.h)
        else:           self.HOURS = str(self.h)
        if self.m<10:   self.MINUTES = '0'+str(self.m)
        else:           self.MINUTES = str(self.m)
        if self.s<10:   self.SECONDS = '0'+str(self.s)
        else:           self.SECONDS = str(self.s)
    def showtime(self):
        self.toString()
        print(f"Time is: {self.HOURS}:{self.MINUTES}:{self.SECONDS}")
    def add(self, h=0, m=0, s=0):
        self.h+=h
        self.m+=m
        self.s+=s


"""10
Создайте класс прямоугольник — Rectangle. Метод __init__ принимает две точки — 
левый верхний и правый нижний угол. Каждая точка представлена экземпляром класса 
Point. Реализуйте методы вычисления площади и периметра прямоугольника.
Добавьте в класс Rectangle метод has_point. Метод принимает точку на плоскости и 
возвращает True, если точка находится внутри прямоугольника и False в 
противном случае.
"""

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def returnCoordinats(self):
        return [self.x,self.y]

class Rectangle():
    def __init__(self, p1, p2):
        self.point1 = p1.returnCoordinats()
        self.point2 = p2.returnCoordinats()
        self.sqr = abs(self.point1[0]-self.point2[0])*abs(self.point1[1]-self.point2[1])
        self.per = (abs(self.point1[0]-self.point2[0])+abs(self.point1[1]-self.point2[1]))*2
    def returnSqr(self):
        return self.sqr
    def returnPer(self):
        return self.per
    def checkDot(self,dot):
        coord = dot.returnCoordinats()
        if (coord[0]>self.point1[0] and coord[0]<self.point2[0]) or (coord[0]>self.point2[0] and coord[0]<self.point1[0]):
            if (coord[1]>self.point1[1] and coord[1]<self.point2[1]) or (coord[1]>self.point2[1] and coord[1]<self.point1[1]):
                return True
            else: return False
        else: return False