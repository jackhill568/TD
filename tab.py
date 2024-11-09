import pygame
import configs
class Tab:

    def __init__(self, pos: tuple[int,int], message: str):
        self._message = pygame.font.SysFont("freesansbold.ttf", int(40)).render(message, True, "black")
        text_size = self._message.get_size()
        self.__rect = pygame.rect.Rect(*pos, text_size[0]+10, text_size[1]+10)

    def draw(self, screen: pygame.Surface) -> None:
        colour = configs.TAB_SELECT_COLOUR if self.check_mouse_collision() else configs.TAB_COLOUR
        pygame.draw.rect(screen, colour, self.__rect)
        screen.blit(self._message, (self.__rect.x+5, self.__rect.y+5))

    def check_mouse_collision(self) -> bool:

        if self.__rect.collidepoint(pygame.mouse.get_pos()): return True
        else: return False