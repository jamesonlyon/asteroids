import pygame
from constants import *
from player import Player

# Main Function
def main():
    pygame.init()

    print(f"""Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}""") # Print boot message

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # create the GUI screen
    fps = pygame.time.Clock() # create a new pygame.time.Clock object
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) # create a player ojbect
    dt = 0 # create delta time (dt) variable set to 0

    while True: # Open the game loop
        for event in pygame.event.get(): # On window close, quit the game
            if event.type == pygame.QUIT:
                print("Quitting Asteroids...")
                return
        
        screen.fill("black") # Fill the screen with black
        player.draw(screen) # Draw the player sprite
        player.update(dt)
        pygame.display.flip() # Refresh the screen
        
        dt = fps.tick(60) / 1000 # Limit framerate to 60 FPS


# Pygame Main Function Call
if __name__ == "__main__":
    main()