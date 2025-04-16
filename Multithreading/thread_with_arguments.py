import threading


def main() -> None:

    print('Cats', 'Dogs', 'Frogs', sep=' & ')

    my_thread = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})

    my_thread.start()


if __name__ == '__main__':
    main()
