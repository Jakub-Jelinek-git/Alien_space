from turtle import Screen
import pygame
import sys

def load_game():
    """loads the game window"""
    #module needed to run the game
    pygame.init()
    #sets the creen size
    screen = pygame.display.set_mode((1200,800))
    #shows the title on top of the screen
    pygame.display.set_caption("Alien Space","AS")
    #stest the background color
    bg_color = (230,230,230)
    
    #start the main loop for the game
    while True:
        
        #event loop watching for mouse and keyboard movements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #chenges the creen color each loop
        screen.fill(bg_color)
        #draws the most recent screen with changes
        pygame.display.flip()
load_game()