'''text = 'add,1,2,3,4,5/delete,1/showall'
textSplit = text.split('/')
print(textSplit)
for line in textSplit:
    comanda = line.split(',')
    if comanda[0] == 'add':
        print(comanda[1], comanda[2], comanda[3], comanda[4], comanda[5])
    elif comanda[0] == 'delete':
        print('Ai ales sa stergi')
    elif comanda[0] == 'showall':
        print('Ai ales sa afisezi')
'''
from Domain.Obiect import toString
from Logic.CRUD import adaugareObiect, stergereObiect

'''lista = []
lista = adaugareObiect('1', "stilou", "italian", 10, "Roma", lista)
lista = adaugareObiect('2', "pix", "italian", 5, "Roma", lista)'''


def help():
    print('Meniul contine comenzi de tip add,delete,showall'
          'ce trebuie separate prin "," sau "/".Mai jos'
          'aveti exemple de folosire a meniului')
    print("add,id,titlu,gen,pret,tipReducere")
    print("delete,id")
    print("showall")
    print("stop")


def UIShowAll(lista):
    for obiect in lista:
        print(toString(obiect))


def UIAdd(ID, nume, descriere, pretAchizitie, locatie, lista):
    try:
        lista = adaugareObiect(ID, nume, descriere, pretAchizitie, locatie, lista)
        return lista
    except ValueError as ve:
        print("Eroare:{}".format(ve))
        return lista


def UIDelete(ID, lista):
    try:
        lista = stergereObiect(ID, lista)
        return lista
    except ValueError as ve:
        print("Eroare:{}".format(ve))
        return lista


def runMeniu2(lista):
    ok = True
    while ok:
        help()
        text = input('Introduceti comenzi:')
        textSplit = text.split('/')
        for line in textSplit:
            comand = line.split(',')
            if comand[0] == 'add':
                lista = UIAdd(comand[1], comand[2], comand[3], comand[4], comand[5], lista)
            elif comand[0] == 'delete':
                lista = UIDelete(comand[1], lista)
            elif comand[0] == 'showall':
                UIShowAll(lista)
            elif comand[0] == 'stop':
                ok = False
