"""1
Написать функцию fill(n, filename)
n - целое число
filename - строка, имя файла
Функция должна n раз взять случайный символ от 'a' до 'z', продублировать его
случайное (от 2 до 9) количество раз, и все эти символы склеить в одну строку
и записать в файл. Если новый символ такой же как предыдущий - нужно взять новый.

Примечания:
Используйте функцию ord('a') для получения численного значения кода символа
Используйте функцию chr(97) для получения символа по коду

Пример содержимого файла для n = 10:

xxxxxffffddddddddiiiiieeeeeeeeeeyyyywwwwwwwwwwvvvvvvjjlll
"""


from string import ascii_lowercase
import random
def fill(n, filename):
    with open (f"{filename}.txt", "w") as file:
        letters = [letter for letter in ascii_lowercase]
        for _ in range(n):
            letter = random.choice(letters)
            number = random.randrange(2,9,1)
            for  _ in range(number):
                file.write(letter)


"""2
Написать функцию encode(in_filename, out_filename)
in_filename - входной файл
out_filename - выходной файл
Функция должна заменять все последовательности повторяющихся символов из
in_filename на <число_повторов><символ>. Склеивать в одну строку и записывать в
out_filename

Пример содержимого для out_filename:

5x4f8d5i10e4y10w6v2j3l
"""


def encode(in_filename, out_filename):
    with open (f"{in_filename}.txt","r") as file_1:
        letters = [letter for letter in file_1.read()]
        unique = list(dict.fromkeys(letters).keys())
        with open (f"{out_filename}.txt","w") as file_2:
            for letter in unique:
                file_2.write(str(letters.count(letter)) + letter)


"""3
Написать функцию decode(in_filename, out_filename)
Функция должна привести результат действия функции encode к исходной строке
"""

def decode(in_filename, out_filename):
     with open (f"{in_filename}.txt","r") as file_1:
        string = [letter for letter in file_1.read()]
        listofletters = [string[i:i+2] for i in range(0,len(string),2)]
        with open (f"{out_filename}.txt","w") as file_2:
            for pair in listofletters:
                file_2.write(pair[1]*int(pair[0]))

"""4
Сгенерировать матрицу NxN из случайных целых чисел
"""


def matrix(N):
    return [[random.randrange(0,9,1) for _ in range(N)] for num in range(N)]

"""5
Вернуть строку и столбец с максимальными суммами элементов
"""
def linesum(line):
    sum = 0
    for element in line:
        sum += element
    return sum

def getmax(matr):
    N = len(matr)
    columns = [[line[i] for line in matr] for i in range(N)]
    for line in matr:
        if matr.index(line)==0:
            maxline = line
        else:
            if linesum(line) > linesum(maxline): 
                maxline = line
    for column in columns:
        if columns.index(column)==0: 
            maxcolumn = column
        else:
            if linesum(column) > linesum(maxcolumn): 
                maxcolumn = column
    return (maxline, maxcolumn)