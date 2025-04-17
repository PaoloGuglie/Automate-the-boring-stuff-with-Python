from subprocess import Popen


def main() -> None:

    # Open the notes.txt file in the notepad
    Popen(['start', 'notes.txt'], shell=True)

    # Open the hello.py file in the notepad
    Popen(['start', 'hello.py'], shell=True)


if __name__ == '__main__':
    main()
