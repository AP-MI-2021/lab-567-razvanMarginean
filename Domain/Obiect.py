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
    '''return {
        'id': ID,
        'nume': nume,
        'descriere': descriere,
        'pretAchizitie': pretAchizitie,
        'locatie': locatie
    }
    '''
    obiect = [ID, nume, descriere, pretAchizitie, locatie]
    return obiect


"""obiect = creareObiect(1, "stilou", "italian", 10, "Roma")
print(obiect['id'])
"""


def getID(obiect):
    #return obiect['id']
    return obiect[0]

def getNume(obiect):
    #return obiect['nume']
    return obiect[1]

def getDescriere(obiect):
    #return obiect['descriere']
    return obiect[2]

def getPretAchizitie(obiect):
    #return obiect['pretAchizitie']
    return obiect[3]

def getLocatie(obiect):
    #return obiect['locatie']
    return obiect[4]

def toString(obiect):
    return "ID:{} nume:{} descriere:{} pretAchizitie:{} locatie:{}".format(
        getID(obiect),
        getNume(obiect),
        getDescriere(obiect),
        getPretAchizitie(obiect),
        getLocatie(obiect)
    )

