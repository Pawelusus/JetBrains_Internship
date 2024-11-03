from random import randint
from sys import maxsize, exit as sys_exit


def Hi():
    print("Hi")
    return


def GetRandom():
    print(randint(-maxsize - 1, maxsize))
    return


def Shutdown():
    sys_exit(0)


if __name__ == "__main__":
    commands = {
        "Hi": Hi,
        "GetRandom": GetRandom,
        "Shutdown": Shutdown,
    }

    while True:
        command = input()

        if command not in commands.keys():
            continue

        commands[command]()
