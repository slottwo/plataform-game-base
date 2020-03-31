# Imports
import pygame

# Clock
clock = pygame.time.Clock()

# Window
win = pygame.display.set_mode((320, 320))
pygame.display.set_caption("Game")

# Boot
pygame.init()


# Classes
class Entity():

    def __init__(self, x: int, y: int, w: int, h: int, color: tuple):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

    def get_me(self):
        return self.x, self.x, self.w, self.h


# Objects
person = Entity(320, 320, 16, 16, (255, 0, 255))

# Run
run = True
while run:
    clock.tick(6)
    pygame.draw.rect(win, person.color, person.get_me())

    # Render
    pygame.display.update()

    # Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Bye')
            run = False

pygame.quit()
