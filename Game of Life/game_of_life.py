# Conway's game of life

from random import randint
from time import sleep

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


def get_next_cells(width: int, height: int, current_cells) -> list[list[str]]:

    next_cells = [[' ' for _ in range(height)] for _ in range(width)]

    for x in range(width):
        for y in range(height):
            # get neighboring coordinates
            left_coordinates = (x - 1) % width
            right_coordinates = (x + 1) % width
            above_coordinates = (y - 1) % height
            below_coordinates = (y + 1) % height

            # Count living neighbors
            neighbors = 0

            if current_cells[left_coordinates][above_coordinates] == '#':
                neighbors += 1
            if current_cells[x][above_coordinates] == '#':
                neighbors += 1
            if current_cells[right_coordinates][above_coordinates] == '#':
                neighbors += 1
            if current_cells[left_coordinates][y] == '#':
                neighbors += 1
            if current_cells[right_coordinates][y] == '#':
                neighbors += 1
            if current_cells[left_coordinates][below_coordinates] == '#':
                neighbors += 1
            if current_cells[x][below_coordinates] == '#':
                neighbors += 1
            if current_cells[right_coordinates][below_coordinates] == '#':
                neighbors += 1

            # Set cells based on Conway's rules
            if current_cells[x][y] == '#' and (neighbors == 2 or neighbors == 3):
                next_cells[x][y] = '#'
            elif current_cells[x][y] == ' ' and neighbors == 3:
                next_cells[x][y] = '#'
            else:
                next_cells[x][y] = ' '

    return next_cells


def main() -> None:

    cells = create_initial_cells(WIDTH, HEIGHT)

    while True:
        print("\n\n\n\n")

        display_cells_on_screen(HEIGHT, WIDTH, cells)

        cells = get_next_cells(WIDTH, HEIGHT, cells)

        sleep(1)


if __name__ == '__main__':
    main()
