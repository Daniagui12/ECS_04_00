import esper
import pygame
from src.ecs.components.c_enemy_spawner import CEnemySpawner
from src.ecs.components.tags.c_tag_enemy import CTagEnemy

def system_finish_game(world: esper.World, screen: pygame.Surface) -> None:
    """System that finishes the game when all enemies are destroyed"""
    _, enemy_spawner = world.get_component(CEnemySpawner)[0]
    if enemy_spawner.done:
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont("Arial", 50)
        text = font.render("You Win!", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (screen.get_width() // 2, screen.get_height() // 2)
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(3000)
        world.clear_database()
        pygame.quit()
        exit()