import math
import random

def zadanie1():
    a = (math.e**4 - math.log(34, 2))**(1/3)
    print("Podpunkt a: ", round(a, 2))

    b = (math.log(20, 10) + math.cos(45) + math.e)**(1/3)
    print("Podpunkt b: ", round(b, 2))

    c = (math.log(20, 3) + math.sin(45) * (5/8))**(1/4)
    print("Podpunkt c: ", round(c, 2))

    d = math.log(23, 2) + (math.sin(34) + 5)**(1/3)
    print("Podpunkt d: ", round(d, 2))

    e = (math.log(32, 2) + math.pi + math.sin(56))**(1/4)
    print("Podpunkt e: ", round(e, 2))


def zadanie2():
    liczba_rzedow = int(input("Podaj liczbe rzedow dla wiezy: "))
    if liczba_rzedow <= 10:
        for i in range(liczba_rzedow+1):
            a = 'A'*i
            print(a)
    else:
        print("Podaj liczbe rzedow nie wieksza niz 10")


def zadanie3():
    liczba_rzedow = int(input("Podaj liczbe rzedow dla wiezy: "))
    if liczba_rzedow <= 10:
        for i in range(liczba_rzedow + 1):
            if i % 2 != 0:
                a = ' A' * i
                print(a.center(19))
            elif i % 2 == 0:
                a = ' A' * i
                print(a.center(20))
            else:
                print("Podaj liczbe rzedow nie wieksza niz 10")

def zadanie5():
    n = int(input("Podaja ilosc wierszy i kolumn: "))
    for i in range(n+1):
        b = ''
        c = 0
        for j in range(n+1):
            a = random.randint(0,9)
            b += '   ' + str(a)
            c += a
        print(f"{b}     Suma wiersza wynosi {c}")



def main():
    #print(zadanie1())
    #print(zadanie2())
    #print(zadanie3())
    print(zadanie5())

main()