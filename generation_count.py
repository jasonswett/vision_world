class GenerationCount:
    def __init__(self, screen, font, generation_game_loop_counter):
        self.screen = screen
        self.font = font
        self.generation_game_loop_counter = generation_game_loop_counter

    def draw(self):
        text = self.font.render(f'Generation: {self.generation_game_loop_counter}', True, (255, 255, 255), (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.bottomright = self.screen.get_rect().bottomright
        self.screen.blit(text, text_rect)
