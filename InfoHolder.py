from mainFile import getEntryInput, getPokemon
from GoogSetup import CreateGoogleSheet


def getpks(lines, typeLines, pokemonNumber, fullNames):
    list = getPokemon(lines, typeLines, pokemonNumber, fullNames)
    return list


def getentry():
    entry = getEntryInput()
    return entry


def createsheet():
    CreateGoogleSheet()
