from subprocess import Popen, PIPE


def WriteToProcess(handle, text: str) -> str:
    """
    Function to comunicate with child process

    :param handle: handle to Popen object
    :param text: input for subprocess

    :return: subprocess response as string
    """
    handle.stdin.write(text)
    handle.stdin.flush()
    return handle.stdout.readline().strip()


if __name__ == "__main__":
    # launching Generator (program A) as a seperate process
    generator = Popen(
        ["python3", "Generator.py"],
        stdin=PIPE,
        stdout=PIPE,
        text=True,
    )

    # sending Hi command and veryfing response
    if WriteToProcess(generator, "Hi\n") != "Hi":
        raise (
            ChildProcessError(
                "There is someting wrong with pseudo-random number generator."
            )
        )

    # retriving 100 random numbers
    random_numbers = []
    for _ in range(100):
        random_numbers.append(int(WriteToProcess(generator, "GetRandom\n")))

    # shuting down generator
    print(WriteToProcess(generator, "Shutdown\n"))

    # printing sorted list to the console
    random_numbers.sort()
    print(random_numbers)

    # calculating and printing median and average
    median = (random_numbers[49] + random_numbers[50]) / 2
    average = sum(random_numbers) / 100
    print(median, average)
