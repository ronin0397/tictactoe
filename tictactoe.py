import pygame
pygame.init()
pygame.font.init()

#window values
black = (0, 0, 0)
white = (200, 200, 200)
width, height = 600, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tic Tac Toe')
FONT = pygame.font.SysFont('Arial', 30)
win.fill(black)


#   load images of players and grid
def draw(coord_x, coord_y, piece):
    blocksize = 200
    cross = pygame.transform.scale(pygame.image.load('cross.png'), (width / 3, height / 3))
    circle = pygame.transform.scale(pygame.image.load('circle.jpg'), (width / 3, height / 3))
    for x in range(0, width, blocksize):
        for y in range(0, height, blocksize):
            rect = pygame.Rect(x, y, blocksize, blocksize)
            pygame.draw.rect(win, white, rect, 1)
    if piece == 'cross':
        win.blit(cross, (coord_x, coord_y))
    if piece == 'circle':
        win.blit(circle, (coord_x, coord_y))


#game logic, returns win flag and winner
def grid_logic(grid, piece):
    winner = 'none'
    won = False
    if grid[0][0] == piece and grid[1][0] == piece and grid[2][0] == piece:
        won = True
        winner = piece
    if grid[0][1] == piece and grid[1][1] == piece and grid[2][1] == piece:
        won = True
        winner = piece
    if grid[0][2] == piece and grid[1][2] == piece and grid[2][2] == piece:
        won = True
        winner = piece
    if grid[0][0] == piece and grid[0][1] == piece and grid[0][2] == piece:
        won = True
        winner = piece
    if grid[1][0] == piece and grid[1][1] == piece and grid[1][2] == piece:
        won = True
        winner = piece
    if grid[2][0] == piece and grid[2][1] == piece and grid[2][2] == piece:
        won = True
        winner = piece
    if grid[0][0] == piece and grid[1][1] == piece and grid[2][2] == piece:
        won = True
        winner = piece
    if grid[2][0] == piece and grid[1][1] == piece and grid[0][2] == piece:
        won = True
        winner = piece
    return won, winner


def main():
    run = True
    x, y = 0, 0
    won = False
    turn = 'none'
    turn_count = 0
    game_array = [['none'] * 3 for o in range(3)]
    print(game_array)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
#           left click to place cross or circle
            if event.type == pygame.MOUSEBUTTONUP:
                if turn == 'none':
                    turn = 'circle'
                if turn_count % 2 == 0:
                    turn = 'cross'
                if turn_count % 2 == 1:
                    turn = 'circle'
                x, y = pygame.mouse.get_pos()
#               row 1
                if x < 200 and y < 200 and (game_array[0][0] == 'none' or game_array[0][0] == turn):
                    x = 0
                    y = 0
                    game_array[0][0] = turn
                if (x >= 200) and (x < 400) and (y < 200) and (game_array[1][0] == 'none' or game_array[1][0] == turn):
                    x = 200
                    y = 0
                    game_array[1][0] = turn
                if x >= 400 and y < 200 and (game_array[2][0] == 'none' or game_array[2][0] == turn):
                    x = 400
                    y = 0
                    game_array[2][0] = turn
#               row 2
                if x < 200 and y < 400 and (y >= 200) and (game_array[0][1] == 'none' or game_array[0][1] == turn):
                    x = 0
                    y = 200
                    game_array[0][1] = turn
                if (x >= 200) and (x < 400) and (y < 400) and (y >= 200) and (game_array[1][1] == 'none' or game_array[1][1] == turn):
                    x = 200
                    y = 200
                    game_array[1][1] = turn
                if x >= 400 and (y < 400) and (y >= 200) and (game_array[2][1] == 'none' or game_array[2][1] == turn):
                    x = 400
                    y = 200
                    game_array[2][1] = turn
#               row 3
                if x < 200 and y >= 400 and (game_array[0][2] == 'none' or game_array[0][2] == turn):
                    x = 0
                    y = 400
                    game_array[0][2] = turn
                if (x >= 200) and (x < 400) and y >= 400 and (game_array[1][2] == 'none' or game_array[1][2] == turn):
                    x = 200
                    y = 400
                    game_array[1][2] = turn
                if x >= 400 and y >= 400 and (game_array[2][2] == 'none' or game_array[2][2] == turn):
                    x = 400
                    y = 400
                    game_array[2][2] = turn
                print(game_array)
                turn_count += 1
#       win condition
        if won is True:
            pygame.time.delay(1000)
            break
#       only draws image if not already occupied by nother pieces
        if game_array[x//200][y//200] == turn:
            draw(x, y, turn)
        winner, victor = grid_logic(game_array, turn)
        if victor != 'none':
            print('Winner is: ' + victor)
            won = winner
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
