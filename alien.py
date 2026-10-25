import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Represent one alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load(
            'images/enemy_4.png'
        ).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if the alien reaches either screen edge."""
        screen_rect = self.screen.get_rect()
        return (
            self.rect.right >= screen_rect.right
            or self.rect.left <= 0
        )

    def update(self):
        """Move the alien in the fleet's current direction."""
        self.x += (
            self.settings.alien_speed
            * self.settings.fleet_direction
        )
        self.rect.x = self.x