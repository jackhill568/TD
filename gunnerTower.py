from typing import overload
import pygame
import bullet
import tower, configs

class Gunner(tower.Tower):

    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        self.__bullets: list[bullet.Bullet] = []
        self.__fireDelay:int = 0
        self._rect: pygame.rect.Rect = pygame.rect.Rect(*pos, 20, 20)
        self._range:int = 300

    def get_bullets(self) -> list[bullet.Bullet]:
        return self.__bullets

    def attack(self, screen: pygame.Surface, targets: list[tuple[int, int]]):
        
        target = (-1,-1)

        for bul in self.__bullets:
            bul.update(screen)
            if bul.get_del():
                self.__bullets.remove(bul)

        for tar in targets:
            if configs.get_distance(self._rect.center, tar)<self._range:
                target = tar

        if self.__fireDelay == 0 and target != (-1,-1):
            angle = configs.getAngle(self._rect.center, target)
            self.__bullets.append(bullet.Bullet(self._rect.center, angle, configs.TOWER_BULLET_COLOUR))
            self.__fireDelay = configs.PLAYER_FIRE_RATE
        elif self.__fireDelay>=1:
            self.__fireDelay -=1

