from random import randint
from sys import maxsize, exit


def Hi():
    print("Hi")
    return


def GetRandom():
    print(randint(-maxsize - 1, maxsize))
    return


def Shutdown():
    exit(0)
