import pygame
import sys

# General setup
pygame.init()

# Setting up main window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Load images
player_image = pygame.image.load('images/spaceinvaders_player.png')
alien_image = pygame.image.load('images/spaceinvaders_alien.png')

# Game Rectangles (player and alien)
player = player_image.get_rect(center = (screen_width/2, screen_height - 60))
alien = alien_image.get_rect(center = (screen_width/2, 10))

# Game Variables
player_speed = 2
alien_speed = [2, 0]

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move_ip(-player_speed, 0)
    if keys[pygame.K_RIGHT]:
        player.move_ip(player_speed, 0)

    # Keeping player on the screen
    if player.left < 0:
        player.left = 0
    if player.right > screen_width:
        player.right = screen_width

    # Alien movement
    alien.move_ip(alien_speed)
    if alien.left < 0 or alien.right > screen_width:
        alien_speed[0] *= -1
        alien.move_ip(0, 25)  # Move the alien down when it hits the side

    # Check for collision
    if alien.colliderect(player):
        print("Game Over")
        pygame.quit()
        sys.exit()

    # Visuals
    screen.fill((0, 0, 0))
    screen.blit(player_image, player)
    screen.blit(alien_image, alien)

    pygame.display.flip()
    pygame.time.Clock().tick(60)
