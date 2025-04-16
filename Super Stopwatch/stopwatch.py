from time import time


def main() -> None:

    print("""Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch""")
    print(" Press q to quit.")

    starting_time = time()

    last_time = starting_time
    lap_number = 1

    # Start tracking lap times

    while input("  - ") != 'q':

        lap_time = round(time() - last_time, 1)
        total_time = round(time() - starting_time, 1)

        print(f"Lap {lap_number}."
              f"\nTotal time : {int(total_time // 60)}m and {total_time}s"
              f"\nLap time : {int(lap_time // 60)}m and {lap_time}s")
        print("\n\n")

        lap_number += 1
        last_time = time()

    print("Goodbye!")


if __name__ == '__main__':
    main()
