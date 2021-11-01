from Domain.Obiect import getLocatie, toString, getDescriere
from Logic.CRUD import adaugareObiect, getByID
from Logic.Functionalitati import mutareInAltaLocatie, concatenareString


def testMutareInAltaLocatie():
    l = []
    l = adaugareObiect(0, "stilou", "italian", 10, "Roma", l)
    l = adaugareObiect(1, "pix", "italian", 5, "Paris", l)

    l = mutareInAltaLocatie('Paris', 'Braila', l)
    l = mutareInAltaLocatie('Roma', 'Galati', l)

    assert (getLocatie(getByID(1, l))) == 'Braila'
    assert (getLocatie(getByID(0, l))) == 'Galati'
    assert (len(l)) == 2

def testconcatenareString():
    l = []
    l = adaugareObiect(0, "stilou", "italian", 101, "Roma", l)
    l = adaugareObiect(1, "pix", "italian", 5, "Paris", l)

    l = concatenareString('nnn', 100, l)

    assert(getDescriere(getByID(0, l))) == 'italiannnn'


    '''for obiect in l:
        print(toString(obiect))
testconcatenareString()'''
