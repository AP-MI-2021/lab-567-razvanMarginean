'''    l = []
    l = adaugareObiect(0, "stilou", "italian", 101, "Roma", l)
    l = adaugareObiect(1, "pix", "italian", 5, "Pari", l)
    l = adaugareObiect(2, "stilou", "italian", 100, "Roma", l)
    l = adaugareObiect(3, "pix", "italian", 6, "Pari", l)'''
from Logic.CRUD import adaugareObiect


def TestUndoRedo():
    undoList = []
    redoList = []
    l = []

    undoList.append(l)
    redoList.clear()
    l = adaugareObiect(0, "stilou", "italian", 101, "Roma", l)

    undoList.append(l)
    redoList.clear()
    l = adaugareObiect(1, "stilou", "italian", 101, "Roma", l)

    undoList.append(l)
    redoList.clear()
    l = adaugareObiect(2, "stilou", "italian", 101, "Roma", l)

    #Facem undo
    if len(undoList) > 0:
        redoList.append(l)
        l = undoList.pop()
    assert(l) == [[0, 'stilou', 'italian', 101, 'Roma'], [1, 'stilou', 'italian', 101, 'Roma']]

    #Facem undo
    if len(undoList) > 0:
        redoList.append(l)
        l = undoList.pop()
    assert (l) == [[0, 'stilou', 'italian', 101, 'Roma']]

    #Facem Undo
    if len(undoList) > 0:
        redoList.append(l)
        l = undoList.pop()
    assert (l) == []

    #Facem undo
    if len(undoList) > 0:
        redoList.append(l)
        l = undoList.pop()
    assert (l) == []


    #Adaugam 3 obiecte
    undoList.append(l)
    redoList.clear()
    l = adaugareObiect(0, "stilou", "italian", 101, "Roma", l)

    undoList.append(l)
    redoList.clear()
    l = adaugareObiect(1, "stilou", "italian", 101, "Roma", l)

    undoList.append(l)
    redoList.clear()
    l = adaugareObiect(2, "stilou", "italian", 101, "Roma", l)
    ##

    #Facem redo
    if len(redoList) > 0:
        undoList.append(l)
        l = redoList.pop()
    assert(l) == [[0, 'stilou', 'italian', 101, 'Roma'], [1, 'stilou', 'italian', 101, 'Roma'], [2, 'stilou', 'italian', 101, 'Roma']]

    #Facem undo de 2 ori
    if len(undoList) > 0:
        redoList.append(l)
        l = undoList.pop()


    if len(undoList) > 0:
        redoList.append(l)
        l = undoList.pop()
    assert (l) == [[0, 'stilou', 'italian', 101, 'Roma']]
    #

    #Adaugam obiect 4
    undoList.append(l)
    redoList.clear()
    l = adaugareObiect(4, "stilou", "italian", 101, "Roma", l)
    assert(l) == [[0, 'stilou', 'italian', 101, 'Roma'], [4, "stilou", "italian", 101, "Roma"]]

    #Redo(nu face nimic lista ramane la fel)
    if len(redoList) > 0:
        undoList.append(l)
        l = redoList.pop()
    assert (l) == [[0, 'stilou', 'italian', 101, 'Roma'], [4, "stilou", "italian", 101, "Roma"]]

    #Undo(lista ramane fara obiectul 4)
    if len(undoList) > 0:
        redoList.append(l)
        l = undoList.pop()
    assert (l) == [[0, 'stilou', 'italian', 101, 'Roma']]

    #Undo(lista ramane goala)
    if len(undoList) > 0:
        redoList.append(l)
        l = undoList.pop()
    assert (l) == []

    #Redo de doua ori(anuleaza ultimele 2 undo)
    if len(redoList) > 0:
        undoList.append(l)
        l = redoList.pop()
    if len(redoList) > 0:
        undoList.append(l)
        l = redoList.pop()
    assert (l) == [[0, 'stilou', 'italian', 101, 'Roma'], [4, "stilou", "italian", 101, "Roma"]]
    





TestUndoRedo()