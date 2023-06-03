import pygame
import random
from Pixel_Painter import Settings

# Set screen dimensions
screen_width = Settings.screen_width
screen_height = Settings.screen_height

# Set cell dimensions
cell_size = Settings.cell_size

# Set colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the Rectangle class
class Rectangle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.initial_x = x  # Store the initial x position
        self.initial_y = y  # Store the initial y position
        self.speed = random.randint(1, 5)
        self.drift = random.uniform(-0.5, 0.5)
        self.drifting = False

    def move(self):
        self.y += self.speed
        if self.drifting:
            self.x += self.drift
        if self.x > screen_width:  # Wrap around to the left side
            self.x = -cell_size
        elif self.x < -cell_size:  # Wrap around to the right side
            self.x = screen_width

    def reset(self):
        self.x = self.initial_x  # Reset to initial x position
        self.y = self.initial_y  # Reset to initial y position

def display_grid(grid):
    # Initialize Pygame
    pygame.init()

    # Calculate the size of the grid
    num_cols = len(grid)
    num_rows = len(grid[0])

    # Initialize the screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Grid Pattern")

    # Create the list of rectangles
    rectangles = []
    for col in range(num_cols):
        for row in range(num_rows):
            if grid[col][row] != BLACK:
                x = col * cell_size
                y = row * cell_size
                color = grid[col][row]
                rectangles.append(Rectangle(x, y, color))

    # Falling animation variables
    falling = False
    drifting = False

    # Store the initial positions of the rectangles
    initial_positions = [(rect.initial_x, rect.initial_y) for rect in rectangles]

    # Game loop
    running = True
    clock = pygame.time.Clock()

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Toggle falling animation on 'p' key press
                if event.key == pygame.K_p:
                    falling = not falling
                # Reset rectangles to initial positions on 'r' key press
                elif event.key == pygame.K_r:
                    if not falling:
                        for rect, (x, y) in zip(rectangles, initial_positions):
                            rect.reset()
                            rect.x = x
                            rect.y = y
                # Change speed of rectangles on 's' key press
                elif event.key == pygame.K_s:
                    for rect in rectangles:
                        rect.speed = random.randint(1, 5)
                # Toggle drifting effect on 'w' key press
                elif event.key == pygame.K_w:
                    drifting = not drifting
                    for rect in rectangles:
                        rect.drifting = drifting

        if falling:
            # Move rectangles if falling animation is active
            for rect in rectangles:
                rect.move()
                if rect.y >= screen_height:
                    rect.y = -cell_size

        # Fill the screen with black color
        screen.fill(BLACK)

        # Draw the rectangles
        for rect in rectangles:
            pygame.draw.rect(screen, rect.color, (rect.x, rect.y, cell_size, cell_size))

        # Update the display
        pygame.display.flip()

        # Limit the frame rate
        clock.tick(60)

    # Quit the game
    pygame.quit()

# Load the grid pattern from the file
script_name = "grid_pattern2.py"
try:
    with open(script_name, 'r') as f:
        exec(f.read(), globals())
except FileNotFoundError:
    print(f"Error: {script_name} not found.")
else:
    # Display the grid pattern
    display_grid(grid)
