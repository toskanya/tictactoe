from pygame.locals import *
import pygame

from const import *

pygame.init()

class Screen():
    def __init__(self, width=SCREEN_WIDTH, height=SCREEN_HEIGHT):
        self.width = width
        self.height = height
        
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill(SCREEN_COLOR)

    def drawGrid(self, grid):
        pygame.draw.rect(grid.display, grid.line_color, (0, 0, grid.width, grid.height), 10)
        for i in range(1, 3):
            pygame.draw.line(grid.display, grid.line_color, (0, grid.cell * i), (self.width, grid.cell * i), grid.line_width)
            pygame.draw.line(grid.display, grid.line_color, (grid.cell * i, 0), (grid.cell * i, self.height), grid.line_width)
        self.screen.blit(grid.display, grid.pos)
        
    def drawMarker(self, grid):
        x_marker = X()
        o_marker = O()
        space = (STEP - x_marker.edge) / 2
        for i, row in enumerate(grid.grid_matrix):
            for j, cell in enumerate(row):
                y, x = i * STEP, j * STEP
                match cell:
                    case 1:
                        grid.display.blit(x_marker.shape, (x + space, y + space))
                    case -1:
                        grid.display.blit(o_marker.shape, (x + space, y + space))
                    case _:
                        pass   
        self.screen.blit(grid.display, grid.pos)
        
    def drawEndGame(self, winner):
        font = pygame.font.Font(None, FONT_SIZE)
        text = font.render(result[winner], True, FONT_COLOR)
        text_rect = text.get_rect(center=(self.width / 2, self.height / 2))
        self.screen.blit(text, text_rect)
        
    def update(self, surface, pos):
        self.screen.blit(surface, pos)
    
class Grid():
    def __init__(self, width=BOARD_WIDTH, height=BOARD_HEIGHT, pos=BOARD_POS):
        self.width = width
        self.height = height
        self.pos = pos
        self.cell = width / 3
        self.line_width = LINE_WIDTH
        self.line_color = LINE_COLOR
        self.grid_matrix = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        
        self.display = pygame.Surface((self.width, self.height))
        self.display.fill(BOARD_COLOR)
    
    def set(self, grid_matrix):
        self.grid_matrix = grid_matrix
    
    def get(self):
        return self.grid_matrix
        
class Marker():
    def __init__(self):
        self.pos = None
        self.edge = MARKER_WIDTH
        self.shape = pygame.surface.Surface((self.edge, self.edge))
        self.shape.fill(BOARD_COLOR)
        
class X(Marker):
    def __init__(self):
        super().__init__()
        self.color = X_COLOR
        self.width = X_WIDTH
        
        pygame.draw.line(self.shape, self.color, (0, 0), (self.edge, self.edge), X_WIDTH)
        pygame.draw.line(self.shape, self.color, (self.edge, 0), (0, self.edge), X_WIDTH)
        
class O(Marker):
    def __init__(self):
        super().__init__()
        self.color = O_COLOR
        self.width = O_WIDTH
        
        pygame.draw.circle(self.shape, self.color, (self.edge / 2, self.edge / 2), self.edge / 2, self.width)