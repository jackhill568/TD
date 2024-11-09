import math
import pygame
import bullet
import configs


class Player:

    def __init__(self, pos:tuple[int, int]):
        
        self.__bullets: list[bullet.Bullet] = []

        self.__fireDelay: int = 0

        self.__sprite_number: int = 0
        images = ["assets/playerRight.png", "assets/playerDown.png", "assets/playerUp.png"]
        self.__sprites = [pygame.image.load(image) for image in images]
        self.__sprites.insert(0, pygame.transform.flip(self.__sprites[0], True, False))

        self.__sprite_rects = [image.get_rect(center=pos) for image in self.__sprites]

        self.__rect = self.__sprite_rects[self.__sprite_number]


    def move_up(self) -> None:
        self.__rect.y -= configs.PLAYER_SPEED
        self.__sprite_number = 3

    def move_down(self) -> None:
        self.__rect.y += configs.PLAYER_SPEED
        self.__sprite_number = 2

    def move_left(self) -> None:
        self.__rect.x -= configs.PLAYER_SPEED
        self.__sprite_number = 0

    def move_right(self) -> None:
        self.__rect.x += configs.PLAYER_SPEED
        self.__sprite_number = 1

    def get_bullets(self) -> list[bullet.Bullet]:
        return self.__bullets
    
    def get_pos(self):
        return self.__rect.center

    def shoot(self) -> None:
        if self.__fireDelay == 0:
            self.__bullets.append(bullet.Bullet(self.__rect.center,
             configs.getAngle(self.__rect.center, pygame.mouse.get_pos()),
             configs.PLAYER_BULLET_COLOUR))
            self.__fireDelay = configs.PLAYER_FIRE_RATE

    def update(self, screen: pygame.Surface) -> None:

        pos = self.__rect.center
        self.__rect = self.__sprite_rects[self.__sprite_number]
        self.__rect.center = pos

        if self.__fireDelay != 0:
            self.__fireDelay -= 1

        for bul in self.__bullets:
            bul.update(screen)
            if bul.get_del():
                self.__bullets.remove(bul)
                
        screen.blit(self.__sprites[self.__sprite_number], self.__sprite_rects[self.__sprite_number])
