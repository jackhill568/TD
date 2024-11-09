import pygame
import enemy

class Goblin(enemy.Enemy):

    def __init__(self, pos):
        super().__init__(pos)
        self._health = 1
        self._damage = 1
        self._angle = 2
        self.rect = pygame.rect.Rect(*pos, 15, 15)
        