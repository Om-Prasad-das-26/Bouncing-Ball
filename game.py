import pygame
import random

pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Game")

clock = pygame.time.Clock()


player_width = 50
player_height = 50
player_x = screen_width / 2 - player_width / 2
player_y = screen_height - player_height
player_speed = 9
player = pygame.Rect(player_x, player_y, player_width, player_height)


enemy_width = 49
enemy_height = 59
enemy_speed = 7
enemies = []
for i in range(5):
    enemy_x = random.randint(0, screen_width - enemy_width)
    enemy_y = random.randint(-screen_height, 0)
    enemy = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
    enemies.append(enemy)

score = 0
font = pygame.font.SysFont(None, 30)


game_over = False
while not game_over:

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < screen_width - player_width:
        player.x += player_speed

    for enemy in enemies:
        enemy.y += enemy_speed
        if enemy.y > screen_height:
            enemy.x = random.randint(0, screen_width - enemy_width)
            enemy.y = random.randint(-screen_height, 0)
            score += 1
        if enemy.colliderect(player):
            game_over = True

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), player)
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), enemy)
    score_text = font.render("Score: {}".format(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()


    clock.tick(60)


pygame.quit()
