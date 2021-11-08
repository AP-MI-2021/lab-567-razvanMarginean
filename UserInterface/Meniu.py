from Domain.Obiect import toString
from Logic.CRUD import adaugareObiect, stergereObiect, modificareObiect
from Logic.Functionalitati import mutareInAltaLocatie, concatenareString, CelMaiMarePret, OrdonareCrescDupaPret, \
    SumePreturiPtLocatie


def UISumePreturiPtLocatie(lista):
    dict = SumePreturiPtLocatie(lista)
    for nume in dict:
        print('Pentru numele {}, suma preturilor este {}'.format(nume, dict[nume]))

def UICelMaiMarePret(lista):
    rezultat = CelMaiMarePret(lista)
    for locatie in rezultat:
        print("Pentru locatia:{} cel mai mare pret il contine obiectul"
              ": {}".format(locatie, toString(rezultat[locatie])))

def UIConcatenareString(lista):
    try:
        string = input('Dati string:')
        valoare = float(input('Dati valoare:'))

        listaNoua = concatenareString(string, valoare, lista)

        return listaNoua
    except ValueError as ve:
        print("Eroare:{}".format(ve))
        return lista


def  UIMutareInAltaLocatie(lista):
    try:
        locatieVeche = input('Introduceti locatia din care obiectul va fi mutat:')
        locatieNoua = input('Introduceti locatie in care obiectul va fi mutat:')

        if len(locatieNoua) != 4:
            raise ValueError("Locatia introdusa trebuie sa contina exact 4 caractere")

        listaNoua = mutareInAltaLocatie(locatieVeche, locatieNoua, lista)

        return listaNoua
    except ValueError as ve:
        print("Eroare:{}".format(ve))
        return lista
def UIModificareObiect(lista, undoList, redoList):
    try:
        ID = input('Dati ID-ul:')
        nume = input('Dati numele:')
        descriere = input('Dati descriere:')
        pretAchizitie = float(input('Dati pret achizitie:'))
        locatie = input('Dati locatie:')
        if len(locatie) != 4:
            raise ValueError("Locatia introdusa trebuie sa contina exact 4 caractere")
        rezultat = modificareObiect(ID, nume, descriere, pretAchizitie, locatie, lista)

        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare:{}".format(ve))
        return lista

def UIStergereObiect(lista, undoList, redoList):
    try:
        ID = input('Dati ID:')
        rezultat = stergereObiect(ID, lista)

        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare:{}".format(ve))
        return lista

def UIAdaugareObiect(lista, undoList, redoList):
    #ID, nume, descriere, pretAchizitie, locatie
    try:
        ID = input('Dati ID-ul:')
        nume = input('Dati numele:')
        descriere = input('Dati descriere:')
        pretAchizitie = float(input('Dati pret achizitie:'))
        locatie = input('Dati locatie:')

        rezultat = adaugareObiect(ID, nume, descriere, pretAchizitie, locatie, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat

    except ValueError as ve:
        print("Eroare:{}".format(ve))
        return lista

def Meniu():
    print("1.Adaugare Obiect.")
    print('2.Stergere obicet.')
    print('3.Modificare obiect.')
    print('4.Mutare obiect dintr o locatie in alta')
    print('5.Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită')
    print('6.Determinarea celui mai mare preț pentru fiecare locație.  ')
    print('7.Ordonarea obiectelor crescător după prețul de achiziție.')
    print('8.Afișarea sumelor prețurilor pentru fiecare nume')
    print('u.Undo')
    print('r.Redo')
    print('x.Iesire.')
    print('a.Show All.')

def showAll(lista):
    for obiect in lista:
        print(toString(obiect))

def runMeniu(lista):
    redoList = []
    undoList = []
    while True:
        Meniu()
        optiune = input('Selectati optiune:')
        if optiune == '1':
            lista = UIAdaugareObiect(lista, undoList, redoList)
        elif optiune == '2':
            lista = UIStergereObiect(lista, undoList, redoList)
        elif optiune == '3':
            lista = UIModificareObiect(lista, undoList, redoList)
        elif optiune == '4':
            lista = UIMutareInAltaLocatie(lista)
        elif optiune == '5':
            lista = UIConcatenareString(lista)
        elif optiune == '6':
            UICelMaiMarePret(lista)
        elif optiune == '7':
            showAll(OrdonareCrescDupaPret(lista))
        elif optiune == '8':
            UISumePreturiPtLocatie(lista)
        elif optiune == 'u':
            if len(undoList) > 0:
                redoList.append(lista)
                lista = undoList.pop()
            else:
                print('Nu se poate face undo!')
        elif optiune == 'r':
            if len(redoList) > 0:
                undoList.append(lista)
                lista = redoList.pop()
            else:
                print('Nu se poate face redo')
        elif optiune == 'a':
            showAll(lista)
        elif optiune == 'x':
            break

