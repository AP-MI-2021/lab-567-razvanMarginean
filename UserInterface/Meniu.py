from Domain.Obiect import toString
from Logic.CRUD import adaugareObiect, stergereObiect, modificareObiect


def UIModificareObiect(lista):
    ID = input('Dati ID-ul:')
    nume = input('Dati numele:')
    descriere = input('Dati descriere:')
    pretAchizitie = input('Dati pret achizitie:')
    locatie = input('Dati locatie:')
    return modificareObiect(ID, nume, descriere, pretAchizitie, locatie, lista)

def UIStergereObiect(lista):
    ID = input('Dati ID:')
    return stergereObiect(ID, lista)

def UIAdaugareObiect(lista):
    #ID, nume, descriere, pretAchizitie, locatie
    ID = input('Dati ID-ul:')
    nume = input('Dati numele:')
    descriere = input('Dati descriere:')
    pretAchizitie = input('Dati pret achizitie:')
    locatie = input('Dati locatie:')
    return adaugareObiect(ID, nume, descriere, pretAchizitie, locatie, lista)

def Meniu():
    print("1.Adaugare Obiect.")
    print('2.Stergere obicet.')
    print('3.Modificare obiect.')
    print('x.Iesire.')
    print('a.Afisare Obiect.')

def showAll(lista):
    for prajitura in lista:
        print(toString(prajitura))

def runMeniu(lista):
    while True:
        Meniu()
        optiune = input('Selectati optiune:')
        if optiune == '1':
            lista = UIAdaugareObiect(lista)
        elif optiune == '2':
            lista = UIStergereObiect(lista)
        elif optiune == '3':
            lista = UIModificareObiect(lista)
        elif optiune == 'a':
            showAll(lista)
        elif optiune == 'x':
            break

