import pygame
import random

class Settings:
    screen_width = 800
    screen_height = 800
    cell_size = 20

if __name__ == "__main__":
    # Initialize Pygame
    pygame.init()

    # Set screen dimensions
    screen_width = Settings.screen_width
    screen_height = Settings.screen_height

    # Set cell dimensions
    cell_size = Settings.cell_size

    # Set colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Initialize the screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Rectangle Game")

    # Set the initial position of the rectangle
    rectangle_x = 0
    rectangle_y = 0

    # Set the initial color of the rectangle
    rectangle_color = WHITE

    # Initialize the grid of colors
    grid = [[BLACK for _ in range(screen_height // cell_size)] for _ in range(screen_width // cell_size)]

    # Game loop
    running = True
    clock = pygame.time.Clock()

    # Set the delay (in milliseconds) between each rectangle movement update
    movement_delay = 75

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Change color on spacebar press
                if event.key == pygame.K_SPACE:
                    rectangle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                # Change current cell color on 's' key press
                elif event.key == pygame.K_s:
                    row = rectangle_y // cell_size
                    col = rectangle_x // cell_size
                    grid[col][row] = rectangle_color
                # Generate script on 'g' key press
                elif event.key == pygame.K_g:
                    script_name = "grid_pattern2.py"
                    with open(script_name, 'w') as f:
                        f.write("grid = ")
                        f.write(str(grid))

        # Move rectangle with arrow keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and rectangle_x > 0:
            rectangle_x -= cell_size
        elif keys[pygame.K_RIGHT] and rectangle_x < screen_width - cell_size:
            rectangle_x += cell_size
        elif keys[pygame.K_UP] and rectangle_y > 0:
            rectangle_y -= cell_size
        elif keys[pygame.K_DOWN] and rectangle_y < screen_height - cell_size:
            rectangle_y += cell_size

        # Fill the screen with black color
        screen.fill(BLACK)

        # Draw the grid cells
        for col in range(screen_width // cell_size):
            for row in range(screen_height // cell_size):
                cell_color = grid[col][row]
                pygame.draw.rect(screen, cell_color, (col * cell_size, row * cell_size, cell_size, cell_size))

        # Draw the rectangle
        pygame.draw.rect(screen, rectangle_color, (rectangle_x, rectangle_y, cell_size, cell_size))

        # Update the display
        pygame.display.flip()

        # Delay for a specific amount of time
        pygame.time.wait(movement_delay)

    # Quit the game
    pygame.quit()
