from Domain.Obiect import creareObiect, getNume, getID, getDescriere, getPretAchizitie, getLocatie
from Logic.CRUD import getByID, adaugareObiect, stergereObiect, modificareObiect


def testGetById():
    obiect1 = creareObiect(1, "stilou", "italian", 10, "Roma")
    obiect2 = creareObiect(2, "pix", "italian", 10, "Roma")
    l = [obiect1, obiect2]

    assert (getNume(getByID(2, l))) == "pix"
    assert (getNume(getByID(1, l))) == "stilou"


def testAdaugareObiect():
    l = []
    l = adaugareObiect(1, "stilou", "italian", 10, "Roma", l)

    assert (getID(l[0])) == 1
    assert (getNume(l[0])) == 'stilou'
    assert (getDescriere(l[0])) == 'italian'
    assert (getPretAchizitie(l[0])) == 10
    assert (getLocatie(l[0])) == 'Roma'


def testStergereObiect():
    l = []
    l = adaugareObiect(1, "stilou", "italian", 10, "Roma", l)
    l = adaugareObiect(2, "pix", "italian", 5, "Roma", l)

    l = stergereObiect(1, l)
    assert (len(l)) == 1
    assert (getByID(1, l)) is None
    '''assert (getByID(2, l)) == {
        'id': 2,
        'nume': 'pix',
        'descriere': 'italian',
        'pretAchizitie': 5,
        'locatie': 'Roma'
    }'''


def testModificareObiect():
    l = []
    l = adaugareObiect(1, "stilou", "italian", 10, "Roma", l)
    l = adaugareObiect(2, "pix", "italian", 5, "Roma", l)

    l = modificareObiect(2, "pixx", "italiann", 55, "Romaa", l)

    '''assert (getByID(2, l)) == {
        'id': 2,
        'nume': 'pixx',
        'descriere': 'italiann',
        'pretAchizitie': 55,
        'locatie': 'Romaa'
    }'''
