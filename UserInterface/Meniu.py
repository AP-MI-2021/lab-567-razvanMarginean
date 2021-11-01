from Domain.Obiect import toString
from Logic.CRUD import adaugareObiect, stergereObiect, modificareObiect
from Logic.Functionalitati import mutareInAltaLocatie, concatenareString


def UIConcatenareString(lista):
    string = input('Dati string:')
    valoare = float(input('Dati valoare:'))

    listaNoua = concatenareString(string, valoare, lista)

    return listaNoua

def  UIMutareInAltaLocatie(lista):
    locatieVeche = input('Introduceti locatia din care obiectul va fi mutat:')
    locatieNoua = input('Introduceti locatie in care obiectul va fi mutat:')

    listaNoua = mutareInAltaLocatie(locatieVeche, locatieNoua, lista)

    return listaNoua

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
    print('4.Mutare obiect dintr o locatie in alta')
    print('5.Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită')
    print('x.Iesire.')
    print('a.Show All.')

def showAll(lista):
    for obiect in lista:
        print(toString(obiect))

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
        elif optiune == '4':
            lista = UIMutareInAltaLocatie(lista)
        elif optiune == '5':
            lista = UIConcatenareString(lista)
        elif optiune == 'a':
            showAll(lista)
        elif optiune == 'x':
            break

