import pygame
from main import Main
import configs
import tab

pygame.init()

class mainMenu:

    def __init__(self):
        self.__screen: pygame.Surface = pygame.display.set_mode(configs.SCREEN_SIZE)
        self.__game: Main = Main(self.__screen) 
        self.quit: bool = False
        self.__current: str = "menu"
        self.__start_game_tab:tab.Tab = tab.Tab((30, 30), "Play")
        self.__exit_game_tab: tab.Tab = tab.Tab((30, 70), "Exit")

    def __runGame(self)->None:
        while  not self.__game.game_over:
            self.__game.update()
        self.__exitGame()

    def __exitGame(self)->None:
        if self.__current == self.__runGame:
            self.__current = "menu"
            self.__screen.fill("black")
            self.__game = Main(self.__screen)
        else:
            self.quit = True
    
    def __menu(self)->None:
        self.__start_game_tab.draw(self.__screen)
        self.__exit_game_tab.draw(self.__screen)
        pygame.display.update()

    def update(self)->None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__exitGame()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.__start_game_tab.check_mouse_collision():
                    self.__current = "runGame"
                elif self.__exit_game_tab.check_mouse_collision():
                    self.__exitGame()

        if self.__current == "menu":
            self.__menu()
        else:
            self.__runGame()

if __name__ == "__main__":
    win = mainMenu()
    while not win.quit:
        win.update()

