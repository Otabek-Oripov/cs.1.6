import pygame
import sys
import math

pygame.init()

# Ekran va sozlamalar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame CS 1.6 Style FPS")
clock = pygame.time.Clock()

# O'yinchi koordinatalari
player_pos = [WIDTH // 2, HEIGHT // 2]
player_angle = 0
move_speed = 5

# Qurol rasmi (sprite)
gun_img = pygame.image.load("image/images-removebg-preview.png").convert_alpha()
gun_img = pygame.transform.scale(gun_img, (300, 200))

# Nishon (crosshair)
def draw_crosshair():
    center = (WIDTH // 2, HEIGHT // 2)
    pygame.draw.line(screen, (255, 0, 0), (center[0] - 10, center[1]), (center[0] + 10, center[1]), 2)
    pygame.draw.line(screen, (255, 0, 0), (center[0], center[1] - 10), (center[0], center[1] + 10), 2)

# Otish
def shoot():
    print("ottim naxxuy")

# O'yin sikli
while True:
    screen.fill((30, 30, 30))  # fon

    # Eventlar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Harakat
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos[1] -= move_speed  # oldinga harakat (faqat y koordinata o'zgaradi)

    # Otish (Mouse 1)
    if pygame.mouse.get_pressed()[0]:
        shoot()

    # Qurol chizish (ekranning past o‘ng qismida)
    gun_pos = (WIDTH // 2 - 10, HEIGHT - 250)
    screen.blit(gun_img, gun_pos)

    # Nishonni chizish
    draw_crosshair()

    pygame.display.flip()
    clock.tick(60)
