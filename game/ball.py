import pygame
import random

# Initialize sound mixer
pygame.mixer.init()

class Ball:
    def __init__(self, x, y, width, height, screen_width, screen_height):
        self.original_x = x
        self.original_y = y
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.velocity_x = random.choice([-5, 5])
        self.velocity_y = random.choice([-3, 3])

        # Load sound effects
        try:
            self.sound_paddle = pygame.mixer.Sound("assets/paddle_hit.wav")
            self.sound_wall = pygame.mixer.Sound("assets/wall_bounce.wav")
            self.sound_score = pygame.mixer.Sound("assets/score.wav")
        except pygame.error as e:
            print(f"Warning: Could not load sound files - {e}")
            self.sound_paddle = None
            self.sound_wall = None
            self.sound_score = None

    def move(self, player=None, ai=None):
        # Move ball
        self.x += self.velocity_x
        self.y += self.velocity_y

        # Bounce off top/bottom walls
        if self.y <= 0 or self.y + self.height >= self.screen_height:
            self.velocity_y *= -1
            if self.sound_wall:
                self.sound_wall.play()

        # Check for paddle collisions immediately (to prevent tunneling)
        if player and ai:
            self.check_collision(player, ai)

    def check_collision(self, player, ai):
        ball_rect = self.rect()
        player_rect = player.rect()
        ai_rect = ai.rect()

        # Player paddle collision
        if ball_rect.colliderect(player_rect) and self.velocity_x < 0:
            self.x = player_rect.right
            self.velocity_x *= -1
            if self.sound_paddle:
                self.sound_paddle.play()

        # AI paddle collision
        elif ball_rect.colliderect(ai_rect) and self.velocity_x > 0:
            self.x = ai_rect.left - self.width
            self.velocity_x *= -1
            if self.sound_paddle:
                self.sound_paddle.play()

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.velocity_x *= -1
        self.velocity_y = random.choice([-3, 3])
        if self.sound_score:
            self.sound_score.play()

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
