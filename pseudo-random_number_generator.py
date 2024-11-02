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


if __name__ == "__main__":
    commands = {
        "Hi": Hi,
        "GetRandom": GetRandom,
        "Shutdown": Shutdown,
    }
    input = input()

    while True:
        if input not in commands.keys():
            continue
        commands[input]()
