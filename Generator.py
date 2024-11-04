from random import randint
from sys import maxsize, exit as sys_exit


def Hi():
    """
    function used for veryfing responses by parent process
    """
    print("Hi")
    return


def GetRandom():
    """
    function for genereting pseudo-random numbers
    """
    print(randint(-maxsize - 1, maxsize))
    return


def Shutdown():
    """
    function for terminating the program
    """
    print("Terminating Generator.py")
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
