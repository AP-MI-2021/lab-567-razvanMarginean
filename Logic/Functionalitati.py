from Domain.Obiect import getLocatie, getID, getPretAchizitie, getDescriere, getNume
from Logic.CRUD import adaugareObiect


def mutareInAltaLocatie(locatieVeche, locatieNoua, lista):
    '''
    muta un obiect dintr o locatie in alta
    :param locatieVeche: str
    :param locatieNoua: str
    :param lista: lista de obiecte
    :return: lista modificata
    '''
    listaNoua = []

    for obiect in lista:
        if getLocatie(obiect) == locatieVeche:
            listaNoua = adaugareObiect(getID(obiect),
                           getNume(obiect),
                           getDescriere(obiect),
                           getPretAchizitie(obiect),
                           locatieNoua,
                           listaNoua)
        else:
            listaNoua.append(obiect)
    return listaNoua

def concatenareString(string, valoare, lista):
    '''
    concateneaza un string citit la toate descrierile obiectelor cu prețul mai mare decât o valoarea citită
    :param string: str
    :param valoare: float
    :param lista: lista de obiecte
    :return: lista modificata
    '''

    rezultat = []


    for obiect in lista:
        if getPretAchizitie(obiect) > valoare:
            rezultat = adaugareObiect(getID(obiect),
                           getNume(obiect),
                           getDescriere(obiect) + string,
                           getPretAchizitie(obiect),
                           getLocatie(obiect),
                           rezultat)
        else:
            rezultat.append(obiect)

    return rezultat

