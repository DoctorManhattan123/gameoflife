import time

import pygame
from typing import List

ALIVE = 1
DEAD = 0

screen_width = 500
screen_height = 500

"""
The given gameboard should be at least 3x3 oe the program will crash
"""

game_board: List[List[int]] = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                               [0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                               [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                               [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

width = len(game_board)
height = len(game_board[0])

if width < 3 or height < 3:
    print("Game board should have be at least size of 3 in each dimension.")
    exit(1)

square_width = screen_width / width
square_height = screen_height / width

round = 0


def run():
    global game_board
    global round

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))

    black_square = pygame.image.load('black_square.png')
    black_square = pygame.transform.scale(black_square, (square_width - 1, square_height - 1))

    green_square = pygame.image.load('green_square.png')
    green_square = pygame.transform.scale(green_square, (square_width - 1, square_height - 1))
    screen.fill((255, 255, 255))

    running = True

    # main loop
    while running:
        round += 1
        # event handling, gets all event from the event queue
        for y in range(height):
            for x in range(width):
                screen.blit(green_square if game_board[y][x] == ALIVE else black_square,
                            (square_width * x, square_height * y))

        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        pygame.time.delay(1000)

        print(f"round: {round}")
        print_2d_array(game_board)

        pygame.display.update()

        update_board()


def print_2d_array(array2d: List[List[int]]):
    for y in range(len(array2d)):
        for x in range(len(array2d[y])):
            print(f"{array2d[y][x]}, ", end='')
        print("\n")


def get_num_of_neighbours_by_coords(x_coord, y_coord) -> int:
    """

    :param x_coord: x coord (on the x-axis)
    :param y_coord: y coord (on the y-axis)
    :return: the number of neighbours in around the cell with the given coordinates
    """
    global game_board
    y_begin = y_coord - 1 if y_coord - 1 > -1 else 0
    y_end = y_coord + 1 if y_coord + 1 < len(game_board) else len(game_board) - 1
    x_begin = x_coord - 1 if x_coord - 1 > -1 else 0
    x_end = x_coord + 1 if x_coord + 1 < len(game_board[0]) else len(game_board[0]) - 1
    num = 0
    for y in range(y_begin, y_end + 1):
        for x in range(x_begin, x_end + 1):
            # if we are in the center.
            if y == y_coord and x == x_coord:
                continue
            num += 1 if game_board[y][x] == ALIVE else 0
    return num


def update_board():
    global game_board
    temp_board = [
        [ALIVE if game_board[y_coord][x_coord] == ALIVE else DEAD for x_coord in range(len(game_board[y_coord]))] for
        y_coord in range(len(game_board))]
    for y in range(height):
        for x in range(width):
            num_of_neighbours = get_num_of_neighbours_by_coords(x, y)
            # Any live cell with two or three live neighbours survives.
            if temp_board[y][x] == ALIVE and (num_of_neighbours == 2 or num_of_neighbours == 3):
                temp_board[y][x] = ALIVE
            # Any dead cell with three live neighbours becomes a live cell.
            elif temp_board[y][x] == DEAD and num_of_neighbours == 3:
                temp_board[y][x] = ALIVE
            # All other live cells die in the next generation. Similarly, all other dead cells stay dead.
            else:
                temp_board[y][x] = DEAD

    game_board = [
        [ALIVE if temp_board[y_coord][x_coord] == ALIVE else DEAD for x_coord in range(len(temp_board[y_coord]))] for
        y_coord in range(len(temp_board))]


if __name__ == '__main__':
    run()
