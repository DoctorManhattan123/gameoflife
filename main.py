import pygame
from typing import List

ALIVE = 1
DEAD = 0

screen_width = 500
screen_height = 500

width = 10
height = 10

square_width = screen_width / width
square_height = screen_height / width

# game_board: List[List[int]] = [[0 if i % 2 == 0 else 1]*width for i in range(height)]

game_board: List[List[int]] = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def run():
    while True:
        print(game_board)


def init_screen():
    global game_board
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))

    black_square = pygame.image.load('black_square.png')
    black_square = pygame.transform.scale(black_square, (square_width-1, square_height-1))

    green_square = pygame.image.load('green_square.png')
    green_square = pygame.transform.scale(green_square, (square_width-1, square_height-1))
    screen.fill((255, 255, 255))

    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for y in range(height):
            for x in range(width):
                print(f"x: {x}, y: {y}")

                screen.blit(green_square if game_board[y][x] == ALIVE else black_square, (square_width * x, square_height * y))

        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        pygame.time.delay(500)
        pygame.display.update()

        update_board()


def get_num_of_neighbours_by_coords(x, y) -> int:
    global game_board
    num = 0
    for i in [y-1, y, y+1]:
        for j in range(x-1, x, x+1):
            # if we are out of bound or in the center we continue
            if j < 0 or j > len(game_board)-1 or i < 0 or i > len(game_board[j])-1 or (i == x and j == y):
                continue
            num += 1 if game_board[i][j] == ALIVE else 0
    return num


def update_board():
    global game_board
    temp_board = game_board.copy()
    # first rule
    for y in range(height):
        for x in range(width):
            print(f"x: {x}, y: {y}")
            num_of_neighbours = get_num_of_neighbours_by_coords(x, y)
            # any living cell with 2 neighbours survives
            if temp_board[y][x] == DEAD and num_of_neighbours == 2:
                temp_board[y][x] = ALIVE
            # any cell with 3 neighbours whether alive or dead will become/stay alive
            elif num_of_neighbours == 3:
                temp_board[y][x] = ALIVE


if __name__ == '__main__':
    init_screen()
    # run()
