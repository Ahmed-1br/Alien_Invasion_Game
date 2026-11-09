import pygame.font

class Scoreboard:
    """Display the current score."""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        

    def prep_score(self):
        """Turn the current score into an image."""
        self.score_image = self.font.render(
            str(self.stats.score), True, (30, 30, 30), self.settings.bg_color
        )
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Prepare the high score for display."""
        self.high_score_image = self.font.render(
            f"High: {self.stats.high_score}",
            True,
            (30, 30, 30),
            self.settings.bg_color
        )
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20

    def prep_level(self):
        """Prepare the current level for display."""
        self.level_image = self.font.render(
            f"Level: {self.stats.level}",
            True,
            (30, 30, 30),
            self.settings.bg_color
        )
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Prepare the remaining ships count for display."""
        self.ships_image = self.font.render(
            f"Ships: {self.stats.ships_left}",
            True,
            (30, 30, 30),
            self.settings.bg_color,
        )
        self.ships_rect = self.ships_image.get_rect()
        self.ships_rect.topleft = (20, 20)

    def show_score(self):
        """Display the score on the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.ships_image, self.ships_rect)