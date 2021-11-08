from Logic.CRUD import adaugareObiect
from Tests.TestAll import TestAll
from UserInterface.Meniu import runMeniu
from UserInterface.Meniu2 import runMeniu2


def main():
    TestAll()
    lista = []
    lista = adaugareObiect('1', "stilou", "italian", 10, "Roma", lista)
    lista = adaugareObiect('2', "pix", "italian", 5, "Roma", lista)

    print('1.Meniu Vechi')
    print('2.Meniu Nou')

    ok = True

    while ok:
        optiune = input('Selectati meniu:')
        if optiune == '1':
            runMeniu(lista)
            ok = False
        elif optiune == '2':
            runMeniu2(lista)
            ok = False
        else:
            print('Optiune invalida!Reincercati!')



main()
