import subprocess


def main() -> None:

    # Use the "Process open" method. It returns a Popen object:
    paint_process = subprocess.Popen('C:\\Windows\\System32\\mspaint.exe')

    # It has two useful methods: .poll() and wait():

    # The .poll() method will return "None" if the process is still running
    # when it's called. If the program has terminated, it will return the
    # process's integer "exit code", used to determine whether the process
    # terminated without errors (0) or whether an error caused the process
    # to terminate (a nonzero exit code, generally 1).

    print("Before closing the program: ", paint_process.poll())

    # The .wait() method is like waiting until the driver has arrived at my
    # destination. It will block unitl the launched process has terminated.
    # The return value of .wait() is the process's integer exit code.

    print("Closing program exit code: ", paint_process.wait())

    print("After the program is closed: ", paint_process.poll())


if __name__ == '__main__':
    main()
