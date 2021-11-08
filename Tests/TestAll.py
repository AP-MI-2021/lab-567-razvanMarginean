from Logic.Functionalitati import mutareInAltaLocatie
from Tests.CRUDTest import testGetById, testAdaugareObiect, testStergereObiect, testModificareObiect
from Tests.DomainTest import testCreeareObiect
from Tests.FunctionalitatiTeste import testMutareInAltaLocatie, testconcatenareString, testCelMaiMarePret, \
    testOrdonareCrescDupaPret, testSumePreturiPtLocatie
from Tests.TestUndoRedo import TestUndoRedo


def TestAll():
    testCreeareObiect()
    testGetById()
    testAdaugareObiect()
    testStergereObiect()
    testModificareObiect()
    testMutareInAltaLocatie()
    testconcatenareString()
    testCelMaiMarePret()
    testOrdonareCrescDupaPret()
    testSumePreturiPtLocatie()

    TestUndoRedo()
