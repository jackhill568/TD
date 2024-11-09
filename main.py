import pygame
import random
import math
import player
import goblin, enemy
import configs
import tower
import bullet
import gunnerTower

pygame.font.init()

class Main:

    def __init__(self, screen: pygame.Surface):
        self.__screen = screen
        pygame.display.set_caption("what")
        self.game_over: bool = False
        self.__clock = pygame.time.Clock()
        start_pos: tuple[int, int] = configs.SCREEN_CENTRE
        self.__player: player.Player = player.Player(start_pos)
        self.__score = 0
        self.__souls: int = 200
        self.__wave: int = 1
        self.__current_wave: list[str] = []
        self.good_bullets = pygame.sprite.Group()
        self.__enemysLoaded = pygame.sprite.Group()
        self.__towers: list[tower.Tower] = []
        self.__towers = []

        self.__flag = pygame.rect.Rect(*configs.SCREEN_CENTRE, 30, 30)

    def __placeTower(self) -> None:
        self.__towers.append(gunnerTower.Gunner(self.__player.get_pos()))
    
    def __get_ran_pos(self)->tuple[int,int]:
        angle = random.randint(0, 360)*math.pi/180
        return (
            int(
                configs.MAX_RADIUS_FROM_FLAG*math.sin(angle)+configs.SCREEN_SIZE[0]/2), 
            int(
                configs.MAX_RADIUS_FROM_FLAG*math.cos(angle)+configs.SCREEN_SIZE[1]/2))

    def __spawnEnemy(self, entype:str) -> None:
        pos = self.__get_ran_pos()
        if entype == "g":
            en = goblin.Goblin(pos)
            self.__enemysLoaded.add(en)

    def target_getter(self) -> list[tuple[int,int]]:
        return [en.get_pos() for en in self.__enemysLoaded[:len(self.__enemysLoaded)//2]]

    def __get_key_input(self) -> None:
        key_press = pygame.key.get_pressed()

        if key_press[pygame.K_a]:
            self.__player.move_left()
        if key_press[pygame.K_d]:
            self.__player.move_right()
        if key_press[pygame.K_w]:
            self.__player.move_up()
        if key_press[pygame.K_s]:
            self.__player.move_down()
    
    def __waves(self):
        if self.__current_wave == [] and len(self.__enemysLoaded)==0:
            self.__wave = self.__wave+1 if self.__wave<3 else 3
            self.__current_wave = [enType[0] 
                for enType in configs.WAVES[self.__wave]
                for i in range(enType[1])]
        if len(self.__current_wave)!=0:
            en = random.choice(self.__current_wave)
            self.__spawnEnemy(en)
            self.__current_wave.remove(en)

    def __bullet_collision(self) ->None:

        for t in self.__towers:
            t.update(self.__screen, self.target_getter())
            self.good_bullets.add(t.get_bullets())

        self.good_bullets.add(self.__player.get_bullets())
        
        pygame.sprite.groupcollide(self.good_bullets, self.__enemysLoaded, True, False)
        self.__enemysLoaded.update(self.__screen)
        # for en in self.__enemysLoaded:
        #     if en._health<=0:
        #         self.__enemysLoaded.remove(en)
        #     elif en._rect.colliderect(self.__flag):
        #         self.__enemysLoaded.kill(en)
        #         self.__score-=1
        #     else:
        #         for b in self.good_bullets:
        #             if b == None:
        #                 pass
        #             elif b.get_rect().colliderect(en._rect):
        #                 en.get_hit(configs.PLAYER_BULLET_DAMAGE)
        #                 b.set_del()
        #                 self.__score += 1
        #                 break
        #     en.update(self.__screen)


    def update(self) -> None:
        self.__screen.fill("black")

        self.__player.update(self.__screen)

        self.__get_key_input()

        self.__screen.blit(pygame.font.SysFont('freesansbold.ttf', 30).render(f"score: {self.__score}", False, "white"),(10,10))
        
        pygame.draw.rect(self.__screen, "red", self.__flag)
        
        self.__waves()

        self.__bullet_collision()
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pressed()
                if mouse[0]:
                    self.__player.shoot()
                if mouse[2]:
                    self.__placeTower()

        self.__clock.tick(144)
        pygame.display.update()

    
