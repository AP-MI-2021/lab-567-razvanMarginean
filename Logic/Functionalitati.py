from Domain.Obiect import getLocatie, getID, getPretAchizitie, getDescriere, getNume, toString
from Logic.CRUD import adaugareObiect, getByID


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


def CelMaiMarePret(lista):
    '''
    Determinarea celui mai mare preț pentru fiecare locație.
    :param ID: str
    :param lista: lista de obiecte
    :return: dictionar
    '''

    rezultat = {}

    for obiect in lista:
        pret = getPretAchizitie(obiect)
        locatie = getLocatie(obiect)
        if locatie in rezultat:
            if pret > getPretAchizitie(rezultat[locatie]):
                rezultat[locatie] = obiect
        else:
            rezultat[locatie] = obiect
    return rezultat


def OrdonareCrescDupaPret(lista):
    '''

    :param lista:
    :return:
    '''
    lista.sort(key=getPretAchizitie)
    return lista

def SumePreturiPtLocatie(lista):
    '''
    Afișarea sumelor prețurilor pentru fiecare nume
    :param lista:
    :return:
    '''
    dict = {}
    for obiect in lista:
        nume = getNume(obiect)
        pret = getPretAchizitie(obiect)
        if nume in dict:
            dict[nume] = dict[nume] + pret
        else:
            dict[nume] = pret
    return dict
