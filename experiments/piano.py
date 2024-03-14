import pygame
from pygame.locals import *
import os

# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 200
WHITE_KEY_WIDTH = 50
WHITE_KEY_HEIGHT = 200
BLACK_KEY_WIDTH = 30
BLACK_KEY_HEIGHT = 120

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define key mappings
WHITE_KEY_MAP = "ZXCVBNM,./QWERTYUIOP[]"
BLACK_KEY_MAP = "SDGHJL;12356890-="

# Initialize pygame
pygame.init()

# Load sounds
C4_SOUND = pygame.mixer.Sound("C4.mp3")
D4_SOUND = pygame.mixer.Sound("D4.mp3")

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Piano App")


# Function to draw keys
def draw_keys():
    x = 0
    y = 0
    for i in range(len(WHITE_KEY_MAP)):
        if WHITE_KEY_MAP[i] == ' ':
            continue
        key_rect = pygame.Rect(x, y, WHITE_KEY_WIDTH, WHITE_KEY_HEIGHT)
        pygame.draw.rect(screen, WHITE, key_rect)
        if pressed_keys[WHITE_KEY_MAP[i]]:
            pygame.draw.rect(screen, RED, key_rect, 3)
        x += WHITE_KEY_WIDTH
    x = WHITE_KEY_WIDTH - (BLACK_KEY_WIDTH // 2)
    for i in range(len(BLACK_KEY_MAP)):
        if BLACK_KEY_MAP[i] == ' ':
            continue
        key_rect = pygame.Rect(x, y, BLACK_KEY_WIDTH, BLACK_KEY_HEIGHT)
        pygame.draw.rect(screen, BLACK, key_rect)
        if pressed_keys[BLACK_KEY_MAP[i]]:
            pygame.draw.rect(screen, RED, key_rect, 3)
        x += WHITE_KEY_WIDTH
        if BLACK_KEY_MAP[i] in ['S', 'D', 'G', 'H', 'J']:
            x += WHITE_KEY_WIDTH


# Main loop
running = True
clock = pygame.time.Clock()
pressed_keys = {key: False for key in (WHITE_KEY_MAP + BLACK_KEY_MAP)}

while running:
    screen.fill(WHITE)
    draw_keys()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key in pressed_keys:
                pressed_keys[event.key] = True
                if event.key == K_z:
                    C4_SOUND.play()
                elif event.key == K_x:
                    D4_SOUND.play()
        elif event.type == KEYUP:
            if event.key in pressed_keys:
                pressed_keys[event.key] = False

    clock.tick(60)

pygame.quit()
