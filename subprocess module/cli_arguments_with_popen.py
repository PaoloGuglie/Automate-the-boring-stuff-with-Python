from subprocess import Popen


def main() -> None:

    filepath = ("C:\\Users\\windows\\Desktop\\Programming projects\\"
                "Automate-the-boring-stuff-with-Python\\subprocess module\\notes.txt")

    Popen(['C:\\Windows\\notepad.exe', filepath])


if __name__ == '__main__':
    main()
