import pygame


class Score:
    def __init__(self) -> None:
        self.player_score = 0
        self.__font = pygame.font.Font(None, 24)
        self.text = self.__font.render(f"Score: {self.player_score}", True, "white")
        self.pos = self.text.get_rect(x=10, y=10)

    def update(self, score: int) -> None:
        self.player_score += score
        self.text = self.__font.render(f"Score: {self.player_score}", True, "white")
