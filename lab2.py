import sys as system

def zadanie1():
    zdanie = input('Podaj zdanie: ')
    ilosc_slow = len(zdanie.split())
    print(ilosc_slow)

def zadanie2():
    system.stdout.write("podaj 3 liczby calkowite: ")
    a = int(system.stdin.readline())
    b = int(system.stdin.readline())
    c = int(system.stdin.readline())
    x = a**b + c
    system.stdout.write(str(x))

def zadanie3():
    a = input('Podaj slowo: ')
    b = a[::-1]
    if a == b:
        print("palindrom")
    else:
        print('nie palindrom')

def zadanie4():
    a = int(input('Podaj liczbe: '))
    if a/1==a and a/a==a:
        print('liczba pierwsza')
    elif a == 0:
        print('nie liczba pierwsza')
    else:
        print('nie liczba pierwsza')

def zadanie5():
    lista = []
    for i in range(1,1001):
        counter = 0
        for j in range(1,i):
            if i % j == 0:
                counter += j
        if counter == i:
            lista.append(i)
    print(lista)

def zadanie6():
    lista = [2, 2.5, 3, 10, 15.1, 20.4]
    lista2 = []
    for i in lista:
        lista2.append(i**2)
    print(lista2)

def zadanie7():
    lista = []
    counter = 0
    while counter < 10:
        a = int(input('Podaj liczbe: '))
        if a%2==0:
            lista.append(a)
        counter += 1
    print(lista)

def zadanie8():
    lista = [5, 'jablko', 'gruszka', 10, 'pomarancza', 3, 7]
    slownik = {}
    for i in lista:
        slownik[i] = lista.count(i)
    lista2 = []
    print(slownik)
    for i in slownik:
        if isinstance(i,str):
            lista2.append(i)
    for i in lista2:
        slownik.pop(i)
    print(slownik)



def main():
    #zadanie1()
    #zadanie2()
    #zadanie3()
    #zadanie4()
    #zadanie5()
    #zadanie6()
    #zadanie7()
    zadanie8()
main()