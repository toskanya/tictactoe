from graphic import *
from minimax import *
import os

def check(grid_matrix): 
    winner = None

    diag1 = 0
    diag2 = 0
    count = 0

    for col, row in enumerate(grid_matrix):
    #row check
        if sum(row) == 3:
            winner = 1
            break
        elif sum(row) == -3:
            winner = -1
            break

    #col check
        if grid_matrix[0][col] + grid_matrix[1][col] + grid_matrix[2][col] == 3:
            winner = 1
            break
        elif grid_matrix[0][col] + grid_matrix[1][col] + grid_matrix[2][col] == -3:
            winner = -1
            break

    #draw check
        for cell in row:
            if cell:
                count += 1
        if count == 9:
            winner = 0

    #diag check
        diag1 += grid_matrix[col][col]
        diag2 += grid_matrix[col][2 - col]

            
    if diag1 == 3 or diag2 == 3:
        winner = 1
    elif diag1 == -3 or diag2 == -3:
        winner = -1
        
    return winner
        
def initGame():
    global winner, game_over, grid_obj, grid_matrix, screen, player, AI
    grid_obj = Grid()
    grid_matrix = grid_obj.get()
    screen = Screen()
    screen.drawGrid(grid_obj)
    
    player = Human['O']
    AI = Computer('X')
    winner = None

def play():
    global winner, game_over, grid_obj, grid_matrix, screen, player, AI
    initGame()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                
            if winner is not None:
                screen.drawEndGame(winner)
                
            if event.type == MOUSEBUTTONUP and winner is not None:
                initGame()  
                
            elif event.type == MOUSEBUTTONUP and winner is None:
                x, y = pygame.mouse.get_pos()
                if x > 45 and x < SCREEN_WIDTH - 45 and y > 45 and y < SCREEN_HEIGHT - 45:
                    x, y = x - 45, y - 45
                    x, y = int(x // STEP), int(y // STEP)
                   
                    if not grid_matrix[y][x] and player == -1:
                        grid_matrix[y][x] = player
                        player *= -1
                    
                    grid_obj.set(grid_matrix)
                    screen.drawMarker(grid_obj)
                    
                    if player == 1:
                        grid_matrix = AI.choice(grid_matrix)
                        player *= -1
                    
                    grid_obj.set(grid_matrix)
                    screen.drawMarker(grid_obj)
                    winner = check(grid_matrix)

            
                
        pygame.display.flip()

    pygame.quit()