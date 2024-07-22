import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matrix Rain with Keanu")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Font settings
FONT_SIZE = 20
FONT = pygame.font.SysFont('Courier', FONT_SIZE, bold=True)

# Columns and Drops
COLUMNS = WIDTH // FONT_SIZE
DROPS = [random.randint(0, HEIGHT // FONT_SIZE) for _ in range(COLUMNS)]

# Load Keanu Reeves image
keanu_image = pygame.image.load("keanu.png")
keanu_image = pygame.transform.scale(keanu_image, (FONT_SIZE, FONT_SIZE))  # Adjust size as needed

# Keanu Drops - match columns with the image drops
keanu_drops = [random.randint(0, HEIGHT // FONT_SIZE) for _ in range(COLUMNS)]

def draw_matrix_rain():
    WIN.fill(BLACK)
    for i in range(len(DROPS)):
        # Draw multiple characters per column
        for j in range(5):
            char = chr(random.randint(33, 126))
            char_surface = FONT.render(char, True, GREEN)
            WIN.blit(char_surface, (i * FONT_SIZE, (DROPS[i] + j) * FONT_SIZE))
        
        if DROPS[i] * FONT_SIZE > HEIGHT and random.random() > 0.975:
            DROPS[i] = 0
        DROPS[i] += 1

        # Draw Keanu's face
        WIN.blit(keanu_image, (i * FONT_SIZE, keanu_drops[i] * FONT_SIZE))
        keanu_drops[i] += 1
        if keanu_drops[i] * FONT_SIZE > HEIGHT:
            keanu_drops[i] = 0

    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        draw_matrix_rain()

if __name__ == "__main__":
    main()
