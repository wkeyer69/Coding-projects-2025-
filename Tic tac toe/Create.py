import pygame 

pygame.init()

screen = pygame.display.set_mode((400, 400))

turn = "x"

winner = None 

draw = None 

board = [[None]*3, [None]*3, [None]*3]

clock = pygame.time.Clock()

ximg = pygame.image.load("X.png")
oimg = pygame.image.load("O.png")

ximg = pygame.transform.scale(ximg, (80, 80))
oimg = pygame.transform.scale(oimg, (80, 80))

def draw_grid():
    screen.fill((0, 0, 255))
    pygame.draw.line(screen, (0, 255, 0), (400 / 3, 0), (400 / 3, 400), 5)
    pygame.draw.line(screen, (0, 255, 0), ((400 / 3) * 2, 0), ((400 / 3)* 2, 400), 5)

    pygame.draw.line(screen, (0, 255, 0), (0, 400 / 3), (400, 400 / 3), 5)
    pygame.draw.line(screen, (0, 255, 0), (0, (400 / 3) * 2), (400, (400 / 3) * 2), 5)

def result(): 
    global winner, draw

    if winner: 
        message = winner + "won!"
    if draw: 
        message = draw + "DRAW"
    font = pygame.font.SysFont('Georgia', 70)
    text = font.render(message, 1, (255, 0, 0))
    text_rect = text.get_rect(center= (400 // 2, 400 // 2))
    screen.blit(text, text_rect)


def wincases(): 
    global draw, winner, board
    for row in range(0, 3): 
        if((board[row][0] == board[row][1] == board[row][2]) and (board[row][0] != None)):
            winner = board[row][0]
            pygame.draw.line(screen, (255, 0, 0), (0, (row + 1) * 66), (400, (row + 1) * 66), 4)
            result()
            break
    for col in range(0, 3): 
        if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] != None)):
            winner = board[0][col]
            pygame.draw.line(screen, (255, 0, 0), ((col + 1) * 66, 0), ((col + 1) * 66, 400), 4)
            result()
            break

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != None:
        winner = board[0][0]
        pygame.draw.line(screen, (255, 0, 0), (50, 50), (350, 350), 4)
        result()
    if (board[0][2] == board[1][2] == board[2][0] and board[0][2] != None): 
        winner = board[0][2]
        pygame.draw.line(screen, (255, 0, 0), (350, 50), (50, 350), 4)
        result()
    if (all([all(row) for row in board])) and winner == None: 
        draw = True 
        result()

def getimg(row, col): 
    global turn, board 

    if row == 1:
        posy = 30
    if row == 2: 
        posy = 133 + 30
    if row == 3:
        posy = 133 * 2 + 30
    if col == 1:
        posx = 30
    if col == 2: 
        posx = 133 + 30
    if col == 3:
        posx = 133 * 2 + 30

    board[row - 1][col - 1] = turn   
    if (turn == "x"):
        screen.blit(ximg, (posx, posy))
        turn = "o"
    else:
        screen.blit(oimg, (posx, posy))
        turn = "x"
    pygame.display.update()

def input_to_block():
    x, y = pygame.mouse.get_pos()

    if(x<400 / 3):#check if the click is within the first vertical line
        col = 1

    elif (x<400 / 3 * 2):#we would move to this case only if the above one is not appropriate 
        col = 2

    elif(x<400):
        col = 3

    else:
        col = None

	# similarly assing the row 
    if(y<400 / 3):
        row = 1

    elif (y<400 / 3 * 2):
        row = 2

    elif(y<400):
        row = 3

    else:
        row = None
    

    if (row and col and board[row - 1][col  - 1] is None ): 
        global turn
        getimg(row, col)
        wincases()


draw_grid()
    











running = True
while running: 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            input_to_block()
    clock.tick(30)
    pygame.display.update()
