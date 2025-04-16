import threading
from time import sleep


def take_a_nap() -> None:
    sleep(2)
    print("Wake up!")


def program_without_join() -> None:

    print("Start of program.")

    thread_object = threading.Thread(target=take_a_nap)
    thread_object.start()

    print("End of program.")


def program_with_join() -> None:
    """ By using .join(), the program "synchs" the thread with the main thread, so that
    the program will wait for the thread to execute before printing the last line. """

    print("Start of program.")

    thread_object = threading.Thread(target=take_a_nap)
    thread_object.start()

    thread_object.join()

    print("End of program.")


def main() -> None:

    print("Press 'a' for the program without .join() or any other key for the program with .join()")

    if input("  - ") == 'a':
        program_without_join()

    else:
        program_with_join()


if __name__ == '__main__':
    main()
