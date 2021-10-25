def creareObiect(ID, nume, descriere, pretAchizitie, locatie):
    '''
    creeaza un dictionar pentru obiect
    :param ID:str
    :param nume:str
    :param descriere:str
    :param pretAchizitie:float
    :param locatie:str
    :return:un dictionar pentru obiect
    '''
    return {
        'id': ID,
        'nume': nume,
        'descriere': descriere,
        'pretAchizitie': pretAchizitie,
        'locatie': locatie
    }


"""obiect = creareObiect(1, "stilou", "italian", 10, "Roma")
print(obiect['id'])
"""


def getID(obiect):
    return obiect['id']


def getNume(obiect):
    return obiect['nume']


def getDescriere(obiect):
    return obiect['descriere']


def getPretAchizitie(obiect):
    return obiect['pretAchizitie']


def getLocatie(obiect):
    return obiect['locatie']

def toString(obiect):
    return "ID:{} nume:{} descriere:{} pretAchizitie:{} locatie:{}".format(
        getID(obiect),
        getNume(obiect),
        getDescriere(obiect),
        getPretAchizitie(obiect),
        getLocatie(obiect)
    )

