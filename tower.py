import pygame

from bullet import Bullet

class Tower:

    def __init__(self):
        self.__fireDelay: int
        self.size: tuple[int]
        self.cost: int
        self.damage: int
        self._range:int
        self._rect: pygame.rect.Rect

    def attack(self, screen: pygame.Surface, targets: list[tuple[int,int]]):
        pass

    def get_fireDelay(self):
        return self.__fireDelay
    
    def get_bullets(self) -> list[Bullet]:
        return []
        
    def upgrade(self):
        pass

    def update(self, screen: pygame.Surface, target: list[tuple[int, int]]):

        self.attack(screen, target)
        
        pygame.draw.rect(screen, "purple", self._rect)