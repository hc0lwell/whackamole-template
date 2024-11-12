import pygame
import random


GRID_WIDTH = 20
GRID_HEIGHT = 16
SQUARE_SIZE = 32


def draw_grid(screen):
    """Draws a 20x16 grid of 32x32 squares on the screen."""
    for x in range(0, GRID_WIDTH * SQUARE_SIZE, SQUARE_SIZE):
        pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, GRID_HEIGHT * SQUARE_SIZE))  # Vertical lines
    for y in range(0, GRID_HEIGHT * SQUARE_SIZE, SQUARE_SIZE):
        pygame.draw.line(screen, (0, 0, 0), (0, y), (GRID_WIDTH * SQUARE_SIZE, y))  # Horizontal lines


def main():
    pygame.init()
    mole_image = pygame.image.load("mole.png")
    screen = pygame.display.set_mode((GRID_WIDTH * SQUARE_SIZE, GRID_HEIGHT * SQUARE_SIZE))
    clock = pygame.time.Clock()
    running = True


    mole_pos = (0, 0)

    while running:
        screen.fill("light green")
        draw_grid(screen)


        screen.blit(mole_image, mole_image.get_rect(topleft=mole_pos))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse click is inside the mole's square
                mouse_x, mouse_y = event.pos
                mole_rect = mole_image.get_rect(topleft=mole_pos)
                if mole_rect.collidepoint(mouse_x, mouse_y):
                    new_x = random.randrange(0, GRID_WIDTH) * SQUARE_SIZE
                    new_y = random.randrange(0, GRID_HEIGHT) * SQUARE_SIZE
                    mole_pos = (new_x, new_y)  # Update mole's position

        pygame.display.flip()  # Update the display
        clock.tick(60)  # Limit the frame rate to 60 FPS

    pygame.quit()


if __name__ == "__main__":
    main()
