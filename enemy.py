import math
import pygame
import configs

class Enemy(pygame.sprite.Sprite):

    def __init__(self, pos:tuple[int,int]):
        super().__init__()
        self._health: int
        self._damage: int
        self._attack_speed: int
        self.rect: pygame.rect.Rect
        self._angle: float = configs.getAngle(pos, configs.SCREEN_CENTRE)

    def get_distance_from_flag(self) -> int:
        vector: tuple[int, int] = (configs.SCREEN_CENTRE[0]-self.rect.x,
                                   configs.SCREEN_CENTRE[1]-self.rect.y)
        return int(math.sqrt(vector[0]**2 + vector[1]**2))

    def get_pos(self)->tuple[int, int]:
        return (self.rect.x, self.rect.y)

    def change_angle(self, angle:float)->None:
        self._angle = angle

    def move(self) -> None:
        self.rect.x -= int(configs.ENEMY_SPEED * math.sin(self._angle))
        self.rect.y -= int(configs.ENEMY_SPEED * math.cos(self._angle))

    def get_hit(self, attack_damage:int) -> None:
        self._health -= attack_damage

    def attack(self) -> None:
        pass

    def update(self, screen: pygame.Surface) -> None:
        
        self.move()
        self._angle = configs.getAngle(self.rect.center, configs.SCREEN_CENTRE)
        pygame.draw.rect(screen, "white", self.rect)

