from Domain.Obiect import getLocatie, toString, getDescriere, getPretAchizitie
from Logic.CRUD import adaugareObiect, getByID
from Logic.Functionalitati import mutareInAltaLocatie, concatenareString, CelMaiMarePret, OrdonareCrescDupaPret, \
    SumePreturiPtLocatie


def testMutareInAltaLocatie():
    l = []
    l = adaugareObiect(0, "stilou", "italian", 10, "Roma", l)
    l = adaugareObiect(1, "pix", "italian", 5, "Pari", l)

    l = mutareInAltaLocatie('Pari', 'Braa', l)
    l = mutareInAltaLocatie('Roma', 'Gala', l)

    assert (getLocatie(getByID(1, l))) == 'Braa'
    assert (getLocatie(getByID(0, l))) == 'Gala'
    assert (len(l)) == 2

def testconcatenareString():
    l = []
    l = adaugareObiect(0, "stilou", "italian", 101, "Roma", l)
    l = adaugareObiect(1, "pix", "italian", 5, "Pari", l)

    l = concatenareString('nnn', 100, l)

    assert(getDescriere(getByID(0, l))) == 'italiannnn'

def testCelMaiMarePret():
    l = []
    l = adaugareObiect(0, "stilou", "italian", 101, "Roma", l)
    l = adaugareObiect(1, "pix", "italian", 5, "Pari", l)
    l = adaugareObiect(2, "stilou", "italian", 100, "Roma", l)
    l = adaugareObiect(3, "pix", "italian", 6, "Pari", l)

    rezultat = CelMaiMarePret(l)

    assert(len(rezultat)) == 2
    l = adaugareObiect(33, "pix", "italian", 6, "Para", l)
    rezultat = CelMaiMarePret(l)
    assert(len(rezultat)) == 3

def testOrdonareCrescDupaPret():
    l = []
    l = adaugareObiect(0, "stilou", "italian", 101, "Roma", l)
    l = adaugareObiect(1, "pix", "italian", 5, "Pari", l)

    rezultat = OrdonareCrescDupaPret(l)

    assert(getPretAchizitie(l[0])) == 5

def testSumePreturiPtLocatie():
    l = []
    l = adaugareObiect(0, "stilou", "italian", 101, "Roma", l)
    l = adaugareObiect(1, "pix", "italian", 5, "Pari", l)
    l = adaugareObiect(2, "stilou", "italian", 100, "Roma", l)
    l = adaugareObiect(3, "pix", "italian", 6, "Pari", l)

    dict = SumePreturiPtLocatie(l)

    assert (dict['stilou']) == 201
    assert (dict['pix']) == 11


'''    print (rezultat)
testOrdonareCrescDupaPret()'''


'''for obiect in l:
        print(toString(obiect))
testconcatenareString()'''
