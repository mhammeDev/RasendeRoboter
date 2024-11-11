import pygame
from sympy.strategies.core import switch


class Robot:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def move(self, position):
        pass

    def return_color(self):
        match(self.color):
            case (255, 0, 0):
                return "rouge"
            case(0, 0, 255):
                return "blue"
            case(0, 255, 0):
                return "green"
            case(255, 255, 0):
                return "yellow"
            case default:
                return "default"



    def place_on_table(self, board):
        x, y = self.position
        color_code = {
            (255, 0, 0): 'R',
            (0, 0, 255): 'B',
            (0, 255, 0): 'G',
            (255, 255, 0): 'Y'
        }
        board.grid[y][x] = color_code[self.color]