# Conway's game of life

from random import randint
from time import sleep
from copy import deepcopy

from settings import *


def create_initial_cells(width: int, height: int) -> list[list[str]]:
    cells = []

    for x in range(width):
        column: list[str] = []

        for y in range(height):

            if randint(0, 1) == 0:
                # add a living cell
                column.append('#')

            else:
                # add a dead cell
                column.append(' ')

        cells.append(column)

    return cells


def display_cells_on_screen(height: int, width: int, cells: list[list[str]]) -> None:
    for y in range(height):
        for x in range(width):
            print(cells[x][y], end='')
        # newline
        print()


def main() -> None:

    # Create a list of lists for the cells
    next_cells = create_initial_cells(WIDTH, HEIGHT)

    # MAIN LOOP
    while True:
        print("\n\n\n\n")
        current_cells = deepcopy(next_cells)

        display_cells_on_screen(HEIGHT, WIDTH, current_cells)

        sleep(30)


if __name__ == '__main__':
    main()
