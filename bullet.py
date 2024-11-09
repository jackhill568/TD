import math
import pygame
import configs


class Bullet(pygame.sprite.Sprite):

    def __init__(self, pos: tuple[int, int], angle: float, colour: tuple[int, int, int]):
        super().__init__()
        self.rect: pygame.rect.Rect = pygame.rect.Rect(*pos, *configs.BULLET_SIZE)
        self.__angle: float = angle
        self.__colour = colour
        self.__del = False
    
    def get_del(self):
        return self.__del

    def set_del(self):
        self.__del = not self.__del

    def get_rect(self) -> pygame.rect.Rect:
        return self.rect

    def update(self, screen:pygame.Surface) -> None:

        if not 0<self.rect.x<configs.SCREEN_SIZE[0] or not 0< self.rect.y < configs.SCREEN_SIZE[1]:
            self.__del = True

        self.rect.x -= int(configs.BULLET_SPEED * math.sin(self.__angle))
        self.rect.y -= int(configs.BULLET_SPEED * math.cos(self.__angle))
        pygame.draw.rect(screen, self.__colour, self.rect)
