from Domain.Obiect import getID, creareObiect


def getByID(ID, lista):
    for obiect in lista:
        if getID(obiect) == ID:
            return obiect

def adaugareObiect(ID, nume, descriere, pretAchizitie, locatie, lista):
    '''
    adauga un obiect de tip dictionar intr o lista
    :param ID: str
    :param nume: str
    :param descriere: str
    :param pretAchizitie: float
    :param locatie: str
    :param lista: lista de dictionare
    :return:o lista de obiecte de tip dictionar
    '''
    obiect = creareObiect(ID, nume, descriere, pretAchizitie, locatie)
    lista = lista + [obiect]
    return lista

def stergereObiect(ID, lista):
    '''
    sterge un obiect(dictionar) dupa un ID dat
    :param ID: str
    :param lista: lista de dictionare
    :return: o lista de dictionare
    '''
    listaNoua = []
    for obiect in lista:
        if getID(obiect) != ID:
            listaNoua.append(obiect)
    return listaNoua


def modificareObiect(ID, nume, descriere, pretAchizitie, locatie, lista):
    '''
    modifica un obiect(dictionar) intr o lista
    :param ID: int
    :param nume: str
    :param descriere: str
    :param pretAchizitie: float
    :param locatie: str
    :param lista: lista de dictionare
    :return: returneaza o lista de dictionare modificata
    '''
    listaNoua = []
    for obiect in lista:
        if getID(obiect) == ID:
            listaNoua.append(creareObiect(ID, nume, descriere, pretAchizitie, locatie))
        else:
            listaNoua.append(obiect)
    return listaNoua

