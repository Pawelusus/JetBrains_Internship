from subprocess import Popen, PIPE

if __name__ == "__main__":
    generator = Popen(
        ["python", "Generator.py"],
        stdin=PIPE,
        stdout=PIPE,
        text=True,
    )
