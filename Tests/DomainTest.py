from Domain.Obiect import creareObiect, getID, getNume, getDescriere, getPretAchizitie, getLocatie


def testCreeareObiect():
    obiect = creareObiect(1, "stilou", "italian", 10, "Roma")
    assert (getID(obiect)) == obiect[0]
    assert (getNume(obiect)) == 'stilou'
    assert (getDescriere(obiect)) == "italian"
    assert (getPretAchizitie(obiect)) == 10
    assert (getLocatie(obiect)) == 'Roma'