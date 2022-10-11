import pygame

screen_width = 500
screen_height = 500

width = 10
height = 10

square_width = screen_width/width
square_height = screen_height/width

game_board = t = [[0]*width for i in range(height)]


def run():
    while True:
        print(game_board)


def init_screen():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((255,255,255))

    black_square = pygame.image.load('black_square.png')
    green_square = pygame.image.load('green_square.png')

    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for i in game_board:
            for j in i:
                screen.fill((255,255,255))
                screen.blit(green_square, (,0))
                pygame.display.update()
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


if __name__ == '__main__':
    init_screen()
    #run()

