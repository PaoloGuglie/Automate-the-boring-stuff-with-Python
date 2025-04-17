from subprocess import run, Popen
from time import sleep


def main() -> None:

    # run() waits for the subprocess to finish before closing this program
    run(['C:\\Python313\\python.exe', 'hello.py'])

    print("\n--------------------\n")

    # Popen() does not wait, so I use sleep() to give the subprocess time.
    Popen(['C:\\Python313\\python.exe', 'hello.py'])
    sleep(1)


if __name__ == '__main__':
    main()
