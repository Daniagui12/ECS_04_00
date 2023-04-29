import pygame
import asyncio

async def system_instruction_show(screen: pygame.Surface):
    # Set up the font
    font = pygame.font.Font(None, 36)

    # Explain the user how to play, arrows for movement and right click for shooting
    text = font.render("Use the arrows to move and right click to shoot", True, (255, 255, 255))
    textpos = text.get_rect()
    textpos.centerx = screen.get_rect().centerx
    textpos.centery = screen.get_rect().centery

    # Display the text
    screen.blit(text, textpos)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return True