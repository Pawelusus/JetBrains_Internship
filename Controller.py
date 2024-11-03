from subprocess import Popen, PIPE

if __name__ == "__main__":
    # launching Generator (program A) as a seperate process
    generator = Popen(
        ["python", "Generator.py"],
        stdin=PIPE,
        stdout=PIPE,
        text=True,
    )

    # sending Hi command and veryfing response
    generator.stdin.write("Hi\n")
    generator.stdin.flush()
    if generator.stdout.readline().strip() != "Hi":
        raise (
            ChildProcessError(
                "There is someting wrong with pseudo-random number generator."
            )
        )

    # retriving 100 random numbers
    random_numbers = []
    for _ in range(100):
        generator.stdin.write("GetRandom\n")
        generator.stdin.flush()
        random_numbers.append(int(generator.stdout.readline().strip()))

    # shuting down generator
    generator.stdin.write("Shutdown\n")
    generator.stdin.flush()

    # printing sorted list to the console
    random_numbers.sort()
    print(random_numbers)

    # calculating and printing median and average
    median = (random_numbers[49] + random_numbers[50]) / 2
    average = sum(random_numbers) / 100
    print(median, average)
