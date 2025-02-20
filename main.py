import pygame
from constants import *

# Main Function
def main():
    pygame.init()
    
    # Print boot message
    print(f"""Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}""")

    # Set the GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create a new pygame.time.Clock object
    fps = pygame.time.Clock()
    
    # create delta time (dt) variable set to 0
    dt = 0

    # Open the game loop
    while True:

        for event in pygame.event.get(): # On window close, quit the game
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black") # Fill the screen with black
        pygame.display.flip() # Refresh the screen

        # Pause the game for 1/60th of a second and
        # update the delta time with time passed since last frame
        dt = fps.tick(60) / 1000


# (For now) Don't touch below this line
if __name__ == "__main__":
    main()