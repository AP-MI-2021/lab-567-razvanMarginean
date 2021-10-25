from Logic.CRUD import adaugareObiect
from Tests.TestAll import TestAll
from UserInterface.Meniu import runMeniu


def main():
    TestAll()
    lista = []
    lista = adaugareObiect('1', "stilou", "italian", 10, "Roma", lista)
    lista = adaugareObiect('2', "pix", "italian", 5, "Roma", lista)
    runMeniu(lista)


main()
