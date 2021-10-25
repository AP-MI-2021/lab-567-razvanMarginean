from Tests.CRUDTest import testGetById, testAdaugareObiect, testStergereObiect, testModificareObiect
from Tests.DomainTest import testCreeareObiect


def TestAll():
    testCreeareObiect()
    testGetById()
    testAdaugareObiect()
    testStergereObiect()
    testModificareObiect()