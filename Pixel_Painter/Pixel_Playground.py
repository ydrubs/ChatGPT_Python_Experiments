import pygame
import random
from Pixel_Painter import Settings
from pygame.math import Vector2

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
        self.position = Vector2(x, y)
        self.color = color
        self.initial_position = Vector2(x, y)
        self.velocity = Vector2(0, random.randint(1, 5))
        self.max_velocity = 10
        self.drift = random.uniform(-0.5, 0.5)
        self.drifting = False

    def move(self, rectangles, collisions_enabled):
        self.position += self.velocity
        if self.drifting:
            self.position.x += self.drift

        self.wrap_around_screen()

        if collisions_enabled:
            for rect in rectangles:
                if rect != self:
                    if self.collides_with(rect):
                        try:
                            self.bounce(rect)
                            self.limit_velocity()
                        except ValueError:
                            self.reset_position(rectangles)

    def collides_with(self, rect):
        return (
            self.position.x < rect.position.x + cell_size
            and self.position.x + cell_size > rect.position.x
            and self.position.y < rect.position.y + cell_size
            and self.position.y + cell_size > rect.position.y
        )

    def bounce(self, rect):
        collision_normal = (self.position - rect.position).normalize()
        if collision_normal.length() == 0:
            raise ValueError("Zero-length vector")
        relative_velocity = self.velocity - rect.velocity
        restitution = 0.8  # Coefficient of restitution
        impulse = -2 * relative_velocity.dot(collision_normal) * collision_normal
        self.velocity += impulse * restitution
        rect.velocity -= impulse * restitution
        self.velocity.y = abs(self.velocity.y)  # Ensure downward movement
        rect.velocity.y = abs(rect.velocity.y)  # Ensure downward movement

    def wrap_around_screen(self):
        if self.position.x < 0:
            self.position.x = screen_width - cell_size
        elif self.position.x >= screen_width:
            self.position.x = 0

        if self.position.y < -cell_size:
            self.position.y = screen_height
        elif self.position.y >= screen_height:
            self.position.y = 0

    def reset_position(self, rectangles):
        self.position = self.initial_position
        for rect in rectangles:
            if rect != self:
                rect.initial_position = Vector2(rect.initial_position.x, rect.initial_position.y)

    def limit_velocity(self):
        if self.velocity.length() > self.max_velocity:
            self.velocity.scale_to_length(self.max_velocity)

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
    collisions_enabled = False

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
                # Change speed of rectangles on 's' key press
                elif event.key == pygame.K_s:
                    for rect in rectangles:
                        rect.velocity.y = random.randint(1, 5)
                # Toggle drifting effect on 'w' key press
                elif event.key == pygame.K_w:
                    drifting = not drifting
                    for rect in rectangles:
                        rect.drifting = drifting
                # Reset rectangles and restore initial positions on 'r' key press
                elif event.key == pygame.K_r:
                    for rect in rectangles:
                        rect.reset_position(rectangles)
                        rect.velocity = Vector2(0, random.randint(1, 5))
                # Toggle collisions on 'c' key press
                elif event.key == pygame.K_c:
                    collisions_enabled = not collisions_enabled

        if falling:
            # Move rectangles if falling animation is active
            for rect in rectangles:
                rect.move(rectangles, collisions_enabled)

        # Fill the screen with black color
        screen.fill(BLACK)

        # Draw the rectangles
        for rect in rectangles:
            pygame.draw.rect(
                screen, rect.color, (rect.position.x, rect.position.y, cell_size, cell_size)
            )

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
