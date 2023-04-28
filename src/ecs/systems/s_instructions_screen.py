import pygame

def system_instructions_screen(screen: pygame.Surface):
    # Show instructions on the screen for the player
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont("Arial", 30)
    text = font.render("Instructions", True, (255, 255, 255))
    screen.blit(text, (10, 10))
    font = pygame.font.SysFont("Arial", 20)
    text = font.render("Use the arrow keys to move the player", True, (255, 255, 255))
    screen.blit(text, (10, 50))
    text = font.render("Press the space bar to shoot", True, (255, 255, 255))

