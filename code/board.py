import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Board :
    def __init__(self, grid_size, cell_size, scale) :
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
        self.scale = scale
        self.target = None

    def init_draw(self, screen) :
            for x in range(self.grid_size):
                for y in range(self.grid_size):
                    rect = pygame.Rect(self.scale + x * self.cell_size, self.scale + y * self.cell_size, self.cell_size, self.cell_size)
                    pygame.draw.rect(screen, WHITE, rect)
                    pygame.draw.rect(screen, BLACK, rect, 1)

    def draw_cells(self, screen):
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                if self.grid[y][x] == 'R':
                    pygame.draw.circle(screen, (255, 0, 0), (self.scale + x * self.cell_size + self.cell_size // 2,self.scale +  y * self.cell_size + self.cell_size // 2), self.cell_size // 3)
                elif self.grid[y][x] == 'B':
                    pygame.draw.circle(screen, (0, 0, 255), (self.scale + x * self.cell_size + self.cell_size // 2,self.scale +  y * self.cell_size + self.cell_size // 2), self.cell_size // 3)
                elif self.grid[y][x] == 'G':
                    pygame.draw.circle(screen, (0, 255, 0), (self.scale + x * self.cell_size + self.cell_size // 2, self.scale + y * self.cell_size + self.cell_size // 2), self.cell_size // 3)
                elif self.grid[y][x] == 'Y':
                    pygame.draw.circle(screen, (255, 255, 0), (self.scale + x * self.cell_size + self.cell_size // 2, self.scale + y * self.cell_size + self.cell_size // 2), self.cell_size // 3)
                if self.target and self.target == (x, y):
                    rect = pygame.Rect(self.scale + x * self.cell_size,self.scale +  y * self.cell_size, self.cell_size, self.cell_size)
                    pygame.draw.rect(screen, (255, 255, 0), rect)
